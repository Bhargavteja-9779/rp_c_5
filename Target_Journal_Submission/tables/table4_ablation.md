**Table 4. Ablation of TD-CP components (alpha = 0.10)**

| dataset | transfer | method | scenarios | mean_coverage | min_coverage | pct_valid | median_width_sd | median_IS_sd | pct_infinite |
|---|---|---|---|---|---|---|---|---|---|
| corn + tablets | DS | TD-CP+ (jackknife+) | 30 | 0.927 | 0.899 | 100.000 | 3.980 | 4.621 | 0.000 |
| corn + tablets | DS | TD-CP absolute scores | 30 | 0.892 | 0.847 | 66.667 | 3.499 | 4.658 | 0.000 |
| corn + tablets | DS | TD-CP signed (pre-specified) | 30 | 0.883 | 0.793 | 60.000 | 3.286 | 4.687 | 0.000 |
| corn + tablets | DS | TD-CP w/o cross-fitting | 30 | 0.597 | 0.056 | 6.667 | 1.403 | 5.482 | 0.000 |
| corn + tablets | DS | TD-sum (union bound) | 30 | 0.961 | 0.870 | 93.333 | 4.931 | 5.547 | 0.000 |
| corn + tablets | DS | Gaussian TD (parametric) | 30 | 0.880 | 0.816 | 46.667 | 3.165 | 4.613 | 0.000 |
| corn + tablets | DS | Naive CP (primary residuals) | 30 | 0.587 | 0.055 | 6.667 | 1.363 | 5.547 | 0.000 |
| corn + tablets | PDS | TD-CP+ (jackknife+) | 30 | 0.939 | 0.916 | 100.000 | 7.066 | 7.974 | 0.000 |
| corn + tablets | PDS | TD-CP absolute scores | 30 | 0.917 | 0.897 | 100.000 | 6.356 | 8.010 | 0.000 |
| corn + tablets | PDS | TD-CP signed (pre-specified) | 30 | 0.895 | 0.855 | 76.667 | 5.471 | 8.137 | 0.000 |
| corn + tablets | PDS | TD-CP w/o cross-fitting | 30 | 0.789 | 0.627 | 0.000 | 3.524 | 8.158 | 0.000 |
| corn + tablets | PDS | TD-sum (union bound) | 30 | 0.966 | 0.924 | 100.000 | 7.630 | 9.024 | 0.000 |
| corn + tablets | PDS | Gaussian TD (parametric) | 30 | 0.901 | 0.881 | 100.000 | 5.311 | 7.654 | 0.000 |
| corn + tablets | PDS | Naive CP (primary residuals) | 30 | 0.483 | 0.044 | 0.000 | 1.363 | 14.290 | 0.000 |
