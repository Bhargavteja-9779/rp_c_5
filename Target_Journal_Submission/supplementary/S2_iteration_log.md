# S2 — Iteration log: deviations from the pre-registered protocol

Every entry lists the observation, the hypothesis, the change, and how the change was checked. No test-set tuning was done. The main-experiment splits (seeds 0–99) are identical across versions, so every method that is unchanged gives identical numbers.

## Iteration 0: data facts that differ from the protocol text (no effect on design)
- The tablets file holds **655** tablets (155 + 40 + 460), not the 654 given on the provider's web page. All 655 are used.

## Iteration 1 (after the pre-registered main experiment; robustness experiments had not yet been inspected)

**Observation.** The pre-registered raw results are archived in `results/preregistered_v1/raw_main.csv`. At α = 0.10:
- Naive CP coverage after transfer: 0.483 (PDS) and 0.587 (DS). This confirms RQ1.
- Pre-registered TD-CP (signed convolution): mean coverage 0.895 (PDS) and 0.883 (DS). The pre-registered validity criterion (≥ 0.88 in ≥ 80% of scenarios) was **not met**: 76.7% (PDS) and 60.0% (DS).
- The shortfall is concentrated in **corn + DS**: 50% of those scenarios are valid. Even the *labelled* Target-CP, which uses leave-one-out target residuals, reaches only 75% there.
- The pre-registered ablation A2 (absolute scores) did better than the signed scores: 100% (PDS) and 66.7% (DS) valid, with a slightly *lower* median interval score.
- The parametric Gauss-TD combination is as efficient as either TD-CP variant.

**Hypotheses.**
- H-a: The signed two-tailed construction estimates each tail of the discrepancy distribution from k = 10 values at level α/2. That is noisier than pooling both tails (absolute scores).
- H-b: DS fitted on k = 10 spectra with p = 700 channels is an *unstable* algorithm. Leave-one-out (jackknife) residuals of unstable algorithms are known to fail to be exchangeable with the test residual of the full-data fit (Barber et al., 2021). The remedy is the jackknife+ construction, which centres the interval on the k leave-one-out predictions f(T_{−j}(x^S)) instead of on f(T(x^S)).

**Changes.** These are added methods. Nothing pre-registered was removed, and all pre-registered methods are still reported.
- `td_cp_plus` (TD-CP+): jackknife+-style. Lower bound = the mirrored order statistic, the (nk + 1 − ⌈(1−α)(n+1)k⌉)-th smallest of {f(T_{−j}(x^S)) − |r_i + δ_j|} (see the last bullet below). Upper bound = ⌈(1−α)(n+1)k⌉-th smallest of {f(T_{−j}(x^S)) + |r_i + δ_j|}. It needs no reference values.
- `target_cp_plus`: the same jackknife+ construction for the labelled Target-CP, so that the labelled reference also benefits (fairness).
- The absolute-score construction (A2) and TD-CP+ are now reported alongside the pre-registered signed TD-CP. Which one to *recommend* is decided only after the confirmatory experiments below.

**Confirmation design (decided before running).** All robustness and generalisation experiments are run with the new methods included: k-sensitivity, Kennard–Stone, preprocessing, ridge, noise, no-standardisation, the official IDRC split, and simulated instruments. None of these experiments was inspected before this change. The recommendation is made only if TD-CP+ or A2 (i) meets the validity criterion in the main experiment for both transfer methods, and (ii) does not lose validity relative to the signed TD-CP in the confirmatory experiments.

**Outcome of the confirmation (recorded after the full run, 13 Oct 2026).**
- Criterion (i): TD-CP+ was valid in 100% of main-experiment scenarios for both PDS and DS at α = 0.10. A2 (absolute scores) was valid in 100% for PDS and 66.7% for DS, so it does **not** meet (i).
- Criterion (ii): across the k-sensitivity, Kennard–Stone, SNV+SG1, ridge, noise, no-standardisation, official-split and simulated-instrument experiments, TD-CP+ never had a lower percentage of valid scenarios than the signed TD-CP (Table 6; `results/scenario_results.csv`).
- Therefore TD-CP+ is the **recommended** variant. The pre-registered signed TD-CP is still reported in full, as is the failure of its pre-registered criterion in the main experiment.
- Negative finding, reported in the manuscript: without any standardisation (transfer = identity), all leave-one-out maps are identical, so TD-CP+ reduces to the symmetric absolute-score interval. It then stays valid but is much less efficient than the signed TD-CP or the Gaussian combination, because the discrepancies carry a large systematic bias.
- Jackknife+ index detail: the first implementation used ⌊α(n+1)k⌋ for the lower order statistic, which is not the mirror of the upper index when the number of values is nk rather than (n+1)k − 1. A unit test caught this *before* any full run. The lower index is now the exact mirror (nk + 1 − upper index), which equals Barber et al.'s definition when k = 1.

## Iteration 2 (internal review round 1)
- Added the `parsimonious_pls` experiment (PLS complexity by the one-standard-error rule) to test whether the collapse of naive coverage comes from over-complex corn models. Result: naive coverage was still 0.576 (PDS) and 0.621 (DS), so it does not.
- Added the `pds_window` experiment (windows of 3, 7 and 11 channels).
- Both are new, non-pre-registered experiments. They are reported as such in Section 3.5.

## Iteration 3 (internal review rounds 4–5)
- Weighted CP (baseline M3) now uses 5-fold cross-fitted classifier probabilities instead of in-sample probabilities, to avoid weakening the baseline.
- Added the `biased_standards` experiment: transfer standards drawn only from samples with reference values below the median. This is an external-validity stress test of unrepresentative standards.
- All experiments were re-run with identical seeds. The previous raw files are archived in `results/pre_review4/`. All other methods are deterministic given the seed, so only M3 changes.
