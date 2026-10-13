# Selected target journal

| Field | Value |
|---|---|
| TARGET JOURNAL | **Analytica Chimica Acta** (ACA) |
| PUBLISHER | Elsevier B.V. |
| ISSN | 0003-2670 (print); 1873-4324 (online) |
| JCR STATUS | Indexed in Clarivate JCR / SCIE. This is aggregator-reported: I could not open the JCR database myself (subscription needed). |
| JCR QUARTILE | Q1, Chemistry, Analytical (aggregator-reported, rank ≈13/80). **Re-verify in JCR before submission.** |
| JOURNAL IMPACT FACTOR | ≈6.0–6.1 (2025 JCR release, aggregator-reported: journalmetrics.org 6.0; another aggregator 6.100). Not verified directly in Clarivate. |
| JCR SUBJECT CATEGORY | Chemistry, Analytical |
| VERIFIED REVIEW/DECISION TIMELINE | Not verified. The publisher "insights" page could not be fetched (HTTP 403). |
| VERIFIED ACCEPTANCE TIMELINE | **Independently measured.** Median **58 days** from receipt to acceptance (IQR 44–77). 69.8% of accepted papers were accepted within 72 days. Basis: n = 400 research articles in PubMed (publication dates 2025-07-01 to 2026-09-30), using the article-history `received` and `accepted` dates. Script: `evidence/pm_speed.py`. This covers accepted papers only and includes revision time. It is not a guarantee. |
| APC | ACA is a hybrid journal. Subscription publication has no APC. The open-access APC was not verified (Elsevier pages returned 403). Check Elsevier's APC price list. |
| SCOPE FIT | The aims and scope cover "fundamental research on analytical chemistry theory and methodology, including chemometric techniques", and data treatment that shows new principles or important applications is "especially encouraged" (from the guide-for-authors text as returned by search). |
| RESEARCH FIT | ACA published at least 7 calibration-transfer method papers in 2024–2026 (PubMed query in `journal_verification.md`). **None** of them provides distribution-free prediction intervals for the transferred model, so this work extends a line of research that is active in this journal. |
| KEY AUTHOR GUIDELINES (verified where possible) | Recent ACA papers use a **structured abstract (Background / Results / Significance)**: 80 of 198 2026 PubMed records, plus 18 that use "Significance and novelty". The guide-for-authors snippet mentions an abstract of at most 250 words. Highlights: 3–5 bullets, each ≤85 characters including spaces, in a separate file. Most papers have 5–6 keywords (PubMed: 5 kw in 102/198). A graphical abstract is expected (the exact current requirement could not be fetched). References are numbered in the Elsevier style. Data/code availability and declaration-of-competing-interest statements are required. A CRediT author statement is expected. |
| KEY REJECTION RISKS | (1) Desk rejection as "insufficient analytical-chemistry novelty / purely statistical". (2) Reviewers asking for more than 2–3 datasets. (3) The view that conformal prediction is "known" (it is: see the FoodChem 2025 and AnalChem 2026 papers), so novelty must sit in the transfer-specific, label-free construction. (4) A concurrent ML paper (Transported Conformal Calibration, arXiv:2609.10737, ICML 2026) uses the paired-unlabeled idea in a general form. It must be cited and the two clearly differentiated. |
