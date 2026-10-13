# S3 — Literature matrix and novelty map

Every entry was checked against Crossref or arXiv by `code/scripts/verify_citations.py`; the results are in `citation_audit.csv`. Content descriptions come from the abstracts I retrieved, or from the original papers where I know them well. "n/r" means not reported in the source I consulted.

## A. Literature matrix

| Paper (year, venue) | Problem | Data | Method | Uncertainty after transfer? | Target labels needed? | Gap relative to this work |
|---|---|---|---|---|---|---|
| Wang, Veltkamp & Kowalski (1991, Anal. Chem.) | Instrument standardisation | Lab NIR | DS, PDS | No (RMSEP only) | Transfer spectra only | No interval statement |
| Bouveresse & Massart (1996, Chemolab) | Improving PDS | NIR | PDS variants | No | Transfer spectra | Same |
| Fearn (2001, JNIRS); Feudale et al. (2002, Chemolab); Workman (2018, Appl. Spectrosc.) | Reviews of calibration transfer | — | DS, PDS, SBC, OSC, FIR, … | Discuss prediction error, but no distribution-free intervals | — | Reviews only |
| Malli et al. (2017, Chemolab) | Standard-free transfer | Corn, tablets and others | Several standard-free methods | No | None | RMSEP only |
| Xie et al. (2024, ACA) | Transfer with very few references | 1 simulated + 2 real | Filter learning | No | 1 labelled sample (or unsupervised) | No intervals |
| Fan et al. (2025, ACA) | Low-data NIR calibration across instruments | 5 NIR sets, 10 spectrometers | PLS scores + ensemble ELM | No | — | No intervals |
| Gao et al. (2026, ACA) | XRF cross-instrument | 140 coal samples, 2 XRF | PDS + fine-tuning | No | Yes | No intervals |
| Huang et al. (2026, ACA) | Standard-free transfer, no recalibration | 3 spectroscopic datasets | Likelihood-maximisation inverse regression with optional covariance compensation | Models error covariance, but reports no coverage-validated intervals | No | Accuracy-oriented; no coverage evaluation |
| Haggam et al. (2026, Chemolab) | Review: transfer + UQ for portable optics | — | Reviews DS/PDS/CCA/DL with bootstrap, Bayesian and GUM budgets | Review-level discussion | — | Proposes no method; no coverage benchmark |
| Faber & Kowalski (1997, J. Chemom.); Faber et al. (2003, TrAC) | Sample-specific prediction error for PLS | — | Error propagation, leverage | Single instrument | — | Assumes the same measurement domain |
| Jovic et al. (2025, Food Chem.) | Conformal regression for mid-IR | 2 adulteration sets | Inductive CP with normalised scores | Single instrument | — | No transfer |
| Wiens et al. (2025/26, Anal. Chem.) | Calibrated UQ for Raman SOC | SERDS Raman | CP on ML models | Single instrument | — | No transfer |
| Duma et al. (2025, arXiv) | UQ for PLS/PCR | NIR, airborne hyperspectral | Conformal-inspired, input-dependent intervals | Single domain | — | No transfer |
| Tibshirani et al. (2019, NeurIPS/arXiv) | CP under covariate shift | Generic | Likelihood-ratio weighting | Covariate shift with overlapping support | No | Weights become degenerate for transferred spectra (tested here as M3) |
| Barber et al. (2021, Ann. Stat.) | Jackknife+ | Generic | LOO-based intervals | — | — | Inspires our cross-fitting |
| Doula (2026, arXiv; ICML 2026) | Conformal calibration transfer via unlabeled paired data | CIFAR-100-C, Tiny-ImageNet-C, SEN12MS | Transports the calibration set; KS / weighting correction | Yes (classification/sets) | No | Concurrent and conceptually related. It differs from this work in task (sets vs regression intervals), construction (transporting the calibration set vs score-level signed convolution of residual and cross-fitted discrepancy) and domain (vision vs spectroscopy). It is not evaluated on chemometric transfer methods. |

## B. Novelty map

- Existing work A (DS/PDS and successors) gives accurate *point* predictions after transfer, and is evaluated by RMSEP.
- Existing work B (CP in chemometrics) gives valid intervals *within one instrument*.
- Existing work C (weighted CP) handles covariate shift with overlapping support. In transferred high-dimensional spectra the weights degenerate.
- Existing work D (TCC, ML) is a general transport of calibration sets for set-valued prediction.
- **Proposed:** the target error splits exactly into a primary residual and a transfer discrepancy, y − f(T(x^S)) = r + δ. δ can be measured *without reference analyses* on the transfer standards that every PDS/DS workflow already acquires, provided the map is **cross-fitted**: in-sample DS reproduces the standards exactly, which gives δ ≡ 0. The two empirical distributions are combined by a signed convolution with an (n+1) correction. This gives a conditional finite-sample coverage statement (Proposition 1). The proposal comes with a benchmark protocol (30 directed instrument-pair × property scenarios, 2 transfer methods, 100 splits each) that evaluates interval validity after transfer.

## C. Gaps (typed)
- Methodological: no distribution-free interval construction for transferred calibrations that needs no target reference values.
- Experimental: calibration-transfer papers report only RMSEP or R². None reports coverage.
- Statistical-validation: there is no repeated-split, scenario-level testing of interval validity.
- Reproducibility: most transfer papers provide no code. This work releases all of it.
