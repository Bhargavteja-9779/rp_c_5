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
- `td_cp_plus` (TD-CP+): jackknife+-style. Lower bound = ⌊α(n+1)k⌋-th smallest of {f(T_{−j}(x^S)) − |r_i + δ_j|}. Upper bound = ⌈(1−α)(n+1)k⌉-th smallest of {f(T_{−j}(x^S)) + |r_i + δ_j|}. It needs no reference values.
- `target_cp_plus`: the same jackknife+ construction for the labelled Target-CP, so that the labelled reference also benefits (fairness).
- The absolute-score construction (A2) and TD-CP+ are now reported alongside the pre-registered signed TD-CP. Which one to *recommend* is decided only after the confirmatory experiments below.

**Confirmation design (decided before running).** All robustness and generalisation experiments are run with the new methods included: k-sensitivity, Kennard–Stone, preprocessing, ridge, noise, no-standardisation, the official IDRC split, and simulated instruments. None of these experiments was inspected before this change. The recommendation is made only if TD-CP+ or A2 (i) meets the validity criterion in the main experiment for both transfer methods, and (ii) does not lose validity relative to the signed TD-CP in the confirmatory experiments.
