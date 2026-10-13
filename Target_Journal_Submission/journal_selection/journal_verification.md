# Journal verification log

## 1. Legitimacy
- Analytica Chimica Acta was founded in 1947 and is published by Elsevier. It is listed in PubMed/MEDLINE under the abbreviation "Anal Chim Acta" and has 1,525 PubMed records with publication dates between Jul 2025 and Sep 2026.
- Its DOI prefix is 10.1016/j.aca.*, and the DOIs resolve through Crossref.
- It does not appear on any hijacked-journal or predatory list that I know of.

## 2. Acceptance timeline (my own measurement)
- Method: PubMed E-utilities. Query: `"Anal Chim Acta"[jour] AND ("2025/07/01"[dp] : "2026/09/30"[dp]) AND journal article[pt] NOT review[pt]`, retmax 400, sorted by publication date. For each article I took `accepted − received` (in days) from `<PubMedPubDate PubStatus=...>`.
- Result: n = 400. Median 58 days, Q1 44, Q3 77, mean 64.1 days. 69.8% of articles took ≤72 days.
- Script: `evidence/pm_speed.py`. Raw output: `evidence/pubmed_received_to_accepted.jsonl`.
- Limitation: this sample contains accepted papers only. A manuscript that needs a major revision will probably take longer than the median.

## 3. Impact factor and quartile
- Aggregator-reported 2025 JIF ≈ 6.0 (journalmetrics.org) or 6.100 (researcher.life). Both describe the journal as Q1 in Chemistry, Analytical, rank 13/80.
- **Not verified directly in Clarivate JCR** (subscription required). An action item for the corresponding author is to confirm these figures in JCR.

## 4. Fit: calibration-transfer papers recently published in ACA
I retrieved these with a PubMed query (title/abstract contains "calibration transfer", ACA or Talanta, 2024–2026):
- UCT-LMIR: a standard-free unsupervised calibration transfer method without model recalibration. ACA 2026. doi:10.1016/j.aca.2026.346104
- Cross-instrument coal quality spectral analysis via a PDS-assisted fine-tuning calibration transfer method. ACA 2026. doi:10.1016/j.aca.2026.345485
- Transfer of multivariate calibrations for potentiometric multisensor systems to account for non-calibrated interferences. ACA 2026. doi:10.1016/j.aca.2026.345387
- PLSELM: a lightweight modeling approach for low-data calibration in NIR spectroscopy. ACA 2025. doi:10.1016/j.aca.2025.344728
- Research on calibration transfer methods in coal quality spectral analysis across instruments and coal types. ACA 2025. doi:10.1016/j.aca.2025.344459
- A systematic calibration transfer and quantification method based on principal components extreme learning machine for NIR. ACA 2025. doi:10.1016/j.aca.2025.344151
- Calibration transfer via filter learning. ACA 2024. doi:10.1016/j.aca.2024.342404

None of these abstracts mentions prediction intervals, coverage, or conformal prediction (I checked automatically with a keyword scan of the abstracts).

## 5. Format requirements checked
- Abstract structure: PubMed AbstractText labels for 198 ACA records from 2026: BACKGROUND/RESULTS/SIGNIFICANCE in 80, the same with "SIGNIFICANCE AND NOVELTY" in 18, unlabelled in 93. **I therefore use a structured Background / Results / Significance abstract, ≤250 words.**
- Keywords: the modal count is 5. I use 6 or fewer.
- Highlights: 3–5 bullets of ≤85 characters each (from the guide-for-authors snippet).

## 6. Items that could not be verified (must be re-checked by the authors)
- The current JIF and quartile in Clarivate JCR.
- The exact APC for gold open access.
- The current article-length limit and graphical-abstract specification (ScienceDirect returned HTTP 403 to automated access).
