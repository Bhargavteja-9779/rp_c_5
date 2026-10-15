# Review round 4 — Reviewer #4 (ML methodology, training protocol, implementation; code inspected)

**Overall:** Minor revision. I read `src/tdcp/` against Sections 2–3. Equations (2)–(7), the PDS/DS definitions, the (n+1) corrections, the jackknife+ indices, the leverage interval and the Gaussian combination all match the code. Unit tests cover the key identities. I found one baseline-fairness problem and several documentation gaps.

| # | Severity | Issue | Fix | Status |
|---|---|---|---|---|
| 1 | MAJOR | Weighted CP (M3) estimated likelihood ratios from **in-sample** logistic-regression probabilities on the same points it reweights. This overstates separability and the degeneracy of the weights, which weakens a baseline (violates rule 4). | Use cross-fitted probabilities. | **Fixed (re-run).** 5-fold cross-fitted probabilities (`methods.weighted_cp`). All experiments were re-run (`results/pre_review4/` keeps the previous raw files). Effect: at α = 0.10 the share of unbounded weighted-CP intervals fell from 30%/26% (PDS/DS) to 18%/11%, and its mean coverage fell from 0.713/0.739 to 0.612/0.634. All 216,000 rows of the other methods are bit-identical. The conclusion (weighted CP fails after transfer) is unchanged. |
| 2 | MODERATE | Out-of-fold residuals are computed at the complexity selected on the same folds, so they are slightly optimistic. | Disclose and quantify. | **Fixed.** Disclosed in Section 3.2. Quantified by the in-domain check: mean coverage 0.900 at nominal 0.90. |
| 3 | MODERATE | Kennard–Stone selection: on which spectra? Noise experiment: are the standards also noisy? | Specify. | **Fixed.** Section 3.5 now says "on their primary spectra" and "all secondary spectra, standards included". This matches `runner.py`. |
| 4 | MODERATE | The leverage interval (M2) is undefined for the ridge model, and that is not mentioned. | Mention. | Table 6 reports only TD-CP+, naive CP, Gaussian TD and target CP+ for robustness, so M2 does not appear for ridge. No claim depends on it. Noted here. |
| 5 | MINOR | The README said "unit tests (15)"; there are 17. | Update. | **Fixed.** |
| 6 | MINOR | The jackknife+ lower index differs from Barber et al.'s ⌊α(n+1)⌋ when there are nk values. | Document. | Documented in S2 (mirrored order statistic) and the docstring. Unit-tested. |
| 7 | MINOR | PDS edge handling (shifted windows) differs from some implementations (truncated windows). | Mention. | Already stated in Section 3.2. |
| 8 | MINOR | The PLS implementation is custom (NIPALS). | Validate it against a reference implementation. | Validated against scikit-learn `PLSRegression` to 1e-6 (`tests/test_core.py::test_pls1_matches_sklearn`). |

No contradictions between code and manuscript were found besides items 1 and 3.
