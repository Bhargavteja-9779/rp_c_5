# Target Journal Submission — Analytica Chimica Acta

**Manuscript:** *Distribution-free prediction intervals for multivariate calibrations transferred between spectrometers using unlabelled transfer standards*

| Folder | Content |
|---|---|
| `journal_selection/` | Journal choice (ACA), comparison of 20+ candidates, and verification. Acceptance times were measured from PubMed/Crossref; scripts are in `evidence/`. |
| `manuscript/` | `Final_Manuscript.docx/.pdf/.md`, `Supplementary_Material.docx`, `highlights.docx`, `cover_letter.docx`, plus the generators (`build_manuscript.py`, `values.py`, `claims.py` with 106 claim checks). |
| `code/` | Complete pipeline (`run_all.py --mode quick|full`), `src/tdcp`, tests, configuration, README. |
| `results/` | Raw per-split results (`raw_*.csv.gz`), scenario results, statistics, logs. Archives: `preregistered_v1/`, `pre_review4/`, `pre_review8/`. |
| `figures/`, `tables/` | Machine-generated figures (PNG/PDF) and tables (CSV/MD). |
| `supplementary/` | S1 topic selection and pre-specified protocol; S2 iteration log; S3 literature matrix; S4 theory; citation audit. |
| `REVIEW/` | Ten internal review rounds and `final_audit.md` (consistency, reproducibility, rejection risk, decision). |

Reproduce everything: `cd code && pip install -r requirements.txt && python run_all.py --mode full && python ../manuscript/build_manuscript.py`.

**Before submission, the authors must:** fill the author, affiliation, CRediT and funding placeholders; verify the JIF/APC and the current guide for authors; deposit the code and data DOI; and review all AI-generated content (see the AI declaration).
