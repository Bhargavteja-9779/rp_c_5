# Review round 9 — Associate Editor, Analytica Chimica Acta

**Question:** Would this manuscript survive peer review at ACA?

**Assessment after rounds 1–8.**
- **Scope.** Fits: chemometric data treatment with a quantifiable analytical benefit (validated uncertainty for transferred calibrations). Recent ACA calibration-transfer papers (2024–2026) are cited, so the paper is positioned within the journal's own literature.
- **Novelty.** Moderate. It is not a new conformal principle (the authors say so in Section 4.10). The new elements are the reference-free, cross-fitted discrepancy idea specific to standardisation-based transfer, and the first systematic benchmark of interval validity after transfer. This is the main reviewer risk: a reviewer may call it "incremental application of conformal prediction". The honest framing mitigates it.
- **Technical quality.** High. Repeated splits, scenario-level tests, effect sizes, dependence caveats, split-level coverage, many robustness experiments, and machine-checked claims.
- **Evidence and completeness.** Adequate, with two benchmark datasets. A third real dataset is lacking, and the authors explain why.
- **Reproducibility.** Excellent: one command, fixed seeds, SHA-256-verified data, a time-stamped protocol.
- **Clarity.** Good after round 7.

| # | Severity | Remaining concern | Action | Status |
|---|---|---|---|---|
| 1 | MAJOR | Length: 10 figures and 7 tables in the main text is heavy for ACA. | Move secondary material to the Supplement. | **Fixed.** The nominal-level figure, the compute figure and the timing table moved to the Supplement (Figs. S2–S3, Table S8). The main text now has 8 figures and 6 tables. |
| 2 | MAJOR | The recommended TD-CP+ has no formal guarantee, while Proposition 1 covers only Eq. (4). Readers could assume the guarantee transfers. | State this explicitly. | **Fixed** (Section 2.4 and the S4 remark). |
| 3 | MAJOR | The most common practical alternative is missing: the SEP-based t-interval from labelled validation samples on the secondary instrument. | Add the baseline. | **Fixed** in round 8 (M7 "Target t-interval"; main and k-sensitivity experiments re-run). |
| 4 | MODERATE | Author, affiliation, funding and CRediT fields are placeholders. | The authors must complete them before submission. | Open: an author action, which cannot be done here. |
| 5 | MODERATE | The JIF/quartile of ACA and the APC were not verified in Clarivate/Elsevier. | Author action. | Open (documented in `journal_selection/journal_verification.md`). |
| 6 | MINOR | A data-repository link (DOI) is needed at acceptance. | Deposit the repository, e.g. on Zenodo. | Open: author action. |
| 7 | MINOR | The AI-use declaration must reflect the extensive use of AI accurately. | Present. | Done. The cover letter also discloses it. |

**AE recommendation:** send out for review. Likely outcome: minor or major revision. The main risk is a novelty judgement by a chemometrics reviewer.
