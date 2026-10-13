# Journal comparison (Phase 0)

Evidence collected 13 Oct 2026. Here, **timeline** means the time from submission to acceptance for papers that were accepted. I measured it myself from the article-history dates (received / accepted) in PubMed records (`evidence/pm_speed.py`) or in Crossref assertions (`evidence/cr_speed.py`). The sample is up to 400 recent research articles per journal, published between 1 Jul 2025 and 30 Sep 2026. Raw outputs are in `evidence/*.jsonl`.

Important caveats:
* These times cover **accepted papers only**. Desk rejections are not included.
* The times include the authors' revision time.
* A median is not a promise for any one manuscript.
* "First decision" metrics are a different measure and are **not** used as acceptance time anywhere in this document.

The JIF and quartile values are **aggregator-reported** (journalmetrics.org, S-Logix, SciJournal, publisher pages as summarised by search engines). I could not check the Clarivate JCR database directly because it needs a subscription. The values marked "~" must be re-checked in JCR before submission.

| # | Journal (publisher) | JIF (agg.) | JCR quartile (agg.) | Median sub→accept (days) [IQR] | % accepted ≤72 d | Scope fit for chemometric UQ / calibration transfer | Decision |
|---|---|---|---|---|---|---|---|
| 1 | **Analytica Chimica Acta** (Elsevier) | ~6.0–6.1 | Q1 (Chemistry, Analytical) | **58** [44–77] (PubMed, n=400) | **69.8%** | Strong: chemometrics is explicitly in scope. 2025–26 calibration-transfer papers include UCT-LMIR (2026), PDS-assisted fine-tuning (2026), filter learning (2024) and PLSELM (2025) | **SELECTED** |
| 2 | Talanta (Elsevier) | ~6.1 | Q1 | 68 [50–95] (PubMed, n=399) | 57.4% | Good (publishes chemometrics) | Runner-up; slower |
| 3 | Journal of Chromatography A (Elsevier) | ~4 | Q1/Q2 | 65 [48–86] | 60.2% | Poor (separation science) | Rejected: scope |
| 4 | Analytical and Bioanalytical Chemistry (Springer) | ~3.8 | Q1/Q2 | 68–69 [50–98] (PubMed & Crossref agree) | 54–57% | Moderate | Rejected: lower JIF, weaker chemometrics profile |
| 5 | Virtual and Physical Prototyping (T&F) | ~10 | Q1 | 65 [50–89] (Crossref) | 60.5% | None (additive manufacturing) | Rejected: scope |
| 6 | J. King Saud Univ. – Comput. Inf. Sci. (Springer) | ~6 | Q1 | 73 [57–98] (Crossref) | 48.9% | Weak (general CS) | Rejected: median >72 d, scope |
| 7 | Results in Engineering (Elsevier) | 7.9–9.4 (sources disagree) | Q1 | 74–76 (publisher insights page, via search snippet) | n/a | Weak | Rejected: >72 d, broad scope |
| 8 | Spectrochimica Acta A (Elsevier) | ~4.8 | Q1 (Spectroscopy) | 77.5 [56–109] | 44.5% | Good | Rejected: >72 d median |
| 9 | J. Chem. Inf. Model. (ACS) | ~5–6 | Q1 | 79 [60–108] | 39.8% | Moderate (cheminformatics) | Rejected: >72 d |
| 10 | Biosensors & Bioelectronics (Elsevier) | ~10 | Q1 | 80 [57–109] | 42.2% | Poor | Rejected: scope, >72 d |
| 11 | Analytical Chemistry (ACS) | ~6–7 | Q1 | 95.5 [73–122] | 25.0% | Good | Rejected: >72 d |
| 12 | Journal of Chemometrics (Wiley) | ~2–3 | Q2/Q3 | 124 [66–190] (Crossref) | 31.8% | Excellent | Rejected: slow, lower JIF |
| 13 | Briefings in Bioinformatics (OUP) | ~6.7–9 | Q1 | 127 [93–171] | 10.8% | None | Rejected: slow, scope |
| 14 | Bioinformatics (OUP) | ~5.5–6 | Q1 | 136 [93–193] | 15.9% | None | Rejected |
| 15 | J. Comput. Design & Eng. (OUP) | ~6.1–6.8 | Q1 | Publisher states 14 weeks (≈98 d) to acceptance | n/a | Weak | Rejected: >72 d |
| 16 | IEEE J. Biomed. Health Inform. (IEEE) | 6.8 (2024, EMBS page) | Q1 | Not verifiable: the EMBS page gives ~29.8 (units not stated) as submission-to-*final decision*, which includes rejections, and <26 weeks to e-publication | n/a | Poor | Rejected: acceptance time unverifiable |
| 17 | Computers in Biology and Medicine (Elsevier) | ~7 | Q1 | 131 [80–204] | 19.0% | Poor | Rejected |
| 18 | Scientific Reports (Springer Nature) | ~3.9 | Q1/Q2 | 132 [92–194] | 12.7% | Generic | Rejected |
| 19 | Neural Networks / IEEE TNNLS / Med. Image Anal. | high | Q1 | 212–231 (TNNLS: no dates in PubMed) | ≤1% | Poor | Rejected |
| 20 | Alexandria Engineering Journal (Elsevier) | ~6 | Q1 | 118–130 (publisher insights page, via search snippet) | n/a | Weak | Rejected |

I also screened about 40 other journals: Oxford journals (GigaScience, NAR Genom. Bioinform., Database, JAMIA, Bioinform. Adv.), Springer AI journals, and Elsevier environmental and food journals. Every one had a median of more than 80 days. Full numbers are in `evidence/`.

## Why Analytica Chimica Acta
1. **Speed.** It has the fastest submission-to-acceptance median among the Q1 journals that genuinely fit the work: 58 days, with 70% of accepted papers accepted within 72 days. This meets the user's hard limit of 72 days as a *typical* outcome. It cannot be guaranteed for any single paper.
2. **Reputation.** The journal was established in 1947, is published by Elsevier, is indexed in JCR/SCIE, and is not on any predatory or hijacked list.
3. **Scientific fit.** The journal's aims explicitly include chemometrics and data-treatment methodology. It publishes calibration-transfer methods regularly (see `journal_verification.md`).
4. **Risk.** ACA screens strongly for novelty and *analytical relevance*, and routine applications get desk-rejected. The work must therefore be framed as a new data-treatment principle that gives a quantifiable analytical benefit: valid uncertainty statements for transferred calibrations.
