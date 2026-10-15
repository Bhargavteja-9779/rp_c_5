# Review round 6 — Reviewer #6 (computational complexity, latency, memory, scalability, deployment)

**Overall:** Minor revision. The method is computationally light, but the manuscript gave only wall-clock times on two small datasets.

| # | Severity | Issue | Fix | Status |
|---|---|---|---|---|
| 1 | MODERATE | No complexity analysis. TD-CP+ forms nk candidate bounds per test sample. How does it scale with large master sets (n in the thousands) or many standards? | Complexity statement plus a scaling benchmark. | **Fixed.** Section 4.9 states O(nk) per test sample with a partial sort. A new benchmark (`code/scripts/benchmark_scaling.py`, `results/scaling.csv`, Fig. S1) gives 0.26 ms per test sample at n = 5000, k = 10 and 0.89 ms at k = 30 on one core. It is run automatically by `run_all.py --mode full`. |
| 2 | MODERATE | Cross-fitting needs k refits of the transfer map. For DS with large p this means k pseudo-inverses of k × p matrices. | Report measured cost. | Table 7: cross-fitting took tens of ms per split for both datasets (k = 10, p = 650–700). This is negligible compared with acquiring the reference analyses that TD-CP+ avoids. |
| 3 | MINOR | Memory: storing nk candidate bounds. | Quantify. | 8·nk bytes per test sample (0.4 MB at n = 5000, k = 10). Trivial. Noted here, not in the paper. |
| 4 | MINOR | Weighted CP with a cross-fitted classifier adds cost but brings no benefit. | — | Correctly treated as a baseline only. |
| 5 | MINOR | Deployment: the k leave-one-out maps must be stored with the calibration. | Mention. | Implied by Eq. (6). Covered in the README usage example. |

**Is the improvement worth its cost?** Yes. The additional cost is milliseconds per split, compared with ~10 reference analyses (hours to days of laboratory work) for the labelled alternative, which was in addition less efficient (Table 3).
