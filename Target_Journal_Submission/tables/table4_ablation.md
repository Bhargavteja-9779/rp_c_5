**Table 4. Ablation of TD-CP components (alpha = 0.10)**

| dataset | transfer | method | scenarios | mean_coverage | min_coverage | pct_valid | median_width_sd | median_IS_sd | pct_infinite |
|---|---|---|---|---|---|---|---|---|---|
| corn | DS | TD-CP+ (jackknife+) | 24 | 0.929 | 0.909 | 100.000 | 4.048 | 4.736 | 0.000 |
| corn | DS | TD-CP absolute scores | 24 | 0.886 | 0.847 | 58.333 | 3.512 | 4.843 | 0.000 |
| corn | DS | TD-CP signed (pre-registered) | 24 | 0.877 | 0.793 | 50.000 | 3.347 | 4.807 | 0.000 |
| corn | DS | TD-CP w/o cross-fitting | 24 | 0.566 | 0.056 | 0.000 | 1.349 | 6.516 | 0.000 |
| corn | DS | TD-sum (union bound) | 24 | 0.957 | 0.870 | 91.667 | 5.063 | 5.566 | 0.000 |
| corn | DS | Gaussian TD (parametric) | 24 | 0.870 | 0.816 | 33.333 | 3.226 | 4.726 | 0.000 |
| corn | DS | Naive CP (primary residuals) | 24 | 0.554 | 0.055 | 0.000 | 1.304 | 6.614 | 0.000 |
| corn | PDS | TD-CP+ (jackknife+) | 24 | 0.939 | 0.920 | 100.000 | 7.245 | 8.370 | 0.000 |
| corn | PDS | TD-CP absolute scores | 24 | 0.916 | 0.897 | 100.000 | 6.577 | 8.527 | 0.000 |
| corn | PDS | TD-CP signed (pre-registered) | 24 | 0.893 | 0.855 | 70.833 | 5.751 | 8.435 | 0.000 |
| corn | PDS | TD-CP w/o cross-fitting | 24 | 0.805 | 0.726 | 0.000 | 4.022 | 8.561 | 0.000 |
| corn | PDS | TD-sum (union bound) | 24 | 0.963 | 0.924 | 100.000 | 8.500 | 9.343 | 0.000 |
| corn | PDS | Gaussian TD (parametric) | 24 | 0.896 | 0.881 | 100.000 | 5.419 | 7.897 | 0.000 |
| corn | PDS | Naive CP (primary residuals) | 24 | 0.445 | 0.044 | 0.000 | 1.304 | 18.756 | 0.000 |
| tablets | DS | TD-CP+ (jackknife+) | 6 | 0.918 | 0.899 | 100.000 | 2.958 | 3.857 | 0.000 |
| tablets | DS | TD-CP absolute scores | 6 | 0.914 | 0.908 | 100.000 | 2.913 | 3.881 | 0.000 |
| tablets | DS | TD-CP signed (pre-registered) | 6 | 0.905 | 0.887 | 100.000 | 2.922 | 3.874 | 0.000 |
| tablets | DS | TD-CP w/o cross-fitting | 6 | 0.720 | 0.492 | 33.333 | 2.380 | 4.276 | 0.000 |
| tablets | DS | TD-sum (union bound) | 6 | 0.978 | 0.971 | 100.000 | 4.621 | 4.916 | 0.000 |
| tablets | DS | Gaussian TD (parametric) | 6 | 0.918 | 0.911 | 100.000 | 2.959 | 3.879 | 0.000 |
| tablets | DS | Naive CP (primary residuals) | 6 | 0.720 | 0.492 | 33.333 | 2.372 | 4.282 | 0.000 |
| tablets | PDS | TD-CP+ (jackknife+) | 6 | 0.940 | 0.916 | 100.000 | 4.096 | 4.981 | 0.000 |
| tablets | PDS | TD-CP absolute scores | 6 | 0.920 | 0.912 | 100.000 | 3.865 | 4.893 | 0.000 |
| tablets | PDS | TD-CP signed (pre-registered) | 6 | 0.900 | 0.892 | 100.000 | 3.747 | 4.856 | 0.000 |
| tablets | PDS | TD-CP w/o cross-fitting | 6 | 0.725 | 0.627 | 0.000 | 2.751 | 5.005 | 0.000 |
| tablets | PDS | TD-sum (union bound) | 6 | 0.978 | 0.976 | 100.000 | 5.779 | 6.107 | 0.000 |
| tablets | PDS | Gaussian TD (parametric) | 6 | 0.920 | 0.912 | 100.000 | 3.780 | 4.790 | 0.000 |
| tablets | PDS | Naive CP (primary residuals) | 6 | 0.635 | 0.487 | 0.000 | 2.372 | 5.438 | 0.000 |
