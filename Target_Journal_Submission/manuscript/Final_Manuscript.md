# Distribution-free prediction intervals for multivariate calibrations transferred between spectrometers using unlabelled transfer standards

Author One^{a,*}, Author Two^{b} [author names withheld — placeholder]

^{a} Affiliation placeholder; ^{b} Affiliation placeholder

^{*} Corresponding author: name, e-mail placeholder


## Highlights

- Intervals calibrated on the primary NIR instrument under-cover after transfer
- Cross-fitted discrepancies on transfer standards need no reference values
- TD-CP+ restores near-nominal coverage across 30 instrument-pair scenarios
- Benchmark: 2 public datasets, PDS and DS, 100 splits per scenario
- Open code regenerates every number, table and figure


## Abstract

**Background:** Calibration transfer (e.g., piecewise direct standardisation, PDS) lets a multivariate calibration built on a primary spectrometer be used on a secondary one, but transfer methods are judged almost exclusively by point accuracy. Prediction intervals inherited from the primary instrument implicitly assume that the transfer is perfect, and no distribution-free method has been established to attach sample-wise uncertainty to a transferred calibration without new reference analyses on the secondary instrument.

**Results:** We decompose the secondary-instrument prediction error exactly into the primary calibration residual and a transfer discrepancy that can be measured, without reference values, on the transfer standards already used to fit PDS or direct standardisation (DS). Combining out-of-fold calibration residuals with cross-fitted discrepancies yields transfer-discrepancy conformal prediction (TD-CP) and a jackknife+ variant (TD-CP+). On two public NIR benchmarks (corn, three instruments; pharmaceutical tablets, two instruments; 30 directed instrument-pair × property scenarios, 100 random splits each, k = 10 standards), intervals calibrated on the primary instrument covered only 0.483 (PDS) and 0.587 (DS) of secondary-instrument samples at a nominal 0.90. TD-CP+ reached 0.939 and 0.927, was within 0.02 of nominal or above in 100% and 100% of scenarios, and had a lower interval score than a comparator requiring reference values for all ten standards. The pre-specified signed TD-CP fell short of its validity criterion with DS.

**Significance:** Transferred calibrations can carry sample-wise intervals with near-nominal coverage without reference values for the standards, as efficient as or more efficient than intervals built from them; reusing primary-instrument intervals is markedly over-confident. Code is openly released.

**Keywords:** Calibration transfer; Conformal prediction; Prediction interval; Near-infrared spectroscopy; Piecewise direct standardisation; Uncertainty quantification


## 1. Introduction

Near-infrared (NIR) and other vibrational spectroscopic methods rely on multivariate calibrations such as partial least squares (PLS) regression [1]. Because spectra of the same sample differ between instruments, a calibration developed on a primary (master) instrument generally cannot be applied to a secondary (slave) instrument without correction [2–4]. Calibration transfer methods such as direct standardisation (DS) and piecewise direct standardisation (PDS) [5,6] map secondary spectra onto the primary domain using a small set of transfer standards measured on both instruments, and the field continues to produce new transfer strategies, including standard-free and few-shot approaches [7–11].

These methods are almost invariably evaluated by point-prediction accuracy (RMSEP, R^{2}). Method validation and routine release decisions, however, require statements about the uncertainty of individual predictions [12,13]. Sample-specific prediction errors for PLS have been derived by error propagation and leverage arguments [14,15], and conformal prediction (CP), which provides distribution-free finite-sample coverage under exchangeability [16–19], has recently been applied to mid-infrared, Raman and NIR regression [20–22]. All of these approaches assume that new spectra come from the same measurement domain as the calibration data. After transfer this assumption fails twice: the secondary spectra differ from the primary spectra, and the transfer map itself is estimated from few standards and is imperfect. A recent review of calibration transfer and uncertainty quantification for portable optical systems emphasises this gap but proposes no validated interval method [23].

Two generic remedies are available but unattractive. Re-calibrating the interval on the secondary instrument requires reference analyses for a sufficiently large labelled set: with k labelled standards, split CP cannot produce a finite 95% interval unless k ≥ 19. Weighted CP for covariate shift [24] requires overlapping supports and estimable likelihood ratios, which are fragile for high-dimensional transferred spectra. A concurrent machine-learning paper transports a labelled source calibration set through unlabelled paired observations for set-valued classification [25]; it does not address regression intervals after chemometric standardisation.

Here we exploit a simple identity: the error of a transferred prediction equals the primary calibration residual plus a *transfer discrepancy*, the difference between the primary-model prediction from the primary spectrum and from the transferred secondary spectrum. The discrepancy needs no reference value and can be measured on the transfer standards that DS/PDS already require, provided that the transfer map is cross-fitted. This matters when standards lack valid reference values (surrogate or stable check materials, or calibration samples whose composition has changed or that were consumed); when reference values are available, the comparison with intervals built from them is part of the evaluation. The contributions are: (i) transfer-discrepancy conformal prediction (TD-CP), which combines out-of-fold calibration residuals with cross-fitted discrepancies, together with a conditional finite-sample coverage statement; (ii) a jackknife+ variant (TD-CP+) that remains reliable when the transfer map is unstable, as DS is when k ≪ p; and (iii) a benchmark of interval validity after transfer on two public multi-instrument datasets, with an analysis protocol fixed and time-stamped in version control before the experiments, ablations, robustness tests and open code. We report all pre-specified outcomes, including the one that the pre-specified signed TD-CP did not meet.

![**Fig. 1.** TD-CP workflow. Residuals of](figures/fig1_workflow.png)

**Fig. 1.** TD-CP workflow. Residuals of the primary calibration (top) and reference-free transfer discrepancies of cross-fitted standardisation maps on the transfer standards (bottom) are combined into the interval for a new secondary-instrument spectrum. Schematic; no data are shown.


## 2. Theory


### 2.1. Problem setting

Let *f* be a calibration fitted on primary spectra *x*^{P} of a labelled master set {(*x*_{i}^{P}, *y*_{i})}, *i* = 1, …, *n*, and let *T* be a transfer map fitted on *k* transfer pairs {(*x*_{j}^{P}, *x*_{j}^{S})} measured on the primary (P) and secondary (S) instruments. A new sample is measured only on S and predicted as ŷ = *f*(*T*(*x*^{S})). We seek an interval [ŷ + *L*, ŷ + *U*] that contains *y* with probability at least 1 − α without reference values for the transfer standards.


### 2.2. Error decomposition

For any sample the prediction error decomposes exactly as

$$ y-f(T(x^{S}))=[\,y-f(x^{P})\,]+[\,f(x^{P})-f(T(x^{S}))\,]=r+\delta \qquad (1) $$

where *r* is the calibration residual and δ the transfer discrepancy. The residual *r* is observable on the labelled master set. We use out-of-fold residuals from *K*-fold cross-validation so that no master sample is sacrificed,

$$ r_{i}=y_{i}-f^{(-\kappa(i))}(x_{i}^{P}),\quad i=1,\ldots,n \qquad (2) $$

where *f*^{(−κ(i))} is fitted without the fold containing sample *i*. The discrepancy δ requires no reference value and is observable on the transfer standards. Because DS and PDS are fitted on these very standards, the in-sample discrepancy is optimistic; for DS with *k* < *p* the pseudo-inverse reproduces the standards exactly and the in-sample discrepancy is identically zero. We therefore cross-fit the map,

$$ \delta_{j}=f(x_{j}^{P})-f(T_{-j}(x_{j}^{S})),\quad j=1,\ldots,k \qquad (3) $$

where *T*_{−*j*} is fitted on the other *k* − 1 pairs.


### 2.3. Transfer-discrepancy conformal prediction (TD-CP)

TD-CP combines the two empirical distributions through the *nk* sums *r*_{i} + δ_{j}. The pre-specified signed version sets *U* to the ⌈(1 − α/2)(*n* + 1)*k*⌉-th smallest sum and *L* to the mirrored order statistic, so that systematic transfer bias shifts the interval. The absolute-score version uses the *m*-th smallest of the *nk* values |*r*_{i} + δ_{j}|, denoted |*r* + δ|_{(m)}:

$$ \hat{q}=|r+\delta|_{(m)},\ \ m=\lceil(1-\alpha)(n+1)k\rceil,\qquad C(x^{S})=[\hat{y}-\hat{q},\ \hat{y}+\hat{q}] \qquad (4) $$

The (*n* + 1) factor is the usual finite-sample correction of split CP; if the index exceeds *nk* the interval is unbounded. Under exchangeable residuals (A1), independence between residuals and discrepancies (A2) and i.i.d. discrepancies with cdf *F*_{δ} (A3), the coverage conditional on the standards satisfies

$$ P\{L\leq y-\hat{y}\leq U\mid\delta_{1:k}\}\ \geq\ 1-\alpha-2D_{k},\qquad D_{k}=\sup_{t}|\hat{F}_{k}(t)-F_{\delta}(t)| \qquad (5) $$

with P(*D*_{k} > ε) ≤ 2 exp(−2*k*ε^{2}) [26,27]. The proof (Supplementary S4) is a rank argument on the augmented set {*r*_{i} + δ_{j}: *i* = 0, …, *n*}; when the test discrepancy is drawn from the empirical distribution of the δ_{j}, coverage ≥ 1 − α holds exactly. The bound makes explicit that (A2) is an assumption and that the guarantee loosens for small *k*; both are examined empirically below.


### 2.4. Jackknife+ variant (TD-CP+)

Cross-fitted discrepancies describe maps fitted on *k* − 1 standards, whereas predictions use the map fitted on all *k*. For unstable maps, such as DS with *k* ≪ *p*, these are not interchangeable, the situation in which jackknife intervals can fail and the jackknife+ was proposed [28]. TD-CP+ attaches each radius |*r*_{i} + δ_{j}| to the leave-one-out prediction of its own map:

$$ C^{+}(x^{S})=\left[\hat{q}^{-}_{\alpha}\{f(T_{-j}(x^{S}))-|r_{i}+\delta_{j}|\},\ \hat{q}^{+}_{1-\alpha}\{f(T_{-j}(x^{S}))+|r_{i}+\delta_{j}|\}\right] \qquad (6) $$

where q̂^{+}_{1−α} is the ⌈(1 − α)(*n* + 1)*k*⌉-th smallest of the *nk* values and q̂^{−}_{α} the mirrored order statistic. If the transfer map does not depend on which standard is left out, Eq. (6) reduces to Eq. (4). We do not prove a finite-sample guarantee for TD-CP+: Eq. (5) covers Eq. (4), and the jackknife+ guarantee of 1 − 2α [28] assumes exchangeable leave-one-out residuals, which the combination of primary residuals and discrepancies satisfies only under (A1)–(A3). Its validity is therefore established empirically below. TD-CP+ was added after inspection of the pre-specified main experiment (Supplementary S2) and is therefore evaluated on confirmatory experiments that had not been examined when it was introduced.


### 2.5. Comparison methods

All interval methods share the same point prediction ŷ. Label-free comparators: (M1) naive split CP with the primary residuals, ±q̂_{1−α}(|*r*|); (M2) the classical leverage-corrected PLS interval, ±*t*_{1−α/2, n−A−1}·RMSECV·(1 + 1/*n* + *h*)^{1/2} with *h* the leverage of the transferred spectrum [12,15]; (M3) weighted CP under covariate shift [24] with likelihood ratios from 5-fold cross-fitted probabilities of a logistic-regression classifier on standardised PLS scores of master versus transferred test spectra; and (M4) a Gaussian combination of the same information used by TD-CP, ŷ + mean(*r*) + mean(δ) ± *z*_{1−α/2}(RMSECV^{2} + s_{δ}^{2})^{1/2}. Methods that additionally require reference values for the *k* standards (an advantaged reference rather than a competitor): (M5) target split CP on leave-one-out target residuals *e*_{j} = *y*_{j} − *f*(*T*_{−*j*}(*x*_{j}^{S})); (M5+) its jackknife+ version; and (M6) pooled CP on {|*r*_{i}|} ∪ {|*e*_{j}|}; and (M7) the classical bias-corrected validation interval mean(*e*) ± *t*_{1−α/2, k−1}·s_{e}(1 + 1/*k*)^{1/2} (added during internal review). Ablations: TD-CP without cross-fitting (in-sample δ), signed versus absolute scores, and a union-bound sum q̂_{1−α/2}(|*r*|) + Q_{1−α/2}(|δ|).


## 3. Experimental


### 3.1. Data

Two public multi-instrument NIR benchmarks distributed by Eigenvector Research were used [29] (Table 1, Fig. 2). Corn: 80 samples measured on three spectrometers (m5, mp5, mp6; 1100–2498 nm, 2 nm, 700 channels) with moisture, oil, protein and starch reference values; all six directed instrument pairs were used. Pharmaceutical tablets (IDRC 2002 shootout): 655 tablets measured on two spectrometers (600–1898 nm, 650 channels) with weight, hardness and assay; both directions were used. This gives 24 + 6 = 30 directed pair × property scenarios. Files were verified by SHA-256 digests. A third candidate dataset (MicroNIR temperature series) was excluded before analysis because its nine formulations span only three nominal concentration levels (Supplementary S1).


### 3.2. Calibration and transfer

PLS1 models (NIPALS, mean-centred raw spectra) were fitted on the primary spectra of the master set, with the number of latent variables chosen by minimum 10-fold RMSECV (maximum 15 for corn, 20 for tablets); the out-of-fold residuals at that complexity served as calibration scores (selecting the complexity on the same folds makes these residuals marginally optimistic; the in-domain check in Section 4.1 quantifies the effect). PDS used a five-channel window with local ridge regression (λ = 10^{−6} × trace of the local Gram matrix) and inward-shifted windows at the spectral edges; DS used the Moore–Penrose pseudo-inverse of the centred secondary standards (rcond = 10^{−6}). These hyperparameters were fixed in advance and not tuned.


### 3.3. Splitting protocol and leakage control

In each repetition the samples were randomly partitioned into disjoint test, transfer and master sets: corn 25/10/45 and tablets 200/10/445. All operations that use reference values (PLS fitting, complexity selection, residuals) used only the master set; transfer maps used only the primary and secondary spectra of the transfer standards; test samples contributed only their secondary spectra. Their primary spectra and reference values were used exclusively for evaluation and diagnostics. Each scenario was repeated with split seeds 0–99 fixed in advance (100 repetitions, 6,000 splits in total for the two transfer methods).


### 3.4. Performance measures and statistical analysis

For every split we computed empirical coverage, mean interval width and the interval (Winkler) score [30]

$$ \mathrm{IS}_{\alpha}=(u-l)+\frac{2}{\alpha}(l-y)\,\mathbf{1}\{y<l\}+\frac{2}{\alpha}(y-u)\,\mathbf{1}\{y>u\} \qquad (7) $$

which rewards narrow intervals and penalises misses (lower is better). Width and IS were divided by the standard deviation of the property to pool scenarios. Because repetitions within a scenario share samples, the scenario mean was the unit of analysis. A scenario was called *valid* if its mean coverage was at least 1 − α − 0.02; the pre-specified success criterion was validity in ≥80% of scenarios for each transfer method. Methods were compared with two-sided Wilcoxon signed-rank tests over the paired scenario means [31] of the absolute coverage gap and of the normalised IS, with Holm adjustment across all 46 comparisons [32], matched-pairs rank-biserial correlations as effect sizes [33] and percentile bootstrap 95% confidence intervals of the median paired difference (10,000 resamples). Infinite intervals were ranked as worst.


### 3.5. Robustness and generalisation experiments

Additional experiments (50 repetitions unless noted) varied one factor at a time: the number of standards *k* ∈ {5, 8, 10, 15, 20, 30}; Kennard–Stone selection of the standards on their primary spectra [34] (100 repetitions); standards drawn only from samples with reference values below the median (unrepresentative standards, added during internal review); SNV followed by a Savitzky–Golay first derivative (11 points, second order) [35,36]; ridge regression instead of PLS; PLS complexity chosen by the one-standard-error rule and PDS windows of 3, 7 and 11 channels (both added during internal review; Supplementary S2); Gaussian noise added to all secondary spectra, standards included (0.5, 1 and 2% of the mean channel standard deviation); no standardisation at all; the official IDRC calibration/validation/test partition of the tablets (100 repetitions over random standard selection); and virtual secondary instruments obtained by perturbing the primary spectra with wavelength shifts (0.5–2 channels), band broadening (Gaussian σ = 1–3 channels), gain (2–10%), sloped baselines and noise at three severity levels. Nominal levels 0.80, 0.90 and 0.95 were analysed for the main experiment.


### 3.6. Software and reproducibility

All computations were run in Python 3.13 (NumPy, SciPy, scikit-learn) on a 4-core CPU without GPU. A single command regenerates all results, tables and figures, and every number in this paper is read from machine-generated result files (Data availability).


## 4. Results and discussion

**Table 1.** Datasets and reference values.

| Dataset | Instruments | n | Channels | Range (nm) | Property | Mean | SD | Min | Max |
|---|---|---|---|---|---|---|---|---|---|
| corn | m5, mp5, mp6 | 80 | 700 | 1100–2498 | moisture | 10.23 | 0.38 | 9.38 | 10.99 |
| corn | m5, mp5, mp6 | 80 | 700 | 1100–2498 | oil | 3.50 | 0.18 | 3.09 | 3.83 |
| corn | m5, mp5, mp6 | 80 | 700 | 1100–2498 | protein | 8.67 | 0.50 | 7.65 | 9.71 |
| corn | m5, mp5, mp6 | 80 | 700 | 1100–2498 | starch | 64.70 | 0.82 | 62.83 | 66.47 |
| tablets | inst1, inst2 | 655 | 650 | 600–1898 | weight | 378.89 | 4.75 | 363.90 | 390.99 |
| tablets | inst1, inst2 | 655 | 650 | 600–1898 | hardness | 19.38 | 1.26 | 13.80 | 23.50 |
| tablets | inst1, inst2 | 655 | 650 | 600–1898 | assay | 189.85 | 17.14 | 151.60 | 239.10 |

![**Fig. 2.** Mean spectra per instrument ](figures/fig2_spectra.png)

**Fig. 2.** Mean spectra per instrument (top) and mean inter-instrument differences (bottom) for the corn (left) and tablet (right) data.


### 4.1. Calibration and transfer quality

The selected PLS models used 8–15 latent variables for corn and 3–20 for tablets. Transfer was imperfect: the median ratio of the secondary-instrument RMSEP after transfer to the RMSEP obtained from the primary spectra of the same test samples was 2.2 (range 1.1–52.6; Table S1), i.e., the transferred predictions carried an error component absent on the primary instrument. The largest ratios occur for corn moisture with m5 as primary, which is predicted almost perfectly from m5 spectra, so that any transfer error dominates. As an in-domain check of the out-of-fold residual scores, the naive interval applied to the *primary* spectra of the test samples covered 0.900 on average at the nominal 0.90 (scenario range 0.872–0.932).


### 4.2. Intervals inherited from the primary instrument are over-confident

Reusing the primary-instrument interval after transfer (naive CP) gave mean coverages of 0.483 after PDS and 0.587 after DS at a nominal 0.90, with individual scenarios as low as 0.044 (Table 2, Fig. 3). The classical leverage-corrected interval was only marginally better (0.574 and 0.656), because leverage measures distance within the calibration space but not the transfer error. Weighted CP for covariate shift raised coverage to 0.612 and 0.634, yet produced unbounded intervals for 18% (PDS) and 11% (DS) of test samples (Table 2), a symptom of degenerate likelihood-ratio weights when transferred and primary spectra are easily distinguished. Pooling the labelled transfer residuals with the primary residuals (pooled CP) also under-covered (0.653, 0.706) because the *k* target residuals are swamped by the *n* primary residuals.

**Table 2.** Interval performance at nominal coverage 0.90 (α = 0.10), k = 10 transfer standards, 30 scenarios per transfer method (24 corn, 6 tablets). Scenario means over 100 random splits; ‘Valid’ = percentage of scenarios with mean coverage ≥ 0.88; width and interval score (IS) are divided by SD(y) and summarised by their median over scenarios; ∞ = unbounded intervals occurred. Methods marked ‘k labelled’ require reference values for the transfer standards. Per-dataset results: Table S2.

| Dataset | Transfer | Method | Mean cov. | Min cov. | Valid (%) | Width/SD | IS/SD |
|---|---|---|---|---|---|---|---|
| corn + tablets | DS | Naive CP (primary residuals) | 0.587 | 0.055 | 7 | 1.36 | 5.55 |
| corn + tablets | DS | Leverage PI (classical) | 0.656 | 0.071 | 7 | 1.71 | 4.71 |
| corn + tablets | DS | Weighted CP (covariate shift) | 0.634 | 0.260 | 3 | ∞ | ∞ |
| corn + tablets | DS | Gaussian TD (parametric) | 0.880 | 0.816 | 47 | 3.16 | 4.61 |
| corn + tablets | DS | TD-CP signed (pre-specified) | 0.883 | 0.793 | 60 | 3.29 | 4.69 |
| corn + tablets | DS | TD-CP absolute scores | 0.892 | 0.847 | 67 | 3.50 | 4.66 |
| corn + tablets | DS | TD-CP+ (jackknife+) | 0.927 | 0.899 | 100 | 3.98 | 4.62 |
| corn + tablets | DS | Target CP (k labelled) | 0.895 | 0.856 | 80 | 3.67 | 4.92 |
| corn + tablets | DS | Target CP+ (k labelled) | 0.926 | 0.910 | 100 | 4.26 | 4.97 |
| corn + tablets | DS | Target t-interval (k labelled) | 0.892 | 0.849 | 80 | 3.52 | 4.81 |
| corn + tablets | DS | Pooled CP (k labelled) | 0.706 | 0.506 | 3 | 1.78 | 5.04 |
| corn + tablets | PDS | Naive CP (primary residuals) | 0.483 | 0.044 | 0 | 1.36 | 14.29 |
| corn + tablets | PDS | Leverage PI (classical) | 0.574 | 0.085 | 0 | 2.18 | 10.59 |
| corn + tablets | PDS | Weighted CP (covariate shift) | 0.612 | 0.361 | 0 | ∞ | ∞ |
| corn + tablets | PDS | Gaussian TD (parametric) | 0.901 | 0.881 | 100 | 5.31 | 7.65 |
| corn + tablets | PDS | TD-CP signed (pre-specified) | 0.895 | 0.855 | 77 | 5.47 | 8.14 |
| corn + tablets | PDS | TD-CP absolute scores | 0.917 | 0.897 | 100 | 6.36 | 8.01 |
| corn + tablets | PDS | TD-CP+ (jackknife+) | 0.939 | 0.916 | 100 | 7.07 | 7.97 |
| corn + tablets | PDS | Target CP (k labelled) | 0.921 | 0.904 | 100 | 6.63 | 8.36 |
| corn + tablets | PDS | Target CP+ (k labelled) | 0.942 | 0.917 | 100 | 7.29 | 8.29 |
| corn + tablets | PDS | Target t-interval (k labelled) | 0.919 | 0.904 | 100 | 6.05 | 7.81 |
| corn + tablets | PDS | Pooled CP (k labelled) | 0.653 | 0.499 | 0 | 2.54 | 10.73 |

![**Fig. 3.** Coverage (top) and interval ](figures/fig3_main_results.png)

**Fig. 3.** Coverage (top) and interval score (bottom, log scale) per scenario for PDS (left) and DS (right) at α = 0.10. Dashed line: nominal 0.90. Each point is one directed instrument pair × property scenario (mean of 100 splits).


### 4.3. Transfer-discrepancy intervals restore coverage without reference values

Adding the cross-fitted transfer discrepancies brought the mean coverage of all TD-CP variants close to nominal (Table 2). The pre-specified signed TD-CP reached mean coverages of 0.895 (PDS) and 0.883 (DS) but was valid in only 77% and 60% of scenarios, missing the pre-specified criterion of 80%. The shortfall was concentrated on corn with DS, where even the target CP using reference values of all ten standards was valid in only 75% of scenarios. TD-CP+ was valid in every scenario for both transfer methods, with mean coverage 0.939 and 0.927: slightly conservative, as expected for jackknife+-type intervals. Its median normalised interval score (7.97 PDS, 4.62 DS) was lower than that of the labelled target CP+ (8.29, 4.97), which needs ten reference analyses on the secondary instrument, and close to that of the parametric Gaussian combination (7.65, 4.61). The Gaussian combination, however, was valid in only 47% of DS scenarios (minimum coverage 0.816), whereas TD-CP+ never fell below 0.899.

Paired comparisons across the 60 scenarios (Table 3) confirmed that TD-CP+ had a smaller absolute coverage gap than naive CP (Holm-adjusted *p* < 0.001, rank-biserial *r* = −1.00), the leverage interval (*p* < 0.001) and weighted CP (*p* < 0.001), and a lower interval score than naive CP (*p* < 0.001, *r* = −1.00) and than the labelled target CP+ (*p* < 0.001, *r* = −1.00). The Gaussian combination, in contrast, tended to have a slightly *lower* interval score than TD-CP+ (median paired difference 0.094 SD units, bootstrap 95% CI [0.024, 0.148], *r* = 0.39; unadjusted *p* = 0.008, Holm-adjusted *p* = 0.063); the advantage of TD-CP+ over it lies in validity under DS, not in efficiency. Note that the absolute coverage gap penalises over-coverage too, so the slightly conservative TD-CP+ is not favoured by this metric relative to methods centred on nominal coverage (e.g., *p* < 0.001 against the Gaussian combination, *r* = 0.59).

The most demanding comparator is the classical secondary-instrument validation interval: a bias-corrected *t*-interval built from the prediction errors of the ten standards after their reference values have been measured on the secondary instrument (M7; ASTM E1655-type practice [12]). It covered 0.919 (PDS) and 0.892 (DS) and was valid in 100% and 80% of scenarios, with median IS/SD 7.81 and 4.81. TD-CP+, which uses no reference values, had a slightly lower interval score in the paired comparison (*p* = 0.044, *r* = −0.42) and higher validity under DS, but a larger absolute coverage gap because it is more conservative (*p* < 0.001, *r* = 0.77). In other words, discrepancies measured on standards without reference analyses gave intervals of practically the same quality as a ten-sample reference validation on the secondary instrument.

Two caveats qualify these tests. First, scenarios are not independent: the 24 corn scenarios reuse the same 80 samples and the PDS and DS scenarios share splits, so the *p*-values are optimistic and the effect sizes and their consistency are more informative. Stratified by dataset and transfer method, TD-CP+ had a smaller absolute coverage gap than naive CP and weighted CP in at least 80% of the scenarios of every stratum (Table S5). Second, the 0.02 tolerance in the validity definition is a convention; with zero tolerance TD-CP+ was valid in 100% (PDS) and 97% (DS) of scenarios, versus 47% and 27% for the Gaussian combination (Table S6).

Coverage averaged over splits is a marginal property; a laboratory deploys a single calibration and a single transfer. Split-level coverage (Table S4) shows how much an individual deployment can deviate. With only 25 test samples, binomial noise alone is substantial for corn: even the ideal in-domain conformal interval (naive CP on the primary spectra) fell below 0.80 coverage in 9% of corn splits. TD-CP+ was below 0.80 in 5% (PDS) and 10% (DS) of corn splits and 1% and 6% of tablet splits, whereas naive CP was below 0.80 in 82% and 82% of corn splits and 68% and 54% of tablet splits.

**Table 3.** TD-CP+ versus each comparator at α = 0.10: medians over scenarios of the absolute coverage gap |coverage − 0.90| and of IS/SD, bootstrap 95% CI of the median paired difference (TD-CP+ − comparator), matched-pairs rank-biserial correlation r_rb (negative: TD-CP+ smaller) and two-sided Wilcoxon signed-rank p-values, Holm-adjusted over all 46 tests. Comparisons with the ablations and the pre-specified TD-CP: Table S7.

| Metric | Comparator | n | Median TD-CP+ | Median comp. | CI low | CI high | r_rb | p (Holm) |
|---|---|---|---|---|---|---|---|---|
| |coverage gap| | Naive CP (primary residuals) | 60 | 0.032 | 0.333 | -0.365 | -0.230 | -1.00 | <0.001 |
| |coverage gap| | Leverage PI (classical) | 60 | 0.032 | 0.254 | -0.269 | -0.159 | -1.00 | <0.001 |
| |coverage gap| | Weighted CP (covariate shift) | 60 | 0.032 | 0.269 | -0.280 | -0.201 | -1.00 | <0.001 |
| |coverage gap| | Gaussian TD (parametric) | 60 | 0.032 | 0.017 | 0.009 | 0.022 | 0.59 | 0.001 |
| |coverage gap| | Target CP (k labelled) | 60 | 0.032 | 0.016 | 0.012 | 0.022 | 0.72 | <0.001 |
| |coverage gap| | Target CP+ (k labelled) | 60 | 0.032 | 0.032 | -0.005 | 0.001 | -0.20 | 1.000 |
| |coverage gap| | Target t-interval (k labelled) | 60 | 0.032 | 0.018 | 0.015 | 0.022 | 0.77 | <0.001 |
| IS/SD | Naive CP (primary residuals) | 60 | 4.864 | 6.614 | -2.995 | -1.187 | -1.00 | <0.001 |
| IS/SD | Leverage PI (classical) | 60 | 4.864 | 5.586 | -1.264 | -0.280 | -0.80 | <0.001 |
| IS/SD | Weighted CP (covariate shift) | 60 | 4.864 | ∞ | −∞ | −∞ | -1.00 | <0.001 |
| IS/SD | Gaussian TD (parametric) | 60 | 4.864 | 4.773 | 0.024 | 0.148 | 0.39 | 0.063 |
| IS/SD | Target CP (k labelled) | 60 | 4.864 | 5.302 | -0.482 | -0.309 | -0.99 | <0.001 |
| IS/SD | Target CP+ (k labelled) | 60 | 4.864 | 5.069 | -0.280 | -0.234 | -1.00 | <0.001 |
| IS/SD | Target t-interval (k labelled) | 60 | 4.864 | 5.073 | -0.235 | -0.027 | -0.42 | 0.044 |


### 4.4. Ablation: which components matter

Cross-fitting is indispensable (Table 4, Fig. 4). With in-sample discrepancies, the standard deviation of δ shrank to a median of 0.62 (PDS) and 0.00 (DS) of its cross-fitted value. For DS the pseudo-inverse reproduces the standards exactly, so TD-CP collapsed to the naive interval (coverage 0.597); for PDS coverage reached only 0.789. Absolute rather than signed scores improved validity (PDS 100%, DS 67% of scenarios valid) at a similar interval score, consistent with pooling both tails of a discrepancy distribution estimated from only ten values. The jackknife+ construction raised DS validity from 67% to 100% without increasing the median interval score (4.66 vs. 4.62). The union-bound sum was valid but over-covered (0.966, 0.961) with larger interval scores (9.02, 5.55).

**Table 4.** Ablation of TD-CP components at α = 0.10 (columns as in Table 2).

| Dataset | Transfer | Method | Mean cov. | Min cov. | Valid (%) | Width/SD | IS/SD |
|---|---|---|---|---|---|---|---|
| corn + tablets | DS | TD-CP+ (jackknife+) | 0.927 | 0.899 | 100 | 3.98 | 4.62 |
| corn + tablets | DS | TD-CP absolute scores | 0.892 | 0.847 | 67 | 3.50 | 4.66 |
| corn + tablets | DS | TD-CP signed (pre-specified) | 0.883 | 0.793 | 60 | 3.29 | 4.69 |
| corn + tablets | DS | TD-CP w/o cross-fitting | 0.597 | 0.056 | 7 | 1.40 | 5.48 |
| corn + tablets | DS | TD-sum (union bound) | 0.961 | 0.870 | 93 | 4.93 | 5.55 |
| corn + tablets | DS | Gaussian TD (parametric) | 0.880 | 0.816 | 47 | 3.16 | 4.61 |
| corn + tablets | DS | Naive CP (primary residuals) | 0.587 | 0.055 | 7 | 1.36 | 5.55 |
| corn + tablets | PDS | TD-CP+ (jackknife+) | 0.939 | 0.916 | 100 | 7.07 | 7.97 |
| corn + tablets | PDS | TD-CP absolute scores | 0.917 | 0.897 | 100 | 6.36 | 8.01 |
| corn + tablets | PDS | TD-CP signed (pre-specified) | 0.895 | 0.855 | 77 | 5.47 | 8.14 |
| corn + tablets | PDS | TD-CP w/o cross-fitting | 0.789 | 0.627 | 0 | 3.52 | 8.16 |
| corn + tablets | PDS | TD-sum (union bound) | 0.966 | 0.924 | 100 | 7.63 | 9.02 |
| corn + tablets | PDS | Gaussian TD (parametric) | 0.901 | 0.881 | 100 | 5.31 | 7.65 |
| corn + tablets | PDS | Naive CP (primary residuals) | 0.483 | 0.044 | 0 | 1.36 | 14.29 |

![**Fig. 4.** Ablation: coverage gap (left](figures/fig4_ablation.png)

**Fig. 4.** Ablation: coverage gap (left) and interval score (right) per scenario, PDS and DS pooled.


### 4.5. Number of transfer standards

With *k* = 5 and 8 labelled standards, target CP cannot produce finite 90% intervals (Fig. 5), because ⌈0.9(*k* + 1)⌉ > *k*; the classical *t*-interval remains finite but was valid in only 80% (PDS) and 40% (DS) of scenarios at *k* = 5. TD-CP+ remained finite for every *k* because it borrows the *n* primary residuals. It was valid in all scenarios from *k* = 8 onwards for both transfer methods, and at *k* = 5 in 100% (PDS) and 47% (DS) of scenarios (coverage 0.950 and 0.875). Its interval score decreased with *k* (PDS: 13.81 at *k* = 5 to 4.23 at *k* = 30), reflecting the improved transfer itself. For DS with *k* = 5, the instability of a 5-spectrum pseudo-inverse is the limiting factor; we recommend *k* ≥ 8 standards.

![**Fig. 5.** Mean coverage (top) and inte](figures/fig5_k_sensitivity.png)

**Fig. 5.** Mean coverage (top) and interval score (bottom) versus the number of transfer standards k; error bars: 95% CI over scenarios. Target CP and Target CP+ are infinite (not shown) for k < 9.


### 4.6. Robustness and generalisation

Table 6 and Fig. 6 summarise the confirmatory experiments; none of them had been inspected when TD-CP+ was introduced, and three (unrepresentative standards, one-standard-error PLS, PDS window) were added during internal review. With Kennard–Stone selection of the standards, which violates the exchangeability between standards and test samples, TD-CP+ covered 0.962 (PDS) and 0.950 (DS). A harsher violation, drawing all standards from samples with reference values below the median, degraded the transfer itself (naive coverage 0.461 and 0.529); TD-CP+ covered 0.939 (PDS, valid in 100% of scenarios) and 0.876 (DS, 60%), against 0.942 and 0.880 for the labelled target CP+. With DS and unrepresentative standards, therefore, neither TD-CP+ nor the method using reference values for all standards was reliably valid: the discrepancies of standards from one part of the calibration range do not describe the transfer error elsewhere. Representative standards are a precondition for TD-CP+, as they are for the transfer itself. With SNV + first-derivative preprocessing it covered 0.936 and 0.925; with a ridge-regression calibration 0.945 (PDS). Because the corn models selected by minimum RMSECV were complex (median 10 latent variables for 45 samples) and complex models can be fragile to instrument differences, we repeated the study with the more parsimonious one-standard-error rule (median 8 latent variables for corn): naive CP still covered only 0.576 (PDS) and 0.621 (DS), while TD-CP+ covered 0.937 and 0.927. Varying the PDS window from 3 to 11 channels changed the transfer quality (naive coverage from 0.536 with 3 channels to 0.404 with 11) but not the validity of TD-CP+ (coverage 0.942 and 0.946). Added secondary-instrument noise (2% of the channel SD) gave 0.953, versus 0.339 for naive CP. Without any standardisation, the transfer discrepancy dominates the error, and TD-CP+ still covered 0.921 (naive CP: 0.283). Here, however, the symmetric TD-CP+ interval was much less efficient (IS/SD 5.61) than the signed TD-CP (2.35, coverage 0.917) or the Gaussian combination (2.28), because an uncorrected instrument difference produces a large systematic bias that only the signed constructions can shift the interval to absorb. When the discrepancies are strongly one-sided, the signed TD-CP is preferable. On the official IDRC partition of the tablets it covered 0.924 (PDS) and 0.916 (DS). For virtual secondary instruments of increasing severity, naive coverage fell from 0.895 to 0.741 (PDS), while TD-CP+ covered 0.918–0.924.

**Table 6.** Robustness and generalisation at α = 0.10: mean coverage over scenarios (30 per condition and transfer method; 7 for each simulated severity, 6 for the IDRC partition) and percentage of scenarios in which TD-CP+ was valid. All methods and interval scores: Table S9.

| Condition | Transfer | Naive CP | Gauss-TD | TD-CP signed | TD-CP+ | TD-CP+ valid (%) | Target CP+ (labelled) |
|---|---|---|---|---|---|---|---|
| standards from lower half of y | DS | 0.529 | 0.824 | 0.825 | 0.876 | 60 | 0.880 |
| standards from lower half of y | PDS | 0.461 | 0.894 | 0.887 | 0.939 | 100 | 0.942 |
| KS selection | DS | 0.573 | 0.915 | 0.917 | 0.950 | 100 | 0.958 |
| KS selection | PDS | 0.482 | 0.941 | 0.936 | 0.962 | 100 | 0.972 |
| no transfer | NONE | 0.283 | 0.903 | 0.917 | 0.921 | 100 | 0.912 |
| noise=0.005 | PDS | 0.406 | 0.899 | 0.888 | 0.945 | 100 | 0.948 |
| noise=0.01 | PDS | 0.365 | 0.899 | 0.888 | 0.948 | 100 | 0.952 |
| noise=0.02 | PDS | 0.339 | 0.907 | 0.895 | 0.953 | 100 | 0.957 |
| IDRC official split | DS | 0.780 | 0.918 | 0.907 | 0.915 | 100 | 0.924 |
| IDRC official split | PDS | 0.826 | 0.918 | 0.908 | 0.924 | 83 | 0.929 |
| PLS, 1-SE rule | DS | 0.621 | 0.888 | 0.892 | 0.927 | 100 | 0.927 |
| PLS, 1-SE rule | PDS | 0.576 | 0.907 | 0.905 | 0.937 | 100 | 0.938 |
| PDS window 11 | PDS | 0.404 | 0.891 | 0.881 | 0.946 | 100 | 0.950 |
| PDS window 3 | PDS | 0.536 | 0.906 | 0.903 | 0.942 | 100 | 0.944 |
| PDS window 7 | PDS | 0.437 | 0.907 | 0.898 | 0.950 | 100 | 0.952 |
| snv_sg1 | DS | 0.684 | 0.894 | 0.902 | 0.925 | 97 | 0.923 |
| snv_sg1 | PDS | 0.762 | 0.918 | 0.930 | 0.936 | 100 | 0.932 |
| ridge | PDS | 0.438 | 0.905 | 0.896 | 0.945 | 100 | 0.946 |
| severity=1 | DS | 0.564 | 0.897 | 0.886 | 0.916 | 100 | 0.922 |
| severity=1 | PDS | 0.895 | 0.911 | 0.922 | 0.918 | 100 | 0.918 |
| severity=2 | DS | 0.564 | 0.896 | 0.887 | 0.915 | 100 | 0.919 |
| severity=2 | PDS | 0.856 | 0.914 | 0.925 | 0.921 | 100 | 0.924 |
| severity=3 | DS | 0.546 | 0.900 | 0.893 | 0.915 | 100 | 0.923 |
| severity=3 | PDS | 0.741 | 0.915 | 0.917 | 0.924 | 100 | 0.927 |

![**Fig. 6.** Mean coverage under simulate](figures/fig6_robustness.png)

**Fig. 6.** Mean coverage under simulated instrument shifts (left), added secondary-instrument noise (centre, PDS) and other protocol changes (right, PDS). Dashed line: nominal 0.90.


### 4.7. Other nominal levels

At α = 0.05, target CP with ten standards is necessarily unbounded, whereas TD-CP+ covered 0.963 (PDS) and 0.956 (DS), valid in 100% and 93% of scenarios. At α = 0.20 it covered 0.849 and 0.845 (Fig. S2, Table S3). The conservativeness of TD-CP+ is therefore modest and roughly constant (≈ 0.03–0.05) across levels.


### 4.8. Error analysis

Coverage is marginal, not conditional. Fig. 7 shows that all methods covered samples with extreme reference values or high leverage less often than central samples; TD-CP+ attenuates but does not remove this pattern. The cross-fitted discrepancy spread closely tracked the true held-out discrepancy spread (median ratio 1.11, range 0.97–1.33), which explains why the reference-free estimate is sufficient. Assumption (A2) is only approximately met: the held-out Spearman correlation between primary residual and discrepancy averaged −0.10 (scenario range −0.40 to 0.03). Correlated residuals and discrepancies would widen the true error distribution beyond the convolution and are a plausible contributor to the residual under-coverage of the signed TD-CP; the jackknife+ margin absorbs it in these data. Fig. 8 illustrates a single split.

![**Fig. 7.** Error analysis at α = 0.10: ](figures/fig8_error_analysis.png)

**Fig. 7.** Error analysis at α = 0.10: coverage by tertile of the reference value (left) and of leverage (centre); cross-fitted versus held-out discrepancy SD, scaled by RMSECV (right).

![**Fig. 8.** Example (corn moisture, m5 →](figures/fig9_example_intervals.png)

**Fig. 8.** Example (corn moisture, m5 → mp6, PDS, k = 10, split seed 0): naive intervals (left) versus TD-CP+ (right) for the 25 secondary-instrument test samples.


### 4.9. Computational cost

TD-CP+ needs *k* additional transfer fits for cross-fitting, which took on average 13 ms (corn, PDS) and 56 ms (tablets, DS) per split on one CPU core, against 23–244 ms for fitting and cross-validating the PLS model (Table S8, Fig. S3). The interval step itself is O(*nk*) per test sample (a partial sort of *nk* candidate bounds): in a synthetic benchmark with *n* = 5000 primary residuals it took 0.21 ms per test sample for *k* = 10 and 0.82 ms for *k* = 30 on one core, against 0.0037 ms for the signed TD-CP (Fig. S1). The cost is negligible in practice.


### 4.10. Relation to existing approaches

TD-CP+ is not a new conformal principle: it applies the split-conformal finite-sample correction [17,18] and the jackknife+ construction [28] to an error decomposition that is specific to standardisation-based calibration transfer. Its novelty lies in (i) recognising that the transfer component of the error can be observed without reference values on the standards that DS/PDS already use, (ii) showing that cross-fitting is necessary for this observation to be informative (in-sample DS discrepancies are identically zero), and (iii) establishing, on public data, that the resulting intervals are valid where established alternatives are not. The Gaussian combination (M4) uses the same two ingredients and was slightly more efficient when valid, which indicates that most of the benefit comes from the discrepancy information itself; its validity, however, depended on the transfer method. The concurrent transported conformal calibration of Doula [25] also exploits unlabelled paired observations, but transports the labelled calibration set itself for set-valued classification and corrects residual mismatch with unlabelled target inputs; it was evaluated on image benchmarks. Weighted CP [24] targets covariate shift and, as shown above, is impractical for transferred spectra.


### 4.11. Practical recommendations and limitations

For a transferred calibration we recommend: (i) never reuse primary-instrument intervals; (ii) measure at least eight transfer standards and keep their primary spectra; (iii) compute cross-fitted discrepancies and report TD-CP+ intervals, which need no reference values for the standards; (iv) where reference values for the standards are known (e.g., re-measured calibration samples), TD-CP+ remains as efficient as the labelled alternatives or more so (Table 3; paired IS versus the *t*-interval: TD-CP+ lower in 50% of PDS and 87% of DS scenarios), and the labelled errors can additionally serve to verify coverage. Limitations: the evidence comes from two benchmark datasets (five instruments, seven properties) and from simulated instruments; coverage is marginal over samples and conditionally lower at the extremes; the discrepancies are informative only if the standards resemble routine samples, so spectrally dissimilar artefacts such as the glass standards supplied with the corn data cannot be used for δ (the model prediction for a glass spectrum is meaningless), and with DS, standards drawn from only half of the concentration range left 40% of scenarios invalid; the guarantee of Eq. (5) depends on assumptions (A1)–(A3), of which (A2) holds only approximately; TD-CP+ was introduced after the pre-specified main analysis, although its confirmatory evaluation used experiments that were not inspected beforehand; the protocol was fixed in a time-stamped version-control commit rather than in a public registry; and process or temporal drift on a single instrument was not studied because no suitable public paired data with continuous reference values were found.


## 5. Conclusions

Prediction intervals calibrated on a primary spectrometer substantially under-cover after calibration transfer, even when PDS or DS give acceptable point predictions. Splitting the error of a transferred prediction into a calibration residual and a transfer discrepancy, and estimating the latter without reference values from cross-fitted maps on the transfer standards, yields intervals with near-nominal (slightly conservative) coverage across 30 public benchmark scenarios, two transfer methods, several nominal levels and a range of robustness conditions, provided that the transfer standards represent the routine samples (with DS and standards from only half of the concentration range, validity was lost in a substantial fraction of scenarios). The jackknife+ form, TD-CP+, was required for reliable validity with the unstable DS map. The approach adds negligible computation, is independent of the regression model, and turns transfer standards that laboratories already measure into a source of validated uncertainty. Future work should evaluate it on process and long-term drift data and on conditional (sample-adaptive) coverage.


## CRediT authorship contribution statement

[Placeholder — to be completed by the authors, e.g., Conceptualization; Methodology; Software; Formal analysis; Writing – original draft; Writing – review & editing.]


## Declaration of competing interest

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.


## Declaration of generative AI and AI-assisted technologies in the manuscript preparation process

During the preparation of this work the authors used an AI system (Claude, Anthropic) to search the literature, write and run the analysis code, and draft the manuscript. After using this tool, the authors reviewed and edited the content as needed and take full responsibility for the content of the published article.


## Data availability

Both datasets are publicly available from Eigenvector Research (corn; NIR shootout 2002). The code, configuration, pre-specified protocol, raw per-split results (854,400 rows), statistical outputs, and scripts that regenerate every table, figure and number of this article are provided in the accompanying repository [link to be inserted upon acceptance].


## Funding

[Placeholder — funding sources or ‘This research did not receive any specific grant from funding agencies in the public, commercial, or not-for-profit sectors.’]


## Appendix A. Supplementary data

Supplementary material (Supplementary_Material.docx): Section S4 proof of Eq. (5); Table S1 per-scenario results; Table S2 main results by dataset; Table S3 coverage at all nominal levels; Table S4 split-level coverage; Table S5 stratum consistency; Table S6 tolerance sensitivity; Table S7 full statistical tests; Table S8 computation times; Table S9 all robustness results; Figs. S1–S3 scaling, nominal levels and computation time. Repository documents: S1 topic selection and pre-specified protocol; S2 iteration log; S3 literature matrix.


## References

[1] S. Wold, M. Sjöström, L. Eriksson, PLS-regression: a basic tool of chemometrics, Chemometr. Intell. Lab. Syst. 58 (2001) 109–130. https://doi.org/10.1016/S0169-7439(01)00155-1.
[2] J.J. Workman, A Review of Calibration Transfer Practices and Instrument Differences in Spectroscopy, Appl. Spectrosc. 72 (2018) 340–365. https://doi.org/10.1177/0003702817736064.
[3] R.N. Feudale, N.A. Woody, H. Tan, A.J. Myles, S.D. Brown, J. Ferré, Transfer of multivariate calibration models: a review, Chemometr. Intell. Lab. Syst. 64 (2002) 181–192. https://doi.org/10.1016/S0169-7439(02)00085-0.
[4] T. Fearn, Standardisation and Calibration Transfer for near Infrared Instruments: A Review, J. Near Infrared Spectrosc. 9 (2001) 229–244. https://doi.org/10.1255/jnirs.309.
[5] Y. Wang, D.J. Veltkamp, B.R. Kowalski, Multivariate instrument standardization, Anal. Chem. 63 (1991) 2750–2756. https://doi.org/10.1021/ac00023a016.
[6] E. Bouveresse, D. Massart, Improvement of the piecewise direct standardisation procedure for the transfer of NIR spectra for multivariate calibration, Chemometr. Intell. Lab. Syst. 32 (1996) 201–213. https://doi.org/10.1016/0169-7439(95)00074-7.
[7] B. Malli, A. Birlutiu, T. Natschläger, Standard-free calibration transfer - An evaluation of different techniques, Chemometr. Intell. Lab. Syst. 161 (2017) 49–60. https://doi.org/10.1016/j.chemolab.2016.12.008.
[8] Z. Xie, X. Chen, J.-M. Roger, S. Ali, G. Huang, W. Shi, Calibration transfer via filter learning, Anal. Chim. Acta 1298 (2024) 342404. https://doi.org/10.1016/j.aca.2024.342404.
[9] X. Huang, X. Chen, G. Huang, Z. Xie, W. Shi, X. Chen et al., UCT-LMIR: A standard-free unsupervised calibration transfer method without model recalibration, Anal. Chim. Acta 1423 (2026) 346104. https://doi.org/10.1016/j.aca.2026.346104.
[10] J. Gao, J. Li, J. Yin, R. Gao, Z. Tian, Y. Zhao et al., Cross-instrument coal quality spectral analysis via a PDS-assisted fine-tuning calibration transfer method, Anal. Chim. Acta 1405 (2026) 345485. https://doi.org/10.1016/j.aca.2026.345485.
[11] X. Fan, L. Shang, S. Zhao, J. Fan, S. Zhang, Q. Yang et al., PLSELM: A lightweight modeling approach for low-data calibration in near-infrared spectroscopy, Anal. Chim. Acta 1379 (2025) 344728. https://doi.org/10.1016/j.aca.2025.344728.
[12] ASTM E1655-17, Standard Practices for Infrared Multivariate Quantitative Analysis, ASTM International, West Conshohocken, PA, 2017.
[13] International Council for Harmonisation, ICH Q2(R2) Guideline: Validation of Analytical Procedures, 2023.
[14] K. Faber, B.R. Kowalski, Propagation of measurement errors for the validation of predictions obtained by principal component regression and partial least squares, J. Chemom. 11 (1997) 181–238. https://doi.org/10.1002/(SICI)1099-128X(199705)11:3<181::AID-CEM459>3.0.CO;2-7.
[15] N. Faber, X.-H. Song, P. Hopke, Sample-specific standard error of prediction for partial least squares regression, TrAC Trends Anal. Chem. 22 (2003) 330–334. https://doi.org/10.1016/s0165-9936(03)00503-x.
[16] V. Vovk, A. Gammerman, G. Shafer, Algorithmic Learning in a Random World, Springer, New York, 2005. https://doi.org/10.1007/b106715.
[17] H. Papadopoulos, K. Proedrou, V. Vovk, A. Gammerman, Inductive Confidence Machines for Regression, in: Machine Learning: ECML 2002, Lect. Notes Comput. Sci. 2430 (2002) 345–356. https://doi.org/10.1007/3-540-36755-1_29.
[18] J. Lei, M. G’Sell, A. Rinaldo, R.J. Tibshirani, L. Wasserman, Distribution-Free Predictive Inference for Regression, J. Am. Stat. Assoc. 113 (2018) 1094–1111. https://doi.org/10.1080/01621459.2017.1307116.
[19] A.N. Angelopoulos, S. Bates, Conformal Prediction: A Gentle Introduction, Found. Trends Mach. Learn. 16 (2023) 494–591. https://doi.org/10.1561/2200000101.
[20] O. Jovic, Conformal predictors in chemometric study of mid-infrared food adulteration: quantification of prediction uncertainty, Food Chem. 492 (2025) 145387. https://doi.org/10.1016/j.foodchem.2025.145387.
[21] J.K. Wiens, N. Solomatova, S. Shokatian, Calibrated Uncertainty Estimation for Soil Organic Carbon from Raman Spectra, Anal. Chem. 98 (2026) 309–316. https://doi.org/10.1021/acs.analchem.5c04616.
[22] Z.-S. Duma, O. Lamminpää, J. Susiluoto, H. Haario, T. Zheng, T. Sihvonen et al., Uncertainty calibration for latent-variable regression models, arXiv preprint arXiv:2512.23444 (2025).
[23] R.A. Haggam, R. Jayabal, K. Mehar, S.K. Jangid, J. Nanda, S.H. M et al., Chemometric and machine-learning strategies for calibration transfer and uncertainty quantification in portable optical analytical systems, Chemometr. Intell. Lab. Syst. 278 (2026) 105848. https://doi.org/10.1016/j.chemolab.2026.105848.
[24] R.J. Tibshirani, R.F. Barber, E.J. Candes, A. Ramdas, Conformal Prediction Under Covariate Shift, arXiv preprint arXiv:1904.06019 (2019).
[25] A. Doula, Conformal Calibration Transfer, arXiv preprint arXiv:2609.10737 (2026).
[26] A. Dvoretzky, J. Kiefer, J. Wolfowitz, Asymptotic Minimax Character of the Sample Distribution Function and of the Classical Multinomial Estimator, Ann. Math. Stat. 27 (1956) 642–669. https://doi.org/10.1214/aoms/1177728174.
[27] P. Massart, The Tight Constant in the Dvoretzky-Kiefer-Wolfowitz Inequality, Ann. Probab. 18 (1990) 1269–1283. https://doi.org/10.1214/aop/1176990746.
[28] R.F. Barber, E.J. Candès, A. Ramdas, R.J. Tibshirani, Predictive inference with the jackknife+, Ann. Stat. 49 (2021) 486–507. https://doi.org/10.1214/20-AOS1965.
[29] Eigenvector Research Inc., Data sets: NIR spectra of corn samples; NIR shootout 2002 pharmaceutical tablets. https://eigenvector.com/resources/data-sets/ (accessed 13 October 2026).
[30] T. Gneiting, A.E. Raftery, Strictly Proper Scoring Rules, Prediction, and Estimation, J. Am. Stat. Assoc. 102 (2007) 359–378. https://doi.org/10.1198/016214506000001437.
[31] F. Wilcoxon, Individual Comparisons by Ranking Methods, Biometrics Bull. 1 (1945) 80–83. https://doi.org/10.2307/3001968.
[32] S. Holm, A simple sequentially rejective multiple test procedure, Scand. J. Stat. 6 (1979) 65–70.
[33] D.S. Kerby, The Simple Difference Formula: An Approach to Teaching Nonparametric Correlation, Compr. Psychol. 3 (2014). https://doi.org/10.2466/11.IT.3.1.
[34] R.W. Kennard, L.A. Stone, Computer Aided Design of Experiments, Technometrics 11 (1969) 137–148. https://doi.org/10.1080/00401706.1969.10490666.
[35] R.J. Barnes, M.S. Dhanoa, S.J. Lister, Standard Normal Variate Transformation and De-Trending of Near-Infrared Diffuse Reflectance Spectra, Appl. Spectrosc. 43 (1989) 772–777. https://doi.org/10.1366/0003702894202201.
[36] A. Savitzky, M.J.E. Golay, Smoothing and Differentiation of Data by Simplified Least Squares Procedures, Anal. Chem. 36 (1964) 1627–1639. https://doi.org/10.1021/ac60214a047.
