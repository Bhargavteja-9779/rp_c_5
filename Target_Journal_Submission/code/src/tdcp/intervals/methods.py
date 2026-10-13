"""Prediction-interval methods for a calibration applied after instrument transfer.

All methods return offsets (lo, hi) such that the interval for test sample t is
[yhat_t + lo_t, yhat_t + hi_t]. Infinite offsets denote the trivial interval that
split conformal prediction returns when the calibration set is too small.

Notation (see manuscript Section 2):
  r      out-of-fold residuals of the primary calibration, r_i = y_i - f_{-i}(x_i^P)
  delta  transfer discrepancies on transfer standards (no reference values needed),
         delta_j = f(x_j^P) - f(T_{-j}(x_j^S))   (cross-fitted), or with T (in-sample)
  e      labelled target residuals, e_j = y_j - f(T_{-j}(x_j^S)) (needs reference values)
"""
from __future__ import annotations

import math

import numpy as np
from scipy import stats
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler


def conformal_quantile(scores: np.ndarray, level: float) -> float:
    """ceil((n+1) level)-th smallest score; +inf if that exceeds n."""
    s = np.sort(np.asarray(scores, dtype=float))
    n = s.size
    idx = math.ceil((n + 1) * level - 1e-12)
    return float(s[idx - 1]) if idx <= n else math.inf


def _const(n_test: int, lo: float, hi: float):
    return np.full(n_test, lo), np.full(n_test, hi)


# ---------------------------------------------------------------- baselines
def naive_cp(r, n_test, alpha):
    """M1: split-conformal interval of the primary instrument, ignoring transfer."""
    q = conformal_quantile(np.abs(r), 1 - alpha)
    return _const(n_test, -q, q)


def leverage_interval(r, leverage_test, n_components, alpha):
    """M2: classical leverage-corrected PLS prediction interval (ASTM E1655-type)."""
    n = r.size
    rmsecv = np.sqrt(np.mean(r**2))
    dof = max(n - n_components - 1, 1)
    half = stats.t.ppf(1 - alpha / 2, dof) * rmsecv * np.sqrt(1 + 1 / n + leverage_test)
    return -half, half


def weighted_cp(r, feat_cal, feat_test, alpha, seed=0):
    """M3: weighted split conformal under covariate shift (Tibshirani et al., 2019).

    Density ratio w(x) = p_test(x)/p_cal(x) estimated with logistic regression
    on standardised low-dimensional features (PLS scores). The test point gets
    its own weight and an atom at +inf.
    """
    Z = np.vstack([feat_cal, feat_test])
    lab = np.r_[np.zeros(len(feat_cal)), np.ones(len(feat_test))]
    Zs = StandardScaler().fit_transform(Z)
    clf = LogisticRegression(max_iter=2000, random_state=seed).fit(Zs, lab)
    pr = np.clip(clf.predict_proba(Zs)[:, 1], 1e-6, 1 - 1e-6)
    odds = pr / (1 - pr) * (len(feat_cal) / len(feat_test))
    w_cal, w_test = odds[: len(feat_cal)], odds[len(feat_cal):]
    s = np.abs(r)
    order = np.argsort(s)
    s_sorted, w_sorted = s[order], w_cal[order]
    cw = np.cumsum(w_sorted)
    half = np.empty(len(feat_test))
    for t, wt in enumerate(w_test):
        cdf = cw / (cw[-1] + wt)
        k = np.searchsorted(cdf, 1 - alpha - 1e-12)
        half[t] = s_sorted[k] if k < s_sorted.size else math.inf
    return -half, half


def gauss_td(r, delta, n_test, alpha):
    """M4: parametric combination of the same information used by TD-CP."""
    z = stats.norm.ppf(1 - alpha / 2)
    centre = float(np.mean(r) + np.mean(delta))
    sd = float(np.sqrt(np.mean(r**2) + np.var(delta, ddof=1)))
    return _const(n_test, centre - z * sd, centre + z * sd)


def target_cp(e, n_test, alpha):
    """M5: split conformal on k labelled transfer standards (requires reference values)."""
    q = conformal_quantile(np.abs(e), 1 - alpha)
    return _const(n_test, -q, q)


def pooled_cp(r, e, n_test, alpha):
    """M6: pooled primary + labelled target residuals (requires reference values)."""
    q = conformal_quantile(np.abs(np.r_[r, e]), 1 - alpha)
    return _const(n_test, -q, q)


# ---------------------------------------------------------------- proposed
def _signed_conv_bounds(r, delta, alpha):
    """Two-sided bounds of the signed convolution r_i + delta_j with an (n+1) correction."""
    S = np.sort((np.asarray(r)[:, None] + np.asarray(delta)[None, :]).ravel())
    n, k = len(r), len(delta)
    idx = math.ceil((1 - alpha / 2) * (n + 1) * k - 1e-9)
    if idx > S.size:
        return -math.inf, math.inf
    return float(S[S.size - idx]), float(S[idx - 1])


def td_cp(r, delta, n_test, alpha):
    """Proposed TD-CP: signed convolution of primary residuals and cross-fitted discrepancies."""
    lo, hi = _signed_conv_bounds(r, delta, alpha)
    return _const(n_test, lo, hi)


def td_cp_abs(r, delta, n_test, alpha):
    """Ablation A2: absolute (symmetric) convolution scores |r_i + delta_j|."""
    S = np.sort(np.abs(np.asarray(r)[:, None] + np.asarray(delta)[None, :]).ravel())
    n, k = len(r), len(delta)
    idx = math.ceil((1 - alpha) * (n + 1) * k - 1e-9)
    q = float(S[idx - 1]) if idx <= S.size else math.inf
    return _const(n_test, -q, q)


def td_sum(r, delta, n_test, alpha):
    """Ablation A3: union-bound style sum of marginal quantiles."""
    q = conformal_quantile(np.abs(r), 1 - alpha / 2) + float(np.quantile(np.abs(delta), 1 - alpha / 2, method="higher"))
    return _const(n_test, -q, q)


def _jackplus(centres: np.ndarray, radii: np.ndarray, n_plus_one_k: int, alpha: float):
    """Jackknife+ bounds (Barber et al., 2021) from per-test centres (n_test, k) and radii (k, m)."""
    m_tot = n_plus_one_k
    hi_idx = math.ceil((1 - alpha) * m_tot - 1e-9)
    n_vals = centres.shape[1] * radii.shape[1]
    lo_idx = n_vals + 1 - hi_idx  # mirror of hi_idx; equals floor(alpha(n+1)) in Barber et al.'s notation
    n_test, k = centres.shape
    lo = np.empty(n_test)
    hi = np.empty(n_test)
    for t in range(n_test):
        up = (centres[t][:, None] + radii).ravel()
        dn = (centres[t][:, None] - radii).ravel()
        hi[t] = np.partition(up, hi_idx - 1)[hi_idx - 1] if hi_idx <= up.size else math.inf
        lo[t] = np.partition(dn, lo_idx - 1)[lo_idx - 1] if lo_idx >= 1 else -math.inf
    return lo, hi


def td_cp_plus(r, delta, yhat_loo, yhat, alpha):
    """TD-CP+ (added after the pre-registered analysis, see S2): jackknife+-style TD-CP.

    yhat_loo[t, j] = f(T_{-j}(x_t^S)). Radii |r_i + delta_j| are attached to the
    leave-one-out centre of their own map j. Upper bound: ceil((1-alpha)(n+1)k)-th
    smallest of {centre_j + radius_ij}; lower bound: the mirrored order statistic of
    {centre_j - radius_ij}. Returned as offsets from yhat.
    """
    radii = np.abs(np.asarray(r)[None, :] + np.asarray(delta)[:, None])  # (k, n)
    lo, hi = _jackplus(yhat_loo, radii, (len(r) + 1) * len(delta), alpha)
    return lo - yhat, hi - yhat


def target_cp_plus(e, yhat_loo, yhat, alpha):
    """Jackknife+ with labelled target residuals (requires reference values)."""
    radii = np.abs(np.asarray(e))[:, None]  # (k, 1)
    lo, hi = _jackplus(yhat_loo, radii, len(e) + 1, alpha)
    return lo - yhat, hi - yhat


LABEL_FREE = ["naive_cp", "leverage", "weighted_cp", "gauss_td", "td_cp", "td_cp_abs", "td_cp_plus"]
LABELLED = ["target_cp", "pooled_cp", "target_cp_plus"]
ABLATIONS = ["td_cp_insample", "td_sum"]
ALL_METHODS = LABEL_FREE + LABELLED + ABLATIONS


def all_intervals(ctx: dict, alpha: float) -> dict[str, tuple[np.ndarray, np.ndarray]]:
    """Compute every method's offsets from a context dictionary produced by the runner."""
    n_test = ctx["n_test"]
    r, d, d_in, e = ctx["r"], ctx["delta_cf"], ctx["delta_in"], ctx["e"]
    out = {
        "naive_cp": naive_cp(r, n_test, alpha),
        "weighted_cp": weighted_cp(r, ctx["feat_cal"], ctx["feat_test"], alpha, ctx.get("seed", 0)),
        "gauss_td": gauss_td(r, d, n_test, alpha),
        "td_cp": td_cp(r, d, n_test, alpha),
        "target_cp": target_cp(e, n_test, alpha),
        "pooled_cp": pooled_cp(r, e, n_test, alpha),
        "td_cp_insample": td_cp(r, d_in, n_test, alpha),
        "td_cp_abs": td_cp_abs(r, d, n_test, alpha),
        "td_sum": td_sum(r, d, n_test, alpha),
        "td_cp_plus": td_cp_plus(r, d, ctx["yhat_loo"], ctx["yhat"], alpha),
        "target_cp_plus": target_cp_plus(e, ctx["yhat_loo"], ctx["yhat"], alpha),
    }
    if ctx.get("leverage_test") is not None:
        out["leverage"] = leverage_interval(r, ctx["leverage_test"], ctx["n_components"], alpha)
    return out
