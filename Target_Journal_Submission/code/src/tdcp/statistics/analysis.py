"""Scenario-level aggregation and pre-registered statistical tests.

Unit of analysis: a *scenario* = dataset x primary x secondary x property x
transfer method (x experimental factor). Repetitions within a scenario share
data and are averaged first, so tests across scenarios avoid pseudo-replication.
"""
from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import pandas as pd
from scipy.stats import wilcoxon

SCEN_KEYS = ["experiment", "dataset", "primary", "secondary", "prop", "transfer", "k", "selection",
             "protocol", "preprocess", "model", "noise", "alpha", "method"]
BIG = 1e6  # finite stand-in for +inf in rank-based tests (only ranks are used)


def load_raw(results: Path) -> pd.DataFrame:
    files = sorted(set(results.glob("raw_*.csv")) | set(results.glob("raw_*.csv.gz")))
    frames = [pd.read_csv(f) for f in files if f.name != "raw_results.csv.gz"]
    df = pd.concat(frames, ignore_index=True)
    df["is_norm"] = df["interval_score"] / df["sd_y"]
    df["width_norm"] = df["width"] / df["sd_y"]
    return df


def scenario_table(df: pd.DataFrame) -> pd.DataFrame:
    g = df.groupby(SCEN_KEYS, dropna=False)
    out = g.agg(
        reps=("seed", "nunique"),
        coverage=("coverage", "mean"),
        coverage_sd=("coverage", "std"),
        width_norm=("width_norm", "mean"),
        is_norm=("is_norm", "mean"),
        frac_infinite=("frac_infinite", "mean"),
        rmsep=("rmsep", "mean"),
        rmsep_primary=("rmsep_primary", "mean"),
        rmsecv=("rmsecv", "mean"),
        n_components=("n_components", "median"),
        delta_cf_sd=("delta_cf_sd", "mean"),
        delta_in_sd=("delta_in_sd", "mean"),
        delta_test_sd=("delta_test_sd", "mean"),
        spearman_r_delta=("spearman_r_delta", "mean"),
        below=("below_coverage", "mean"),
        above=("above_coverage", "mean"),
        t_interval=("t_interval_mean", "mean"),
        t_crossfit=("t_crossfit", "mean"),
        t_calibration=("t_calibration", "mean"),
        t_transfer=("t_transfer", "mean"),
    ).reset_index()
    out["coverage_se"] = out["coverage_sd"] / np.sqrt(out["reps"])
    out["gap"] = out["coverage"] - (1 - out["alpha"])
    out["abs_gap"] = out["gap"].abs()
    out["valid"] = out["gap"] >= -0.02
    return out


def _bootstrap_median_ci(d: np.ndarray, B: int, seed: int) -> tuple[float, float]:
    rng = np.random.default_rng(seed)
    idx = rng.integers(0, d.size, size=(B, d.size))
    meds = np.median(d[idx], axis=1)
    return float(np.quantile(meds, 0.025)), float(np.quantile(meds, 0.975))


def paired_tests(scen: pd.DataFrame, ref: str, others: list[str], metric: str, B: int, seed: int) -> list[dict]:
    rows = []
    keys = [k for k in SCEN_KEYS if k != "method"]
    wide = scen.pivot_table(index=keys, columns="method", values=metric, aggfunc="first", dropna=False)
    for m in others:
        if m not in wide or ref not in wide:
            continue
        pair = wide[[ref, m]].dropna()
        a = pair[ref].replace(np.inf, BIG).to_numpy()
        b = pair[m].replace(np.inf, BIG).to_numpy()
        d = a - b
        nz = d[d != 0]
        if nz.size < 5:
            continue
        res = wilcoxon(a, b, zero_method="wilcox", alternative="two-sided")
        ranks = pd.Series(np.abs(nz)).rank().to_numpy()
        wpos, wneg = ranks[nz > 0].sum(), ranks[nz < 0].sum()
        lo, hi = _bootstrap_median_ci(d, B, seed)
        rows.append(dict(metric=metric, reference=ref, comparator=m, n_scenarios=int(d.size),
                         median_ref=float(np.median(a)), median_comp=float(np.median(b)),
                         median_diff=float(np.median(d)), ci95_low=lo, ci95_high=hi,
                         wilcoxon_W=float(res.statistic), p_value=float(res.pvalue),
                         rank_biserial=float((wpos - wneg) / (wpos + wneg)),
                         ref_better_fraction=float(np.mean(d < 0))))
    return rows


def holm(p: np.ndarray) -> np.ndarray:
    order = np.argsort(p)
    m = p.size
    adj = np.empty(m)
    run = 0.0
    for i, j in enumerate(order):
        run = max(run, (m - i) * p[j])
        adj[j] = min(1.0, run)
    return adj


def analyse(results: Path, cfg: dict, log) -> None:
    df = load_raw(results)
    scen = scenario_table(df)
    scen.to_csv(results / "scenario_results.csv", index=False)
    st = cfg["statistics"]
    main = scen[(scen.experiment == "main") & (scen.alpha == 0.1)]
    comparators = ["naive_cp", "leverage", "weighted_cp", "gauss_td", "td_cp", "td_cp_abs", "td_cp_insample", "td_sum",
                   "target_cp", "target_cp_plus", "pooled_cp"]
    tests = []
    for ref in ("td_cp_plus", "td_cp"):  # recommended (post hoc, see S2) and pre-registered TD-CP
        for metric in ("abs_gap", "is_norm"):
            tests += paired_tests(main, ref, [c for c in comparators if c != ref], metric,
                                  st["bootstrap_resamples"], st["bootstrap_seed"])
    tdf = pd.DataFrame(tests)
    if not tdf.empty:
        tdf["p_holm"] = holm(tdf["p_value"].to_numpy())
    tdf.to_csv(results / "statistical_tests.csv", index=False)

    # validity criterion (pre-registered): mean coverage >= 1 - alpha - 0.02 in >= 80% of scenarios
    validity = (scen[scen.experiment == "main"].groupby(["alpha", "transfer", "method"])
                .agg(n=("valid", "size"), frac_valid=("valid", "mean"), mean_cov=("coverage", "mean"),
                     min_cov=("coverage", "min"), median_is_norm=("is_norm", "median"),
                     median_width_norm=("width_norm", "median"), frac_inf=("frac_infinite", "mean"))
                .reset_index())
    validity.to_csv(results / "validity_summary.csv", index=False)

    metrics = {
        "n_raw_rows": int(len(df)),
        "n_scenarios_main_alpha0.1": int(main[["dataset", "primary", "secondary", "prop", "transfer"]].drop_duplicates().shape[0]),
        "main_alpha0.1": {
            m: {
                "mean_coverage": float(g.coverage.mean()),
                "frac_scenarios_valid": float(g.valid.mean()),
                "median_is_norm": float(g.is_norm.median()),
                "median_width_norm": float(g.width_norm.median()),
                "mean_frac_infinite": float(g.frac_infinite.mean()),
            }
            for m, g in main.groupby("method")
        },
    }
    (results / "metrics.json").write_text(json.dumps(metrics, indent=2))
    statistics = {"tests": tdf.to_dict(orient="records"),
                  "test": "two-sided Wilcoxon signed-rank on scenario means, Holm-adjusted across all listed comparisons",
                  "effect_size": "matched-pairs rank-biserial correlation (negative => reference smaller)",
                  "ci": f"percentile bootstrap of the median paired difference, B={st['bootstrap_resamples']}"}
    (results / "statistics.json").write_text(json.dumps(statistics, indent=2))
    log.info("analysis: %d scenario rows, %d tests", len(scen), len(tdf))
