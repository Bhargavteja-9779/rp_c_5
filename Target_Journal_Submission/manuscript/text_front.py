"""Front matter, Introduction, Theory and Experimental sections.

Citations are written as [@key] or [@key1;@key2] and numbered in order of first
appearance by build_manuscript.py. Numbers in braces {name} are filled from the
machine-generated results (see values.py); no result is typed by hand.
"""

TITLE = ("Distribution-free prediction intervals for multivariate calibrations transferred between "
         "spectrometers using unlabelled transfer standards")

HIGHLIGHTS = [
    "Intervals calibrated on the primary NIR instrument under-cover after transfer",
    "Cross-fitted discrepancies on transfer standards need no reference values",
    "TD-CP+ restores near-nominal coverage across 30 instrument-pair scenarios",
    "Benchmark: 2 public datasets, PDS and DS, 100 splits per scenario",
    "Open code regenerates every number, table and figure",
]

KEYWORDS = ["Calibration transfer", "Conformal prediction", "Prediction interval",
            "Near-infrared spectroscopy", "Piecewise direct standardisation", "Uncertainty quantification"]

ABSTRACT = {
    "Background": (
        "Calibration transfer (e.g., piecewise direct standardisation, PDS) lets a multivariate calibration "
        "built on a primary spectrometer be used on a secondary one, but transfer methods are judged almost "
        "exclusively by point accuracy. Prediction intervals inherited from the primary instrument implicitly "
        "assume that the transfer is perfect, and no distribution-free method exists to attach sample-wise "
        "uncertainty to a transferred calibration without new reference analyses on the secondary instrument."),
    "Results": (
        "We decompose the secondary-instrument prediction error exactly into the primary calibration residual and "
        "a transfer discrepancy that can be measured, without reference values, on the transfer standards already "
        "used to fit PDS or direct standardisation (DS). Combining out-of-fold calibration residuals with "
        "cross-fitted discrepancies yields transfer-discrepancy conformal prediction (TD-CP) and a jackknife+ "
        "variant (TD-CP+). On two public NIR benchmarks (corn, three instruments; pharmaceutical tablets, two "
        "instruments; 30 directed instrument-pair × property scenarios, 100 random splits each, k = 10 "
        "standards), intervals calibrated on the primary instrument covered only {naive_cov_pds} (PDS) and "
        "{naive_cov_ds} (DS) of secondary-instrument samples at a nominal 0.90. TD-CP+ reached {plus_cov_pds} "
        "and {plus_cov_ds}, was within 0.02 of nominal or above in {plus_valid_pds} and {plus_valid_ds} of "
        "scenarios, and had a lower interval score than a comparator requiring reference values for all ten standards. "
        "The pre-registered signed TD-CP fell short of its validity criterion with DS."),
    "Significance": (
        "Transferred calibrations can be accompanied by sample-wise intervals with near-nominal coverage at "
        "no extra reference-analysis cost, whereas the common practice of reusing primary-instrument intervals "
        "is markedly over-confident. The method is model-agnostic, computationally negligible and openly released."),
}

INTRO = [
    ("p", "Near-infrared (NIR) and other vibrational spectroscopic methods rely on multivariate calibrations such as "
          "partial least squares (PLS) regression [@wold2001]. Because spectra of the same sample differ between "
          "instruments, a calibration developed on a primary (master) instrument generally cannot be applied to a "
          "secondary (slave) instrument without correction [@workman2018;@feudale2002;@fearn2001]. Calibration "
          "transfer methods such as direct standardisation (DS) and piecewise direct standardisation (PDS) "
          "[@wang1991;@bouveresse1996] map secondary spectra onto the primary domain using a small set of transfer "
          "standards measured on both instruments, and the field continues to produce new transfer strategies, "
          "including standard-free and few-shot approaches [@malli2017;@aca_filter2024;@aca_uct2026;@aca_pdsft2026;@aca_plselm2025]."),
    ("p", "These methods are almost invariably evaluated by point-prediction accuracy (RMSEP, R^{2}). Method validation "
          "and routine release decisions, however, require statements about the uncertainty of individual "
          "predictions [@astm_e1655;@ich_q2r2]. Sample-specific prediction errors for PLS have been derived by error "
          "propagation and leverage arguments [@faber1997;@faber2003], and conformal prediction (CP), which provides "
          "distribution-free finite-sample coverage under exchangeability [@vovk2005;@papadopoulos2002;@lei2018;@angelopoulos2023], "
          "has recently been applied to mid-infrared, Raman and NIR regression [@foodchem2025;@analchem2026;@duma2025]. "
          "All of these approaches assume that new spectra come from the same measurement domain as the calibration "
          "data. After transfer this assumption fails twice: the secondary spectra differ from the primary spectra, and the "
          "transfer map itself is estimated from few standards and is imperfect. A recent review of calibration transfer "
          "and uncertainty quantification for portable optical systems emphasises this gap but proposes no validated "
          "interval method [@haggam2026]."),
    ("p", "Two generic remedies are available but unattractive. Re-calibrating the interval on the secondary instrument "
          "requires reference analyses for a sufficiently large labelled set: with k labelled standards, split CP "
          "cannot produce a finite 95% interval unless k ≥ 19. Weighted CP for covariate shift [@tibshirani2019] "
          "requires overlapping supports and estimable likelihood ratios, which are fragile for high-dimensional "
          "transferred spectra. A concurrent machine-learning paper transports a labelled source calibration set through "
          "unlabelled paired observations for set-valued classification [@doula2026]; it does not address regression "
          "intervals after chemometric standardisation."),
    ("p", "Here we exploit a simple identity: the error of a transferred prediction equals the primary calibration "
          "residual plus a *transfer discrepancy*, the difference between the primary-model prediction from the "
          "primary spectrum and from the transferred secondary spectrum. The discrepancy needs no reference value and "
          "can be measured on the transfer standards that DS/PDS already require, provided that the transfer map is "
          "cross-fitted. The contributions are: (i) transfer-discrepancy conformal prediction (TD-CP), which combines "
          "out-of-fold calibration residuals with cross-fitted discrepancies, together with a conditional finite-sample "
          "coverage statement; (ii) a jackknife+ variant (TD-CP+) that remains reliable when the transfer map is "
          "unstable, as DS is when k ≪ p; and (iii) a benchmark of interval validity after transfer on two public "
          "multi-instrument datasets, with pre-registered analysis, ablations, robustness tests and open code. "
          "We report all pre-registered outcomes, including the one that the pre-registered signed TD-CP did not meet."),
]

THEORY = [
    ("h2", "2.1. Problem setting"),
    ("p", "Let *f* be a calibration fitted on primary spectra *x*^{P} of a labelled master set {(*x*_{i}^{P}, *y*_{i})}, "
          "*i* = 1, …, *n*, and let *T* be a transfer map fitted on *k* transfer pairs {(*x*_{j}^{P}, *x*_{j}^{S})} measured on the "
          "primary (P) and secondary (S) instruments. A new sample is measured only on S and predicted as "
          "ŷ = *f*(*T*(*x*^{S})). We seek an interval [ŷ + *L*, ŷ + *U*] that contains *y* with probability at least 1 − α "
          "without reference values for the transfer standards."),
    ("h2", "2.2. Error decomposition"),
    ("p", "For any sample the prediction error decomposes exactly as"),
    ("eq", r"y-f(T(x^{S}))=[\,y-f(x^{P})\,]+[\,f(x^{P})-f(T(x^{S}))\,]=r+\delta", 1),
    ("p", "where *r* is the calibration residual and δ the transfer discrepancy. The residual *r* is observable on the labelled master set. We use out-of-fold residuals from *K*-fold "
          "cross-validation so that no master sample is sacrificed,"),
    ("eq", r"r_{i}=y_{i}-f^{(-\kappa(i))}(x_{i}^{P}),\quad i=1,\ldots,n", 2),
    ("p", "where *f*^{(−κ(i))} is fitted without the fold containing sample *i*. The discrepancy δ requires no reference "
          "value and is observable on the transfer standards. Because DS and PDS are fitted on these very standards, the "
          "in-sample discrepancy is optimistic; for DS with *k* < *p* the pseudo-inverse reproduces the standards exactly "
          "and the in-sample discrepancy is identically zero. We therefore cross-fit the map,"),
    ("eq", r"\delta_{j}=f(x_{j}^{P})-f(T_{-j}(x_{j}^{S})),\quad j=1,\ldots,k", 3),
    ("p", "where *T*_{−*j*} is fitted on the other *k* − 1 pairs."),
    ("h2", "2.3. Transfer-discrepancy conformal prediction (TD-CP)"),
    ("p", "TD-CP combines the two empirical distributions through the *nk* sums *r*_{i} + δ_{j}. The pre-registered "
          "signed version sets *U* to the ⌈(1 − α/2)(*n* + 1)*k*⌉-th smallest sum and *L* to the mirrored order statistic, "
          "so that systematic transfer bias shifts the interval. The absolute-score version uses the *m*-th smallest of the *nk* values |*r*_{i} + δ_{j}|, denoted |*r* + δ|_{(m)}:"),
    ("eq", r"\hat{q}=|r+\delta|_{(m)},\ \ m=\lceil(1-\alpha)(n+1)k\rceil,\qquad C(x^{S})=[\hat{y}-\hat{q},\ \hat{y}+\hat{q}]", 4),
    ("p", "The (*n* + 1) factor is the usual finite-sample correction of split CP; if the index exceeds *nk* the interval is "
          "unbounded. Under exchangeable residuals (A1), independence between residuals and discrepancies (A2) and "
          "i.i.d. discrepancies with cdf *F*_{δ} (A3), the coverage conditional on the standards satisfies"),
    ("eq", r"P\{L\leq y-\hat{y}\leq U\mid\delta_{1:k}\}\ \geq\ 1-\alpha-2D_{k},\qquad D_{k}=\sup_{t}|\hat{F}_{k}(t)-F_{\delta}(t)|", 5),
    ("p", "with P(*D*_{k} > ε) ≤ 2 exp(−2*k*ε^{2}) [@dkw1956;@massart1990]. The proof (Supplementary S4) is a rank argument "
          "on the augmented set {*r*_{i} + δ_{j}: *i* = 0, …, *n*}; when the test discrepancy is drawn from the empirical "
          "distribution of the δ_{j}, coverage ≥ 1 − α holds exactly. The bound makes explicit that (A2) is an assumption "
          "and that the guarantee loosens for small *k*; both are examined empirically below."),
    ("h2", "2.4. Jackknife+ variant (TD-CP+)"),
    ("p", "Cross-fitted discrepancies describe maps fitted on *k* − 1 standards, whereas predictions use the map fitted on all *k*. "
          "For unstable maps, such as DS with *k* ≪ *p*, these are not interchangeable, the situation in which "
          "jackknife intervals can fail and the jackknife+ was proposed [@barber2021]. TD-CP+ attaches each radius "
          "|*r*_{i} + δ_{j}| to the leave-one-out prediction of its own map:"),
    ("eq", r"C^{+}(x^{S})=\left[\hat{q}^{-}_{\alpha}\{f(T_{-j}(x^{S}))-|r_{i}+\delta_{j}|\},\ \hat{q}^{+}_{1-\alpha}\{f(T_{-j}(x^{S}))+|r_{i}+\delta_{j}|\}\right]", 6),
    ("p", "where q̂^{+}_{1−α} is the ⌈(1 − α)(*n* + 1)*k*⌉-th smallest of the *nk* values and q̂^{−}_{α} the mirrored order "
          "statistic. If the transfer map does not depend on which standard is left out, Eq. (6) reduces to Eq. (4). TD-CP+ "
          "was added after inspection of the pre-registered main experiment (Supplementary S2) and is therefore evaluated "
          "on confirmatory experiments that had not been examined when it was introduced."),
    ("h2", "2.5. Comparison methods"),
    ("p", "All interval methods share the same point prediction ŷ. Label-free comparators: (M1) naive split CP "
          "with the primary residuals, ±q̂_{1−α}(|*r*|); (M2) the classical leverage-corrected PLS interval, "
          "±*t*_{1−α/2, n−A−1}·RMSECV·(1 + 1/*n* + *h*)^{1/2} with *h* the leverage of the transferred spectrum [@astm_e1655;@faber2003]; "
          "(M3) weighted CP under covariate shift [@tibshirani2019] with likelihood ratios from a logistic-regression classifier "
          "on PLS scores of master versus transferred test spectra; and (M4) a Gaussian combination of the same information "
          "used by TD-CP, ŷ + mean(*r*) + mean(δ) ± *z*_{1−α/2}(RMSECV^{2} + s_{δ}^{2})^{1/2}. Methods that additionally require "
          "reference values for the *k* standards (an advantaged reference rather than a competitor): (M5) target split CP "
          "on leave-one-out target residuals *e*_{j} = *y*_{j} − *f*(*T*_{−*j*}(*x*_{j}^{S})); (M5+) its jackknife+ version; and "
          "(M6) pooled CP on {|*r*_{i}|} ∪ {|*e*_{j}|}. Ablations: TD-CP without cross-fitting (in-sample δ), signed versus "
          "absolute scores, and a union-bound sum q̂_{1−α/2}(|*r*|) + Q_{1−α/2}(|δ|)."),
]

EXPERIMENTAL = [
    ("h2", "3.1. Data"),
    ("p", "Two public multi-instrument NIR benchmarks distributed by Eigenvector Research were used [@eigenvector_data] "
          "(Table 1, Fig. 2). Corn: {corn_n} samples measured on three spectrometers (m5, mp5, mp6; 1100–2498 nm, 2 nm, "
          "{corn_p} channels) with moisture, oil, protein and starch reference values; all six directed instrument pairs were "
          "used. Pharmaceutical tablets (IDRC 2002 shootout): {tab_n} tablets measured on two spectrometers (600–1898 nm, "
          "{tab_p} channels) with weight, hardness and assay; both directions were used. This gives 24 + 6 = 30 directed "
          "pair × property scenarios. Files were verified by SHA-256 digests. A third candidate dataset (MicroNIR "
          "temperature series) was excluded before analysis because its nine formulations span only three nominal "
          "concentration levels (Supplementary S1)."),
    ("h2", "3.2. Calibration and transfer"),
    ("p", "PLS1 models (NIPALS, mean-centred raw spectra) were fitted on the primary spectra of the master set, with the "
          "number of latent variables chosen by minimum 10-fold RMSECV (maximum 15 for corn, 20 for tablets); the out-of-fold "
          "residuals at that complexity served as calibration scores. PDS used a five-channel window with local ridge "
          "regression (λ = 10^{−6} × trace of the local Gram matrix) and inward-shifted windows at the spectral edges; DS used "
          "the Moore–Penrose pseudo-inverse of the centred secondary standards (rcond = 10^{−6}). These hyperparameters were "
          "fixed in advance and not tuned."),
    ("h2", "3.3. Splitting protocol and leakage control"),
    ("p", "In each repetition the samples were randomly partitioned into disjoint test, transfer and master sets: "
          "corn 25/10/45 and tablets 200/10/{tab_master}. All operations that use reference values (PLS fitting, "
          "complexity selection, residuals) used only the master set; transfer maps used only the primary and secondary "
          "spectra of the transfer standards; test samples contributed only their secondary spectra. Their primary spectra "
          "and reference values were used exclusively for evaluation and diagnostics. Each scenario was repeated with "
          "split seeds 0–99 fixed in advance (100 repetitions, {n_main_splits} splits in total for the two transfer methods)."),
    ("h2", "3.4. Performance measures and statistical analysis"),
    ("p", "For every split we computed empirical coverage, mean interval width and the interval (Winkler) score "
          "[@gneiting2007]"),
    ("eq", r"\mathrm{IS}_{\alpha}=(u-l)+\frac{2}{\alpha}(l-y)\,\mathbf{1}\{y<l\}+\frac{2}{\alpha}(y-u)\,\mathbf{1}\{y>u\}", 7),
    ("p", "which rewards narrow intervals and penalises misses (lower is better). Width and IS were divided by the standard "
          "deviation of the property to pool scenarios. Because repetitions within a scenario share samples, the scenario "
          "mean was the unit of analysis. A scenario was called *valid* if its mean coverage was at least 1 − α − 0.02; the "
          "pre-registered success criterion was validity in ≥80% of scenarios for each transfer method. Methods were compared "
          "with two-sided Wilcoxon signed-rank tests over the paired scenario means [@wilcoxon1945] of the absolute coverage "
          "gap and of the normalised IS, with Holm adjustment across all {n_tests} comparisons [@holm1979], matched-pairs "
          "rank-biserial correlations as effect sizes [@kerby2014] and percentile bootstrap 95% confidence intervals of the "
          "median paired difference (10,000 resamples). Infinite intervals were ranked as worst."),
    ("h2", "3.5. Robustness and generalisation experiments"),
    ("p", "Additional experiments (50 repetitions unless noted) varied one factor at a time: the number of standards "
          "*k* ∈ {5, 8, 10, 15, 20, 30}; Kennard–Stone instead of random selection of standards [@kennard1969] (100 repetitions); "
          "SNV followed by a Savitzky–Golay first derivative (11 points, second order) [@barnes1989;@savitzky1964]; ridge "
          "regression instead of PLS; Gaussian noise added to secondary spectra (0.5, 1 and 2% of the mean channel standard "
          "deviation); no standardisation at all; the official IDRC calibration/validation/test partition of the tablets "
          "(100 repetitions over random standard selection); and virtual secondary instruments obtained by perturbing the "
          "primary spectra with wavelength shifts (0.5–2 channels), band broadening (Gaussian σ = 1–3 channels), gain "
          "(2–10%), sloped baselines and noise at three severity levels. Nominal levels 0.80, 0.90 and 0.95 were analysed "
          "for the main experiment."),
    ("h2", "3.6. Software and reproducibility"),
    ("p", "All computations were run in Python 3.13 (NumPy, SciPy, scikit-learn) on a 4-core CPU without GPU. A single "
          "command regenerates all results, tables and figures, and every number in this paper is read from machine-generated "
          "result files (Data availability)."),
]
