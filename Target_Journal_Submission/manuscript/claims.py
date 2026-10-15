"""Claim–evidence audit: each qualitative statement in the manuscript is asserted here
against the machine-generated numbers. The build stops if any claim is unsupported."""
from __future__ import annotations


def check_claims(V: dict) -> list[str]:
    R = V["_raw"]
    checks = []

    def claim(text, ok):
        checks.append((text, bool(ok)))

    for tr in ("pds", "ds"):
        claim(f"naive CP under-covers after {tr}", R[f"naive_cp_{tr}_a10"]["cov"] < 0.70)
        claim(f"leverage PI under-covers after {tr}", R[f"leverage_{tr}_a10"]["cov"] < 0.75)
        claim(f"weighted CP under-covers or is infinite after {tr}", R[f"weighted_cp_{tr}_a10"]["cov"] < 0.80 and R[f"weighted_cp_{tr}_a10"]["inf"] > 0)
        claim(f"TD-CP+ valid in all scenarios at alpha 0.10 ({tr})", R[f"td_cp_plus_{tr}_a10"]["valid"] == 1.0)
        claim(f"TD-CP+ conservative by <= 0.05 ({tr})", R[f"td_cp_plus_{tr}_a10"]["cov"] <= 0.95)
        claim(f"TD-CP+ median IS not worse than labelled Target CP+ ({tr})", R[f"td_cp_plus_{tr}_a10"]["IS"] <= R[f"target_cp_plus_{tr}_a10"]["IS"])
        claim(f"Target CP infinite at alpha 0.05 with k=10 ({tr})", R[f"target_cp_{tr}_a5"]["inf"] == 1.0)
        claim(f"TD-CP+ valid in >=90% at alpha 0.05 ({tr})", R[f"td_cp_plus_{tr}_a5"]["valid"] >= 0.9)
        claim(f"TD-CP+ valid in all scenarios at alpha 0.20 ({tr})", R[f"td_cp_plus_{tr}_a20"]["valid"] == 1.0)
        claim(f"no cross-fitting under-covers ({tr})", R[f"td_cp_insample_{tr}_a10"]["cov"] < 0.80)
        claim(f"union-bound sum over-covers ({tr})", R[f"td_sum_{tr}_a10"]["cov"] > 0.95)
        claim(f"k=8 TD-CP+ valid everywhere ({tr})", R[f"k8_td_cp_plus_{tr}"]["valid"] == 1.0)
        claim(f"Target CP infinite for k=5 and 8 ({tr})", R[f"k5_target_cp_{tr}"]["inf"] == 1.0 and R[f"k8_target_cp_{tr}"]["inf"] == 1.0)
    claim("pre-specified signed TD-CP misses criterion for DS", R["td_cp_ds_a10"]["valid"] < 0.8)
    claim("pre-specified signed TD-CP misses criterion for PDS", R["td_cp_pds_a10"]["valid"] < 0.8)
    claim("Gaussian TD misses criterion for DS", R["gauss_td_ds_a10"]["valid"] < 0.8)
    claim("Gaussian TD meets criterion for PDS", R["gauss_td_pds_a10"]["valid"] >= 0.8)
    claim("TD-CP+ k=5 DS not valid everywhere", R["k5_td_cp_plus_ds"]["valid"] < 1.0)
    claim("in-domain naive coverage close to nominal", 0.88 <= R["primary_cov"] <= 0.92)
    claim("in-sample DS discrepancies ~ zero", R["dsd_in_ratio_ds"] < 0.01)
    claim("in-sample PDS discrepancies smaller than cross-fitted", R["dsd_in_ratio_pds"] < 0.9)
    claim("cross-fitted discrepancy SD close to held-out", 0.8 <= R["dsd_ratio_median"] <= 1.3)
    claim("weak r-delta dependence on average", abs(R["spearman_mean"]) < 0.2)
    g = R["t_td_cp_plus_gauss_td_IS"]
    claim("Gaussian TD tends to lower IS than TD-CP+ (CI excludes 0; both p values reported)", g["rank_biserial"] > 0 and g["ci95_low"] > 0)
    tp = R["t_td_cp_plus_target_cp_plus_IS"]
    claim("TD-CP+ IS significantly lower than Target CP+", tp["p_holm"] < 0.05 and tp["rank_biserial"] < 0)
    for c in ("naive_cp", "leverage", "weighted_cp"):
        x = R[f"t_td_cp_plus_{c}_gap"]
        claim(f"TD-CP+ smaller coverage gap than {c}", x["p_holm"] < 0.05 and x["rank_biserial"] < 0)
    x = R["t_td_cp_plus_naive_cp_IS"]
    claim("TD-CP+ lower IS than naive", x["p_holm"] < 0.05 and x["rank_biserial"] < 0)
    x = R["t_td_cp_plus_gauss_td_gap"]
    claim("TD-CP+ larger |gap| than Gaussian (over-coverage)", x["rank_biserial"] > 0)
    for k in ("pls1se", "pdsw3", "pdsw7", "pdsw11", "ks", "snv", "ridge", "noise5", "noise10", "noise20", "nostd", "official", "sim1", "sim2", "sim3", "k5", "k8", "k15", "k20", "k30"):
        for tr in ("pds", "ds", "none"):
            a, b = R.get(f"{k}_td_cp_plus_{tr}"), R.get(f"{k}_td_cp_{tr}")
            if a and b:
                claim(f"confirmatory: TD-CP+ validity >= signed TD-CP ({k},{tr})", a["valid"] >= b["valid"])
    for tr in ("pds", "ds"):
        claim(f"parsimonious PLS: naive still under-covers ({tr})", R[f"pls1se_naive_cp_{tr}"]["cov"] < 0.7)
        claim(f"parsimonious PLS: TD-CP+ valid everywhere ({tr})", R[f"pls1se_td_cp_plus_{tr}"]["valid"] == 1.0)
    for w in (3, 7, 11):
        claim(f"PDS window {w}: TD-CP+ valid everywhere", R[f"pdsw{w}_td_cp_plus_pds"]["valid"] == 1.0)
        claim(f"PDS window {w}: naive under-covers", R[f"pdsw{w}_naive_cp_pds"]["cov"] < 0.6)
    for ds in ("corn", "tablets"):
        for tr in ("pds", "ds"):
            a = R[f"sl_td_cp_plus_{ds}_{tr}"]["frac_below_080"]; b = R[f"sl_naive_cp_primary_test_{ds}_{tr}"]["frac_below_080"]
            claim(f"split-level: TD-CP+ tail close to in-domain CP ({ds},{tr})", a <= b + 0.07)
            claim(f"split-level: naive mostly below 0.8 ({ds},{tr})", R[f"sl_naive_cp_{ds}_{tr}"]["frac_below_080"] > 0.5)
    st = R["strata"]
    for comp in ("naive_cp", "weighted_cp"):
        claim(f"stratum consistency vs {comp}", (st[st.comparator == comp].frac_smaller_gap >= 0.8).all())
    claim("TD-CP+ valid at zero tolerance in >=95% of scenarios", R["tol0_td_cp_plus_pds"] >= 0.95 and R["tol0_td_cp_plus_ds"] >= 0.95)
    claim("biased standards + DS: TD-CP+ not reliably valid (stated)", R["biased_td_cp_plus_ds"]["valid"] < 0.8)
    claim("biased standards + DS: labelled target CP+ equally affected (stated)", R["biased_target_cp_plus_ds"]["valid"] <= R["biased_td_cp_plus_ds"]["valid"] + 0.1)
    claim("biased standards + PDS: TD-CP+ valid everywhere", R["biased_td_cp_plus_pds"]["valid"] == 1.0)
    x = R["t_td_cp_plus_target_t_IS"]
    claim("TD-CP+ slightly lower IS than target t (stated with p)", x["rank_biserial"] < 0 and x["p_holm"] < 0.05)
    x = R["t_td_cp_plus_target_t_gap"]
    claim("TD-CP+ larger |gap| than target t (stated)", x["rank_biserial"] > 0)
    claim("target t valid 100% PDS", R["target_t_pds_a10"]["valid"] == 1.0)
    claim("TD-CP+ higher validity than target t under DS", R["td_cp_plus_ds_a10"]["valid"] > R["target_t_ds_a10"]["valid"])
    claim("as efficient as target t under PDS (tie: |median diff| < 0.05 SD)", abs(R["pair_t_pds"]["med"]) < 0.05)
    claim("more efficient than target t under DS", R["pair_t_ds"]["frac"] > 0.7 and R["pair_t_ds"]["med"] < 0)
    claim("no-standardisation: TD-CP+ much less efficient than signed", R["nostd_td_cp_plus_none"]["IS"] > 1.5 * R["nostd_td_cp_none"]["IS"])
    bad = [t for t, ok in checks if not ok]
    for t, ok in checks:
        print(("OK   " if ok else "FAIL ") + t)
    if bad:
        raise SystemExit(f"{len(bad)} unsupported claims: {bad}")
    return [t for t, _ in checks]
