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

**Background:** Calibration transfer (e.g., piecewise direct standardisation, PDS) lets a multivariate calibration built on a primary spectrometer be used on a secondary one, but transfer methods are judged almost exclusively by point accuracy. Prediction intervals inherited from the primary instrument implicitly assume that the transfer is perfect, and no distribution-free method exists to attach sample-wise uncertainty to a transferred calibration without new reference analyses on the secondary instrument.

**Results:** We decompose the secondary-instrument prediction error exactly into the primary calibration residual and a transfer discrepancy that can be measured, without reference values, on the transfer standards already used to fit PDS or direct standardisation (DS). Combining out-of-fold calibration residuals with cross-fitted discrepancies yields transfer-discrepancy conformal prediction (TD-CP) and a jackknife+ variant (TD-CP+). On two public NIR benchmarks (corn, three instruments; pharmaceutical tablets, two instruments; 30 directed instrument-pair × property scenarios, 100 random splits each, k = 10 standards), intervals calibrated on the primary instrument covered only 0.483 (PDS) and 0.587 (DS) of secondary-instrument samples at a nominal 0.90. TD-CP+ reached 0.939 and 0.927, was within 0.02 of nominal or above in 100% and 100% of scenarios, and had a lower interval score than a comparator requiring reference values for all ten standards. The pre-registered signed TD-CP fell short of its validity criterion with DS.

**Significance:** Transferred calibrations can be accompanied by sample-wise intervals with near-nominal coverage at no extra reference-analysis cost, whereas the common practice of reusing primary-instrument intervals is markedly over-confident. The method is model-agnostic, computationally negligible and openly released.

**Keywords:** Calibration transfer; Conformal prediction; Prediction interval; Near-infrared spectroscopy; Piecewise direct standardisation; Uncertainty quantification


## 1. Introduction

Near-infrared (NIR) and other vibrational spectroscopic methods rely on multivariate calibrations such as partial least squares (PLS) regression [1]. Because spectra of the same sample differ between instruments, a calibration developed on a primary (master) instrument generally cannot be applied to a secondary (slave) instrument without correction [2–4]. Calibration transfer methods such as direct standardisation (DS) and piecewise direct standardisation (PDS) [5,6] map secondary spectra onto the primary domain using a small set of transfer standards measured on both instruments, and the field continues to produce new transfer strategies, including standard-free and few-shot approaches [7–11].

These methods are almost invariably evaluated by point-prediction accuracy (RMSEP, R^{2}). Method validation and routine release decisions, however, require statements about the uncertainty of individual predictions [12,13]. Sample-specific prediction errors for PLS have been derived by error propagation and leverage arguments [14,15], and conformal prediction (CP), which provides distribution-free finite-sample coverage under exchangeability [16–19], has recently been applied to mid-infrared, Raman and NIR regression [20–22]. All of these approaches assume that new spectra come from the same measurement domain as the calibration data. After transfer this assumption fails twice: the secondary spectra differ from the primary spectra, and the transfer map itself is estimated from few standards and is imperfect. A recent review of calibration transfer and uncertainty quantification for portable optical systems emphasises this gap but proposes no validated interval method [23].

Two generic remedies are available but unattractive. Re-calibrating the interval on the secondary instrument requires reference analyses for a sufficiently large labelled set: with k labelled standards, split CP cannot produce a finite 95% interval unless k ≥ 19. Weighted CP for covariate shift [24] requires overlapping supports and estimable likelihood ratios, which are fragile for high-dimensional transferred spectra. A concurrent machine-learning paper transports a labelled source calibration set through unlabelled paired observations for set-valued classification [25]; it does not address regression intervals after chemometric standardisation.

Here we exploit a simple identity: the error of a transferred prediction equals the primary calibration residual plus a *transfer discrepancy*, the difference between the primary-model prediction from the primary spectrum and from the transferred secondary spectrum. The discrepancy needs no reference value and can be measured on the transfer standards that DS/PDS already require, provided that the transfer map is cross-fitted. The contributions are: (i) transfer-discrepancy conformal prediction (TD-CP), which combines out-of-fold calibration residuals with cross-fitted discrepancies, together with a conditional finite-sample coverage statement; (ii) a jackknife+ variant (TD-CP+) that remains reliable when the transfer map is unstable, as DS is when k ≪ p; and (iii) a benchmark of interval validity after transfer on two public multi-instrument datasets, with pre-registered analysis, ablations, robustness tests and open code. We report all pre-registered outcomes, including the one that the pre-registered signed TD-CP did not meet.

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

TD-CP combines the two empirical distributions through the *nk* sums *r*_{i} + δ_{j}. The pre-registered signed version sets *U* to the ⌈(1 − α/2)(*n* + 1)*k*⌉-th smallest sum and *L* to the mirrored order statistic, so that systematic transfer bias shifts the interval. The absolute-score version uses the *m*-th smallest of the *nk* values |*r*_{i} + δ_{j}|, denoted |*r* + δ|_{(m)}:

$$ \hat{q}=|r+\delta|_{(m)},\ \ m=\lceil(1-\alpha)(n+1)k\rceil,\qquad C(x^{S})=[\hat{y}-\hat{q},\ \hat{y}+\hat{q}] \qquad (4) $$

The (*n* + 1) factor is the usual finite-sample correction of split CP; if the index exceeds *nk* the interval is unbounded. Under exchangeable residuals (A1), independence between residuals and discrepancies (A2) and i.i.d. discrepancies with cdf *F*_{δ} (A3), the coverage conditional on the standards satisfies

$$ P\{L\leq y-\hat{y}\leq U\mid\delta_{1:k}\}\ \geq\ 1-\alpha-2D_{k},\qquad D_{k}=\sup_{t}|\hat{F}_{k}(t)-F_{\delta}(t)| \qquad (5) $$

with P(*D*_{k} > ε) ≤ 2 exp(−2*k*ε^{2}) [26,27]. The proof (Supplementary S4) is a rank argument on the augmented set {*r*_{i} + δ_{j}: *i* = 0, …, *n*}; when the test discrepancy is drawn from the empirical distribution of the δ_{j}, coverage ≥ 1 − α holds exactly. The bound makes explicit that (A2) is an assumption and that the guarantee loosens for small *k*; both are examined empirically below.


### 2.4. Jackknife+ variant (TD-CP+)

Cross-fitted discrepancies describe maps fitted on *k* − 1 standards, whereas predictions use the map fitted on all *k*. For unstable maps, such as DS with *k* ≪ *p*, these are not interchangeable, the situation in which jackknife intervals can fail and the jackknife+ was proposed [28]. TD-CP+ attaches each radius |*r*_{i} + δ_{j}| to the leave-one-out prediction of its own map:

$$ C^{+}(x^{S})=\left[\hat{q}^{-}_{\alpha}\{f(T_{-j}(x^{S}))-|r_{i}+\delta_{j}|\},\ \hat{q}^{+}_{1-\alpha}\{f(T_{-j}(x^{S}))+|r_{i}+\delta_{j}|\}\right] \qquad (6) $$

where q̂^{+}_{1−α} is the ⌈(1 − α)(*n* + 1)*k*⌉-th smallest of the *nk* values and q̂^{−}_{α} the mirrored order statistic. If the transfer map does not depend on which standard is left out, Eq. (6) reduces to Eq. (4). TD-CP+ was added after inspection of the pre-registered main experiment (Supplementary S2) and is therefore evaluated on confirmatory experiments that had not been examined when it was introduced.


### 2.5. Comparison methods

All interval methods share the same point prediction ŷ. Label-free comparators: (M1) naive split CP with the primary residuals, ±q̂_{1−α}(|*r*|); (M2) the classical leverage-corrected PLS interval, ±*t*_{1−α/2, n−A−1}·RMSECV·(1 + 1/*n* + *h*)^{1/2} with *h* the leverage of the transferred spectrum [12,15]; (M3) weighted CP under covariate shift [24] with likelihood ratios from a logistic-regression classifier on PLS scores of master versus transferred test spectra; and (M4) a Gaussian combination of the same information used by TD-CP, ŷ + mean(*r*) + mean(δ) ± *z*_{1−α/2}(RMSECV^{2} + s_{δ}^{2})^{1/2}. Methods that additionally require reference values for the *k* standards (an advantaged reference rather than a competitor): (M5) target split CP on leave-one-out target residuals *e*_{j} = *y*_{j} − *f*(*T*_{−*j*}(*x*_{j}^{S})); (M5+) its jackknife+ version; and (M6) pooled CP on {|*r*_{i}|} ∪ {|*e*_{j}|}. Ablations: TD-CP without cross-fitting (in-sample δ), signed versus absolute scores, and a union-bound sum q̂_{1−α/2}(|*r*|) + Q_{1−α/2}(|δ|).


## 3. Experimental


### 3.1. Data

Two public multi-instrument NIR benchmarks distributed by Eigenvector Research were used [29] (Table 1, Fig. 2). Corn: 80 samples measured on three spectrometers (m5, mp5, mp6; 1100–2498 nm, 2 nm, 700 channels) with moisture, oil, protein and starch reference values; all six directed instrument pairs were used. Pharmaceutical tablets (IDRC 2002 shootout): 655 tablets measured on two spectrometers (600–1898 nm, 650 channels) with weight, hardness and assay; both directions were used. This gives 24 + 6 = 30 directed pair × property scenarios. Files were verified by SHA-256 digests. A third candidate dataset (MicroNIR temperature series) was excluded before analysis because its nine formulations span only three nominal concentration levels (Supplementary S1).


### 3.2. Calibration and transfer

PLS1 models (NIPALS, mean-centred raw spectra) were fitted on the primary spectra of the master set, with the number of latent variables chosen by minimum 10-fold RMSECV (maximum 15 for corn, 20 for tablets); the out-of-fold residuals at that complexity served as calibration scores. PDS used a five-channel window with local ridge regression (λ = 10^{−6} × trace of the local Gram matrix) and inward-shifted windows at the spectral edges; DS used the Moore–Penrose pseudo-inverse of the centred secondary standards (rcond = 10^{−6}). These hyperparameters were fixed in advance and not tuned.


### 3.3. Splitting protocol and leakage control

In each repetition the samples were randomly partitioned into disjoint test, transfer and master sets: corn 25/10/45 and tablets 200/10/445. All operations that use reference values (PLS fitting, complexity selection, residuals) used only the master set; transfer maps used only the primary and secondary spectra of the transfer standards; test samples contributed only their secondary spectra. Their primary spectra and reference values were used exclusively for evaluation and diagnostics. Each scenario was repeated with split seeds 0–99 fixed in advance (100 repetitions, 6,000 splits in total for the two transfer methods).


### 3.4. Performance measures and statistical analysis

For every split we computed empirical coverage, mean interval width and the interval (Winkler) score [30]

$$ \mathrm{IS}_{\alpha}=(u-l)+\frac{2}{\alpha}(l-y)\,\mathbf{1}\{y<l\}+\frac{2}{\alpha}(y-u)\,\mathbf{1}\{y>u\} \qquad (7) $$

which rewards narrow intervals and penalises misses (lower is better). Width and IS were divided by the standard deviation of the property to pool scenarios. Because repetitions within a scenario share samples, the scenario mean was the unit of analysis. A scenario was called *valid* if its mean coverage was at least 1 − α − 0.02; the pre-registered success criterion was validity in ≥80% of scenarios for each transfer method. Methods were compared with two-sided Wilcoxon signed-rank tests over the paired scenario means [31] of the absolute coverage gap and of the normalised IS, with Holm adjustment across all 42 comparisons [32], matched-pairs rank-biserial correlations as effect sizes [33] and percentile bootstrap 95% confidence intervals of the median paired difference (10,000 resamples). Infinite intervals were ranked as worst.


### 3.5. Robustness and generalisation experiments

Additional experiments (50 repetitions unless noted) varied one factor at a time: the number of standards *k* ∈ {5, 8, 10, 15, 20, 30}; Kennard–Stone instead of random selection of standards [34] (100 repetitions); SNV followed by a Savitzky–Golay first derivative (11 points, second order) [35,36]; ridge regression instead of PLS; Gaussian noise added to secondary spectra (0.5, 1 and 2% of the mean channel standard deviation); no standardisation at all; the official IDRC calibration/validation/test partition of the tablets (100 repetitions over random standard selection); and virtual secondary instruments obtained by perturbing the primary spectra with wavelength shifts (0.5–2 channels), band broadening (Gaussian σ = 1–3 channels), gain (2–10%), sloped baselines and noise at three severity levels. Nominal levels 0.80, 0.90 and 0.95 were analysed for the main experiment.


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

The selected PLS models used 8–15 latent variables for corn and 3–20 for tablets. Transfer was imperfect: the median ratio of the secondary-instrument RMSEP after transfer to the RMSEP obtained from the primary spectra of the same test samples was 2.2 (range 1.1–52.6; Table S1), i.e., the transferred predictions carried an error component absent on the primary instrument. As an in-domain check of the out-of-fold residual scores, the naive interval applied to the *primary* spectra of the test samples covered 0.900 on average at the nominal 0.90 (scenario range 0.872–0.932).


### 4.2. Intervals inherited from the primary instrument are over-confident

Reusing the primary-instrument interval after transfer (naive CP) gave mean coverages of 0.483 after PDS and 0.587 after DS at a nominal 0.90, with individual scenarios as low as 0.044 (Table 2, Fig. 3). The classical leverage-corrected interval was only marginally better (0.574 and 0.656), because leverage measures distance within the calibration space but not the transfer error. Weighted CP for covariate shift raised coverage to 0.713 and 0.739, yet produced unbounded intervals for a sizeable fraction of test samples (Table 2): the classifier separates transferred from primary spectra almost perfectly, so the likelihood ratios degenerate. Pooling the labelled transfer residuals with the primary residuals (pooled CP) also under-covered (0.653, 0.706) because the *k* target residuals are swamped by the *n* primary residuals.

**Table 2.** Interval performance at nominal coverage 0.90 (α = 0.10), k = 10 transfer standards. Scenario means over 100 random splits; ‘Valid’ = percentage of scenarios with mean coverage ≥ 0.88; width and interval score (IS) are divided by SD(y) and summarised by their median over scenarios. Methods marked ‘k labelled’ require reference values for the transfer standards.

| Dataset | Transfer | Method | Mean cov. | Min cov. | Valid (%) | Width/SD | IS/SD |
|---|---|---|---|---|---|---|---|
| corn | DS | Naive CP (primary residuals) | 0.554 | 0.055 | 0 | 1.30 | 6.61 |
| corn | DS | Leverage PI (classical) | 0.627 | 0.071 | 0 | 1.66 | 5.44 |
| corn | DS | Weighted CP (covariate shift) | 0.743 | 0.520 | 0 | ∞ | ∞ |
| corn | DS | Gaussian TD (parametric) | 0.870 | 0.816 | 33 | 3.23 | 4.73 |
| corn | DS | TD-CP signed (pre-registered) | 0.877 | 0.793 | 50 | 3.35 | 4.81 |
| corn | DS | TD-CP absolute scores | 0.886 | 0.847 | 58 | 3.51 | 4.84 |
| corn | DS | TD-CP+ (jackknife+) | 0.929 | 0.909 | 100 | 4.05 | 4.74 |
| corn | DS | Target CP (k labelled) | 0.889 | 0.856 | 75 | 3.71 | 4.93 |
| corn | DS | Target CP+ (k labelled) | 0.926 | 0.910 | 100 | 4.29 | 4.99 |
| corn | DS | Pooled CP (k labelled) | 0.702 | 0.543 | 0 | 1.77 | 5.25 |
| corn | PDS | Naive CP (primary residuals) | 0.445 | 0.044 | 0 | 1.30 | 18.76 |
| corn | PDS | Leverage PI (classical) | 0.541 | 0.085 | 0 | 2.09 | 12.84 |
| corn | PDS | Weighted CP (covariate shift) | 0.708 | 0.560 | 0 | ∞ | ∞ |
| corn | PDS | Gaussian TD (parametric) | 0.896 | 0.881 | 100 | 5.42 | 7.90 |
| corn | PDS | TD-CP signed (pre-registered) | 0.893 | 0.855 | 71 | 5.75 | 8.43 |
| corn | PDS | TD-CP absolute scores | 0.916 | 0.897 | 100 | 6.58 | 8.53 |
| corn | PDS | TD-CP+ (jackknife+) | 0.939 | 0.920 | 100 | 7.24 | 8.37 |
| corn | PDS | Target CP (k labelled) | 0.918 | 0.904 | 100 | 6.75 | 8.58 |
| corn | PDS | Target CP+ (k labelled) | 0.941 | 0.918 | 100 | 7.40 | 8.47 |
| corn | PDS | Pooled CP (k labelled) | 0.655 | 0.551 | 0 | 2.57 | 11.10 |
| tablets | DS | Naive CP (primary residuals) | 0.720 | 0.492 | 33 | 2.37 | 4.28 |
| tablets | DS | Leverage PI (classical) | 0.773 | 0.616 | 33 | 2.49 | 3.85 |
| tablets | DS | Weighted CP (covariate shift) | 0.723 | 0.511 | 17 | ∞ | ∞ |
| tablets | DS | Gaussian TD (parametric) | 0.918 | 0.911 | 100 | 2.96 | 3.88 |
| tablets | DS | TD-CP signed (pre-registered) | 0.905 | 0.887 | 100 | 2.92 | 3.87 |
| tablets | DS | TD-CP absolute scores | 0.914 | 0.908 | 100 | 2.91 | 3.88 |
| tablets | DS | TD-CP+ (jackknife+) | 0.918 | 0.899 | 100 | 2.96 | 3.86 |
| tablets | DS | Target CP (k labelled) | 0.921 | 0.906 | 100 | 3.62 | 4.60 |
| tablets | DS | Target CP+ (k labelled) | 0.924 | 0.914 | 100 | 3.67 | 4.58 |
| tablets | DS | Pooled CP (k labelled) | 0.726 | 0.506 | 17 | 2.39 | 4.18 |
| tablets | PDS | Naive CP (primary residuals) | 0.635 | 0.487 | 0 | 2.37 | 5.44 |
| tablets | PDS | Leverage PI (classical) | 0.703 | 0.536 | 0 | 2.60 | 5.17 |
| tablets | PDS | Weighted CP (covariate shift) | 0.734 | 0.653 | 0 | ∞ | ∞ |
| tablets | PDS | Gaussian TD (parametric) | 0.920 | 0.912 | 100 | 3.78 | 4.79 |
| tablets | PDS | TD-CP signed (pre-registered) | 0.900 | 0.892 | 100 | 3.75 | 4.86 |
| tablets | PDS | TD-CP absolute scores | 0.920 | 0.912 | 100 | 3.86 | 4.89 |
| tablets | PDS | TD-CP+ (jackknife+) | 0.940 | 0.916 | 100 | 4.10 | 4.98 |
| tablets | PDS | Target CP (k labelled) | 0.930 | 0.912 | 100 | 4.75 | 5.74 |
| tablets | PDS | Target CP+ (k labelled) | 0.947 | 0.917 | 100 | 5.02 | 5.88 |
| tablets | PDS | Pooled CP (k labelled) | 0.645 | 0.499 | 0 | 2.45 | 5.38 |

![**Fig. 3.** Coverage (top) and interval ](figures/fig3_main_results.png)

**Fig. 3.** Coverage (top) and interval score (bottom, log scale) per scenario for PDS (left) and DS (right) at α = 0.10. Dashed line: nominal 0.90. Each point is one directed instrument pair × property scenario (mean of 100 splits).


### 4.3. Transfer-discrepancy intervals restore coverage without reference values

Adding the cross-fitted transfer discrepancies restored coverage close to nominal for all TD-CP variants (Table 2). The pre-registered signed TD-CP reached mean coverages of 0.895 (PDS) and 0.883 (DS) but was valid in only 77% and 60% of scenarios, missing the pre-registered criterion of 80%. The shortfall was concentrated on corn with DS, where even the target CP using reference values of all ten standards was valid in only 75% of scenarios. TD-CP+ was valid in 100% (PDS) and 100% (DS) of scenarios, with mean coverage 0.939 and 0.927: slightly conservative, as expected for jackknife+-type intervals. Its median normalised interval score (7.97 PDS, 4.62 DS) was lower than that of the labelled target CP+ (8.29, 4.97), which needs ten reference analyses on the secondary instrument, and close to that of the parametric Gaussian combination (7.65, 4.61). The Gaussian combination, however, was valid in only 47% of DS scenarios (minimum coverage 0.816), whereas TD-CP+ never fell below 0.899.

Paired comparisons across the 60 scenarios (Table 3) confirmed that TD-CP+ had a smaller absolute coverage gap than naive CP (Holm-adjusted *p* = <0.001, rank-biserial *r* = -1.00), the leverage interval (*p* = <0.001) and weighted CP (*p* = <0.001), and a lower interval score than naive CP (*p* = <0.001, *r* = -1.00) and than the labelled target CP+ (*p* = <0.001, *r* = -1.00). The Gaussian combination, in contrast, had a slightly *lower* interval score than TD-CP+ (median paired difference 0.094 SD units, 95% CI [0.024, 0.148], *p* = 0.047, *r* = 0.39); the advantage of TD-CP+ over it lies in validity under DS, not in efficiency. Note that the absolute coverage gap penalises over-coverage too, so the slightly conservative TD-CP+ is not favoured by this metric relative to methods centred on nominal coverage (e.g., *p* = <0.001 against the Gaussian combination, *r* = 0.59).

**Table 3.** TD-CP+ versus each comparator at α = 0.10: medians over scenarios of the absolute coverage gap |coverage − 0.90| and of IS/SD, bootstrap 95% CI of the median paired difference (TD-CP+ − comparator), matched-pairs rank-biserial correlation r_rb (negative: TD-CP+ smaller) and two-sided Wilcoxon signed-rank p-values, Holm-adjusted over all 42 tests (including those for the pre-registered TD-CP, Supplementary).

| Metric | Comparator | n | Median TD-CP+ | Median comp. | CI low | CI high | r_rb | p (Holm) |
|---|---|---|---|---|---|---|---|---|
| |coverage gap| | Naive CP (primary residuals) | 60 | 0.032 | 0.333 | -0.365 | -0.230 | -1.00 | <0.001 |
| |coverage gap| | Leverage PI (classical) | 60 | 0.032 | 0.254 | -0.269 | -0.159 | -1.00 | <0.001 |
| |coverage gap| | Weighted CP (covariate shift) | 60 | 0.032 | 0.171 | -0.156 | -0.113 | -1.00 | <0.001 |
| |coverage gap| | Gaussian TD (parametric) | 60 | 0.032 | 0.017 | 0.009 | 0.022 | 0.59 | 0.001 |
| |coverage gap| | TD-CP signed (pre-registered) | 60 | 0.032 | 0.015 | 0.008 | 0.022 | 0.66 | <0.001 |
| |coverage gap| | TD-CP absolute scores | 60 | 0.032 | 0.016 | 0.014 | 0.023 | 0.78 | <0.001 |
| |coverage gap| | TD-CP w/o cross-fitting | 60 | 0.032 | 0.161 | -0.192 | -0.087 | -0.98 | <0.001 |
| |coverage gap| | TD-sum (union bound) | 60 | 0.032 | 0.069 | -0.042 | -0.030 | -0.95 | <0.001 |
| |coverage gap| | Target CP (k labelled) | 60 | 0.032 | 0.016 | 0.012 | 0.022 | 0.72 | <0.001 |
| |coverage gap| | Target CP+ (k labelled) | 60 | 0.032 | 0.032 | -0.005 | 0.001 | -0.20 | 0.750 |
| |coverage gap| | Pooled CP (k labelled) | 60 | 0.032 | 0.235 | -0.223 | -0.146 | -1.00 | <0.001 |
| IS/SD | Naive CP (primary residuals) | 60 | 4.864 | 6.614 | -2.995 | -1.187 | -1.00 | <0.001 |
| IS/SD | Leverage PI (classical) | 60 | 4.864 | 5.586 | -1.264 | -0.280 | -0.80 | <0.001 |
| IS/SD | Weighted CP (covariate shift) | 60 | 4.864 | ∞ | −∞ | −∞ | -1.00 | <0.001 |
| IS/SD | Gaussian TD (parametric) | 60 | 4.864 | 4.773 | 0.024 | 0.148 | 0.39 | 0.047 |
| IS/SD | TD-CP signed (pre-registered) | 60 | 4.864 | 4.965 | -0.198 | -0.034 | -0.63 | <0.001 |
| IS/SD | TD-CP absolute scores | 60 | 4.864 | 5.027 | -0.213 | -0.073 | -0.72 | <0.001 |
| IS/SD | TD-CP w/o cross-fitting | 60 | 4.864 | 6.516 | -0.866 | -0.353 | -0.80 | <0.001 |
| IS/SD | TD-sum (union bound) | 60 | 4.864 | 5.911 | -1.113 | -0.953 | -1.00 | <0.001 |
| IS/SD | Target CP (k labelled) | 60 | 4.864 | 5.302 | -0.482 | -0.309 | -0.99 | <0.001 |
| IS/SD | Target CP+ (k labelled) | 60 | 4.864 | 5.069 | -0.280 | -0.234 | -1.00 | <0.001 |
| IS/SD | Pooled CP (k labelled) | 60 | 4.864 | 5.413 | -1.299 | -0.545 | -1.00 | <0.001 |
| |coverage gap| | Naive CP (primary residuals) | 60 | 0.015 | 0.333 | -0.393 | -0.251 | -1.00 | <0.001 |
| |coverage gap| | Leverage PI (classical) | 60 | 0.015 | 0.254 | -0.291 | -0.185 | -1.00 | <0.001 |
| |coverage gap| | Weighted CP (covariate shift) | 60 | 0.015 | 0.171 | -0.186 | -0.129 | -1.00 | <0.001 |
| |coverage gap| | Gaussian TD (parametric) | 60 | 0.015 | 0.017 | -0.005 | 0.005 | 0.07 | 1.000 |
| |coverage gap| | TD-CP absolute scores | 60 | 0.015 | 0.016 | -0.002 | 0.006 | 0.22 | 0.652 |
| |coverage gap| | TD-CP w/o cross-fitting | 60 | 0.015 | 0.161 | -0.207 | -0.110 | -1.00 | <0.001 |
| |coverage gap| | TD-sum (union bound) | 60 | 0.015 | 0.069 | -0.063 | -0.050 | -0.86 | <0.001 |
| |coverage gap| | Target CP (k labelled) | 60 | 0.015 | 0.016 | -0.005 | 0.005 | 0.12 | 1.000 |
| |coverage gap| | Target CP+ (k labelled) | 60 | 0.015 | 0.032 | -0.019 | -0.006 | -0.67 | <0.001 |
| |coverage gap| | Pooled CP (k labelled) | 60 | 0.015 | 0.235 | -0.227 | -0.160 | -1.00 | <0.001 |
| IS/SD | Naive CP (primary residuals) | 60 | 4.965 | 6.614 | -2.522 | -1.212 | -1.00 | <0.001 |
| IS/SD | Leverage PI (classical) | 60 | 4.965 | 5.586 | -1.083 | -0.191 | -0.75 | <0.001 |
| IS/SD | Weighted CP (covariate shift) | 60 | 4.965 | ∞ | −∞ | −∞ | -1.00 | <0.001 |
| IS/SD | Gaussian TD (parametric) | 60 | 4.965 | 4.773 | 0.102 | 0.193 | 0.97 | <0.001 |
| IS/SD | TD-CP absolute scores | 60 | 4.965 | 5.027 | -0.041 | 0.028 | -0.12 | 1.000 |
| IS/SD | TD-CP w/o cross-fitting | 60 | 4.965 | 6.516 | -0.774 | -0.211 | -0.71 | <0.001 |
| IS/SD | TD-sum (union bound) | 60 | 4.965 | 5.911 | -1.082 | -0.692 | -1.00 | <0.001 |
| IS/SD | Target CP (k labelled) | 60 | 4.965 | 5.302 | -0.280 | -0.164 | -0.97 | <0.001 |
| IS/SD | Target CP+ (k labelled) | 60 | 4.965 | 5.069 | -0.269 | -0.042 | -0.54 | 0.002 |
| IS/SD | Pooled CP (k labelled) | 60 | 4.965 | 5.413 | -1.160 | -0.465 | -0.99 | <0.001 |


### 4.4. Ablation: which components matter

Cross-fitting is indispensable (Table 4, Fig. 4). With in-sample discrepancies, the standard deviation of δ shrank to a median of 0.62 (PDS) and 0.00 (DS) of its cross-fitted value. For DS the pseudo-inverse reproduces the standards exactly, so TD-CP collapsed to the naive interval (coverage 0.597); for PDS coverage reached only 0.789. Absolute rather than signed scores improved validity (PDS 100%, DS 67% of scenarios valid) at a similar interval score, consistent with pooling both tails of a discrepancy distribution estimated from only ten values. The jackknife+ construction raised DS validity from 67% to 100% without increasing the median interval score (4.66 vs. 4.62). The union-bound sum was valid but over-covered (0.966, 0.961) with larger interval scores (9.02, 5.55).

**Table 4.** Ablation of TD-CP components at α = 0.10 (columns as in Table 2).

| Dataset | Transfer | Method | Mean cov. | Min cov. | Valid (%) | Width/SD | IS/SD |
|---|---|---|---|---|---|---|---|
| corn | DS | TD-CP+ (jackknife+) | 0.929 | 0.909 | 100 | 4.05 | 4.74 |
| corn | DS | TD-CP absolute scores | 0.886 | 0.847 | 58 | 3.51 | 4.84 |
| corn | DS | TD-CP signed (pre-registered) | 0.877 | 0.793 | 50 | 3.35 | 4.81 |
| corn | DS | TD-CP w/o cross-fitting | 0.566 | 0.056 | 0 | 1.35 | 6.52 |
| corn | DS | TD-sum (union bound) | 0.957 | 0.870 | 92 | 5.06 | 5.57 |
| corn | DS | Gaussian TD (parametric) | 0.870 | 0.816 | 33 | 3.23 | 4.73 |
| corn | DS | Naive CP (primary residuals) | 0.554 | 0.055 | 0 | 1.30 | 6.61 |
| corn | PDS | TD-CP+ (jackknife+) | 0.939 | 0.920 | 100 | 7.24 | 8.37 |
| corn | PDS | TD-CP absolute scores | 0.916 | 0.897 | 100 | 6.58 | 8.53 |
| corn | PDS | TD-CP signed (pre-registered) | 0.893 | 0.855 | 71 | 5.75 | 8.43 |
| corn | PDS | TD-CP w/o cross-fitting | 0.805 | 0.726 | 0 | 4.02 | 8.56 |
| corn | PDS | TD-sum (union bound) | 0.963 | 0.924 | 100 | 8.50 | 9.34 |
| corn | PDS | Gaussian TD (parametric) | 0.896 | 0.881 | 100 | 5.42 | 7.90 |
| corn | PDS | Naive CP (primary residuals) | 0.445 | 0.044 | 0 | 1.30 | 18.76 |
| tablets | DS | TD-CP+ (jackknife+) | 0.918 | 0.899 | 100 | 2.96 | 3.86 |
| tablets | DS | TD-CP absolute scores | 0.914 | 0.908 | 100 | 2.91 | 3.88 |
| tablets | DS | TD-CP signed (pre-registered) | 0.905 | 0.887 | 100 | 2.92 | 3.87 |
| tablets | DS | TD-CP w/o cross-fitting | 0.720 | 0.492 | 33 | 2.38 | 4.28 |
| tablets | DS | TD-sum (union bound) | 0.978 | 0.971 | 100 | 4.62 | 4.92 |
| tablets | DS | Gaussian TD (parametric) | 0.918 | 0.911 | 100 | 2.96 | 3.88 |
| tablets | DS | Naive CP (primary residuals) | 0.720 | 0.492 | 33 | 2.37 | 4.28 |
| tablets | PDS | TD-CP+ (jackknife+) | 0.940 | 0.916 | 100 | 4.10 | 4.98 |
| tablets | PDS | TD-CP absolute scores | 0.920 | 0.912 | 100 | 3.86 | 4.89 |
| tablets | PDS | TD-CP signed (pre-registered) | 0.900 | 0.892 | 100 | 3.75 | 4.86 |
| tablets | PDS | TD-CP w/o cross-fitting | 0.725 | 0.627 | 0 | 2.75 | 5.00 |
| tablets | PDS | TD-sum (union bound) | 0.978 | 0.976 | 100 | 5.78 | 6.11 |
| tablets | PDS | Gaussian TD (parametric) | 0.920 | 0.912 | 100 | 3.78 | 4.79 |
| tablets | PDS | Naive CP (primary residuals) | 0.635 | 0.487 | 0 | 2.37 | 5.44 |

![**Fig. 4.** Ablation: coverage gap (left](figures/fig4_ablation.png)

**Fig. 4.** Ablation: coverage gap (left) and interval score (right) per scenario, PDS and DS pooled.


### 4.5. Number of transfer standards

With *k* = 5 and 8 labelled standards, target CP cannot produce finite 90% intervals (Fig. 5), because ⌈0.9(*k* + 1)⌉ > *k*. TD-CP+ remained finite for every *k* because it borrows the *n* primary residuals. It was valid in all scenarios from *k* = 8 onwards for both transfer methods, and at *k* = 5 in 100% (PDS) and 47% (DS) of scenarios (coverage 0.950 and 0.875). Its interval score decreased with *k* (PDS: 13.81 at *k* = 5 to 4.23 at *k* = 30), reflecting the improved transfer itself. For DS with *k* = 5, the instability of a 5-spectrum pseudo-inverse is the limiting factor; we recommend *k* ≥ 8 standards.

![**Fig. 5.** Mean coverage (top) and inte](figures/fig5_k_sensitivity.png)

**Fig. 5.** Mean coverage (top) and interval score (bottom) versus the number of transfer standards k; error bars: 95% CI over scenarios. Target CP and Target CP+ are infinite (not shown) for k < 9.


### 4.6. Robustness and generalisation

Table 6 and Fig. 6 summarise the confirmatory experiments, none of which had been inspected when TD-CP+ was introduced. With Kennard–Stone selection of the standards, which violates the exchangeability between standards and test samples, TD-CP+ covered 0.962 (PDS) and 0.950 (DS). With SNV + first-derivative preprocessing it covered 0.936 and 0.925; with a ridge-regression calibration 0.945 (PDS). Added secondary-instrument noise (2% of the channel SD) gave 0.953, versus 0.339 for naive CP. Without any standardisation, the transfer discrepancy dominates the error, and TD-CP+ still covered 0.921 (naive CP: 0.283). Here, however, the symmetric TD-CP+ interval was much less efficient (IS/SD 5.61) than the signed TD-CP (2.35, coverage 0.917) or the Gaussian combination (2.28), because an uncorrected instrument difference produces a large systematic bias that only the signed constructions can shift the interval to absorb. When the discrepancies are strongly one-sided, the signed TD-CP is preferable. On the official IDRC partition of the tablets it covered 0.924 (PDS) and 0.916 (DS). For virtual secondary instruments of increasing severity, naive coverage fell from 0.895 to 0.741 (PDS), while TD-CP+ covered 0.918–0.924.

**Table 6.** Robustness and generalisation experiments at α = 0.10 (n = number of scenarios; other columns as in Table 2).

| Experiment | Condition | Transfer | Method | n | Mean cov. | Valid (%) | IS/SD |
|---|---|---|---|---|---|---|---|
| kennard_stone | KS selection | ds | Gaussian TD (parametric) | 30 | 0.915 | 90 | 4.38 |
| kennard_stone | KS selection | ds | Naive CP (primary residuals) | 30 | 0.573 | 3 | 5.52 |
| kennard_stone | KS selection | ds | Target CP+ (k labelled) | 30 | 0.958 | 100 | 5.07 |
| kennard_stone | KS selection | ds | TD-CP+ (jackknife+) | 30 | 0.950 | 100 | 4.54 |
| kennard_stone | KS selection | pds | Gaussian TD (parametric) | 30 | 0.941 | 100 | 6.52 |
| kennard_stone | KS selection | pds | Naive CP (primary residuals) | 30 | 0.482 | 0 | 11.08 |
| kennard_stone | KS selection | pds | Target CP+ (k labelled) | 30 | 0.972 | 100 | 8.42 |
| kennard_stone | KS selection | pds | TD-CP+ (jackknife+) | 30 | 0.962 | 100 | 7.58 |
| no_standardisation | no transfer | none | Gaussian TD (parametric) | 30 | 0.903 | 80 | 2.28 |
| no_standardisation | no transfer | none | Naive CP (primary residuals) | 30 | 0.283 | 0 | 26.11 |
| no_standardisation | no transfer | none | Target CP+ (k labelled) | 30 | 0.912 | 100 | 5.69 |
| no_standardisation | no transfer | none | TD-CP+ (jackknife+) | 30 | 0.921 | 100 | 5.61 |
| noise | noise=0.005 | pds | Gaussian TD (parametric) | 30 | 0.899 | 73 | 9.43 |
| noise | noise=0.005 | pds | Naive CP (primary residuals) | 30 | 0.406 | 0 | 22.16 |
| noise | noise=0.005 | pds | Target CP+ (k labelled) | 30 | 0.948 | 100 | 9.93 |
| noise | noise=0.005 | pds | TD-CP+ (jackknife+) | 30 | 0.945 | 100 | 9.52 |
| noise | noise=0.01 | pds | Gaussian TD (parametric) | 30 | 0.899 | 80 | 10.18 |
| noise | noise=0.01 | pds | Naive CP (primary residuals) | 30 | 0.365 | 0 | 26.64 |
| noise | noise=0.01 | pds | Target CP+ (k labelled) | 30 | 0.952 | 100 | 10.50 |
| noise | noise=0.01 | pds | TD-CP+ (jackknife+) | 30 | 0.948 | 100 | 9.85 |
| noise | noise=0.02 | pds | Gaussian TD (parametric) | 30 | 0.907 | 93 | 10.31 |
| noise | noise=0.02 | pds | Naive CP (primary residuals) | 30 | 0.339 | 0 | 28.52 |
| noise | noise=0.02 | pds | Target CP+ (k labelled) | 30 | 0.957 | 100 | 10.97 |
| noise | noise=0.02 | pds | TD-CP+ (jackknife+) | 30 | 0.953 | 100 | 10.14 |
| official_split | IDRC official split | ds | Gaussian TD (parametric) | 6 | 0.918 | 67 | 3.69 |
| official_split | IDRC official split | ds | Naive CP (primary residuals) | 6 | 0.780 | 33 | 3.86 |
| official_split | IDRC official split | ds | Target CP+ (k labelled) | 6 | 0.924 | 100 | 4.86 |
| official_split | IDRC official split | ds | TD-CP+ (jackknife+) | 6 | 0.915 | 100 | 3.56 |
| official_split | IDRC official split | pds | Gaussian TD (parametric) | 6 | 0.918 | 67 | 3.69 |
| official_split | IDRC official split | pds | Naive CP (primary residuals) | 6 | 0.826 | 33 | 3.53 |
| official_split | IDRC official split | pds | Target CP+ (k labelled) | 6 | 0.929 | 100 | 5.13 |
| official_split | IDRC official split | pds | TD-CP+ (jackknife+) | 6 | 0.924 | 83 | 3.58 |
| preprocessing | snv_sg1 | ds | Gaussian TD (parametric) | 30 | 0.894 | 77 | 3.70 |
| preprocessing | snv_sg1 | ds | Naive CP (primary residuals) | 30 | 0.684 | 0 | 4.21 |
| preprocessing | snv_sg1 | ds | Target CP+ (k labelled) | 30 | 0.923 | 100 | 3.85 |
| preprocessing | snv_sg1 | ds | TD-CP+ (jackknife+) | 30 | 0.925 | 97 | 3.67 |
| preprocessing | snv_sg1 | pds | Gaussian TD (parametric) | 30 | 0.918 | 90 | 2.76 |
| preprocessing | snv_sg1 | pds | Naive CP (primary residuals) | 30 | 0.762 | 13 | 2.97 |
| preprocessing | snv_sg1 | pds | Target CP+ (k labelled) | 30 | 0.932 | 100 | 3.08 |
| preprocessing | snv_sg1 | pds | TD-CP+ (jackknife+) | 30 | 0.936 | 100 | 2.84 |
| ridge_model | ridge | pds | Gaussian TD (parametric) | 30 | 0.905 | 97 | 8.61 |
| ridge_model | ridge | pds | Naive CP (primary residuals) | 30 | 0.438 | 0 | 21.26 |
| ridge_model | ridge | pds | Target CP+ (k labelled) | 30 | 0.946 | 100 | 9.20 |
| ridge_model | ridge | pds | TD-CP+ (jackknife+) | 30 | 0.945 | 100 | 9.16 |
| simulated | severity=1 | ds | Gaussian TD (parametric) | 7 | 0.897 | 86 | 4.02 |
| simulated | severity=1 | ds | Naive CP (primary residuals) | 7 | 0.564 | 14 | 5.05 |
| simulated | severity=1 | ds | Target CP+ (k labelled) | 7 | 0.922 | 100 | 4.62 |
| simulated | severity=1 | ds | TD-CP+ (jackknife+) | 7 | 0.916 | 100 | 4.39 |
| simulated | severity=1 | pds | Gaussian TD (parametric) | 7 | 0.911 | 100 | 1.35 |
| simulated | severity=1 | pds | Naive CP (primary residuals) | 7 | 0.895 | 100 | 1.35 |
| simulated | severity=1 | pds | Target CP+ (k labelled) | 7 | 0.918 | 100 | 1.44 |
| simulated | severity=1 | pds | TD-CP+ (jackknife+) | 7 | 0.918 | 100 | 1.36 |
| simulated | severity=2 | ds | Gaussian TD (parametric) | 7 | 0.896 | 86 | 3.94 |
| simulated | severity=2 | ds | Naive CP (primary residuals) | 7 | 0.564 | 14 | 5.35 |
| simulated | severity=2 | ds | Target CP+ (k labelled) | 7 | 0.919 | 100 | 4.69 |
| simulated | severity=2 | ds | TD-CP+ (jackknife+) | 7 | 0.915 | 100 | 4.33 |
| simulated | severity=2 | pds | Gaussian TD (parametric) | 7 | 0.914 | 100 | 1.58 |
| simulated | severity=2 | pds | Naive CP (primary residuals) | 7 | 0.856 | 43 | 1.63 |
| simulated | severity=2 | pds | Target CP+ (k labelled) | 7 | 0.924 | 100 | 1.71 |
| simulated | severity=2 | pds | TD-CP+ (jackknife+) | 7 | 0.921 | 100 | 1.59 |
| simulated | severity=3 | ds | Gaussian TD (parametric) | 7 | 0.900 | 86 | 3.98 |
| simulated | severity=3 | ds | Naive CP (primary residuals) | 7 | 0.546 | 14 | 5.88 |
| simulated | severity=3 | ds | Target CP+ (k labelled) | 7 | 0.923 | 100 | 4.69 |
| simulated | severity=3 | ds | TD-CP+ (jackknife+) | 7 | 0.915 | 100 | 4.37 |
| simulated | severity=3 | pds | Gaussian TD (parametric) | 7 | 0.915 | 100 | 2.33 |
| simulated | severity=3 | pds | Naive CP (primary residuals) | 7 | 0.741 | 29 | 2.88 |
| simulated | severity=3 | pds | Target CP+ (k labelled) | 7 | 0.927 | 100 | 2.59 |
| simulated | severity=3 | pds | TD-CP+ (jackknife+) | 7 | 0.924 | 100 | 2.39 |

![**Fig. 6.** Mean coverage under simulate](figures/fig6_robustness.png)

**Fig. 6.** Mean coverage under simulated instrument shifts (left), added secondary-instrument noise (centre, PDS) and other protocol changes (right, PDS). Dashed line: nominal 0.90.


### 4.7. Other nominal levels

At α = 0.05, target CP with ten standards is necessarily unbounded, whereas TD-CP+ covered 0.963 (PDS) and 0.956 (DS), valid in 100% and 93% of scenarios. At α = 0.20 it covered 0.849 and 0.845 (Fig. 7, Table S2). The conservativeness of TD-CP+ is therefore modest and roughly constant (≈ 0.03–0.05) across levels.

![**Fig. 7.** Mean empirical versus nomina](figures/fig7_alpha_calibration.png)

**Fig. 7.** Mean empirical versus nominal coverage (PDS and DS pooled); diagonal = perfect calibration.


### 4.8. Error analysis

Coverage is marginal, not conditional. Fig. 8 shows that all methods covered samples with extreme reference values or high leverage less often than central samples; TD-CP+ attenuates but does not remove this pattern. The cross-fitted discrepancy spread closely tracked the true held-out discrepancy spread (median ratio 1.11, range 0.97–1.33), which explains why the reference-free estimate is sufficient. Assumption (A2) is only approximately met: the held-out Spearman correlation between primary residual and discrepancy averaged -0.10 (scenario range -0.40 to 0.03). Correlated residuals and discrepancies would widen the true error distribution beyond the convolution and are a plausible contributor to the residual under-coverage of the signed TD-CP; the jackknife+ margin absorbs it in these data. Fig. 9 illustrates a single split.

![**Fig. 8.** Error analysis at α = 0.10: ](figures/fig8_error_analysis.png)

**Fig. 8.** Error analysis at α = 0.10: coverage by tertile of the reference value (left) and of leverage (centre); cross-fitted versus held-out discrepancy SD, scaled by RMSECV (right).

![**Fig. 9.** Example (corn moisture, m5 →](figures/fig9_example_intervals.png)

**Fig. 9.** Example (corn moisture, m5 → mp6, PDS, k = 10, split seed 0): naive intervals (left) versus TD-CP+ (right) for the 25 secondary-instrument test samples.


### 4.9. Computational cost

TD-CP+ needs *k* additional transfer fits for cross-fitting, which took on average 24 ms (corn, PDS) and 92 ms (tablets, DS) per split on one CPU core, against 41–358 ms for fitting and cross-validating the PLS model (Table 7, Fig. 10). The cost is negligible in practice.

**Table 7.** Mean wall-clock time per split (single core).

| Dataset | Transfer | PLS + CV (s) | Transfer (s) | Cross-fitting (s) | Interval (s) |
|---|---|---|---|---|---|
| corn | ds | 0.041 | 0.0062 | 0.0447 | 0.00060 |
| corn | pds | 0.041 | 0.0026 | 0.0243 | 0.00061 |
| tablets | ds | 0.366 | 0.0116 | 0.0924 | 0.00161 |
| tablets | pds | 0.358 | 0.0096 | 0.0636 | 0.00157 |

![**Fig. 10.** Computation time per split ](figures/fig10_compute.png)

**Fig. 10.** Computation time per split by stage.


### 4.10. Practical recommendations and limitations

For a transferred calibration we recommend: (i) never reuse primary-instrument intervals; (ii) measure at least eight transfer standards and keep their primary spectra; (iii) compute cross-fitted discrepancies and report TD-CP+ intervals, which need no reference analyses on the secondary instrument; (iv) where reference values for the standards are available, use them to verify coverage rather than to build the interval. Limitations: the evidence comes from two benchmark datasets (five instruments, seven properties) and from simulated instruments; coverage is marginal over samples and conditionally lower at the extremes; the guarantee of Eq. (5) depends on assumptions (A1)–(A3), of which (A2) holds only approximately; TD-CP+ was introduced after the pre-registered main analysis, although its confirmatory evaluation used experiments that were not inspected beforehand; and process or temporal drift on a single instrument was not studied because no suitable public paired data with continuous reference values were found.


## 5. Conclusions

Prediction intervals calibrated on a primary spectrometer substantially under-cover after calibration transfer, even when PDS or DS give acceptable point predictions. Splitting the error of a transferred prediction into a calibration residual and a transfer discrepancy, and estimating the latter without reference values from cross-fitted maps on the transfer standards, yields intervals with near-nominal (slightly conservative) coverage across 30 public benchmark scenarios, two transfer methods, several nominal levels and a range of robustness conditions. The jackknife+ form, TD-CP+, was required for reliable validity with the unstable DS map. The approach adds negligible computation, is independent of the regression model, and turns transfer standards that laboratories already measure into a source of validated uncertainty. Future work should evaluate it on process and long-term drift data and on conditional (sample-adaptive) coverage.


## CRediT authorship contribution statement

[Placeholder — to be completed by the authors, e.g., Conceptualization; Methodology; Software; Formal analysis; Writing – original draft; Writing – review & editing.]


## Declaration of competing interest

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.


## Declaration of generative AI and AI-assisted technologies in the manuscript preparation process

During the preparation of this work the authors used an AI system (Claude, Anthropic) to search the literature, write and run the analysis code, and draft the manuscript. After using this tool, the authors reviewed and edited the content as needed and take full responsibility for the content of the published article.


## Data availability

Both datasets are publicly available from Eigenvector Research (corn; NIR shootout 2002). The code, configuration, pre-registered protocol, raw per-split results (684,900 rows), statistical outputs, and scripts that regenerate every table, figure and number of this article are provided in the accompanying repository [link to be inserted upon acceptance].


## Funding

[Placeholder — funding sources or ‘This research did not receive any specific grant from funding agencies in the public, commercial, or not-for-profit sectors.’]


## Appendix A. Supplementary data

Supplementary material: S1 topic selection and pre-registered protocol; S2 iteration log; S3 literature matrix; S4 proof of Eq. (5); Table S1 per-scenario results; Table S2 coverage at all nominal levels; full statistical test output.


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
