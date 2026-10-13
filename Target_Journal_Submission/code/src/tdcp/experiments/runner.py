"""One repetition of one scenario: split -> calibrate -> transfer -> intervals -> metrics."""
from __future__ import annotations

import time
from dataclasses import asdict, dataclass

import numpy as np
from scipy.spatial.distance import cdist
from scipy.stats import spearmanr

from tdcp.data.datasets import PairedSpectra
from tdcp.evaluation.metrics import grouped_coverage, interval_metrics
from tdcp.intervals.methods import all_intervals
from tdcp.models.regression import fit_calibration
from tdcp.models.transfer import make_transfer
from tdcp.preprocessing.spectra import PREPROCESSORS, simulate_secondary


@dataclass(frozen=True)
class Job:
    experiment: str
    dataset: str
    primary: str
    secondary: str  # instrument name, or "sim<severity>" for a simulated secondary
    prop: int
    transfer: str
    seed: int
    k: int = 10
    n_test: int = 25
    selection: str = "random"  # random | kennard_stone
    protocol: str = "random"  # random | official
    preprocess: str = "none"
    model: str = "pls"
    noise: float = 0.0
    alphas: tuple = (0.1,)


def kennard_stone(X: np.ndarray, k: int) -> np.ndarray:
    """Kennard & Stone (1969) uniform design in Euclidean spectral space."""
    D = cdist(X, X)
    first = list(np.unravel_index(np.argmax(D), D.shape))
    sel = first
    mind = D[sel].min(axis=0)
    while len(sel) < k:
        mind[sel] = -1
        j = int(np.argmax(mind))
        sel.append(j)
        mind = np.minimum(mind, D[j])
    return np.array(sel[:k])


def _split(job: Job, data: PairedSpectra, Xp: np.ndarray, valid: np.ndarray, rng: np.random.Generator):
    idx = np.flatnonzero(valid)
    if job.protocol == "official":
        test = idx[data.official_split[idx] == "test"]
        pool = idx[data.official_split[idx] != "test"]
    else:
        perm = rng.permutation(idx)
        test, pool = perm[: job.n_test], perm[job.n_test:]
    if job.selection == "kennard_stone":
        tr = pool[kennard_stone(Xp[pool], job.k)]
    else:
        tr = rng.choice(pool, size=job.k, replace=False)
    master = np.setdiff1d(pool, tr)
    return master, tr, test


def run_job(job: Job, data: PairedSpectra, cfg: dict, details: bool = False):
    t0 = time.perf_counter()
    rng = np.random.default_rng(job.seed)
    pre = PREPROCESSORS[job.preprocess]
    y_all = data.y[:, job.prop]
    valid = np.isfinite(y_all)
    Xp_raw = data.spectra[job.primary]
    if job.secondary.startswith("sim"):
        Xs_raw = simulate_secondary(Xp_raw, int(job.secondary[3:]), np.random.default_rng(10_000 + job.seed))
    else:
        Xs_raw = data.spectra[job.secondary]
    if job.noise > 0:
        scale = Xp_raw.std(axis=0).mean()
        Xs_raw = Xs_raw + np.random.default_rng(20_000 + job.seed).normal(0, job.noise * scale, Xs_raw.shape)
    Xp, Xs = pre(Xp_raw), pre(Xs_raw)

    master, tr, test = _split(job, data, Xp, valid, rng)
    max_comp = cfg["max_components"][job.dataset]
    t_cal = time.perf_counter()
    cal = fit_calibration(Xp[master], y_all[master], job.model, max_comp, cfg["cv_folds"], job.seed)
    t_cal = time.perf_counter() - t_cal

    t_tr = time.perf_counter()
    T = make_transfer(job.transfer, cfg).fit(Xp[tr], Xs[tr])
    Xs_test_T = T.transform(Xs[test])
    yhat = cal.predict(Xs_test_T)
    t_tr = time.perf_counter() - t_tr

    # transfer discrepancies (label-free) and labelled target residuals, both cross-fitted
    t_td = time.perf_counter()
    fP_tr = cal.predict(Xp[tr])
    f_cf = np.empty(job.k)
    yhat_loo = np.empty((test.size, job.k))
    for j in range(job.k):
        keep = np.arange(job.k) != j
        Tj = make_transfer(job.transfer, cfg).fit(Xp[tr][keep], Xs[tr][keep])
        f_cf[j] = cal.predict(Tj.transform(Xs[tr][j : j + 1]))[0]
        yhat_loo[:, j] = cal.predict(Tj.transform(Xs[test]))
    delta_cf = fP_tr - f_cf
    delta_in = fP_tr - cal.predict(T.transform(Xs[tr]))
    t_td = time.perf_counter() - t_td
    e = y_all[tr] - f_cf

    ctx = dict(
        n_test=test.size, yhat=yhat, yhat_loo=yhat_loo, r=cal.cv_residuals, delta_cf=delta_cf, delta_in=delta_in, e=e,
        feat_cal=cal.feature_fn(Xp[master]), feat_test=cal.feature_fn(Xs_test_T),
        leverage_test=cal.leverage(Xs_test_T), n_components=cal.n_components, seed=job.seed,
    )
    y_test = y_all[test]
    # diagnostics using held-out truth (never used by any method)
    fP_test = cal.predict(Xp[test])
    r_test, d_test = y_test - fP_test, fP_test - yhat
    rho = spearmanr(r_test, d_test).statistic if test.size > 2 else np.nan
    y_terc = np.digitize(y_test, np.quantile(y_all[valid], [1 / 3, 2 / 3]))
    lev = ctx["leverage_test"]
    lev_terc = np.digitize(lev, np.quantile(lev, [1 / 3, 2 / 3])) if lev is not None else None
    base = asdict(job)
    base.pop("alphas")
    base.update(
        n_master=master.size, n_components=cal.n_components, rmsecv=cal.rmsecv,
        rmsep=float(np.sqrt(np.mean((y_test - yhat) ** 2))),
        rmsep_primary=float(np.sqrt(np.mean(r_test**2))),
        sd_y=float(np.std(y_all[valid], ddof=1)),
        delta_cf_mean=float(delta_cf.mean()), delta_cf_sd=float(delta_cf.std(ddof=1)),
        delta_in_sd=float(delta_in.std(ddof=1)), delta_test_mean=float(d_test.mean()),
        delta_test_sd=float(d_test.std(ddof=1)), spearman_r_delta=float(rho),
        t_calibration=t_cal, t_transfer=t_tr, t_crossfit=t_td,
    )
    rows = []
    for alpha in job.alphas:
        t_int = time.perf_counter()
        ints = all_intervals(ctx, alpha)
        t_int = (time.perf_counter() - t_int) / len(ints)
        for name, (lo, hi) in ints.items():
            m = interval_metrics(y_test, yhat + lo, yhat + hi, alpha)
            cov = (y_test >= yhat + lo) & (y_test <= yhat + hi)
            yc = grouped_coverage(cov, y_terc)
            row = dict(base, alpha=alpha, method=name, t_interval_mean=t_int, **m,
                       cov_ylow=yc[0], cov_ymid=yc[1], cov_yhigh=yc[2])
            if lev_terc is not None:
                lc = grouped_coverage(cov, lev_terc)
                row.update(cov_levlow=lc[0], cov_levmid=lc[1], cov_levhigh=lc[2])
            rows.append(row)
        # in-domain sanity: naive CP applied to primary-instrument spectra of the test samples
        lo, hi = ints["naive_cp"]
        m = interval_metrics(y_test, fP_test + lo, fP_test + hi, alpha)
        rows.append(dict(base, alpha=alpha, method="naive_cp_primary_test", t_interval_mean=0.0, **m))
    for r in rows:
        r["t_total"] = time.perf_counter() - t0
    if details:
        ints = all_intervals(ctx, job.alphas[0])
        return rows, dict(y_test=y_test, yhat=yhat, yhat_primary=fP_test, intervals=ints,
                          delta_cf=delta_cf, delta_test=d_test, r=cal.cv_residuals, r_test=r_test)
    return rows
