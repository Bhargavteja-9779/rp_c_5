# S1 — Topic discovery, stress test, gap analysis and pre-registered protocol

This file was written **before any interval-method result was computed**. It was committed as the first version and is frozen. Deviations made after results were inspected are listed in `S2_iteration_log.md`, each with its reason.

## 1. Constraints that shaped the choice of topic
- Target journal: Analytica Chimica Acta (see `journal_selection/`). The topic therefore has to be an analytical-chemistry / chemometrics data-treatment contribution with a measurable analytical benefit.
- Compute: 4 CPU cores and no GPU. The topic must not depend on large deep-learning training runs.
- Data: datasets must be public and redistributable (or downloadable by script), with paired multi-condition measurements.

## 2. Candidate directions considered (15) and why they were rejected or kept
| # | Direction | Main reason for rejection / selection |
|---|---|---|
| 1 | 1D-CNN vs PLS for NIR regression | Saturated literature. Results depend on the dataset. Incremental. |
| 2 | Standard-free calibration transfer (new algorithm) | Crowded field (UCT-LMIR 2026, filter learning 2024, etc.). Gains would be small and dataset-specific. |
| 3 | Plain conformal prediction for PLS | Already done: FoodChem 2025 (mid-IR), AnalChem 2026 (Raman SOC), Duma et al. arXiv 2025. Not novel. |
| 4 | Variable selection stability for NIR | Many existing methods. Low impact. |
| 5 | Spectral data augmentation | Incremental. Effects are hard to separate from regularisation. |
| 6 | TabPFN / foundation models for spectra | Compute- and licensing-sensitive, and the novelty is fast-moving and unverifiable. |
| 7 | Raman bacterial ID with OOD detection | GPU-heavy. Better suited to biomedical journals. |
| 8 | Local PLS model libraries | Recently covered in ACA (2026 "rethinking local modelling"). |
| 9 | Outlier / applicability-domain detection after transfer | Reasonable, but Q/T² diagnostics already exist. The benefit is hard to quantify. |
| 10 | Multivariate curve resolution uncertainty | Too far from available paired data. |
| 11 | Uncertainty for classical PLS (Faber-type) after transfer | Parametric. Relies on noise models that are hard to verify. Overlaps with 12. |
| 12 | **Distribution-free prediction intervals for calibrations transferred between instruments, using only unlabeled transfer standards** | **SELECTED.** The problem is real: transferred models are used without validated sample-wise uncertainty. Testable on public paired data. Model-agnostic. No chemometric prior art found. |
| 13 | Weighted (covariate-shift) conformal for spectra | Density-ratio weights become degenerate in high dimension. Used here as a baseline, not as the contribution. |
| 14 | Mini-spectrometer temperature robustness | The only public dataset has 3 concentration levels, which is too coarse. |
| 15 | Process (blending) condition transfer | In-line data with autocorrelated scans. Leakage risk. Few reference levels. |

## 3. Editor's stress test of direction 12
- *Too incremental?* Conformal prediction is known. The new element is how the target-domain uncertainty is constructed from (i) labeled primary-instrument residuals and (ii) **label-free** discrepancies of cross-fitted transfers on standards, which every calibration-transfer workflow already measures. Without this, naive intervals under-cover. The distinction has to be shown by experiment (RQ1–RQ3), not just asserted.
- *Simpler alternative?* A Gaussian combination of variances uses the same information. It is included as a required competitor (M4) and as an ablation.
- *Concurrent prior art?* Doula, "Conformal Calibration Transfer" (arXiv:2609.10737, ICML 2026) also transports labeled source calibration through unlabeled paired data. Differences: classification and images, transport of the calibration *set*, and KS / density-ratio correction. Our method combines residuals at the score level (signed convolution), cross-fits the transfer map, and is evaluated on spectroscopy. It will be cited, and the overlap will be stated openly.
- *Is the data enough?* Two classic public paired benchmarks: corn (80 samples × 3 instruments × 4 properties) and IDRC-2002 tablets (654 × 2 instruments × 3 properties). Simulated instrument perturbations will be added as a controlled stress test. Small n for corn is a known limitation, handled by repeated splits.
- *Leakage?* Every split is done at the physical-sample level. Transfer standards, master samples and test samples are disjoint. The primary-instrument spectra of test samples are **never** used by any method.
- *Statistical weakness?* The unit of analysis is the scenario (dataset × instrument pair × property × transfer method), with means over 100 repeated random splits. Paired Wilcoxon tests across scenarios, Holm correction, and effect sizes.

## 4. Gap statement
- WHAT EXISTS: calibration-transfer algorithms (DS, PDS and many successors) that are judged on RMSEP. Conformal and other UQ methods for spectroscopic regression that assume one instrument (exchangeable data). Weighted conformal for covariate shift. A general ML transport approach (TCC).
- WHAT IS MISSING: a validated, distribution-free way to attach sample-wise prediction intervals to a calibration *after* transfer, without new reference analyses on the secondary instrument.
- WHY IT MATTERS: ICH Q2(R2) / ASTM E1655-style method validation needs prediction uncertainty. When a transfer is imperfect, an interval taken from the primary instrument is over-confident. That leads to false accept/reject decisions.
- WHAT WE ADD: TD-CP (Transfer-Discrepancy Conformal Prediction) and a benchmark protocol for interval validity after transfer.
- HOW IT IS VERIFIED: empirical coverage and interval score on held-out secondary-instrument spectra, over 30 instrument-pair × property scenarios, 2 transfer methods, and 100 splits each.

## 5. Proposed method (fixed before experiments)
Notation: primary instrument P, secondary instrument S. f is the regression model fitted on primary spectra (PLS). T is the transfer map (PDS or DS) fitted on k transfer pairs (x_j^P, x_j^S). The prediction for a test spectrum is ŷ = f(T(x^S)).

Decomposition: y − ŷ = [y − f(x^P)] + [f(x^P) − f(T(x^S))] = r + δ.
- r (calibration residual): out-of-fold 10-fold CV residuals r_i on the labeled master set (n values).
- δ (transfer discrepancy, **needs no reference values**): δ_j = f(x_j^P) − f(T_{−j}(x_j^S)), where T_{−j} is refitted without pair j (leave-one-out cross-fitting) (k values).
- TD-CP interval: [ŷ + L, ŷ + U]. U is the smallest u such that (1/((n+1)k)) Σ_i Σ_j 1{r_i + δ_j ≤ u} ≥ 1 − α/2. L is defined symmetrically at α/2, using the lower tail.
- Components that will be ablated: C1 δ-augmentation; C2 cross-fitting; C3 signed/asymmetric scores (vs absolute); C4 non-parametric convolution (vs Gaussian combination).

## 6. Research questions → experiments
- RQ1 (problem): Do intervals calibrated on the primary instrument lose coverage after transfer? → E1 (naive CP coverage on secondary vs primary test spectra).
- RQ2 (validity): Does TD-CP reach nominal coverage without target reference values? → E1/E2.
- RQ3 (efficiency vs. competitors): Is TD-CP's interval score lower than that of label-free competitors, and how does it compare with methods that need k labeled target samples? → E2.
- RQ4 (components): Which components are needed? → E3 ablation.
- RQ5 (robustness/generalisation): sensitivity to k, standard selection (random vs Kennard–Stone), α, transfer method, preprocessing, regressor, added noise, simulated instrument perturbations, reverse direction, official IDRC split. → E4, E5, E7.
- RQ6 (cost): computational overhead. → E6.
- Error analysis: conditional coverage by y range and by leverage; scenarios where it fails. → E8.

## 7. Baselines (interval methods; all use the same point predictor ŷ)
- M1 Naive-CP: ±Q̂_{1−α}(|r|), with (n+1) correction.
- M2 Classical leverage interval: ±t_{1−α/2, n−A−1} · RMSECV · sqrt(1 + 1/n + h(T(x^S))).
- M3 Weighted-CP (Tibshirani et al. 2019): density ratio from logistic regression on PLS scores (master spectra vs transferred test spectra), with |r| scores. Label-free.
- M4 Gauss-TD (label-free, same information as TD-CP): ŷ + mean(δ) ± z_{1−α/2}·sqrt(s_r² + s_δ²).
- M5 Target-CP (**needs k reference values**): LOO residuals e_j = y_j − f(T_{−j}(x_j^S)), ±Q̂_{1−α}(|e|) with (k+1) correction. Infinite width when ⌈(k+1)(1−α)⌉ > k.
- M6 Pooled-CP (**needs k reference values**): |r| ∪ |e| with (n+k+1) correction.
- Ablations: A1 TD-CP without cross-fitting; A2 TD-CP with absolute scores |r_i + δ_j| (symmetric); A3 TD-sum: Q̂_{1−α/2}(|r|) + empirical Q_{1−α/2}(|δ|) (union-bound style).

## 8. Data and splits
- Corn (Eigenvector Research): 80 samples measured on m5, mp5 and mp6 (700 points, 1100–2498 nm). Properties: moisture, oil, protein, starch. All 6 directed pairs. Per split: k = 10 transfer, 25 test, 45 master.
- Tablets (IDRC 2002 shootout, Eigenvector): 654 tablets on 2 instruments (650 points, 600–1898 nm). Properties: weight, hardness, assay. Both directions. Primary protocol: random split per repetition with k = 10, test = 200, master = rest (444). Secondary: the official partition (calibrate+validate → master/transfer, test = official test).
- Excluded: the MicroNIR temperature dataset (Mendeley 10.17632/4p63x5r852.1), because it has only 3 nominal concentration levels (≈40/50/60%) across 9 formulations, which is inadequate for evaluating regression intervals.
- Rows with missing reference values are removed per property.
- Repetitions: R = 100 per scenario, seeds 0–99, fixed in advance. Quick mode: R = 5.

## 9. Fixed hyperparameters
- PLS: mean-centred, raw spectra. Number of LVs by 10-fold CV on the master set (minimum RMSECV, max 15 for corn and 20 for tablets).
- PDS: window 2w+1 with w = 2, local ridge regression with intercept, λ = 1e-6·trace(XᵀX). DS: pseudo-inverse with rcond = 1e-6 on centred spectra.
- α = 0.10 primary; 0.05 and 0.20 for sensitivity.

## 10. Metrics and statistics
- Per split: coverage (PICP), mean width (MPIW), interval (Winkler) score IS_α, and RMSEP.
- Per scenario: mean over splits. Coverage gap = mean coverage − (1 − α).
- Primary comparisons: TD-CP vs each label-free competitor (M1–M4) on |coverage gap| and on mean IS_α normalised by SD(y). Two-sided Wilcoxon signed-rank test over scenarios, Holm-adjusted. Effect size: matched-pairs rank-biserial correlation. Bootstrap 95% CI of the median paired difference (10,000 resamples, seed 12345).
- Pre-registered success criterion for TD-CP validity: scenario mean coverage ≥ 1 − α − 0.02 in ≥ 80% of scenarios, for both transfer methods.
