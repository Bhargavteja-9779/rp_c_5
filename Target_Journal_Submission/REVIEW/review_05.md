# Review round 5 — Reviewer #5 (dataset validity, generalisation, domain shift, external validity, deployment)

**Overall:** Major revision. I tried to invalidate the central claim ("TD-CP+ gives valid intervals after transfer without reference values").

| # | Severity | Issue / attack | Fix | Status |
|---|---|---|---|---|
| 1 | MAJOR | **Representativeness of the standards.** In every main experiment the standards were drawn at random from the same population as the test samples. That is the most favourable case for an exchangeability-based method. In practice standards are often a few stable samples from part of the range. | Stress test with unrepresentative standards. | **Fixed (new experiment, 3,000 splits).** Standards were drawn only from samples below the median reference value. **The claim is weakened, and the manuscript says so:** with DS, TD-CP+ covered 0.876 and was valid in only 60% of scenarios. The labelled target CP+ did the same (0.880, 60%). With PDS, TD-CP+ stayed valid in 100%. Representative standards are now stated as a precondition (Sections 4.6 and 4.11). |
| 2 | MAJOR | Only two datasets, both established public benchmarks (corn, IDRC 2002). The external validity for modern portable or process instruments is unknown. | Add data, or bound the claims. | Partially addressed. Simulated secondary instruments (3 severities × 2 datasets) cover controlled shifts. The only other public paired dataset found (MicroNIR temperature series) has three concentration levels and was excluded before analysis, with the reason given. The claims are restricted to "two benchmark datasets (five instruments, seven properties)" in the Limitations. |
| 3 | MODERATE | Spectrally dissimilar transfer artefacts (e.g., the NBS glass standards shipped with the corn data) cannot be used to compute δ. | State as a limitation. | **Fixed** (Limitations). |
| 4 | MODERATE | Test samples outside the calibration range, i.e. extrapolation. | Error analysis by y-tertile and leverage. | Already in Fig. 8. Coverage is lower at the extremes for all methods, and this is stated. |
| 5 | MODERATE | The official IDRC partition differs from the random splits (the test set is fixed). Does TD-CP+ hold? | Report. | Reported: 0.924 (PDS) and 0.916 (DS) coverage; valid in 83% and 100% of scenarios (6 scenarios each). |
| 6 | MINOR | Long-term drift on one instrument is not studied. | Limitation. | Stated. |

**Net effect of this round:** one claim was narrowed (validity requires representative standards; DS + unrepresentative standards fails for TD-CP+ and the labelled reference alike). No claim was broadened.
