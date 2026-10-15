"""Results and discussion, conclusions and declarations (numbers via {placeholders})."""
from __future__ import annotations

from pathlib import Path

import pandas as pd

FIG = None  # set at runtime


def _tbl(path: Path, cols: dict, fmt: dict | None = None, query=None) -> pd.DataFrame:
    df = pd.read_csv(path)
    if query is not None:
        df = query(df)
    df = df[list(cols)].rename(columns=cols)
    fmt = fmt or {}
    for c in df.columns:
        if df[c].dtype.kind == "f":
            nd = fmt.get(c, 3)
            df[c] = df[c].map(lambda x, nd=nd: "∞" if x == float("inf") else f"{x:.{nd}f}")
    return df


def results_blocks(V, T, root: Path):
    f = root / "figures"
    t = root / "tables"
    tab1 = _tbl(t / "table1_datasets.csv", {"dataset": "Dataset", "instruments": "Instruments", "n_samples": "n",
                                            "n_channels": "Channels", "range_nm": "Range (nm)", "property": "Property",
                                            "y_mean": "Mean", "y_sd": "SD", "y_min": "Min", "y_max": "Max"}, {"Mean": 2, "SD": 2, "Min": 2, "Max": 2})
    main_cols = {"dataset": "Dataset", "transfer": "Transfer", "method": "Method", "mean_coverage": "Mean cov.",
                 "min_coverage": "Min cov.", "pct_valid": "Valid (%)", "median_width_sd": "Width/SD", "median_IS_sd": "IS/SD"}
    tab2 = _tbl(t / "table2_main_results.csv", main_cols, {"Valid (%)": 0, "Width/SD": 2, "IS/SD": 2})
    tab3 = _tbl(t / "table3_statistical_tests.csv",
                {"metric": "Metric", "comparator": "Comparator", "n_scenarios": "n", "median_ref": "Median TD-CP+",
                 "median_comp": "Median comp.", "ci95_low": "CI low", "ci95_high": "CI high", "rank_biserial": "r_rb", "p_holm": "p (Holm)"},
                {"r_rb": 2}, query=lambda d: d[(d.reference == "td_cp_plus") & d.comparator.isin(
                    ["Naive CP (primary residuals)", "Leverage PI (classical)", "Weighted CP (covariate shift)",
                     "Gaussian TD (parametric)", "Target CP (k labelled)", "Target CP+ (k labelled)", "Target t-interval (k labelled)"])])
    for c in ("Median TD-CP+", "Median comp.", "CI low", "CI high"):
        tab3[c] = [("∞" if float(v) > 1e5 else ("−∞" if float(v) < -1e5 else v)) if v not in ("∞",) else v for v in tab3[c]]
    tab3.loc[tab3["Median comp."] == "∞", ["CI low", "CI high"]] = "−∞"
    tab3["Metric"] = tab3["Metric"].map({"abs_gap": "|coverage gap|", "is_norm": "IS/SD"})
    tab3["p (Holm)"] = [("<0.001" if float(p) < 0.001 else p) for p in tab3["p (Holm)"]]
    tab6 = _tbl(t / "table6_robustness_compact.csv", {"condition": "Condition", "transfer": "Transfer", "naive_cov": "Naive CP",
                                                     "gauss_cov": "Gauss-TD", "tdcp_signed_cov": "TD-CP signed",
                                                     "tdcp_plus_cov": "TD-CP+", "tdcp_plus_pct_valid": "TD-CP+ valid (%)",
                                                     "target_cp_plus_cov": "Target CP+ (labelled)"}, {"TD-CP+ valid (%)": 0})
    tab6["Transfer"] = tab6["Transfer"].str.upper()
    tab7 = _tbl(t / "table7_compute.csv", {"dataset": "Dataset", "transfer": "Transfer", "t_calibration_s": "PLS + CV (s)",
                                          "t_transfer_s": "Transfer (s)", "t_crossfit_s": "Cross-fitting (s)", "t_interval_s": "Interval (s)"},
                {"PLS + CV (s)": 3, "Transfer (s)": 4, "Cross-fitting (s)": 4, "Interval (s)": 5})

    B = []
    B += [("h1", "4. Results and discussion")]
    B += [("table", tab1, "**Table 1.** Datasets and reference values.")]
    B += [("fig", f / "fig2_spectra.png", "**Fig. 2.** Mean spectra per instrument (top) and mean inter-instrument differences (bottom) for the corn (left) and tablet (right) data.")]
    B += [("h2", "4.1. Calibration and transfer quality")]
    B += [("p", "The selected PLS models used {ncomp_corn} latent variables for corn and {ncomp_tab} for tablets. Transfer was imperfect: "
                "the median ratio of the secondary-instrument RMSEP after transfer to the RMSEP obtained from the primary spectra "
                "of the same test samples was {rmsep_ratio_median} (range {rmsep_ratio_min}–{rmsep_ratio_max}; Table S1), i.e., "
                "the transferred predictions carried an error component absent on the primary instrument. The largest ratios occur "
                "for corn moisture with m5 as primary, which is predicted almost perfectly from m5 spectra, so that any transfer "
                "error dominates. As an in-domain "
                "check of the out-of-fold residual scores, the naive interval applied to the *primary* spectra of the test samples "
                "covered {primary_cov} on average at the nominal 0.90 (scenario range {primary_cov_min}–{primary_cov_max}).")]
    B += [("h2", "4.2. Intervals inherited from the primary instrument are over-confident")]
    B += [("p", "Reusing the primary-instrument interval after transfer (naive CP) gave mean coverages of {naive_cp_pds_a10_cov} "
                "after PDS and {naive_cp_ds_a10_cov} after DS at a nominal 0.90, with individual scenarios as low as "
                "{naive_cp_pds_a10_mincov} (Table 2, Fig. 3). The classical leverage-corrected interval was only marginally better "
                "({leverage_pds_a10_cov} and {leverage_ds_a10_cov}), because leverage measures distance within the calibration "
                "space but not the transfer error. Weighted CP for covariate shift raised coverage to {weighted_cp_pds_a10_cov} and "
                "{weighted_cp_ds_a10_cov}, yet produced unbounded intervals for {weighted_cp_pds_a10_inf} (PDS) and "
                "{weighted_cp_ds_a10_inf} (DS) of test samples (Table 2), a symptom of degenerate likelihood-ratio weights when "
                "transferred and primary spectra are easily distinguished. "
                "Pooling the labelled transfer residuals with the primary residuals (pooled CP) also under-covered "
                "({pooled_cp_pds_a10_cov}, {pooled_cp_ds_a10_cov}) because the *k* target residuals are swamped by the *n* "
                "primary residuals.")]
    B += [("table", tab2, "**Table 2.** Interval performance at nominal coverage 0.90 (α = 0.10), k = 10 transfer standards, 30 "
                          "scenarios per transfer method (24 corn, 6 tablets). Scenario means over 100 random splits; ‘Valid’ = percentage "
                          "of scenarios with mean coverage ≥ 0.88; width and interval score (IS) are divided by SD(y) and summarised by "
                          "their median over scenarios; ∞ = unbounded intervals occurred. Methods marked ‘k labelled’ require reference "
                          "values for the transfer standards. Per-dataset results: Table S2.")]
    B += [("fig", f / "fig3_main_results.png", "**Fig. 3.** Coverage (top) and interval score (bottom, log scale) per scenario for PDS (left) and DS "
                                               "(right) at α = 0.10. Dashed line: nominal 0.90. Each point is one directed instrument pair × property "
                                               "scenario (mean of 100 splits).")]
    B += [("h2", "4.3. Transfer-discrepancy intervals restore coverage without reference values")]
    B += [("p", "Adding the cross-fitted transfer discrepancies brought the mean coverage of all TD-CP variants close to nominal (Table 2). "
                "The pre-specified signed TD-CP reached mean coverages of {td_cp_pds_a10_cov} (PDS) and {td_cp_ds_a10_cov} (DS) but "
                "was valid in only {td_cp_pds_a10_valid} and {td_cp_ds_a10_valid} of scenarios, missing the pre-specified criterion "
                "of 80%. The shortfall was concentrated on corn with DS, where even the target CP using reference values of all ten "
                "standards was valid in only {target_cp_corn_ds_valid} of scenarios. TD-CP+ was valid in every scenario for both "
                "transfer methods, with mean coverage {td_cp_plus_pds_a10_cov} and "
                "{td_cp_plus_ds_a10_cov}: slightly conservative, as expected for jackknife+-type intervals. Its median normalised "
                "interval score ({td_cp_plus_pds_a10_IS} PDS, {td_cp_plus_ds_a10_IS} DS) was lower than that of the labelled "
                "target CP+ ({target_cp_plus_pds_a10_IS}, {target_cp_plus_ds_a10_IS}), which needs ten reference analyses on the "
                "secondary instrument, and close to that of the parametric Gaussian combination ({gauss_td_pds_a10_IS}, "
                "{gauss_td_ds_a10_IS}). The Gaussian combination, however, was valid in only {gauss_td_ds_a10_valid} of DS "
                "scenarios (minimum coverage {gauss_td_ds_a10_mincov}), whereas TD-CP+ never fell below {td_cp_plus_ds_a10_mincov}.")]
    B += [("p", "Paired comparisons across the {t_td_cp_plus_naive_cp_gap_n} scenarios (Table 3) confirmed that TD-CP+ had a smaller "
                "absolute coverage gap than naive CP (Holm-adjusted *p* {t_td_cp_plus_naive_cp_gap_p}, rank-biserial "
                "*r* = {t_td_cp_plus_naive_cp_gap_rb}), the leverage interval (*p* {t_td_cp_plus_leverage_gap_p}) and weighted CP "
                "(*p* {t_td_cp_plus_weighted_cp_gap_p}), and a lower interval score than naive CP (*p* {t_td_cp_plus_naive_cp_IS_p}, "
                "*r* = {t_td_cp_plus_naive_cp_IS_rb}) and than the labelled target CP+ (*p* {t_td_cp_plus_target_cp_plus_IS_p}, "
                "*r* = {t_td_cp_plus_target_cp_plus_IS_rb}). The Gaussian combination, in contrast, tended to have a slightly *lower* interval "
                "score than TD-CP+ (median paired difference {t_td_cp_plus_gauss_td_IS_md} SD units, bootstrap 95% CI "
                "{t_td_cp_plus_gauss_td_IS_ci}, *r* = {t_td_cp_plus_gauss_td_IS_rb}; unadjusted *p* {t_td_cp_plus_gauss_td_IS_praw}, "
                "Holm-adjusted *p* {t_td_cp_plus_gauss_td_IS_p}); the "
                "advantage of TD-CP+ over it lies in validity under DS, not in efficiency. Note that the absolute "
                "coverage gap penalises over-coverage too, so the slightly conservative TD-CP+ is not favoured by this metric "
                "relative to methods centred on nominal coverage (e.g., *p* {t_td_cp_plus_gauss_td_gap_p} against the Gaussian "
                "combination, *r* = {t_td_cp_plus_gauss_td_gap_rb}).")]
    B += [("p", "The most demanding comparator is the classical secondary-instrument validation interval: a bias-corrected "
                "*t*-interval built from the prediction errors of the ten standards after their reference values have been measured "
                "on the secondary instrument (M7; ASTM E1655-type practice [@astm_e1655]). It covered {target_t_pds_a10_cov} (PDS) and "
                "{target_t_ds_a10_cov} (DS) and was valid in {target_t_pds_a10_valid} and {target_t_ds_a10_valid} of scenarios, with "
                "median IS/SD {target_t_pds_a10_IS} and {target_t_ds_a10_IS}. TD-CP+, which uses no reference values, had a slightly "
                "lower interval score in the paired comparison (*p* {t_td_cp_plus_target_t_IS_p}, *r* = {t_td_cp_plus_target_t_IS_rb}) "
                "and higher validity under DS, but a larger absolute coverage gap because it is more conservative (*p* "
                "{t_td_cp_plus_target_t_gap_p}, *r* = {t_td_cp_plus_target_t_gap_rb}). In other words, discrepancies measured on "
                "standards without reference analyses gave intervals of practically the same quality as a ten-sample reference "
                "validation on the secondary instrument.")]
    B += [("p", "Two caveats qualify these tests. First, scenarios are not independent: the 24 corn scenarios reuse the same 80 "
                "samples and the PDS and DS scenarios share splits, so the *p*-values are optimistic and the effect sizes and their "
                "consistency are more informative. Stratified by dataset and transfer method, TD-CP+ had a smaller absolute coverage "
                "gap than naive CP and weighted CP in at least 80% of the scenarios of every stratum (Table S5). Second, the 0.02 "
                "tolerance in the validity definition is a convention; with zero tolerance TD-CP+ was valid in {tol0_td_cp_plus_pds_a} "
                "(PDS) and {tol0_td_cp_plus_ds_a} (DS) of scenarios, versus {tol0_gauss_td_pds_a} and {tol0_gauss_td_ds_a} for the "
                "Gaussian combination (Table S6).")]
    B += [("p", "Coverage averaged over splits is a marginal property; a laboratory deploys a single calibration and a single "
                "transfer. Split-level coverage (Table S4) shows how much an individual deployment can deviate. With only 25 test "
                "samples, binomial noise alone is substantial for corn: even the ideal in-domain conformal interval (naive CP on the "
                "primary spectra) fell below 0.80 coverage in {sl_naive_cp_primary_test_corn_pds_below} of corn splits. TD-CP+ was "
                "below 0.80 in {sl_td_cp_plus_corn_pds_below} (PDS) and {sl_td_cp_plus_corn_ds_below} (DS) of corn splits and "
                "{sl_td_cp_plus_tablets_pds_below} and {sl_td_cp_plus_tablets_ds_below} of tablet splits, whereas naive CP was below 0.80 "
                "in {sl_naive_cp_corn_pds_below} and {sl_naive_cp_corn_ds_below} of corn splits and {sl_naive_cp_tablets_pds_below} and "
                "{sl_naive_cp_tablets_ds_below} of tablet splits.")]
    B += [("table", tab3, "**Table 3.** TD-CP+ versus each comparator at α = 0.10: medians over scenarios of the absolute coverage gap "
                          "|coverage − 0.90| and of IS/SD, bootstrap 95% CI of the median paired difference (TD-CP+ − comparator), matched-pairs "
                          "rank-biserial correlation r_rb (negative: TD-CP+ smaller) and two-sided Wilcoxon signed-rank p-values, "
                          "Holm-adjusted over all {n_tests} tests. Comparisons with the ablations and the pre-specified TD-CP: Table S7.")]
    B += [("h2", "4.4. Ablation: which components matter")]
    B += [("p", "Cross-fitting is indispensable (Table 4, Fig. 4). With in-sample discrepancies, the standard deviation of δ shrank to "
                "a median of {dsd_in_ratio_pds} (PDS) and {dsd_in_ratio_ds} (DS) of its cross-fitted value. For DS the pseudo-inverse "
                "reproduces the standards exactly, so TD-CP collapsed to the naive interval (coverage {td_cp_insample_ds_a10_cov}); "
                "for PDS coverage reached only {td_cp_insample_pds_a10_cov}. Absolute rather than signed scores improved validity "
                "(PDS {td_cp_abs_pds_a10_valid}, DS {td_cp_abs_ds_a10_valid} of scenarios valid) at a similar interval score, "
                "consistent with pooling both tails of a discrepancy distribution estimated from only ten values. The jackknife+ "
                "construction raised DS validity from {td_cp_abs_ds_a10_valid} to {td_cp_plus_ds_a10_valid} without increasing the "
                "median interval score ({td_cp_abs_ds_a10_IS} vs. {td_cp_plus_ds_a10_IS}). The union-bound sum was valid but "
                "over-covered ({td_sum_pds_a10_cov}, {td_sum_ds_a10_cov}) with larger interval scores ({td_sum_pds_a10_IS}, "
                "{td_sum_ds_a10_IS}).")]
    tab4 = _tbl(t / "table4_ablation.csv", main_cols, {"Valid (%)": 0, "Width/SD": 2, "IS/SD": 2})
    B += [("table", tab4, "**Table 4.** Ablation of TD-CP components at α = 0.10 (columns as in Table 2).")]
    B += [("fig", f / "fig4_ablation.png", "**Fig. 4.** Ablation: coverage gap (left) and interval score (right) per scenario, PDS and DS pooled.")]
    B += [("h2", "4.5. Number of transfer standards")]
    B += [("p", "With *k* = 5 and 8 labelled standards, target CP cannot produce finite 90% intervals (Fig. 5), because "
                "⌈0.9(*k* + 1)⌉ > *k*; the classical *t*-interval remains finite but was valid in only {k5_target_t_pds_valid} (PDS) and "
                "{k5_target_t_ds_valid} (DS) of scenarios at *k* = 5. TD-CP+ remained finite for every *k* because it borrows the *n* primary residuals. It was "
                "valid in all scenarios from *k* = 8 onwards for both transfer methods, and at *k* = 5 in {k5_td_cp_plus_pds_valid} "
                "(PDS) and {k5_td_cp_plus_ds_valid} (DS) of scenarios (coverage {k5_td_cp_plus_pds_cov} and {k5_td_cp_plus_ds_cov}). "
                "Its interval score decreased with *k* (PDS: {k5_td_cp_plus_pds_IS} at *k* = 5 to {k30_td_cp_plus_pds_IS} at *k* = 30), "
                "reflecting the improved transfer itself. For DS with *k* = 5, the instability of a 5-spectrum pseudo-inverse is "
                "the limiting factor; we recommend *k* ≥ 8 standards.")]
    B += [("fig", f / "fig5_k_sensitivity.png", "**Fig. 5.** Mean coverage (top) and interval score (bottom) versus the number of transfer standards k; "
                                                "error bars: 95% CI over scenarios. Target CP and Target CP+ are infinite (not shown) for k < 9.")]
    B += [("h2", "4.6. Robustness and generalisation")]
    B += [("p", "Table 6 and Fig. 6 summarise the confirmatory experiments; none of them had been inspected when TD-CP+ was "
                "introduced, and three (unrepresentative standards, one-standard-error PLS, PDS window) were added during internal review. With Kennard–Stone selection of the standards, which violates the exchangeability between standards and "
                "test samples, TD-CP+ covered {ks_td_cp_plus_pds_cov} (PDS) and {ks_td_cp_plus_ds_cov} (DS). A harsher violation, "
                "drawing all standards from samples with reference values below the median, degraded the transfer itself (naive coverage "
                "{biased_naive_cp_pds_cov} and {biased_naive_cp_ds_cov}); TD-CP+ covered {biased_td_cp_plus_pds_cov} (PDS, valid in "
                "{biased_td_cp_plus_pds_valid} of scenarios) and {biased_td_cp_plus_ds_cov} (DS, {biased_td_cp_plus_ds_valid}), "
                "against {biased_target_cp_plus_pds_cov} and {biased_target_cp_plus_ds_cov} for the labelled target CP+. With DS and "
                "unrepresentative standards, therefore, neither TD-CP+ nor the method using reference values for all standards was "
                "reliably valid: the discrepancies of standards from one part of the calibration range do not describe the transfer "
                "error elsewhere. Representative standards are a precondition for TD-CP+, as they are for the transfer itself. With SNV + first-derivative "
                "preprocessing it covered {snv_td_cp_plus_pds_cov} and {snv_td_cp_plus_ds_cov}; with a ridge-regression calibration "
                "{ridge_td_cp_plus_pds_cov} (PDS). Because the corn models selected by minimum RMSECV were complex (median "
                "{ncomp_corn_med} latent variables for 45 samples) and complex models can be fragile to instrument differences, we "
                "repeated the study with the more parsimonious one-standard-error rule (median {ncomp1se_corn} latent variables for "
                "corn): naive CP still covered only {pls1se_naive_cp_pds_cov} (PDS) and {pls1se_naive_cp_ds_cov} (DS), while TD-CP+ "
                "covered {pls1se_td_cp_plus_pds_cov} and {pls1se_td_cp_plus_ds_cov}. Varying the PDS window from 3 to 11 channels "
                "changed the transfer quality (naive coverage from {pdsw3_naive_cp_pds_cov} with 3 channels to {pdsw11_naive_cp_pds_cov} "
                "with 11) but not the validity of TD-CP+ (coverage {pdsw3_td_cp_plus_pds_cov} and {pdsw11_td_cp_plus_pds_cov}). Added secondary-instrument noise (2% of the channel SD) gave {noise20_td_cp_plus_pds_cov}, "
                "versus {noise20_naive_cp_pds_cov} for naive CP. Without any standardisation, the transfer discrepancy dominates the "
                "error, and TD-CP+ still covered {nostd_td_cp_plus_none_cov} (naive CP: {nostd_naive_cp_none_cov}). Here, however, the "
                "symmetric TD-CP+ interval was much less efficient (IS/SD {nostd_td_cp_plus_none_IS}) than the signed TD-CP "
                "({nostd_td_cp_none_IS}, coverage {nostd_td_cp_none_cov}) or the Gaussian combination ({nostd_gauss_td_none_IS}), because "
                "an uncorrected instrument difference produces a large systematic bias that only the signed constructions can shift "
                "the interval to absorb. When the discrepancies are strongly one-sided, the signed TD-CP is preferable. On the official IDRC partition of the "
                "tablets it covered {official_td_cp_plus_pds_cov} (PDS) and {official_td_cp_plus_ds_cov} (DS). For virtual secondary "
                "instruments of increasing severity, naive coverage fell from {sim1_naive_cp_pds_cov} to {sim3_naive_cp_pds_cov} (PDS), "
                "while TD-CP+ covered {sim1_td_cp_plus_pds_cov}–{sim3_td_cp_plus_pds_cov}.")]
    B += [("table", tab6, "**Table 6.** Robustness and generalisation at α = 0.10: mean coverage over scenarios (30 per condition and transfer "
                          "method; 7 for each simulated severity, 6 for the IDRC partition) and percentage of scenarios in which TD-CP+ "
                          "was valid. All methods and interval scores: Table S9.")]
    B += [("fig", f / "fig6_robustness.png", "**Fig. 6.** Mean coverage under simulated instrument shifts (left), added secondary-instrument noise (centre, PDS) "
                                             "and other protocol changes (right, PDS). Dashed line: nominal 0.90.")]
    B += [("h2", "4.7. Other nominal levels")]
    B += [("p", "At α = 0.05, target CP with ten standards is necessarily unbounded, whereas TD-CP+ covered {td_cp_plus_pds_a5_cov} "
                "(PDS) and {td_cp_plus_ds_a5_cov} (DS), valid in {td_cp_plus_pds_a5_valid} and {td_cp_plus_ds_a5_valid} of scenarios. "
                "At α = 0.20 it covered {td_cp_plus_pds_a20_cov} and {td_cp_plus_ds_a20_cov} (Fig. S2, Table S3). The conservativeness "
                "of TD-CP+ is therefore modest and roughly constant (≈ 0.03–0.05) across levels.")]
    B += [("h2", "4.8. Error analysis")]
    B += [("p", "Coverage is marginal, not conditional. Fig. 7 shows that all methods covered samples with extreme reference "
                "values or high leverage less often than central samples; TD-CP+ attenuates but does not remove this pattern. The "
                "cross-fitted discrepancy spread closely tracked the true held-out discrepancy spread (median ratio "
                "{dsd_ratio_median}, range {dsd_ratio_min}–{dsd_ratio_max}), which explains why the reference-free estimate is "
                "sufficient. Assumption (A2) is only approximately met: the held-out Spearman correlation between primary residual "
                "and discrepancy averaged {spearman_mean} (scenario range {spearman_min} to {spearman_max}). Correlated "
                "residuals and discrepancies would widen the true error distribution beyond the convolution and are a plausible "
                "contributor to the residual under-coverage of the signed TD-CP; the jackknife+ margin absorbs it in these data. "
                "Fig. 8 illustrates a single split.")]
    B += [("fig", f / "fig8_error_analysis.png", "**Fig. 7.** Error analysis at α = 0.10: coverage by tertile of the reference value (left) and of leverage "
                                                 "(centre); cross-fitted versus held-out discrepancy SD, scaled by RMSECV (right).")]
    B += [("fig", f / "fig9_example_intervals.png", "**Fig. 8.** Example (corn moisture, m5 → mp6, PDS, k = 10, split seed 0): naive intervals (left) "
                                                    "versus TD-CP+ (right) for the 25 secondary-instrument test samples.")]
    B += [("h2", "4.9. Computational cost")]
    B += [("p", "TD-CP+ needs *k* additional transfer fits for cross-fitting, which took on average {t_cf_corn_pds} ms (corn, PDS) and "
                "{t_cf_tablets_ds} ms (tablets, DS) per split on one CPU core, against {t_cal_corn_pds}–{t_cal_tablets_pds} ms for "
                "fitting and cross-validating the PLS model (Table S8, Fig. S3). The interval step itself is O(*nk*) per test sample "
                "(a partial sort of *nk* candidate bounds): in a synthetic benchmark with *n* = 5000 primary residuals it took "
                "{scal_plus_5000_10} ms per test sample for *k* = 10 and {scal_plus_5000_30} ms for *k* = 30 on one core, against "
                "{scal_signed_5000_10} ms for the signed TD-CP (Fig. S1). The cost is negligible in practice.")]
    B += [("h2", "4.10. Relation to existing approaches")]
    B += [("p", "TD-CP+ is not a new conformal principle: it applies the split-conformal finite-sample correction "
                "[@papadopoulos2002;@lei2018] and the jackknife+ construction [@barber2021] to an error decomposition that is specific "
                "to standardisation-based calibration transfer. Its novelty lies in (i) recognising that the transfer component of the "
                "error can be observed without reference values on the standards that DS/PDS already use, (ii) showing that cross-fitting "
                "is necessary for this observation to be informative (in-sample DS discrepancies are identically zero), and (iii) "
                "establishing, on public data, that the resulting intervals are valid where established alternatives are not. The Gaussian "
                "combination (M4) uses the same two ingredients and was slightly more efficient when valid, which indicates that most of "
                "the benefit comes from the discrepancy information itself; its validity, however, depended on the transfer method. The "
                "concurrent transported conformal calibration of Doula [@doula2026] also exploits unlabelled paired observations, but "
                "transports the labelled calibration set itself for set-valued classification and corrects residual mismatch with "
                "unlabelled target inputs; it was evaluated on image benchmarks. Weighted CP [@tibshirani2019] targets covariate shift "
                "and, as shown above, is impractical for transferred spectra.")]
    B += [("h2", "4.11. Practical recommendations and limitations")]
    B += [("p", "For a transferred calibration we recommend: (i) never reuse primary-instrument intervals; (ii) measure at least eight "
                "transfer standards and keep their primary spectra; (iii) compute cross-fitted discrepancies and report TD-CP+ "
                "intervals, which need no reference values for the standards; (iv) where reference values for the standards are "
                "known (e.g., re-measured calibration samples), TD-CP+ remains as efficient as the labelled alternatives or more so "
                "(Table 3; paired IS versus the *t*-interval: TD-CP+ lower in {pair_t_pds} of PDS and {pair_t_ds} of DS scenarios), and the labelled errors can additionally serve to verify coverage. Limitations: the evidence "
                "comes from two benchmark datasets (five instruments, seven properties) and from simulated instruments; coverage is "
                "marginal over samples and conditionally lower at the extremes; the discrepancies are informative only if the standards "
                "resemble routine samples, so spectrally dissimilar artefacts such as the glass standards supplied with the corn data "
                "cannot be used for δ (the model prediction for a glass spectrum is meaningless), and with DS, standards drawn from only "
                "half of the concentration range left {biased_td_cp_plus_ds_valid_inv} of scenarios invalid; the guarantee of Eq. (5) depends on assumptions "
                "(A1)–(A3), of which (A2) holds only approximately; TD-CP+ was introduced after the pre-specified main analysis, "
                "although its confirmatory evaluation used experiments that were not inspected beforehand; the protocol was fixed in a "
                "time-stamped version-control commit rather than in a public registry; and process or temporal "
                "drift on a single instrument was not studied because no suitable public paired data with continuous reference "
                "values were found.")]
    return B


CONCLUSIONS = [
    ("p", "Prediction intervals calibrated on a primary spectrometer substantially under-cover after calibration transfer, "
          "even when PDS or DS give acceptable point predictions. Splitting the error of a transferred prediction into a "
          "calibration residual and a transfer discrepancy, and estimating the latter without reference values from cross-fitted "
          "maps on the transfer standards, yields intervals with near-nominal (slightly conservative) coverage across 30 public "
          "benchmark scenarios, two transfer methods, several nominal levels and a range of robustness conditions, provided "
          "that the transfer standards represent the routine samples (with DS and standards from only half of the "
          "concentration range, validity was lost in a substantial fraction of scenarios). The jackknife+ "
          "form, TD-CP+, was required for reliable validity with the unstable DS map. The approach adds negligible computation, "
          "is independent of the regression model, and turns transfer standards that laboratories already measure into a "
          "source of validated uncertainty. Future work should evaluate it on process and long-term drift data and on "
          "conditional (sample-adaptive) coverage."),
]


def declarations():
    return [
        ("h1", "CRediT authorship contribution statement"),
        ("p", "[Placeholder — to be completed by the authors, e.g., Conceptualization; Methodology; Software; Formal analysis; Writing – original draft; Writing – review & editing.]"),
        ("h1", "Declaration of competing interest"),
        ("p", "The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper."),
        ("h1", "Declaration of generative AI and AI-assisted technologies in the manuscript preparation process"),
        ("p", "During the preparation of this work the authors used an AI system (Claude, Anthropic) to search the literature, write and "
              "run the analysis code, and draft the manuscript. After using this tool, the authors reviewed and edited the content "
              "as needed and take full responsibility for the content of the published article."),
        ("h1", "Data availability"),
        ("p", "Both datasets are publicly available from Eigenvector Research (corn; NIR shootout 2002). The code, configuration, "
              "pre-specified protocol, raw per-split results ({n_raw_rows} rows), statistical outputs, and scripts that regenerate "
              "every table, figure and number of this article are provided in the accompanying repository [link to be inserted upon acceptance]."),
        ("h1", "Funding"),
        ("p", "[Placeholder — funding sources or ‘This research did not receive any specific grant from funding agencies in the public, commercial, or not-for-profit sectors.’]"),
        ("h1", "Appendix A. Supplementary data"),
        ("p", "Supplementary material (Supplementary_Material.docx): Section S4 proof of Eq. (5); Table S1 per-scenario results; "
              "Table S2 main results by dataset; Table S3 coverage at all nominal levels; Table S4 split-level coverage; Table S5 "
              "stratum consistency; Table S6 tolerance sensitivity; Table S7 full statistical tests; Table S8 computation times; Table S9 all robustness results; Figs. S1–S3 scaling, nominal levels and computation time. "
              "Repository documents: S1 topic selection and pre-specified protocol; S2 iteration log; S3 literature matrix."),
    ]
