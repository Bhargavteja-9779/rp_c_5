"""Extract every number quoted in the manuscript from machine-generated result files."""
from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import pandas as pd

M_ALL = ["naive_cp", "leverage", "weighted_cp", "gauss_td", "td_cp", "td_cp_abs", "td_cp_plus", "target_cp",
         "target_cp_plus", "pooled_cp", "td_cp_insample", "td_sum", "naive_cp_primary_test"]


def _f(x, nd=3):
    if x is None or (isinstance(x, float) and np.isnan(x)):
        return "n/a"
    if np.isinf(x):
        return "∞"
    return f"{x:.{nd}f}".replace("-", "−")


def _pct(x):
    return f"{100 * x:.0f}%"


def _p(p):
    return "< 0.001" if p < 0.001 else f"= {p:.3f}"


def compute_values(root: Path):
    res = root / "results"
    scen = pd.read_csv(res / "scenario_results.csv")
    tests = pd.read_csv(res / "statistical_tests.csv")
    t1 = pd.read_csv(root / "tables" / "table1_datasets.csv")
    V: dict = {}
    raw = {}  # numeric values for claim checks

    main = scen[scen.experiment == "main"]
    for (a, tr, m), g in main.groupby(["alpha", "transfer", "method"]):
        key = f"{m}_{tr}_a{int(round(a * 100))}"
        raw[key] = dict(cov=g.coverage.mean(), valid=g.valid.mean(), IS=g.is_norm.median(), W=g.width_norm.median(),
                        mincov=g.coverage.min(), inf=g.frac_infinite.mean(), n=len(g))
        V[key + "_cov"] = _f(raw[key]["cov"])
        V[key + "_mincov"] = _f(raw[key]["mincov"])
        V[key + "_valid"] = _pct(raw[key]["valid"])
        V[key + "_IS"] = _f(raw[key]["IS"], 2)
        V[key + "_W"] = _f(raw[key]["W"], 2)
        V[key + "_inf"] = f"{100 * raw[key]['inf']:.0f}%"
    for (ds, tr, m), g in main[main.alpha == 0.1].groupby(["dataset", "transfer", "method"]):
        key = f"{m}_{ds}_{tr}"
        raw[key] = dict(cov=g.coverage.mean(), valid=g.valid.mean(), IS=g.is_norm.median())
        V[key + "_cov"] = _f(raw[key]["cov"]); V[key + "_valid"] = _pct(raw[key]["valid"]); V[key + "_IS"] = _f(raw[key]["IS"], 2)

    # convenience aliases used in the abstract
    for tr in ("pds", "ds"):
        V[f"naive_cov_{tr}"] = V[f"naive_cp_{tr}_a10_cov"]
        V[f"plus_cov_{tr}"] = V[f"td_cp_plus_{tr}_a10_cov"]
        V[f"plus_valid_{tr}"] = V[f"td_cp_plus_{tr}_a10_valid"]

    # diagnostics
    d = main[(main.alpha == 0.1) & (main.method == "td_cp_plus")]
    raw["spearman_mean"] = d.spearman_r_delta.mean(); raw["spearman_min"] = d.spearman_r_delta.min(); raw["spearman_max"] = d.spearman_r_delta.max()
    V["spearman_mean"], V["spearman_min"], V["spearman_max"] = _f(raw["spearman_mean"], 2), _f(raw["spearman_min"], 2), _f(raw["spearman_max"], 2)
    ratio = d.rmsep / d.rmsep_primary
    raw["rmsep_ratio_median"] = ratio.median(); V["rmsep_ratio_median"] = _f(ratio.median(), 1)
    V["rmsep_ratio_min"], V["rmsep_ratio_max"] = _f(ratio.min(), 1), _f(ratio.max(), 1)
    dr = d.delta_cf_sd / d.delta_test_sd
    raw["dsd_ratio_median"] = dr.median(); V["dsd_ratio_median"] = _f(dr.median(), 2); V["dsd_ratio_min"] = _f(dr.min(), 2); V["dsd_ratio_max"] = _f(dr.max(), 2)
    ins = main[(main.alpha == 0.1) & (main.method == "td_cp_insample")]
    for tr in ("pds", "ds"):
        g = ins[ins.transfer == tr]
        raw[f"dsd_in_ratio_{tr}"] = (g.delta_in_sd / g.delta_cf_sd).median()
        V[f"dsd_in_ratio_{tr}"] = _f(raw[f"dsd_in_ratio_{tr}"], 2)
    prim = main[(main.alpha == 0.1) & (main.method == "naive_cp_primary_test")]
    raw["primary_cov"] = prim.coverage.mean(); V["primary_cov"] = _f(prim.coverage.mean())
    V["primary_cov_min"] = _f(prim.coverage.min()); V["primary_cov_max"] = _f(prim.coverage.max())
    V["ncomp_corn"] = f"{int(main[(main.dataset == 'corn')].n_components.min())}–{int(main[(main.dataset == 'corn')].n_components.max())}"
    p1 = scen[(scen.experiment == "parsimonious_pls") & (scen.alpha == 0.1) & (scen.method == "td_cp_plus")]
    V["ncomp1se_corn"] = f"{int(p1[p1.dataset == 'corn'].n_components.median())}"
    V["ncomp_corn_med"] = f"{int(main[(main.dataset == 'corn') & (main.method == 'td_cp_plus')].n_components.median())}"
    V["ncomp_tab"] = f"{int(main[(main.dataset == 'tablets')].n_components.min())}–{int(main[(main.dataset == 'tablets')].n_components.max())}"

    # tests
    V["n_tests"] = str(len(tests))
    for _, r in tests.iterrows():
        key = f"t_{r.reference}_{r.comparator}_{'gap' if r.metric == 'abs_gap' else 'IS'}"
        raw[key] = r.to_dict()
        V[key + "_p"] = _p(r.p_holm)
        V[key + "_praw"] = _p(r.p_value)
        V[key + "_rb"] = _f(r.rank_biserial, 2)
        V[key + "_md"] = _f(r.median_diff, 3)
        V[key + "_ci"] = f"[{_f(r.ci95_low, 3)}, {_f(r.ci95_high, 3)}]"
        V[key + "_better"] = _pct(r.ref_better_fraction)
        V[key + "_n"] = str(int(r.n_scenarios))

    # robustness experiments (alpha = 0.1)
    rob = scen[(scen.alpha == 0.1) & (scen.experiment != "main")]
    def cond(e, extra=None):
        g = rob[rob.experiment == e]
        return g if extra is None else g[extra(g)]
    specs = {
        "ks": ("kennard_stone", None), "snv": ("preprocessing", None), "ridge": ("ridge_model", None),
        "nostd": ("no_standardisation", None), "official": ("official_split", None),
        "pls1se": ("parsimonious_pls", None), "biased": ("biased_standards", None),
    }
    for w in (1, 3, 5):
        specs[f"pdsw{2 * w + 1}"] = ("pds_window", lambda g, w=w: g.pds_half_window == w)
    for lvl in (0.005, 0.01, 0.02):
        specs[f"noise{int(lvl * 1000)}"] = ("noise", lambda g, l=lvl: np.isclose(g.noise, l))
    for sev in (1, 2, 3):
        specs[f"sim{sev}"] = ("simulated", lambda g, s=sev: g.secondary == f"sim{s}")
    for kk in (5, 8, 15, 20, 30):
        specs[f"k{kk}"] = ("k_sensitivity", lambda g, k=kk: g.k == k)
    for name, (e, flt) in specs.items():
        g = cond(e, flt)
        for (tr, m), h in g.groupby(["transfer", "method"]):
            key = f"{name}_{m}_{tr}"
            raw[key] = dict(cov=h.coverage.mean(), valid=h.valid.mean(), IS=h.is_norm.median(), W=h.width_norm.median(), n=len(h),
                            inf=h.frac_infinite.mean())
            V[key + "_cov"] = _f(raw[key]["cov"]); V[key + "_valid"] = _pct(raw[key]["valid"]); V[key + "_IS"] = _f(raw[key]["IS"], 2)
            V[key + "_W"] = _f(raw[key]["W"], 2); V[key + "_inf"] = _pct(raw[key]["inf"])
    # data
    V["corn_n"] = str(int(t1[t1.dataset == "corn"].n_samples.iloc[0])); V["corn_p"] = str(int(t1[t1.dataset == "corn"].n_channels.iloc[0]))
    V["tab_n"] = str(int(t1[t1.dataset == "tablets"].n_samples.iloc[0])); V["tab_p"] = str(int(t1[t1.dataset == "tablets"].n_channels.iloc[0]))
    V["tab_master"] = str(int(t1[t1.dataset == "tablets"].n_samples.iloc[0]) - 210)
    V["n_main_splits"] = f"{int(main[(main.alpha == 0.1) & (main.method == 'td_cp')].reps.sum()):,}"
    # compute
    comp = main[(main.alpha == 0.1) & (main.method == "td_cp_plus")]
    for (ds, tr), g in comp.groupby(["dataset", "transfer"]):
        V[f"t_cal_{ds}_{tr}"] = f"{1000 * g.t_calibration.mean():.0f}"
        V[f"t_cf_{ds}_{tr}"] = f"{1000 * g.t_crossfit.mean():.0f}"
        V[f"t_int_{ds}_{tr}"] = f"{1000 * g.t_interval.mean():.1f}"
    sl = pd.read_csv(res / "split_level_coverage.csv")
    for _, r in sl.iterrows():
        key = f"sl_{r.method}_{r.dataset}_{r.transfer}"
        raw[key] = r.to_dict()
        V[key + "_below"] = f"{100 * r.frac_below_080:.0f}%"
        V[key + "_p10"] = _f(r.p10_cov, 2)
    tv = pd.read_csv(res / "validity_tolerance.csv")
    for _, r in tv.iterrows():
        key = f"tol{int(round(r.tolerance * 100))}_{r.method}_{r.transfer}"
        raw[key] = r.frac_valid
        V[key + "_a"] = f"{100 * r.frac_valid:.0f}%"
    st = pd.read_csv(res / "stratum_consistency.csv")
    raw["strata"] = st
    mm = main[main.alpha == 0.1].pivot_table(index=["dataset", "primary", "secondary", "prop", "transfer"], columns="method",
                                              values="is_norm").reset_index()
    for tr, g in mm.groupby("transfer"):
        d = g["td_cp_plus"] - g["target_t"]
        raw[f"pair_t_{tr}"] = dict(frac=float((d < 0).mean()), med=float(d.median()))
        V[f"pair_t_{tr}"] = f"{100 * (d < 0).mean():.0f}%"
    sc = pd.read_csv(res / "scaling.csv")
    for _, r in sc.iterrows():
        tag = "plus" if "plus" in r.method else "signed"
        V[f"scal_{tag}_{int(r.n)}_{int(r.k)}"] = f"{r.ms_per_test_sample:.2f}" if r.ms_per_test_sample >= 0.01 else f"{r.ms_per_test_sample:.4f}"
    b = raw.get("biased_td_cp_plus_ds")
    if b:
        V["biased_td_cp_plus_ds_valid_inv"] = f"{100 * (1 - b['valid']):.0f}%"
    metrics = json.loads((res / "metrics.json").read_text())
    V["n_raw_rows"] = f"{metrics['n_raw_rows']:,}"
    V["_raw"] = raw
    return V, {"scen": scen, "tests": tests, "t1": t1}
