# Review round 10 — Final adversarial review (goal: find one reason to reject)

## Search for a fatal flaw
**Candidate fatal flaw F1: "the label-free premise is vacuous."** In most calibration-transfer practice the standards are calibration samples, so their reference values are already known. Reference values belong to the sample, not to the instrument. If so, the labelled alternatives cost nothing extra, and a paper whose sole selling point is "no reference values needed" would collapse.
- *Verdict:* **not fatal, but it forced a reframing.** The evidence shows that TD-CP+ is also competitive when reference values exist:
  - its interval score is lower than target CP+ in 100% of scenarios;
  - versus the classical t-interval it is lower in 50% of PDS scenarios (a tie, median difference +0.012 SD) and in 87% of DS scenarios;
  - it is valid more often under DS, at α = 0.05 (where target CP is unbounded with k = 10), and at small k.
- *Fix applied:* the Introduction now names the label-free use cases (surrogate/check materials; changed or consumed calibration samples). The Abstract/Significance claims "as efficient as or more efficient than intervals built from them", backed by two new claim checks. The recommendations in Section 4.11 cover the known-reference-value case.

**Candidate fatal flaw F2: "the recommended method has no theory."** Proposition 1 covers Eq. (4), not TD-CP+. *Verdict:* not fatal for an analytical journal, because the empirical validation is extensive, but it had to be stated. **Fixed** in Section 2.4 and the S4 remark.

No other candidate fatal flaw survived scrutiny.

## Major weaknesses (remaining or fixed in this round)
1. Two real datasets only (effectively two independent sample sets). *Open; stated.*
2. Unrepresentative standards with DS → 60% valid. *Open; stated prominently.*
3. TD-CP+ is conservative (≈ 0.03–0.04 over nominal); the Gaussian combination tends to be more efficient when valid. *Open; stated with both unadjusted and Holm p-values.*
4. Post-hoc introduction of TD-CP+. *Mitigated:* confirmatory experiments, a time-stamped log, and the pre-specified method reported in full.
5. Scenario dependence makes the p-values optimistic. *Mitigated:* stratum consistency and split-level analyses.
6. Conditional coverage at the extremes of y and leverage is below nominal for all methods. *Open; stated (Fig. 7).*
7. No single-instrument drift data. *Open; stated.*
8. The protocol is not in a public registry. *Stated.*

## Moderate weaknesses
1. Corn n_test = 25, so split-level coverage is noisy. Quantified (Table S4).
2. PLS complexity is selected on the same folds that produce the residuals. Quantified by the in-domain check (0.900).
3. The robustness experiments were run before M7 was added, so the t-interval appears only in the main and k-sensitivity experiments. Stated in S2.
4. The weighted-CP classifier uses default regularisation (C = 1) without tuning. A tuned classifier is unlikely to fix degenerate supports, but this is not tested. Noted here.
5. Simulated instruments are produced by one perturbation model. The parameters are disclosed.
6. The scaling benchmark uses synthetic scores (by design) and wall-clock timings that vary slightly between runs.
7. The JIF, quartile and APC of the target journal are aggregator-reported. Author action.

## Minor weaknesses
- Placeholders (authors, CRediT, funding, repository DOI).
- One verified reference (Vovk 2012) is unused. It was dropped automatically from the reference list.
- Table 6 merges simulated and real conditions in one table. Acceptable: the condition column distinguishes them.

## Author response
All fixable items above have been fixed. The remaining items are disclosed in Section 4.11 and in `final_audit.md`.
