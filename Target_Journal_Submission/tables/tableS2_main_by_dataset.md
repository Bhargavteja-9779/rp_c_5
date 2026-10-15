**Table S2. Main results at alpha = 0.10 by dataset**

| dataset | transfer | method | scenarios | mean_coverage | min_coverage | pct_valid | median_width_sd | median_IS_sd | pct_infinite |
|---|---|---|---|---|---|---|---|---|---|
| corn | DS | Naive CP (primary residuals) | 24 | 0.554 | 0.055 | 0.000 | 1.304 | 6.614 | 0.000 |
| corn | DS | Leverage PI (classical) | 24 | 0.627 | 0.071 | 0.000 | 1.660 | 5.437 | 0.000 |
| corn | DS | Weighted CP (covariate shift) | 24 | 0.618 | 0.260 | 0.000 | ∞ | ∞ | 13.733 |
| corn | DS | Gaussian TD (parametric) | 24 | 0.870 | 0.816 | 33.333 | 3.226 | 4.726 | 0.000 |
| corn | DS | TD-CP signed (pre-specified) | 24 | 0.877 | 0.793 | 50.000 | 3.347 | 4.807 | 0.000 |
| corn | DS | TD-CP absolute scores | 24 | 0.886 | 0.847 | 58.333 | 3.512 | 4.843 | 0.000 |
| corn | DS | TD-CP+ (jackknife+) | 24 | 0.929 | 0.909 | 100.000 | 4.048 | 4.736 | 0.000 |
| corn | DS | Target CP (k labelled) | 24 | 0.889 | 0.856 | 75.000 | 3.714 | 4.935 | 0.000 |
| corn | DS | Target CP+ (k labelled) | 24 | 0.926 | 0.910 | 100.000 | 4.293 | 4.990 | 0.000 |
| corn | DS | Pooled CP (k labelled) | 24 | 0.702 | 0.543 | 0.000 | 1.768 | 5.253 | 0.000 |
| corn | PDS | Naive CP (primary residuals) | 24 | 0.445 | 0.044 | 0.000 | 1.304 | 18.756 | 0.000 |
| corn | PDS | Leverage PI (classical) | 24 | 0.541 | 0.085 | 0.000 | 2.087 | 12.838 | 0.000 |
| corn | PDS | Weighted CP (covariate shift) | 24 | 0.585 | 0.361 | 0.000 | ∞ | ∞ | 19.510 |
| corn | PDS | Gaussian TD (parametric) | 24 | 0.896 | 0.881 | 100.000 | 5.419 | 7.897 | 0.000 |
| corn | PDS | TD-CP signed (pre-specified) | 24 | 0.893 | 0.855 | 70.833 | 5.751 | 8.435 | 0.000 |
| corn | PDS | TD-CP absolute scores | 24 | 0.916 | 0.897 | 100.000 | 6.577 | 8.527 | 0.000 |
| corn | PDS | TD-CP+ (jackknife+) | 24 | 0.939 | 0.920 | 100.000 | 7.245 | 8.370 | 0.000 |
| corn | PDS | Target CP (k labelled) | 24 | 0.918 | 0.904 | 100.000 | 6.752 | 8.585 | 0.000 |
| corn | PDS | Target CP+ (k labelled) | 24 | 0.941 | 0.918 | 100.000 | 7.401 | 8.472 | 0.000 |
| corn | PDS | Pooled CP (k labelled) | 24 | 0.655 | 0.551 | 0.000 | 2.567 | 11.101 | 0.000 |
| tablets | DS | Naive CP (primary residuals) | 6 | 0.720 | 0.492 | 33.333 | 2.372 | 4.282 | 0.000 |
| tablets | DS | Leverage PI (classical) | 6 | 0.773 | 0.616 | 33.333 | 2.493 | 3.847 | 0.000 |
| tablets | DS | Weighted CP (covariate shift) | 6 | 0.700 | 0.488 | 16.667 | ∞ | ∞ | 1.368 |
| tablets | DS | Gaussian TD (parametric) | 6 | 0.918 | 0.911 | 100.000 | 2.959 | 3.879 | 0.000 |
| tablets | DS | TD-CP signed (pre-specified) | 6 | 0.905 | 0.887 | 100.000 | 2.922 | 3.874 | 0.000 |
| tablets | DS | TD-CP absolute scores | 6 | 0.914 | 0.908 | 100.000 | 2.913 | 3.881 | 0.000 |
| tablets | DS | TD-CP+ (jackknife+) | 6 | 0.918 | 0.899 | 100.000 | 2.958 | 3.857 | 0.000 |
| tablets | DS | Target CP (k labelled) | 6 | 0.921 | 0.906 | 100.000 | 3.620 | 4.598 | 0.000 |
| tablets | DS | Target CP+ (k labelled) | 6 | 0.924 | 0.914 | 100.000 | 3.665 | 4.582 | 0.000 |
| tablets | DS | Pooled CP (k labelled) | 6 | 0.726 | 0.506 | 16.667 | 2.389 | 4.184 | 0.000 |
| tablets | PDS | Naive CP (primary residuals) | 6 | 0.635 | 0.487 | 0.000 | 2.372 | 5.438 | 0.000 |
| tablets | PDS | Leverage PI (classical) | 6 | 0.703 | 0.536 | 0.000 | 2.602 | 5.169 | 0.000 |
| tablets | PDS | Weighted CP (covariate shift) | 6 | 0.717 | 0.628 | 0.000 | ∞ | ∞ | 10.382 |
| tablets | PDS | Gaussian TD (parametric) | 6 | 0.920 | 0.912 | 100.000 | 3.780 | 4.790 | 0.000 |
| tablets | PDS | TD-CP signed (pre-specified) | 6 | 0.900 | 0.892 | 100.000 | 3.747 | 4.856 | 0.000 |
| tablets | PDS | TD-CP absolute scores | 6 | 0.920 | 0.912 | 100.000 | 3.865 | 4.893 | 0.000 |
| tablets | PDS | TD-CP+ (jackknife+) | 6 | 0.940 | 0.916 | 100.000 | 4.096 | 4.981 | 0.000 |
| tablets | PDS | Target CP (k labelled) | 6 | 0.930 | 0.912 | 100.000 | 4.750 | 5.745 | 0.000 |
| tablets | PDS | Target CP+ (k labelled) | 6 | 0.947 | 0.917 | 100.000 | 5.016 | 5.879 | 0.000 |
| tablets | PDS | Pooled CP (k labelled) | 6 | 0.645 | 0.499 | 0.000 | 2.445 | 5.381 | 0.000 |
