# Review round 1 — Reviewer #1 (general, hostile but fair; Analytica Chimica Acta)

**Overall:** Major revision. The problem is relevant and the evidence base is large. However, one alternative explanation for the central finding has not been ruled out, and several presentation issues reduce credibility.

| # | Severity | Issue | Required fix | Status |
|---|---|---|---|---|
| 1 | MAJOR | The corn PLS models often hit the 15-LV cap (median 10–11 LVs for 45 samples; 15 for moisture). Over-complex models are known to be fragile to instrument differences, so the collapse of naive coverage may be an artifact of over-fitting rather than a general phenomenon. | Repeat with a parsimonious complexity rule. | **Fixed (experiment).** Added the 1-SE-rule experiment (3,000 splits). Naive coverage was 0.576/0.621, still far below nominal; TD-CP+ covered 0.937/0.927 (Section 4.6). |
| 2 | MAJOR | The PDS window (5 channels) was fixed without justification. The results could depend on it. | Window sensitivity. | **Fixed (experiment).** Windows of 3, 7 and 11 channels (4,500 splits). TD-CP+ was valid in all scenarios for every window. |
| 3 | MODERATE | Table 2 has 40 rows mixing datasets and transfer methods, which is hard to read. | Pool over datasets in the main text and move the per-dataset rows to the Supplement. | **Fixed.** Table 2 is now pooled (30 scenarios per method); Table S2 is per dataset. |
| 4 | MODERATE | "The classifier separates transferred from primary spectra almost perfectly" is asserted without evidence (no AUC was computed). | Remove or support. | **Fixed.** The text now cites the measured fraction of unbounded intervals and is worded as a symptom. |
| 5 | MODERATE | The RMSEP ratio range up to 52.6 is unexplained and looks suspicious. | Explain. | **Fixed.** Corn moisture on m5 has a primary RMSEP of 0.011, so any transfer error dominates. This is now stated. |
| 6 | MODERATE | Table 3 printed 1000000 for weighted-CP medians (the internal rank stand-in for ∞). | Display ∞. | **Fixed** in the table generator. |
| 7 | MODERATE | The original draft wrongly stated that the TD-CP+ vs Gaussian IS difference was "not significant" (Holm p = 0.047, r = +0.39, Gaussian better). | Correct the text, and make claims machine-checked. | **Fixed.** The text now states that the Gaussian combination has a slightly lower IS. A claim assertion was added in `manuscript/claims.py`. |
| 8 | MINOR | Abstract phrase "100% and 100%" is clumsy; "oracle-like" is a misnomer for target CP+. | Rephrase. | **Fixed.** |
| 9 | MINOR | Fig. 1 used plain-text pseudo-notation with overflowing labels. | Redraw with proper math. | **Fixed.** |
| 10 | MINOR | Equation (4) used non-standard notation. | Define the order statistic. | **Fixed.** |
