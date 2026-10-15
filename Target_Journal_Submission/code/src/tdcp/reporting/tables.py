"""Machine-generated tables (CSV + Markdown). No number is typed by hand."""
from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd

from tdcp.data.datasets import load

METHOD_LABELS = {
    "naive_cp": "Naive CP (primary residuals)",
    "leverage": "Leverage PI (classical)",
    "weighted_cp": "Weighted CP (covariate shift)",
    "gauss_td": "Gaussian TD (parametric)",
    "td_cp": "TD-CP signed (pre-specified)",
    "td_cp_abs": "TD-CP absolute scores",
    "td_cp_plus": "TD-CP+ (jackknife+)",
    "target_cp_plus": "Target CP+ (k labelled)",
    "target_cp": "Target CP (k labelled)",
    "pooled_cp": "Pooled CP (k labelled)",
    "td_cp_insample": "TD-CP w/o cross-fitting",
    "td_sum": "TD-sum (union bound)",
    "naive_cp_primary_test": "Naive CP on primary test spectra",
}
LABEL_FREE_ORDER = ["naive_cp", "leverage", "weighted_cp", "gauss_td", "td_cp", "td_cp_abs", "td_cp_plus"]
LABELLED_ORDER = ["target_cp", "target_cp_plus", "pooled_cp"]
ABLATION_ORDER = ["td_cp_plus", "td_cp_abs", "td_cp", "td_cp_insample", "td_sum", "gauss_td", "naive_cp"]


def _fmt(x, nd=3):
    if isinstance(x, (float, np.floating)):
        if np.isinf(x):
            return "∞"
        if np.isnan(x):
            return "–"
        return f"{x:.{nd}f}"
    return str(x)


def _save(df: pd.DataFrame, path: Path, title: str):
    df.to_csv(path.with_suffix(".csv"), index=False)
    md = [f"**{title}**", "", "| " + " | ".join(df.columns) + " |", "|" + "---|" * len(df.columns)]
    for _, r in df.iterrows():
        md.append("| " + " | ".join(_fmt(v) for v in r.values) + " |")
    path.with_suffix(".md").write_text("\n".join(md) + "\n")


def dataset_table(raw_dir: Path, tables: Path) -> None:
    rows = []
    for name in ("corn", "tablets"):
        d = load(name, raw_dir)
        for j, p in enumerate(d.properties):
            y = d.y[:, j]
            rows.append(dict(dataset=name, instruments=", ".join(d.instruments), n_samples=d.n_samples,
                             n_channels=d.wavelengths.size,
                             range_nm=f"{d.wavelengths.min():.0f}–{d.wavelengths.max():.0f}",
                             property=p, y_mean=float(np.nanmean(y)), y_sd=float(np.nanstd(y, ddof=1)),
                             y_min=float(np.nanmin(y)), y_max=float(np.nanmax(y))))
    _save(pd.DataFrame(rows), tables / "table1_datasets", "Table 1. Datasets")


def _summary(scen: pd.DataFrame, methods: list[str], pooled: bool = False) -> pd.DataFrame:
    rows = []
    scen = scen.assign(dataset="corn + tablets") if pooled else scen
    for (ds, tr), g in scen.groupby(["dataset", "transfer"]):
        for m in methods:
            h = g[g.method == m]
            if h.empty:
                continue
            rows.append(dict(dataset=ds, transfer=tr.upper(), method=METHOD_LABELS[m], scenarios=len(h),
                             mean_coverage=h.coverage.mean(), min_coverage=h.coverage.min(),
                             pct_valid=100 * h.valid.mean(), median_width_sd=h.width_norm.median(),
                             median_IS_sd=h.is_norm.median(), pct_infinite=100 * h.frac_infinite.mean()))
    return pd.DataFrame(rows)


def make_tables(results: Path, tables: Path, log) -> None:
    scen = pd.read_csv(results / "scenario_results.csv")
    main = scen[(scen.experiment == "main") & (scen.alpha == 0.1)]
    _save(_summary(main, LABEL_FREE_ORDER + LABELLED_ORDER, pooled=True), tables / "table2_main_results",
          "Table 2. Main results at alpha = 0.10, 30 scenarios per transfer method (scenario means over repetitions)")
    _save(_summary(main, LABEL_FREE_ORDER + LABELLED_ORDER), tables / "tableS2_main_by_dataset",
          "Table S2. Main results at alpha = 0.10 by dataset")
    _save(_summary(main, ABLATION_ORDER, pooled=True), tables / "table4_ablation", "Table 4. Ablation of TD-CP components (alpha = 0.10)")

    t = pd.read_csv(results / "statistical_tests.csv")
    if not t.empty:
        t = t.assign(comparator=t.comparator.map(METHOD_LABELS))
        cols = ["metric", "comparator", "n_scenarios", "median_ref", "median_comp", "median_diff", "ci95_low",
                "ci95_high", "rank_biserial", "p_value", "p_holm", "ref_better_fraction"]
        _save(t[cols], tables / "table3_statistical_tests",
              "Table 3. TD-CP vs comparators: paired Wilcoxon over scenarios (Holm-adjusted)")

    # alpha calibration
    allm = scen[scen.experiment == "main"]
    a = (allm[allm.method.isin(["naive_cp", "leverage", "weighted_cp", "gauss_td", "td_cp", "td_cp_abs", "td_cp_plus", "target_cp", "target_cp_plus"])]
         .groupby(["alpha", "transfer", "method"]).agg(mean_coverage=("coverage", "mean"), pct_valid=("valid", "mean"),
                                                       median_IS_sd=("is_norm", "median")).reset_index())
    a["pct_valid"] *= 100
    a["nominal"] = 1 - a["alpha"]
    a["method"] = a["method"].map(METHOD_LABELS)
    _save(a[["alpha", "nominal", "transfer", "method", "mean_coverage", "pct_valid", "median_IS_sd"]],
          tables / "tableS3_alpha_levels", "Table S3. Coverage at different nominal levels")

    # robustness overview
    rob = scen[(scen.alpha == 0.1) & (scen.experiment != "main") & scen.method.isin(["naive_cp", "gauss_td", "td_cp", "td_cp_abs", "td_cp_plus", "target_cp", "target_cp_plus"])]
    if not rob.empty:
        rob = rob.copy()
        rob["condition"] = rob.apply(_condition, axis=1)
        r = (rob.groupby(["experiment", "condition", "transfer", "method"])
             .agg(scenarios=("coverage", "size"), mean_coverage=("coverage", "mean"), pct_valid=("valid", "mean"),
                  median_IS_sd=("is_norm", "median"), mean_rmsep_ratio=("rmsep", "mean")).reset_index())
        r["pct_valid"] *= 100
        r["method"] = r["method"].map(METHOD_LABELS)
        r = r.drop(columns="mean_rmsep_ratio")
        _save(r, tables / "table6_robustness", "Table 6. Robustness and generalisation experiments (alpha = 0.10)")

    sl = pd.read_csv(results / "split_level_coverage.csv")
    sl["method"] = sl["method"].map(METHOD_LABELS)
    _save(sl, tables / "tableS4_split_level_coverage", "Table S4. Split-level (training-conditional) coverage at alpha = 0.10, main experiment")
    st = pd.read_csv(results / "stratum_consistency.csv")
    st["comparator"] = st["comparator"].map(METHOD_LABELS)
    _save(st, tables / "tableS5_stratum_consistency", "Table S5. Fraction of scenarios in which TD-CP+ beats each comparator, per dataset x transfer stratum")
    tv = pd.read_csv(results / "validity_tolerance.csv")
    tv = tv[tv.method.isin(["naive_cp", "gauss_td", "td_cp", "td_cp_abs", "td_cp_plus", "target_cp", "target_cp_plus"])]
    tv = tv.pivot_table(index=["transfer", "method"], columns="tolerance", values="frac_valid").reset_index()
    tv.columns = ["transfer", "method"] + [f"valid_tol_{c}" for c in tv.columns[2:]]
    tv["method"] = tv["method"].map(METHOD_LABELS)
    _save(tv, tables / "tableS6_validity_tolerance", "Table S6. Fraction of valid scenarios for different tolerances (alpha = 0.10)")

    # computational cost (main experiment, per split)
    c = (main.groupby(["dataset", "transfer"]).agg(t_calibration_s=("t_calibration", "mean"), t_transfer_s=("t_transfer", "mean"),
                                                    t_crossfit_s=("t_crossfit", "mean"), t_interval_s=("t_interval", "mean"))
         .reset_index())
    _save(c, tables / "table7_compute", "Table 7. Mean wall-clock time per split (s), single CPU core")

    # full per-scenario supplementary table
    s = main[main.method.isin(LABEL_FREE_ORDER + LABELLED_ORDER)][
        ["dataset", "primary", "secondary", "prop", "transfer", "method", "coverage", "coverage_se", "width_norm", "is_norm",
         "rmsep", "rmsep_primary", "delta_cf_sd", "delta_test_sd", "spearman_r_delta"]].copy()
    s["method"] = s["method"].map(METHOD_LABELS)
    _save(s, tables / "tableS1_per_scenario", "Table S1. Per-scenario results (alpha = 0.10)")
    log.info("tables written to %s", tables)


def _condition(r) -> str:
    e = r["experiment"]
    if e == "k_sensitivity":
        return f"k={int(r['k'])}"
    if e == "noise":
        return f"noise={r['noise']}"
    if e == "simulated":
        return f"severity={r['secondary'][3:]}"
    if e == "preprocessing":
        return r["preprocess"]
    if e == "pds_window":
        return f"PDS window {2 * int(r['pds_half_window']) + 1}"
    if e == "parsimonious_pls":
        return "PLS, 1-SE rule"
    if e == "ridge_model":
        return "ridge"
    if e == "biased_standards":
        return "standards from lower half of y"
    if e == "kennard_stone":
        return "KS selection"
    if e == "official_split":
        return "IDRC official split"
    if e == "no_standardisation":
        return "no transfer"
    return e
