**Table 2. Main results at alpha = 0.10, 30 scenarios per transfer method (scenario means over repetitions)**

| dataset | transfer | method | scenarios | mean_coverage | min_coverage | pct_valid | median_width_sd | median_IS_sd | pct_infinite |
|---|---|---|---|---|---|---|---|---|---|
| corn + tablets | DS | Naive CP (primary residuals) | 30 | 0.587 | 0.055 | 6.667 | 1.363 | 5.547 | 0.000 |
| corn + tablets | DS | Leverage PI (classical) | 30 | 0.656 | 0.071 | 6.667 | 1.708 | 4.706 | 0.000 |
| corn + tablets | DS | Weighted CP (covariate shift) | 30 | 0.634 | 0.260 | 3.333 | ∞ | ∞ | 11.260 |
| corn + tablets | DS | Gaussian TD (parametric) | 30 | 0.880 | 0.816 | 46.667 | 3.165 | 4.613 | 0.000 |
| corn + tablets | DS | TD-CP signed (pre-specified) | 30 | 0.883 | 0.793 | 60.000 | 3.286 | 4.687 | 0.000 |
| corn + tablets | DS | TD-CP absolute scores | 30 | 0.892 | 0.847 | 66.667 | 3.499 | 4.658 | 0.000 |
| corn + tablets | DS | TD-CP+ (jackknife+) | 30 | 0.927 | 0.899 | 100.000 | 3.980 | 4.621 | 0.000 |
| corn + tablets | DS | Target CP (k labelled) | 30 | 0.895 | 0.856 | 80.000 | 3.674 | 4.922 | 0.000 |
| corn + tablets | DS | Target CP+ (k labelled) | 30 | 0.926 | 0.910 | 100.000 | 4.255 | 4.972 | 0.000 |
| corn + tablets | DS | Target t-interval (k labelled) | 30 | 0.892 | 0.849 | 80.000 | 3.521 | 4.809 | 0.000 |
| corn + tablets | DS | Pooled CP (k labelled) | 30 | 0.706 | 0.506 | 3.333 | 1.782 | 5.043 | 0.000 |
| corn + tablets | PDS | Naive CP (primary residuals) | 30 | 0.483 | 0.044 | 0.000 | 1.363 | 14.290 | 0.000 |
| corn + tablets | PDS | Leverage PI (classical) | 30 | 0.574 | 0.085 | 0.000 | 2.181 | 10.594 | 0.000 |
| corn + tablets | PDS | Weighted CP (covariate shift) | 30 | 0.612 | 0.361 | 0.000 | ∞ | ∞ | 17.684 |
| corn + tablets | PDS | Gaussian TD (parametric) | 30 | 0.901 | 0.881 | 100.000 | 5.311 | 7.654 | 0.000 |
| corn + tablets | PDS | TD-CP signed (pre-specified) | 30 | 0.895 | 0.855 | 76.667 | 5.471 | 8.137 | 0.000 |
| corn + tablets | PDS | TD-CP absolute scores | 30 | 0.917 | 0.897 | 100.000 | 6.356 | 8.010 | 0.000 |
| corn + tablets | PDS | TD-CP+ (jackknife+) | 30 | 0.939 | 0.916 | 100.000 | 7.066 | 7.974 | 0.000 |
| corn + tablets | PDS | Target CP (k labelled) | 30 | 0.921 | 0.904 | 100.000 | 6.632 | 8.362 | 0.000 |
| corn + tablets | PDS | Target CP+ (k labelled) | 30 | 0.942 | 0.917 | 100.000 | 7.286 | 8.291 | 0.000 |
| corn + tablets | PDS | Target t-interval (k labelled) | 30 | 0.919 | 0.904 | 100.000 | 6.048 | 7.815 | 0.000 |
| corn + tablets | PDS | Pooled CP (k labelled) | 30 | 0.653 | 0.499 | 0.000 | 2.535 | 10.730 | 0.000 |
