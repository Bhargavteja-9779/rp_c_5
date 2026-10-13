**Table S1. Per-scenario results (alpha = 0.10)**

| dataset | primary | secondary | prop | transfer | method | coverage | coverage_se | width_norm | is_norm | rmsep | rmsep_primary | delta_cf_sd | delta_test_sd | spearman_r_delta |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| corn | m5 | mp5 | 0 | ds | Gaussian TD (parametric) | 0.816 | 0.020 | 3.045 | 5.363 | 0.352 | 0.011 | 0.352 | 0.335 | -0.053 |
| corn | m5 | mp5 | 0 | ds | Leverage PI (classical) | 0.080 | 0.006 | 0.166 | 13.098 | 0.352 | 0.011 | 0.352 | 0.335 | -0.053 |
| corn | m5 | mp5 | 0 | ds | Naive CP (primary residuals) | 0.060 | 0.005 | 0.117 | 13.513 | 0.352 | 0.011 | 0.352 | 0.335 | -0.053 |
| corn | m5 | mp5 | 0 | ds | Pooled CP (k labelled) | 0.543 | 0.024 | 1.386 | 7.255 | 0.352 | 0.011 | 0.352 | 0.335 | -0.053 |
| corn | m5 | mp5 | 0 | ds | Target CP (k labelled) | 0.856 | 0.018 | 3.495 | 5.392 | 0.352 | 0.011 | 0.352 | 0.335 | -0.053 |
| corn | m5 | mp5 | 0 | ds | Target CP+ (k labelled) | 0.913 | 0.014 | 4.248 | 5.052 | 0.352 | 0.011 | 0.352 | 0.335 | -0.053 |
| corn | m5 | mp5 | 0 | ds | TD-CP signed (pre-registered) | 0.793 | 0.020 | 2.926 | 5.532 | 0.352 | 0.011 | 0.352 | 0.335 | -0.053 |
| corn | m5 | mp5 | 0 | ds | TD-CP absolute scores | 0.852 | 0.018 | 3.436 | 5.396 | 0.352 | 0.011 | 0.352 | 0.335 | -0.053 |
| corn | m5 | mp5 | 0 | ds | TD-CP+ (jackknife+) | 0.909 | 0.015 | 4.190 | 5.037 | 0.352 | 0.011 | 0.352 | 0.335 | -0.053 |
| corn | m5 | mp5 | 0 | ds | Weighted CP (covariate shift) | 0.532 | 0.023 | ∞ | ∞ | 0.352 | 0.011 | 0.352 | 0.335 | -0.053 |
| corn | m5 | mp5 | 0 | pds | Gaussian TD (parametric) | 0.886 | 0.011 | 5.135 | 7.953 | 0.580 | 0.011 | 0.594 | 0.555 | -0.044 |
| corn | m5 | mp5 | 0 | pds | Leverage PI (classical) | 0.085 | 0.006 | 0.293 | 20.404 | 0.580 | 0.011 | 0.594 | 0.555 | -0.044 |
| corn | m5 | mp5 | 0 | pds | Naive CP (primary residuals) | 0.044 | 0.004 | 0.117 | 21.901 | 0.580 | 0.011 | 0.594 | 0.555 | -0.044 |
| corn | m5 | mp5 | 0 | pds | Pooled CP (k labelled) | 0.565 | 0.019 | 2.103 | 11.095 | 0.580 | 0.011 | 0.594 | 0.555 | -0.044 |
| corn | m5 | mp5 | 0 | pds | Target CP (k labelled) | 0.921 | 0.010 | 6.591 | 8.665 | 0.580 | 0.011 | 0.594 | 0.555 | -0.044 |
| corn | m5 | mp5 | 0 | pds | Target CP+ (k labelled) | 0.944 | 0.008 | 7.269 | 8.446 | 0.580 | 0.011 | 0.594 | 0.555 | -0.044 |
| corn | m5 | mp5 | 0 | pds | TD-CP signed (pre-registered) | 0.855 | 0.013 | 5.183 | 8.643 | 0.580 | 0.011 | 0.594 | 0.555 | -0.044 |
| corn | m5 | mp5 | 0 | pds | TD-CP absolute scores | 0.919 | 0.010 | 6.546 | 8.642 | 0.580 | 0.011 | 0.594 | 0.555 | -0.044 |
| corn | m5 | mp5 | 0 | pds | TD-CP+ (jackknife+) | 0.942 | 0.008 | 7.219 | 8.429 | 0.580 | 0.011 | 0.594 | 0.555 | -0.044 |
| corn | m5 | mp5 | 0 | pds | Weighted CP (covariate shift) | 0.560 | 0.022 | ∞ | ∞ | 0.580 | 0.011 | 0.594 | 0.555 | -0.044 |
| corn | m5 | mp5 | 1 | ds | Gaussian TD (parametric) | 0.845 | 0.013 | 3.270 | 5.324 | 0.178 | 0.063 | 0.162 | 0.162 | -0.068 |
| corn | m5 | mp5 | 1 | ds | Leverage PI (classical) | 0.640 | 0.014 | 1.696 | 6.063 | 0.178 | 0.063 | 0.162 | 0.162 | -0.068 |
| corn | m5 | mp5 | 1 | ds | Naive CP (primary residuals) | 0.520 | 0.014 | 1.245 | 7.905 | 0.178 | 0.063 | 0.162 | 0.162 | -0.068 |
| corn | m5 | mp5 | 1 | ds | Pooled CP (k labelled) | 0.662 | 0.015 | 1.762 | 6.444 | 0.178 | 0.063 | 0.162 | 0.162 | -0.068 |
| corn | m5 | mp5 | 1 | ds | Target CP (k labelled) | 0.875 | 0.013 | 3.732 | 5.408 | 0.178 | 0.063 | 0.162 | 0.162 | -0.068 |
| corn | m5 | mp5 | 1 | ds | Target CP+ (k labelled) | 0.921 | 0.011 | 4.323 | 5.076 | 0.178 | 0.063 | 0.162 | 0.162 | -0.068 |
| corn | m5 | mp5 | 1 | ds | TD-CP signed (pre-registered) | 0.846 | 0.013 | 3.419 | 5.460 | 0.178 | 0.063 | 0.162 | 0.162 | -0.068 |
| corn | m5 | mp5 | 1 | ds | TD-CP absolute scores | 0.866 | 0.014 | 3.533 | 5.264 | 0.178 | 0.063 | 0.162 | 0.162 | -0.068 |
| corn | m5 | mp5 | 1 | ds | TD-CP+ (jackknife+) | 0.915 | 0.011 | 4.115 | 4.911 | 0.178 | 0.063 | 0.162 | 0.162 | -0.068 |
| corn | m5 | mp5 | 1 | ds | Weighted CP (covariate shift) | 0.777 | 0.013 | ∞ | ∞ | 0.178 | 0.063 | 0.162 | 0.162 | -0.068 |
| corn | m5 | mp5 | 1 | pds | Gaussian TD (parametric) | 0.901 | 0.011 | 11.125 | 16.381 | 0.541 | 0.063 | 0.594 | 0.520 | -0.031 |
| corn | m5 | mp5 | 1 | pds | Leverage PI (classical) | 0.368 | 0.016 | 2.735 | 26.196 | 0.541 | 0.063 | 0.594 | 0.520 | -0.031 |
| corn | m5 | mp5 | 1 | pds | Naive CP (primary residuals) | 0.229 | 0.015 | 1.245 | 36.966 | 0.541 | 0.063 | 0.594 | 0.520 | -0.031 |
| corn | m5 | mp5 | 1 | pds | Pooled CP (k labelled) | 0.557 | 0.019 | 4.209 | 22.698 | 0.541 | 0.063 | 0.594 | 0.520 | -0.031 |
| corn | m5 | mp5 | 1 | pds | Target CP (k labelled) | 0.934 | 0.007 | 14.137 | 17.928 | 0.541 | 0.063 | 0.594 | 0.520 | -0.031 |
| corn | m5 | mp5 | 1 | pds | Target CP+ (k labelled) | 0.956 | 0.007 | 15.980 | 17.953 | 0.541 | 0.063 | 0.594 | 0.520 | -0.031 |
| corn | m5 | mp5 | 1 | pds | TD-CP signed (pre-registered) | 0.884 | 0.011 | 11.601 | 17.585 | 0.541 | 0.063 | 0.594 | 0.520 | -0.031 |
| corn | m5 | mp5 | 1 | pds | TD-CP absolute scores | 0.926 | 0.009 | 13.780 | 17.831 | 0.541 | 0.063 | 0.594 | 0.520 | -0.031 |
| corn | m5 | mp5 | 1 | pds | TD-CP+ (jackknife+) | 0.946 | 0.008 | 15.556 | 17.705 | 0.541 | 0.063 | 0.594 | 0.520 | -0.031 |
| corn | m5 | mp5 | 1 | pds | Weighted CP (covariate shift) | 0.635 | 0.018 | ∞ | ∞ | 0.541 | 0.063 | 0.594 | 0.520 | -0.031 |
| corn | m5 | mp5 | 2 | ds | Gaussian TD (parametric) | 0.856 | 0.015 | 2.726 | 4.226 | 0.380 | 0.118 | 0.393 | 0.352 | -0.089 |
| corn | m5 | mp5 | 2 | ds | Leverage PI (classical) | 0.570 | 0.016 | 1.096 | 5.297 | 0.380 | 0.118 | 0.393 | 0.352 | -0.089 |
| corn | m5 | mp5 | 2 | ds | Naive CP (primary residuals) | 0.472 | 0.015 | 0.823 | 6.530 | 0.380 | 0.118 | 0.393 | 0.352 | -0.089 |
| corn | m5 | mp5 | 2 | ds | Pooled CP (k labelled) | 0.654 | 0.019 | 1.381 | 5.133 | 0.380 | 0.118 | 0.393 | 0.352 | -0.089 |
| corn | m5 | mp5 | 2 | ds | Target CP (k labelled) | 0.888 | 0.016 | 3.159 | 4.396 | 0.380 | 0.118 | 0.393 | 0.352 | -0.089 |
| corn | m5 | mp5 | 2 | ds | Target CP+ (k labelled) | 0.930 | 0.012 | 3.711 | 4.289 | 0.380 | 0.118 | 0.393 | 0.352 | -0.089 |
| corn | m5 | mp5 | 2 | ds | TD-CP signed (pre-registered) | 0.862 | 0.015 | 2.793 | 4.252 | 0.380 | 0.118 | 0.393 | 0.352 | -0.089 |
| corn | m5 | mp5 | 2 | ds | TD-CP absolute scores | 0.874 | 0.016 | 2.946 | 4.232 | 0.380 | 0.118 | 0.393 | 0.352 | -0.089 |
| corn | m5 | mp5 | 2 | ds | TD-CP+ (jackknife+) | 0.921 | 0.013 | 3.511 | 4.125 | 0.380 | 0.118 | 0.393 | 0.352 | -0.089 |
| corn | m5 | mp5 | 2 | ds | Weighted CP (covariate shift) | 0.734 | 0.018 | ∞ | ∞ | 0.380 | 0.118 | 0.393 | 0.352 | -0.089 |
| corn | m5 | mp5 | 2 | pds | Gaussian TD (parametric) | 0.892 | 0.013 | 7.072 | 10.217 | 0.962 | 0.118 | 1.063 | 0.921 | -0.114 |
| corn | m5 | mp5 | 2 | pds | Leverage PI (classical) | 0.397 | 0.020 | 1.853 | 16.682 | 0.962 | 0.118 | 1.063 | 0.921 | -0.114 |
| corn | m5 | mp5 | 2 | pds | Naive CP (primary residuals) | 0.254 | 0.017 | 0.823 | 24.045 | 0.962 | 0.118 | 1.063 | 0.921 | -0.114 |
| corn | m5 | mp5 | 2 | pds | Pooled CP (k labelled) | 0.600 | 0.019 | 2.958 | 13.773 | 0.962 | 0.118 | 1.063 | 0.921 | -0.114 |
| corn | m5 | mp5 | 2 | pds | Target CP (k labelled) | 0.919 | 0.012 | 8.601 | 11.105 | 0.962 | 0.118 | 1.063 | 0.921 | -0.114 |
| corn | m5 | mp5 | 2 | pds | Target CP+ (k labelled) | 0.954 | 0.008 | 9.652 | 10.480 | 0.962 | 0.118 | 1.063 | 0.921 | -0.114 |
| corn | m5 | mp5 | 2 | pds | TD-CP signed (pre-registered) | 0.892 | 0.012 | 7.308 | 10.557 | 0.962 | 0.118 | 1.063 | 0.921 | -0.114 |
| corn | m5 | mp5 | 2 | pds | TD-CP absolute scores | 0.919 | 0.012 | 8.360 | 10.903 | 0.962 | 0.118 | 1.063 | 0.921 | -0.114 |
| corn | m5 | mp5 | 2 | pds | TD-CP+ (jackknife+) | 0.952 | 0.008 | 9.393 | 10.277 | 0.962 | 0.118 | 1.063 | 0.921 | -0.114 |
| corn | m5 | mp5 | 2 | pds | Weighted CP (covariate shift) | 0.664 | 0.017 | ∞ | ∞ | 0.962 | 0.118 | 1.063 | 0.921 | -0.114 |
| corn | m5 | mp5 | 3 | ds | Gaussian TD (parametric) | 0.855 | 0.015 | 3.847 | 5.906 | 0.886 | 0.216 | 0.926 | 0.811 | -0.022 |
| corn | m5 | mp5 | 3 | ds | Leverage PI (classical) | 0.510 | 0.013 | 1.372 | 7.890 | 0.886 | 0.216 | 0.926 | 0.811 | -0.022 |
| corn | m5 | mp5 | 3 | ds | Naive CP (primary residuals) | 0.396 | 0.013 | 0.984 | 9.955 | 0.886 | 0.216 | 0.926 | 0.811 | -0.022 |
| corn | m5 | mp5 | 3 | ds | Pooled CP (k labelled) | 0.658 | 0.020 | 1.959 | 7.107 | 0.886 | 0.216 | 0.926 | 0.811 | -0.022 |
| corn | m5 | mp5 | 3 | ds | Target CP (k labelled) | 0.887 | 0.014 | 4.392 | 6.025 | 0.886 | 0.216 | 0.926 | 0.811 | -0.022 |
| corn | m5 | mp5 | 3 | ds | Target CP+ (k labelled) | 0.945 | 0.010 | 5.252 | 5.922 | 0.886 | 0.216 | 0.926 | 0.811 | -0.022 |
| corn | m5 | mp5 | 3 | ds | TD-CP signed (pre-registered) | 0.854 | 0.014 | 3.839 | 5.947 | 0.886 | 0.216 | 0.926 | 0.811 | -0.022 |
| corn | m5 | mp5 | 3 | ds | TD-CP absolute scores | 0.871 | 0.015 | 4.095 | 5.905 | 0.886 | 0.216 | 0.926 | 0.811 | -0.022 |
| corn | m5 | mp5 | 3 | ds | TD-CP+ (jackknife+) | 0.936 | 0.011 | 4.939 | 5.673 | 0.886 | 0.216 | 0.926 | 0.811 | -0.022 |
| corn | m5 | mp5 | 3 | ds | Weighted CP (covariate shift) | 0.716 | 0.016 | ∞ | ∞ | 0.886 | 0.216 | 0.926 | 0.811 | -0.022 |
| corn | m5 | mp5 | 3 | pds | Gaussian TD (parametric) | 0.888 | 0.012 | 8.615 | 12.236 | 2.041 | 0.216 | 2.134 | 1.922 | -0.024 |
| corn | m5 | mp5 | 3 | pds | Leverage PI (classical) | 0.356 | 0.015 | 2.385 | 21.224 | 2.041 | 0.216 | 2.134 | 1.922 | -0.024 |
| corn | m5 | mp5 | 3 | pds | Naive CP (primary residuals) | 0.195 | 0.012 | 0.984 | 31.061 | 2.041 | 0.216 | 2.134 | 1.922 | -0.024 |
| corn | m5 | mp5 | 3 | pds | Pooled CP (k labelled) | 0.557 | 0.018 | 3.598 | 17.826 | 2.041 | 0.216 | 2.134 | 1.922 | -0.024 |
| corn | m5 | mp5 | 3 | pds | Target CP (k labelled) | 0.924 | 0.010 | 10.688 | 13.359 | 2.041 | 0.216 | 2.134 | 1.922 | -0.024 |
| corn | m5 | mp5 | 3 | pds | Target CP+ (k labelled) | 0.956 | 0.005 | 11.948 | 13.143 | 2.041 | 0.216 | 2.134 | 1.922 | -0.024 |
| corn | m5 | mp5 | 3 | pds | TD-CP signed (pre-registered) | 0.872 | 0.012 | 8.727 | 12.948 | 2.041 | 0.216 | 2.134 | 1.922 | -0.024 |
| corn | m5 | mp5 | 3 | pds | TD-CP absolute scores | 0.916 | 0.011 | 10.257 | 13.174 | 2.041 | 0.216 | 2.134 | 1.922 | -0.024 |
| corn | m5 | mp5 | 3 | pds | TD-CP+ (jackknife+) | 0.950 | 0.006 | 11.497 | 12.826 | 2.041 | 0.216 | 2.134 | 1.922 | -0.024 |
| corn | m5 | mp5 | 3 | pds | Weighted CP (covariate shift) | 0.680 | 0.018 | ∞ | ∞ | 2.041 | 0.216 | 2.134 | 1.922 | -0.024 |
| corn | m5 | mp6 | 0 | ds | Gaussian TD (parametric) | 0.833 | 0.017 | 3.268 | 5.280 | 0.359 | 0.011 | 0.378 | 0.342 | -0.070 |
| corn | m5 | mp6 | 0 | ds | Leverage PI (classical) | 0.071 | 0.006 | 0.169 | 13.282 | 0.359 | 0.011 | 0.378 | 0.342 | -0.070 |
| corn | m5 | mp6 | 0 | ds | Naive CP (primary residuals) | 0.055 | 0.005 | 0.117 | 13.722 | 0.359 | 0.011 | 0.378 | 0.342 | -0.070 |
| corn | m5 | mp6 | 0 | ds | Pooled CP (k labelled) | 0.579 | 0.023 | 1.552 | 6.922 | 0.359 | 0.011 | 0.378 | 0.342 | -0.070 |
| corn | m5 | mp6 | 0 | ds | Target CP (k labelled) | 0.856 | 0.017 | 3.792 | 5.628 | 0.359 | 0.011 | 0.378 | 0.342 | -0.070 |
| corn | m5 | mp6 | 0 | ds | Target CP+ (k labelled) | 0.926 | 0.012 | 4.550 | 5.175 | 0.359 | 0.011 | 0.378 | 0.342 | -0.070 |
| corn | m5 | mp6 | 0 | ds | TD-CP signed (pre-registered) | 0.799 | 0.017 | 3.077 | 5.537 | 0.359 | 0.011 | 0.378 | 0.342 | -0.070 |
| corn | m5 | mp6 | 0 | ds | TD-CP absolute scores | 0.847 | 0.018 | 3.737 | 5.626 | 0.359 | 0.011 | 0.378 | 0.342 | -0.070 |
| corn | m5 | mp6 | 0 | ds | TD-CP+ (jackknife+) | 0.919 | 0.013 | 4.492 | 5.147 | 0.359 | 0.011 | 0.378 | 0.342 | -0.070 |
| corn | m5 | mp6 | 0 | ds | Weighted CP (covariate shift) | 0.520 | 0.022 | ∞ | ∞ | 0.359 | 0.011 | 0.378 | 0.342 | -0.070 |
| corn | m5 | mp6 | 0 | pds | Gaussian TD (parametric) | 0.882 | 0.012 | 5.290 | 8.225 | 0.600 | 0.011 | 0.612 | 0.577 | -0.049 |
| corn | m5 | mp6 | 0 | pds | Leverage PI (classical) | 0.087 | 0.006 | 0.316 | 20.928 | 0.600 | 0.011 | 0.612 | 0.577 | -0.049 |
| corn | m5 | mp6 | 0 | pds | Naive CP (primary residuals) | 0.048 | 0.004 | 0.117 | 22.605 | 0.600 | 0.011 | 0.612 | 0.577 | -0.049 |
| corn | m5 | mp6 | 0 | pds | Pooled CP (k labelled) | 0.569 | 0.018 | 2.167 | 11.432 | 0.600 | 0.011 | 0.612 | 0.577 | -0.049 |
| corn | m5 | mp6 | 0 | pds | Target CP (k labelled) | 0.916 | 0.011 | 6.831 | 9.121 | 0.600 | 0.011 | 0.612 | 0.577 | -0.049 |
| corn | m5 | mp6 | 0 | pds | Target CP+ (k labelled) | 0.946 | 0.008 | 7.499 | 8.782 | 0.600 | 0.011 | 0.612 | 0.577 | -0.049 |
| corn | m5 | mp6 | 0 | pds | TD-CP signed (pre-registered) | 0.859 | 0.013 | 5.360 | 8.803 | 0.600 | 0.011 | 0.612 | 0.577 | -0.049 |
| corn | m5 | mp6 | 0 | pds | TD-CP absolute scores | 0.913 | 0.011 | 6.778 | 9.115 | 0.600 | 0.011 | 0.612 | 0.577 | -0.049 |
| corn | m5 | mp6 | 0 | pds | TD-CP+ (jackknife+) | 0.944 | 0.008 | 7.444 | 8.760 | 0.600 | 0.011 | 0.612 | 0.577 | -0.049 |
| corn | m5 | mp6 | 0 | pds | Weighted CP (covariate shift) | 0.584 | 0.021 | ∞ | ∞ | 0.600 | 0.011 | 0.612 | 0.577 | -0.049 |
| corn | m5 | mp6 | 1 | ds | Gaussian TD (parametric) | 0.860 | 0.015 | 3.412 | 5.378 | 0.174 | 0.063 | 0.170 | 0.160 | -0.082 |
| corn | m5 | mp6 | 1 | ds | Leverage PI (classical) | 0.641 | 0.015 | 1.719 | 5.792 | 0.174 | 0.063 | 0.170 | 0.160 | -0.082 |
| corn | m5 | mp6 | 1 | ds | Naive CP (primary residuals) | 0.526 | 0.015 | 1.245 | 7.700 | 0.174 | 0.063 | 0.170 | 0.160 | -0.082 |
| corn | m5 | mp6 | 1 | ds | Pooled CP (k labelled) | 0.662 | 0.017 | 1.790 | 6.301 | 0.174 | 0.063 | 0.170 | 0.160 | -0.082 |
| corn | m5 | mp6 | 1 | ds | Target CP (k labelled) | 0.872 | 0.016 | 3.860 | 5.662 | 0.174 | 0.063 | 0.170 | 0.160 | -0.082 |
| corn | m5 | mp6 | 1 | ds | Target CP+ (k labelled) | 0.922 | 0.013 | 4.540 | 5.410 | 0.174 | 0.063 | 0.170 | 0.160 | -0.082 |
| corn | m5 | mp6 | 1 | ds | TD-CP signed (pre-registered) | 0.862 | 0.014 | 3.544 | 5.510 | 0.174 | 0.063 | 0.170 | 0.160 | -0.082 |
| corn | m5 | mp6 | 1 | ds | TD-CP absolute scores | 0.875 | 0.014 | 3.680 | 5.420 | 0.174 | 0.063 | 0.170 | 0.160 | -0.082 |
| corn | m5 | mp6 | 1 | ds | TD-CP+ (jackknife+) | 0.922 | 0.011 | 4.300 | 5.138 | 0.174 | 0.063 | 0.170 | 0.160 | -0.082 |
| corn | m5 | mp6 | 1 | ds | Weighted CP (covariate shift) | 0.773 | 0.013 | ∞ | ∞ | 0.174 | 0.063 | 0.170 | 0.160 | -0.082 |
| corn | m5 | mp6 | 1 | pds | Gaussian TD (parametric) | 0.905 | 0.012 | 11.665 | 17.065 | 0.563 | 0.063 | 0.623 | 0.541 | -0.044 |
| corn | m5 | mp6 | 1 | pds | Leverage PI (classical) | 0.380 | 0.019 | 2.811 | 27.804 | 0.563 | 0.063 | 0.623 | 0.541 | -0.044 |
| corn | m5 | mp6 | 1 | pds | Naive CP (primary residuals) | 0.236 | 0.017 | 1.245 | 39.031 | 0.563 | 0.063 | 0.623 | 0.541 | -0.044 |
| corn | m5 | mp6 | 1 | pds | Pooled CP (k labelled) | 0.580 | 0.017 | 4.616 | 22.492 | 0.563 | 0.063 | 0.623 | 0.541 | -0.044 |
| corn | m5 | mp6 | 1 | pds | Target CP (k labelled) | 0.922 | 0.011 | 15.050 | 19.153 | 0.563 | 0.063 | 0.623 | 0.541 | -0.044 |
| corn | m5 | mp6 | 1 | pds | Target CP+ (k labelled) | 0.964 | 0.006 | 16.846 | 18.413 | 0.563 | 0.063 | 0.623 | 0.541 | -0.044 |
| corn | m5 | mp6 | 1 | pds | TD-CP signed (pre-registered) | 0.876 | 0.012 | 12.017 | 18.605 | 0.563 | 0.063 | 0.623 | 0.541 | -0.044 |
| corn | m5 | mp6 | 1 | pds | TD-CP absolute scores | 0.917 | 0.012 | 14.591 | 18.953 | 0.563 | 0.063 | 0.623 | 0.541 | -0.044 |
| corn | m5 | mp6 | 1 | pds | TD-CP+ (jackknife+) | 0.956 | 0.008 | 16.352 | 18.100 | 0.563 | 0.063 | 0.623 | 0.541 | -0.044 |
| corn | m5 | mp6 | 1 | pds | Weighted CP (covariate shift) | 0.657 | 0.019 | ∞ | ∞ | 0.563 | 0.063 | 0.623 | 0.541 | -0.044 |
| corn | m5 | mp6 | 2 | ds | Gaussian TD (parametric) | 0.856 | 0.017 | 2.898 | 4.448 | 0.391 | 0.118 | 0.421 | 0.364 | -0.076 |
| corn | m5 | mp6 | 2 | ds | Leverage PI (classical) | 0.530 | 0.017 | 1.102 | 5.577 | 0.391 | 0.118 | 0.421 | 0.364 | -0.076 |
| corn | m5 | mp6 | 2 | ds | Naive CP (primary residuals) | 0.430 | 0.016 | 0.823 | 6.978 | 0.391 | 0.118 | 0.421 | 0.364 | -0.076 |
| corn | m5 | mp6 | 2 | ds | Pooled CP (k labelled) | 0.647 | 0.023 | 1.481 | 5.296 | 0.391 | 0.118 | 0.421 | 0.364 | -0.076 |
| corn | m5 | mp6 | 2 | ds | Target CP (k labelled) | 0.886 | 0.017 | 3.309 | 4.619 | 0.391 | 0.118 | 0.421 | 0.364 | -0.076 |
| corn | m5 | mp6 | 2 | ds | Target CP+ (k labelled) | 0.932 | 0.013 | 3.886 | 4.477 | 0.391 | 0.118 | 0.421 | 0.364 | -0.076 |
| corn | m5 | mp6 | 2 | ds | TD-CP signed (pre-registered) | 0.858 | 0.016 | 2.892 | 4.456 | 0.391 | 0.118 | 0.421 | 0.364 | -0.076 |
| corn | m5 | mp6 | 2 | ds | TD-CP absolute scores | 0.876 | 0.017 | 3.068 | 4.464 | 0.391 | 0.118 | 0.421 | 0.364 | -0.076 |
| corn | m5 | mp6 | 2 | ds | TD-CP+ (jackknife+) | 0.932 | 0.012 | 3.670 | 4.278 | 0.391 | 0.118 | 0.421 | 0.364 | -0.076 |
| corn | m5 | mp6 | 2 | ds | Weighted CP (covariate shift) | 0.722 | 0.017 | ∞ | ∞ | 0.391 | 0.118 | 0.421 | 0.364 | -0.076 |
| corn | m5 | mp6 | 2 | pds | Gaussian TD (parametric) | 0.895 | 0.012 | 7.373 | 10.395 | 1.036 | 0.118 | 1.109 | 0.989 | -0.104 |
| corn | m5 | mp6 | 2 | pds | Leverage PI (classical) | 0.360 | 0.018 | 1.918 | 18.270 | 1.036 | 0.118 | 1.109 | 0.989 | -0.104 |
| corn | m5 | mp6 | 2 | pds | Naive CP (primary residuals) | 0.228 | 0.016 | 0.823 | 26.303 | 1.036 | 0.118 | 1.109 | 0.989 | -0.104 |
| corn | m5 | mp6 | 2 | pds | Pooled CP (k labelled) | 0.551 | 0.018 | 2.973 | 15.168 | 1.036 | 0.118 | 1.109 | 0.989 | -0.104 |
| corn | m5 | mp6 | 2 | pds | Target CP (k labelled) | 0.926 | 0.011 | 8.995 | 11.367 | 1.036 | 0.118 | 1.109 | 0.989 | -0.104 |
| corn | m5 | mp6 | 2 | pds | Target CP+ (k labelled) | 0.954 | 0.008 | 10.168 | 10.988 | 1.036 | 0.118 | 1.109 | 0.989 | -0.104 |
| corn | m5 | mp6 | 2 | pds | TD-CP signed (pre-registered) | 0.873 | 0.013 | 7.579 | 11.242 | 1.036 | 0.118 | 1.109 | 0.989 | -0.104 |
| corn | m5 | mp6 | 2 | pds | TD-CP absolute scores | 0.922 | 0.012 | 8.746 | 11.200 | 1.036 | 0.118 | 1.109 | 0.989 | -0.104 |
| corn | m5 | mp6 | 2 | pds | TD-CP+ (jackknife+) | 0.953 | 0.008 | 9.875 | 10.759 | 1.036 | 0.118 | 1.109 | 0.989 | -0.104 |
| corn | m5 | mp6 | 2 | pds | Weighted CP (covariate shift) | 0.654 | 0.019 | ∞ | ∞ | 1.036 | 0.118 | 1.109 | 0.989 | -0.104 |
| corn | m5 | mp6 | 3 | ds | Gaussian TD (parametric) | 0.865 | 0.016 | 3.915 | 6.103 | 0.876 | 0.216 | 0.945 | 0.813 | -0.025 |
| corn | m5 | mp6 | 3 | ds | Leverage PI (classical) | 0.511 | 0.015 | 1.384 | 7.818 | 0.876 | 0.216 | 0.945 | 0.813 | -0.025 |
| corn | m5 | mp6 | 3 | ds | Naive CP (primary residuals) | 0.404 | 0.015 | 0.984 | 9.835 | 0.876 | 0.216 | 0.945 | 0.813 | -0.025 |
| corn | m5 | mp6 | 3 | ds | Pooled CP (k labelled) | 0.657 | 0.021 | 1.971 | 7.227 | 0.876 | 0.216 | 0.945 | 0.813 | -0.025 |
| corn | m5 | mp6 | 3 | ds | Target CP (k labelled) | 0.887 | 0.015 | 4.547 | 6.252 | 0.876 | 0.216 | 0.945 | 0.813 | -0.025 |
| corn | m5 | mp6 | 3 | ds | Target CP+ (k labelled) | 0.947 | 0.009 | 5.413 | 6.085 | 0.876 | 0.216 | 0.945 | 0.813 | -0.025 |
| corn | m5 | mp6 | 3 | ds | TD-CP signed (pre-registered) | 0.857 | 0.016 | 3.942 | 6.126 | 0.876 | 0.216 | 0.945 | 0.813 | -0.025 |
| corn | m5 | mp6 | 3 | ds | TD-CP absolute scores | 0.878 | 0.015 | 4.193 | 6.092 | 0.876 | 0.216 | 0.945 | 0.813 | -0.025 |
| corn | m5 | mp6 | 3 | ds | TD-CP+ (jackknife+) | 0.941 | 0.011 | 5.069 | 5.836 | 0.876 | 0.216 | 0.945 | 0.813 | -0.025 |
| corn | m5 | mp6 | 3 | ds | Weighted CP (covariate shift) | 0.725 | 0.017 | ∞ | ∞ | 0.876 | 0.216 | 0.945 | 0.813 | -0.025 |
| corn | m5 | mp6 | 3 | pds | Gaussian TD (parametric) | 0.881 | 0.012 | 8.861 | 12.602 | 2.114 | 0.216 | 2.195 | 2.004 | -0.010 |
| corn | m5 | mp6 | 3 | pds | Leverage PI (classical) | 0.377 | 0.015 | 2.522 | 22.274 | 2.114 | 0.216 | 2.195 | 2.004 | -0.010 |
| corn | m5 | mp6 | 3 | pds | Naive CP (primary residuals) | 0.212 | 0.012 | 0.984 | 32.712 | 2.114 | 0.216 | 2.195 | 2.004 | -0.010 |
| corn | m5 | mp6 | 3 | pds | Pooled CP (k labelled) | 0.569 | 0.019 | 3.863 | 18.274 | 2.114 | 0.216 | 2.195 | 2.004 | -0.010 |
| corn | m5 | mp6 | 3 | pds | Target CP (k labelled) | 0.916 | 0.010 | 10.673 | 13.471 | 2.114 | 0.216 | 2.195 | 2.004 | -0.010 |
| corn | m5 | mp6 | 3 | pds | Target CP+ (k labelled) | 0.952 | 0.007 | 12.033 | 13.301 | 2.114 | 0.216 | 2.195 | 2.004 | -0.010 |
| corn | m5 | mp6 | 3 | pds | TD-CP signed (pre-registered) | 0.868 | 0.013 | 8.836 | 13.279 | 2.114 | 0.216 | 2.195 | 2.004 | -0.010 |
| corn | m5 | mp6 | 3 | pds | TD-CP absolute scores | 0.907 | 0.011 | 10.295 | 13.350 | 2.114 | 0.216 | 2.195 | 2.004 | -0.010 |
| corn | m5 | mp6 | 3 | pds | TD-CP+ (jackknife+) | 0.947 | 0.008 | 11.609 | 13.047 | 2.114 | 0.216 | 2.195 | 2.004 | -0.010 |
| corn | m5 | mp6 | 3 | pds | Weighted CP (covariate shift) | 0.671 | 0.018 | ∞ | ∞ | 2.114 | 0.216 | 2.195 | 2.004 | -0.010 |
| corn | mp5 | m5 | 0 | ds | Gaussian TD (parametric) | 0.923 | 0.009 | 2.865 | 3.532 | 0.258 | 0.153 | 0.288 | 0.262 | -0.379 |
| corn | mp5 | m5 | 0 | ds | Leverage PI (classical) | 0.796 | 0.015 | 1.624 | 3.330 | 0.258 | 0.153 | 0.288 | 0.262 | -0.379 |
| corn | mp5 | m5 | 0 | ds | Naive CP (primary residuals) | 0.724 | 0.018 | 1.363 | 4.086 | 0.258 | 0.153 | 0.288 | 0.262 | -0.379 |
| corn | mp5 | m5 | 0 | ds | Pooled CP (k labelled) | 0.784 | 0.015 | 1.585 | 3.689 | 0.258 | 0.153 | 0.288 | 0.262 | -0.379 |
| corn | mp5 | m5 | 0 | ds | Target CP (k labelled) | 0.914 | 0.011 | 3.032 | 3.682 | 0.258 | 0.153 | 0.288 | 0.262 | -0.379 |
| corn | mp5 | m5 | 0 | ds | Target CP+ (k labelled) | 0.932 | 0.011 | 3.486 | 3.855 | 0.258 | 0.153 | 0.288 | 0.262 | -0.379 |
| corn | mp5 | m5 | 0 | ds | TD-CP signed (pre-registered) | 0.931 | 0.009 | 3.029 | 3.663 | 0.258 | 0.153 | 0.288 | 0.262 | -0.379 |
| corn | mp5 | m5 | 0 | ds | TD-CP absolute scores | 0.941 | 0.008 | 3.080 | 3.607 | 0.258 | 0.153 | 0.288 | 0.262 | -0.379 |
| corn | mp5 | m5 | 0 | ds | TD-CP+ (jackknife+) | 0.965 | 0.006 | 3.487 | 3.680 | 0.258 | 0.153 | 0.288 | 0.262 | -0.379 |
| corn | mp5 | m5 | 0 | ds | Weighted CP (covariate shift) | 0.826 | 0.014 | ∞ | ∞ | 0.258 | 0.153 | 0.288 | 0.262 | -0.379 |
| corn | mp5 | m5 | 0 | pds | Gaussian TD (parametric) | 0.890 | 0.013 | 6.930 | 10.903 | 0.780 | 0.153 | 0.785 | 0.758 | -0.210 |
| corn | mp5 | m5 | 0 | pds | Leverage PI (classical) | 0.431 | 0.017 | 2.128 | 16.388 | 0.780 | 0.153 | 0.785 | 0.758 | -0.210 |
| corn | mp5 | m5 | 0 | pds | Naive CP (primary residuals) | 0.357 | 0.018 | 1.363 | 21.801 | 0.780 | 0.153 | 0.785 | 0.758 | -0.210 |
| corn | mp5 | m5 | 0 | pds | Pooled CP (k labelled) | 0.570 | 0.018 | 2.756 | 15.216 | 0.780 | 0.153 | 0.785 | 0.758 | -0.210 |
| corn | mp5 | m5 | 0 | pds | Target CP (k labelled) | 0.906 | 0.014 | 8.827 | 12.451 | 0.780 | 0.153 | 0.785 | 0.758 | -0.210 |
| corn | mp5 | m5 | 0 | pds | Target CP+ (k labelled) | 0.930 | 0.011 | 9.787 | 11.516 | 0.780 | 0.153 | 0.785 | 0.758 | -0.210 |
| corn | mp5 | m5 | 0 | pds | TD-CP signed (pre-registered) | 0.880 | 0.013 | 7.347 | 11.560 | 0.780 | 0.153 | 0.785 | 0.758 | -0.210 |
| corn | mp5 | m5 | 0 | pds | TD-CP absolute scores | 0.906 | 0.013 | 8.417 | 12.091 | 0.780 | 0.153 | 0.785 | 0.758 | -0.210 |
| corn | mp5 | m5 | 0 | pds | TD-CP+ (jackknife+) | 0.928 | 0.012 | 9.368 | 11.240 | 0.780 | 0.153 | 0.785 | 0.758 | -0.210 |
| corn | mp5 | m5 | 0 | pds | Weighted CP (covariate shift) | 0.624 | 0.018 | ∞ | ∞ | 0.780 | 0.153 | 0.785 | 0.758 | -0.210 |
| corn | mp5 | m5 | 1 | ds | Gaussian TD (parametric) | 0.883 | 0.014 | 3.611 | 5.127 | 0.168 | 0.106 | 0.159 | 0.147 | -0.212 |
| corn | mp5 | m5 | 1 | ds | Leverage PI (classical) | 0.788 | 0.016 | 2.286 | 4.749 | 0.168 | 0.106 | 0.159 | 0.147 | -0.212 |
| corn | mp5 | m5 | 1 | ds | Naive CP (primary residuals) | 0.735 | 0.018 | 2.012 | 5.558 | 0.168 | 0.106 | 0.159 | 0.147 | -0.212 |
| corn | mp5 | m5 | 1 | ds | Pooled CP (k labelled) | 0.782 | 0.017 | 2.299 | 5.209 | 0.168 | 0.106 | 0.159 | 0.147 | -0.212 |
| corn | mp5 | m5 | 1 | ds | Target CP (k labelled) | 0.888 | 0.014 | 3.823 | 5.228 | 0.168 | 0.106 | 0.159 | 0.147 | -0.212 |
| corn | mp5 | m5 | 1 | ds | Target CP+ (k labelled) | 0.915 | 0.012 | 4.381 | 5.373 | 0.168 | 0.106 | 0.159 | 0.147 | -0.212 |
| corn | mp5 | m5 | 1 | ds | TD-CP signed (pre-registered) | 0.903 | 0.013 | 3.893 | 5.134 | 0.168 | 0.106 | 0.159 | 0.147 | -0.212 |
| corn | mp5 | m5 | 1 | ds | TD-CP absolute scores | 0.892 | 0.014 | 3.819 | 5.157 | 0.168 | 0.106 | 0.159 | 0.147 | -0.212 |
| corn | mp5 | m5 | 1 | ds | TD-CP+ (jackknife+) | 0.924 | 0.012 | 4.293 | 5.190 | 0.168 | 0.106 | 0.159 | 0.147 | -0.212 |
| corn | mp5 | m5 | 1 | ds | Weighted CP (covariate shift) | 0.814 | 0.016 | ∞ | ∞ | 0.168 | 0.106 | 0.159 | 0.147 | -0.212 |
| corn | mp5 | m5 | 1 | pds | Gaussian TD (parametric) | 0.909 | 0.010 | 5.507 | 7.468 | 0.274 | 0.106 | 0.273 | 0.254 | -0.171 |
| corn | mp5 | m5 | 1 | pds | Leverage PI (classical) | 0.663 | 0.020 | 2.646 | 9.155 | 0.274 | 0.106 | 0.273 | 0.254 | -0.171 |
| corn | mp5 | m5 | 1 | pds | Naive CP (primary residuals) | 0.582 | 0.022 | 2.012 | 12.745 | 0.274 | 0.106 | 0.273 | 0.254 | -0.171 |
| corn | mp5 | m5 | 1 | pds | Pooled CP (k labelled) | 0.692 | 0.019 | 2.753 | 9.980 | 0.274 | 0.106 | 0.273 | 0.254 | -0.171 |
| corn | mp5 | m5 | 1 | pds | Target CP (k labelled) | 0.924 | 0.010 | 6.673 | 8.220 | 0.274 | 0.106 | 0.273 | 0.254 | -0.171 |
| corn | mp5 | m5 | 1 | pds | Target CP+ (k labelled) | 0.944 | 0.008 | 7.303 | 8.135 | 0.274 | 0.106 | 0.273 | 0.254 | -0.171 |
| corn | mp5 | m5 | 1 | pds | TD-CP signed (pre-registered) | 0.910 | 0.010 | 5.921 | 8.048 | 0.274 | 0.106 | 0.273 | 0.254 | -0.171 |
| corn | mp5 | m5 | 1 | pds | TD-CP absolute scores | 0.928 | 0.010 | 6.321 | 7.926 | 0.274 | 0.106 | 0.273 | 0.254 | -0.171 |
| corn | mp5 | m5 | 1 | pds | TD-CP+ (jackknife+) | 0.950 | 0.008 | 6.912 | 7.799 | 0.274 | 0.106 | 0.273 | 0.254 | -0.171 |
| corn | mp5 | m5 | 1 | pds | Weighted CP (covariate shift) | 0.738 | 0.017 | ∞ | ∞ | 0.274 | 0.106 | 0.273 | 0.254 | -0.171 |
| corn | mp5 | m5 | 2 | ds | Gaussian TD (parametric) | 0.880 | 0.013 | 3.184 | 4.698 | 0.425 | 0.164 | 0.454 | 0.396 | -0.168 |
| corn | mp5 | m5 | 2 | ds | Leverage PI (classical) | 0.602 | 0.018 | 1.297 | 5.665 | 0.425 | 0.164 | 0.454 | 0.396 | -0.168 |
| corn | mp5 | m5 | 2 | ds | Naive CP (primary residuals) | 0.522 | 0.017 | 1.047 | 6.759 | 0.425 | 0.164 | 0.454 | 0.396 | -0.168 |
| corn | mp5 | m5 | 2 | ds | Pooled CP (k labelled) | 0.661 | 0.019 | 1.520 | 5.571 | 0.425 | 0.164 | 0.454 | 0.396 | -0.168 |
| corn | mp5 | m5 | 2 | ds | Target CP (k labelled) | 0.907 | 0.012 | 3.751 | 4.944 | 0.425 | 0.164 | 0.454 | 0.396 | -0.168 |
| corn | mp5 | m5 | 2 | ds | Target CP+ (k labelled) | 0.930 | 0.009 | 4.345 | 5.054 | 0.425 | 0.164 | 0.454 | 0.396 | -0.168 |
| corn | mp5 | m5 | 2 | ds | TD-CP signed (pre-registered) | 0.888 | 0.012 | 3.373 | 4.849 | 0.425 | 0.164 | 0.454 | 0.396 | -0.168 |
| corn | mp5 | m5 | 2 | ds | TD-CP absolute scores | 0.900 | 0.013 | 3.579 | 4.890 | 0.425 | 0.164 | 0.454 | 0.396 | -0.168 |
| corn | mp5 | m5 | 2 | ds | TD-CP+ (jackknife+) | 0.929 | 0.009 | 4.119 | 4.817 | 0.425 | 0.164 | 0.454 | 0.396 | -0.168 |
| corn | mp5 | m5 | 2 | ds | Weighted CP (covariate shift) | 0.702 | 0.016 | ∞ | ∞ | 0.425 | 0.164 | 0.454 | 0.396 | -0.168 |
| corn | mp5 | m5 | 2 | pds | Gaussian TD (parametric) | 0.898 | 0.011 | 6.167 | 8.847 | 0.918 | 0.164 | 0.913 | 0.861 | -0.080 |
| corn | mp5 | m5 | 2 | pds | Leverage PI (classical) | 0.524 | 0.024 | 2.046 | 14.660 | 0.918 | 0.164 | 0.913 | 0.861 | -0.080 |
| corn | mp5 | m5 | 2 | pds | Naive CP (primary residuals) | 0.390 | 0.024 | 1.047 | 21.596 | 0.918 | 0.164 | 0.913 | 0.861 | -0.080 |
| corn | mp5 | m5 | 2 | pds | Pooled CP (k labelled) | 0.603 | 0.018 | 2.559 | 13.629 | 0.918 | 0.164 | 0.913 | 0.861 | -0.080 |
| corn | mp5 | m5 | 2 | pds | Target CP (k labelled) | 0.914 | 0.010 | 7.524 | 9.813 | 0.918 | 0.164 | 0.913 | 0.861 | -0.080 |
| corn | mp5 | m5 | 2 | pds | Target CP+ (k labelled) | 0.950 | 0.007 | 8.388 | 9.161 | 0.918 | 0.164 | 0.913 | 0.861 | -0.080 |
| corn | mp5 | m5 | 2 | pds | TD-CP signed (pre-registered) | 0.896 | 0.010 | 6.441 | 9.517 | 0.918 | 0.164 | 0.913 | 0.861 | -0.080 |
| corn | mp5 | m5 | 2 | pds | TD-CP absolute scores | 0.910 | 0.011 | 7.336 | 9.723 | 0.918 | 0.164 | 0.913 | 0.861 | -0.080 |
| corn | mp5 | m5 | 2 | pds | TD-CP+ (jackknife+) | 0.944 | 0.007 | 8.140 | 9.003 | 0.918 | 0.164 | 0.913 | 0.861 | -0.080 |
| corn | mp5 | m5 | 2 | pds | Weighted CP (covariate shift) | 0.685 | 0.017 | ∞ | ∞ | 0.918 | 0.164 | 0.913 | 0.861 | -0.080 |
| corn | mp5 | m5 | 3 | ds | Gaussian TD (parametric) | 0.875 | 0.014 | 3.893 | 5.755 | 0.869 | 0.405 | 0.877 | 0.775 | -0.125 |
| corn | mp5 | m5 | 3 | ds | Leverage PI (classical) | 0.647 | 0.017 | 1.924 | 6.155 | 0.869 | 0.405 | 0.877 | 0.775 | -0.125 |
| corn | mp5 | m5 | 3 | ds | Naive CP (primary residuals) | 0.590 | 0.017 | 1.645 | 7.285 | 0.869 | 0.405 | 0.877 | 0.775 | -0.125 |
| corn | mp5 | m5 | 3 | ds | Pooled CP (k labelled) | 0.699 | 0.019 | 2.111 | 6.345 | 0.869 | 0.405 | 0.877 | 0.775 | -0.125 |
| corn | mp5 | m5 | 3 | ds | Target CP (k labelled) | 0.887 | 0.015 | 4.490 | 6.212 | 0.869 | 0.405 | 0.877 | 0.775 | -0.125 |
| corn | mp5 | m5 | 3 | ds | Target CP+ (k labelled) | 0.914 | 0.014 | 5.127 | 6.252 | 0.869 | 0.405 | 0.877 | 0.775 | -0.125 |
| corn | mp5 | m5 | 3 | ds | TD-CP signed (pre-registered) | 0.879 | 0.013 | 4.141 | 5.880 | 0.869 | 0.405 | 0.877 | 0.775 | -0.125 |
| corn | mp5 | m5 | 3 | ds | TD-CP absolute scores | 0.887 | 0.014 | 4.296 | 5.952 | 0.869 | 0.405 | 0.877 | 0.775 | -0.125 |
| corn | mp5 | m5 | 3 | ds | TD-CP+ (jackknife+) | 0.922 | 0.012 | 4.897 | 5.800 | 0.869 | 0.405 | 0.877 | 0.775 | -0.125 |
| corn | mp5 | m5 | 3 | ds | Weighted CP (covariate shift) | 0.742 | 0.016 | ∞ | ∞ | 0.869 | 0.405 | 0.877 | 0.775 | -0.125 |
| corn | mp5 | m5 | 3 | pds | Gaussian TD (parametric) | 0.890 | 0.012 | 5.669 | 7.841 | 1.295 | 0.405 | 1.340 | 1.206 | -0.133 |
| corn | mp5 | m5 | 3 | pds | Leverage PI (classical) | 0.594 | 0.020 | 2.357 | 10.505 | 1.295 | 0.405 | 1.340 | 1.206 | -0.133 |
| corn | mp5 | m5 | 3 | pds | Naive CP (primary residuals) | 0.494 | 0.022 | 1.645 | 14.423 | 1.295 | 0.405 | 1.340 | 1.206 | -0.133 |
| corn | mp5 | m5 | 3 | pds | Pooled CP (k labelled) | 0.654 | 0.018 | 2.632 | 10.366 | 1.295 | 0.405 | 1.340 | 1.206 | -0.133 |
| corn | mp5 | m5 | 3 | pds | Target CP (k labelled) | 0.914 | 0.011 | 6.876 | 8.505 | 1.295 | 0.405 | 1.340 | 1.206 | -0.133 |
| corn | mp5 | m5 | 3 | pds | Target CP+ (k labelled) | 0.942 | 0.007 | 7.582 | 8.497 | 1.295 | 0.405 | 1.340 | 1.206 | -0.133 |
| corn | mp5 | m5 | 3 | pds | TD-CP signed (pre-registered) | 0.892 | 0.012 | 5.989 | 8.226 | 1.295 | 0.405 | 1.340 | 1.206 | -0.133 |
| corn | mp5 | m5 | 3 | pds | TD-CP absolute scores | 0.906 | 0.012 | 6.609 | 8.411 | 1.295 | 0.405 | 1.340 | 1.206 | -0.133 |
| corn | mp5 | m5 | 3 | pds | TD-CP+ (jackknife+) | 0.937 | 0.008 | 7.270 | 8.311 | 1.295 | 0.405 | 1.340 | 1.206 | -0.133 |
| corn | mp5 | m5 | 3 | pds | Weighted CP (covariate shift) | 0.718 | 0.015 | ∞ | ∞ | 1.295 | 0.405 | 1.340 | 1.206 | -0.133 |
| corn | mp5 | mp6 | 0 | ds | Gaussian TD (parametric) | 0.878 | 0.012 | 2.728 | 3.863 | 0.291 | 0.153 | 0.271 | 0.248 | -0.086 |
| corn | mp5 | mp6 | 0 | ds | Leverage PI (classical) | 0.709 | 0.012 | 1.560 | 3.967 | 0.291 | 0.153 | 0.271 | 0.248 | -0.086 |
| corn | mp5 | mp6 | 0 | ds | Naive CP (primary residuals) | 0.645 | 0.014 | 1.363 | 4.685 | 0.291 | 0.153 | 0.271 | 0.248 | -0.086 |
| corn | mp5 | mp6 | 0 | ds | Pooled CP (k labelled) | 0.733 | 0.015 | 1.714 | 4.149 | 0.291 | 0.153 | 0.271 | 0.248 | -0.086 |
| corn | mp5 | mp6 | 0 | ds | Target CP (k labelled) | 0.891 | 0.014 | 2.982 | 4.041 | 0.291 | 0.153 | 0.271 | 0.248 | -0.086 |
| corn | mp5 | mp6 | 0 | ds | Target CP+ (k labelled) | 0.927 | 0.012 | 3.496 | 4.001 | 0.291 | 0.153 | 0.271 | 0.248 | -0.086 |
| corn | mp5 | mp6 | 0 | ds | TD-CP signed (pre-registered) | 0.892 | 0.011 | 2.866 | 3.872 | 0.291 | 0.153 | 0.271 | 0.248 | -0.086 |
| corn | mp5 | mp6 | 0 | ds | TD-CP absolute scores | 0.889 | 0.012 | 2.827 | 3.831 | 0.291 | 0.153 | 0.271 | 0.248 | -0.086 |
| corn | mp5 | mp6 | 0 | ds | TD-CP+ (jackknife+) | 0.932 | 0.010 | 3.270 | 3.743 | 0.291 | 0.153 | 0.271 | 0.248 | -0.086 |
| corn | mp5 | mp6 | 0 | ds | Weighted CP (covariate shift) | 0.765 | 0.012 | ∞ | ∞ | 0.291 | 0.153 | 0.271 | 0.248 | -0.086 |
| corn | mp5 | mp6 | 0 | pds | Gaussian TD (parametric) | 0.915 | 0.010 | 2.860 | 3.639 | 0.286 | 0.153 | 0.288 | 0.246 | -0.130 |
| corn | mp5 | mp6 | 0 | pds | Leverage PI (classical) | 0.726 | 0.017 | 1.587 | 3.959 | 0.286 | 0.153 | 0.288 | 0.246 | -0.130 |
| corn | mp5 | mp6 | 0 | pds | Naive CP (primary residuals) | 0.668 | 0.019 | 1.363 | 4.841 | 0.286 | 0.153 | 0.288 | 0.246 | -0.130 |
| corn | mp5 | mp6 | 0 | pds | Pooled CP (k labelled) | 0.736 | 0.017 | 1.635 | 4.187 | 0.286 | 0.153 | 0.288 | 0.246 | -0.130 |
| corn | mp5 | mp6 | 0 | pds | Target CP (k labelled) | 0.912 | 0.011 | 3.419 | 4.065 | 0.286 | 0.153 | 0.288 | 0.246 | -0.130 |
| corn | mp5 | mp6 | 0 | pds | Target CP+ (k labelled) | 0.925 | 0.011 | 3.664 | 4.159 | 0.286 | 0.153 | 0.288 | 0.246 | -0.130 |
| corn | mp5 | mp6 | 0 | pds | TD-CP signed (pre-registered) | 0.929 | 0.009 | 3.152 | 3.843 | 0.286 | 0.153 | 0.288 | 0.246 | -0.130 |
| corn | mp5 | mp6 | 0 | pds | TD-CP absolute scores | 0.928 | 0.010 | 3.237 | 3.901 | 0.286 | 0.153 | 0.288 | 0.246 | -0.130 |
| corn | mp5 | mp6 | 0 | pds | TD-CP+ (jackknife+) | 0.932 | 0.009 | 3.450 | 3.962 | 0.286 | 0.153 | 0.288 | 0.246 | -0.130 |
| corn | mp5 | mp6 | 0 | pds | Weighted CP (covariate shift) | 0.773 | 0.014 | ∞ | ∞ | 0.286 | 0.153 | 0.288 | 0.246 | -0.130 |
| corn | mp5 | mp6 | 1 | ds | Gaussian TD (parametric) | 0.888 | 0.012 | 2.950 | 4.404 | 0.151 | 0.106 | 0.118 | 0.111 | -0.087 |
| corn | mp5 | mp6 | 1 | ds | Leverage PI (classical) | 0.830 | 0.015 | 2.225 | 4.093 | 0.151 | 0.106 | 0.118 | 0.111 | -0.087 |
| corn | mp5 | mp6 | 1 | ds | Naive CP (primary residuals) | 0.794 | 0.017 | 2.012 | 4.734 | 0.151 | 0.106 | 0.118 | 0.111 | -0.087 |
| corn | mp5 | mp6 | 1 | ds | Pooled CP (k labelled) | 0.825 | 0.015 | 2.189 | 4.516 | 0.151 | 0.106 | 0.118 | 0.111 | -0.087 |
| corn | mp5 | mp6 | 1 | ds | Target CP (k labelled) | 0.908 | 0.012 | 3.381 | 4.626 | 0.151 | 0.106 | 0.118 | 0.111 | -0.087 |
| corn | mp5 | mp6 | 1 | ds | Target CP+ (k labelled) | 0.923 | 0.011 | 3.719 | 4.437 | 0.151 | 0.106 | 0.118 | 0.111 | -0.087 |
| corn | mp5 | mp6 | 1 | ds | TD-CP signed (pre-registered) | 0.911 | 0.011 | 3.251 | 4.490 | 0.151 | 0.106 | 0.118 | 0.111 | -0.087 |
| corn | mp5 | mp6 | 1 | ds | TD-CP absolute scores | 0.903 | 0.011 | 3.151 | 4.455 | 0.151 | 0.106 | 0.118 | 0.111 | -0.087 |
| corn | mp5 | mp6 | 1 | ds | TD-CP+ (jackknife+) | 0.929 | 0.010 | 3.473 | 4.116 | 0.151 | 0.106 | 0.118 | 0.111 | -0.087 |
| corn | mp5 | mp6 | 1 | ds | Weighted CP (covariate shift) | 0.845 | 0.013 | ∞ | ∞ | 0.151 | 0.106 | 0.118 | 0.111 | -0.087 |
| corn | mp5 | mp6 | 1 | pds | Gaussian TD (parametric) | 0.895 | 0.007 | 2.858 | 3.964 | 0.148 | 0.106 | 0.107 | 0.091 | 0.026 |
| corn | mp5 | mp6 | 1 | pds | Leverage PI (classical) | 0.832 | 0.014 | 2.234 | 4.030 | 0.148 | 0.106 | 0.107 | 0.091 | 0.026 |
| corn | mp5 | mp6 | 1 | pds | Naive CP (primary residuals) | 0.791 | 0.017 | 2.012 | 4.720 | 0.148 | 0.106 | 0.107 | 0.091 | 0.026 |
| corn | mp5 | mp6 | 1 | pds | Pooled CP (k labelled) | 0.820 | 0.013 | 2.169 | 4.290 | 0.148 | 0.106 | 0.107 | 0.091 | 0.026 |
| corn | mp5 | mp6 | 1 | pds | Target CP (k labelled) | 0.904 | 0.009 | 3.371 | 4.378 | 0.148 | 0.106 | 0.107 | 0.091 | 0.026 |
| corn | mp5 | mp6 | 1 | pds | Target CP+ (k labelled) | 0.918 | 0.009 | 3.566 | 4.336 | 0.148 | 0.106 | 0.107 | 0.091 | 0.026 |
| corn | mp5 | mp6 | 1 | pds | TD-CP signed (pre-registered) | 0.916 | 0.007 | 3.228 | 4.157 | 0.148 | 0.106 | 0.107 | 0.091 | 0.026 |
| corn | mp5 | mp6 | 1 | pds | TD-CP absolute scores | 0.911 | 0.007 | 3.129 | 4.030 | 0.148 | 0.106 | 0.107 | 0.091 | 0.026 |
| corn | mp5 | mp6 | 1 | pds | TD-CP+ (jackknife+) | 0.927 | 0.006 | 3.259 | 3.924 | 0.148 | 0.106 | 0.107 | 0.091 | 0.026 |
| corn | mp5 | mp6 | 1 | pds | Weighted CP (covariate shift) | 0.835 | 0.013 | ∞ | ∞ | 0.148 | 0.106 | 0.107 | 0.091 | 0.026 |
| corn | mp5 | mp6 | 2 | ds | Gaussian TD (parametric) | 0.854 | 0.016 | 2.341 | 3.770 | 0.349 | 0.164 | 0.317 | 0.306 | -0.046 |
| corn | mp5 | mp6 | 2 | ds | Leverage PI (classical) | 0.645 | 0.015 | 1.248 | 4.155 | 0.349 | 0.164 | 0.317 | 0.306 | -0.046 |
| corn | mp5 | mp6 | 2 | ds | Naive CP (primary residuals) | 0.579 | 0.016 | 1.047 | 5.021 | 0.349 | 0.164 | 0.317 | 0.306 | -0.046 |
| corn | mp5 | mp6 | 2 | ds | Pooled CP (k labelled) | 0.686 | 0.017 | 1.350 | 4.365 | 0.349 | 0.164 | 0.317 | 0.306 | -0.046 |
| corn | mp5 | mp6 | 2 | ds | Target CP (k labelled) | 0.888 | 0.016 | 2.741 | 3.970 | 0.349 | 0.164 | 0.317 | 0.306 | -0.046 |
| corn | mp5 | mp6 | 2 | ds | Target CP+ (k labelled) | 0.923 | 0.012 | 3.178 | 3.863 | 0.349 | 0.164 | 0.317 | 0.306 | -0.046 |
| corn | mp5 | mp6 | 2 | ds | TD-CP signed (pre-registered) | 0.870 | 0.014 | 2.486 | 3.735 | 0.349 | 0.164 | 0.317 | 0.306 | -0.046 |
| corn | mp5 | mp6 | 2 | ds | TD-CP absolute scores | 0.868 | 0.016 | 2.505 | 3.825 | 0.349 | 0.164 | 0.317 | 0.306 | -0.046 |
| corn | mp5 | mp6 | 2 | ds | TD-CP+ (jackknife+) | 0.916 | 0.012 | 2.899 | 3.607 | 0.349 | 0.164 | 0.317 | 0.306 | -0.046 |
| corn | mp5 | mp6 | 2 | ds | Weighted CP (covariate shift) | 0.729 | 0.015 | ∞ | ∞ | 0.349 | 0.164 | 0.317 | 0.306 | -0.046 |
| corn | mp5 | mp6 | 2 | pds | Gaussian TD (parametric) | 0.889 | 0.009 | 2.320 | 3.196 | 0.342 | 0.164 | 0.306 | 0.280 | -0.021 |
| corn | mp5 | mp6 | 2 | pds | Leverage PI (classical) | 0.710 | 0.020 | 1.335 | 3.896 | 0.342 | 0.164 | 0.306 | 0.280 | -0.021 |
| corn | mp5 | mp6 | 2 | pds | Naive CP (primary residuals) | 0.628 | 0.023 | 1.047 | 5.182 | 0.342 | 0.164 | 0.306 | 0.280 | -0.021 |
| corn | mp5 | mp6 | 2 | pds | Pooled CP (k labelled) | 0.728 | 0.017 | 1.379 | 4.062 | 0.342 | 0.164 | 0.306 | 0.280 | -0.021 |
| corn | mp5 | mp6 | 2 | pds | Target CP (k labelled) | 0.916 | 0.010 | 2.906 | 3.491 | 0.342 | 0.164 | 0.306 | 0.280 | -0.021 |
| corn | mp5 | mp6 | 2 | pds | Target CP+ (k labelled) | 0.932 | 0.008 | 3.079 | 3.461 | 0.342 | 0.164 | 0.306 | 0.280 | -0.021 |
| corn | mp5 | mp6 | 2 | pds | TD-CP signed (pre-registered) | 0.896 | 0.010 | 2.525 | 3.374 | 0.342 | 0.164 | 0.306 | 0.280 | -0.021 |
| corn | mp5 | mp6 | 2 | pds | TD-CP absolute scores | 0.912 | 0.009 | 2.589 | 3.310 | 0.342 | 0.164 | 0.306 | 0.280 | -0.021 |
| corn | mp5 | mp6 | 2 | pds | TD-CP+ (jackknife+) | 0.926 | 0.007 | 2.795 | 3.220 | 0.342 | 0.164 | 0.306 | 0.280 | -0.021 |
| corn | mp5 | mp6 | 2 | pds | Weighted CP (covariate shift) | 0.747 | 0.016 | ∞ | ∞ | 0.342 | 0.164 | 0.306 | 0.280 | -0.021 |
| corn | mp5 | mp6 | 3 | ds | Gaussian TD (parametric) | 0.876 | 0.013 | 3.295 | 4.755 | 0.747 | 0.405 | 0.710 | 0.635 | -0.086 |
| corn | mp5 | mp6 | 3 | ds | Leverage PI (classical) | 0.711 | 0.015 | 1.854 | 4.893 | 0.747 | 0.405 | 0.710 | 0.635 | -0.086 |
| corn | mp5 | mp6 | 3 | ds | Naive CP (primary residuals) | 0.664 | 0.017 | 1.645 | 5.648 | 0.747 | 0.405 | 0.710 | 0.635 | -0.086 |
| corn | mp5 | mp6 | 3 | ds | Pooled CP (k labelled) | 0.748 | 0.017 | 2.050 | 5.056 | 0.747 | 0.405 | 0.710 | 0.635 | -0.086 |
| corn | mp5 | mp6 | 3 | ds | Target CP (k labelled) | 0.904 | 0.013 | 3.770 | 4.920 | 0.747 | 0.405 | 0.710 | 0.635 | -0.086 |
| corn | mp5 | mp6 | 3 | ds | Target CP+ (k labelled) | 0.935 | 0.009 | 4.339 | 4.982 | 0.747 | 0.405 | 0.710 | 0.635 | -0.086 |
| corn | mp5 | mp6 | 3 | ds | TD-CP signed (pre-registered) | 0.896 | 0.011 | 3.492 | 4.736 | 0.747 | 0.405 | 0.710 | 0.635 | -0.086 |
| corn | mp5 | mp6 | 3 | ds | TD-CP absolute scores | 0.891 | 0.012 | 3.502 | 4.797 | 0.747 | 0.405 | 0.710 | 0.635 | -0.086 |
| corn | mp5 | mp6 | 3 | ds | TD-CP+ (jackknife+) | 0.925 | 0.010 | 4.005 | 4.743 | 0.747 | 0.405 | 0.710 | 0.635 | -0.086 |
| corn | mp5 | mp6 | 3 | ds | Weighted CP (covariate shift) | 0.757 | 0.013 | ∞ | ∞ | 0.747 | 0.405 | 0.710 | 0.635 | -0.086 |
| corn | mp5 | mp6 | 3 | pds | Gaussian TD (parametric) | 0.898 | 0.009 | 2.898 | 3.884 | 0.656 | 0.405 | 0.574 | 0.462 | -0.039 |
| corn | mp5 | mp6 | 3 | pds | Leverage PI (classical) | 0.792 | 0.015 | 1.904 | 4.033 | 0.656 | 0.405 | 0.574 | 0.462 | -0.039 |
| corn | mp5 | mp6 | 3 | pds | Naive CP (primary residuals) | 0.746 | 0.017 | 1.645 | 4.914 | 0.656 | 0.405 | 0.574 | 0.462 | -0.039 |
| corn | mp5 | mp6 | 3 | pds | Pooled CP (k labelled) | 0.799 | 0.013 | 1.940 | 4.137 | 0.656 | 0.405 | 0.574 | 0.462 | -0.039 |
| corn | mp5 | mp6 | 3 | pds | Target CP (k labelled) | 0.916 | 0.010 | 3.605 | 4.334 | 0.656 | 0.405 | 0.574 | 0.462 | -0.039 |
| corn | mp5 | mp6 | 3 | pds | Target CP+ (k labelled) | 0.934 | 0.008 | 3.810 | 4.342 | 0.656 | 0.405 | 0.574 | 0.462 | -0.039 |
| corn | mp5 | mp6 | 3 | pds | TD-CP signed (pre-registered) | 0.916 | 0.008 | 3.179 | 4.073 | 0.656 | 0.405 | 0.574 | 0.462 | -0.039 |
| corn | mp5 | mp6 | 3 | pds | TD-CP absolute scores | 0.915 | 0.008 | 3.315 | 4.113 | 0.656 | 0.405 | 0.574 | 0.462 | -0.039 |
| corn | mp5 | mp6 | 3 | pds | TD-CP+ (jackknife+) | 0.933 | 0.007 | 3.488 | 4.062 | 0.656 | 0.405 | 0.574 | 0.462 | -0.039 |
| corn | mp5 | mp6 | 3 | pds | Weighted CP (covariate shift) | 0.824 | 0.013 | ∞ | ∞ | 0.656 | 0.405 | 0.574 | 0.462 | -0.039 |
| corn | mp6 | m5 | 0 | ds | Gaussian TD (parametric) | 0.901 | 0.012 | 2.949 | 4.002 | 0.292 | 0.169 | 0.293 | 0.294 | -0.401 |
| corn | mp6 | m5 | 0 | ds | Leverage PI (classical) | 0.795 | 0.016 | 1.846 | 3.608 | 0.292 | 0.169 | 0.293 | 0.294 | -0.401 |
| corn | mp6 | m5 | 0 | ds | Naive CP (primary residuals) | 0.698 | 0.019 | 1.463 | 4.807 | 0.292 | 0.169 | 0.293 | 0.294 | -0.401 |
| corn | mp6 | m5 | 0 | ds | Pooled CP (k labelled) | 0.759 | 0.015 | 1.709 | 4.271 | 0.292 | 0.169 | 0.293 | 0.294 | -0.401 |
| corn | mp6 | m5 | 0 | ds | Target CP (k labelled) | 0.892 | 0.014 | 3.205 | 4.358 | 0.292 | 0.169 | 0.293 | 0.294 | -0.401 |
| corn | mp6 | m5 | 0 | ds | Target CP+ (k labelled) | 0.936 | 0.011 | 3.653 | 4.077 | 0.292 | 0.169 | 0.293 | 0.294 | -0.401 |
| corn | mp6 | m5 | 0 | ds | TD-CP signed (pre-registered) | 0.916 | 0.010 | 3.109 | 4.063 | 0.292 | 0.169 | 0.293 | 0.294 | -0.401 |
| corn | mp6 | m5 | 0 | ds | TD-CP absolute scores | 0.910 | 0.011 | 3.126 | 4.097 | 0.292 | 0.169 | 0.293 | 0.294 | -0.401 |
| corn | mp6 | m5 | 0 | ds | TD-CP+ (jackknife+) | 0.959 | 0.007 | 3.560 | 3.844 | 0.292 | 0.169 | 0.293 | 0.294 | -0.401 |
| corn | mp6 | m5 | 0 | ds | Weighted CP (covariate shift) | 0.835 | 0.014 | ∞ | ∞ | 0.292 | 0.169 | 0.293 | 0.294 | -0.401 |
| corn | mp6 | m5 | 0 | pds | Gaussian TD (parametric) | 0.906 | 0.012 | 8.156 | 11.476 | 0.847 | 0.169 | 0.926 | 0.831 | -0.243 |
| corn | mp6 | m5 | 0 | pds | Leverage PI (classical) | 0.478 | 0.018 | 2.629 | 16.371 | 0.847 | 0.169 | 0.926 | 0.831 | -0.243 |
| corn | mp6 | m5 | 0 | pds | Naive CP (primary residuals) | 0.339 | 0.020 | 1.463 | 24.068 | 0.847 | 0.169 | 0.926 | 0.831 | -0.243 |
| corn | mp6 | m5 | 0 | pds | Pooled CP (k labelled) | 0.598 | 0.019 | 3.375 | 15.665 | 0.847 | 0.169 | 0.926 | 0.831 | -0.243 |
| corn | mp6 | m5 | 0 | pds | Target CP (k labelled) | 0.917 | 0.011 | 9.778 | 12.657 | 0.847 | 0.169 | 0.926 | 0.831 | -0.243 |
| corn | mp6 | m5 | 0 | pds | Target CP+ (k labelled) | 0.942 | 0.011 | 10.948 | 12.547 | 0.847 | 0.169 | 0.926 | 0.831 | -0.243 |
| corn | mp6 | m5 | 0 | pds | TD-CP signed (pre-registered) | 0.894 | 0.013 | 8.463 | 12.184 | 0.847 | 0.169 | 0.926 | 0.831 | -0.243 |
| corn | mp6 | m5 | 0 | pds | TD-CP absolute scores | 0.918 | 0.012 | 9.560 | 12.454 | 0.847 | 0.169 | 0.926 | 0.831 | -0.243 |
| corn | mp6 | m5 | 0 | pds | TD-CP+ (jackknife+) | 0.947 | 0.010 | 10.663 | 12.336 | 0.847 | 0.169 | 0.926 | 0.831 | -0.243 |
| corn | mp6 | m5 | 0 | pds | Weighted CP (covariate shift) | 0.647 | 0.018 | ∞ | ∞ | 0.847 | 0.169 | 0.926 | 0.831 | -0.243 |
| corn | mp6 | m5 | 1 | ds | Gaussian TD (parametric) | 0.869 | 0.015 | 3.761 | 5.955 | 0.195 | 0.108 | 0.171 | 0.177 | -0.217 |
| corn | mp6 | m5 | 1 | ds | Leverage PI (classical) | 0.745 | 0.017 | 2.370 | 5.715 | 0.195 | 0.108 | 0.171 | 0.177 | -0.217 |
| corn | mp6 | m5 | 1 | ds | Naive CP (primary residuals) | 0.668 | 0.020 | 1.971 | 7.281 | 0.195 | 0.108 | 0.171 | 0.177 | -0.217 |
| corn | mp6 | m5 | 1 | ds | Pooled CP (k labelled) | 0.732 | 0.019 | 2.342 | 6.540 | 0.195 | 0.108 | 0.171 | 0.177 | -0.217 |
| corn | mp6 | m5 | 1 | ds | Target CP (k labelled) | 0.874 | 0.016 | 4.105 | 6.194 | 0.195 | 0.108 | 0.171 | 0.177 | -0.217 |
| corn | mp6 | m5 | 1 | ds | Target CP+ (k labelled) | 0.910 | 0.013 | 4.642 | 5.777 | 0.195 | 0.108 | 0.171 | 0.177 | -0.217 |
| corn | mp6 | m5 | 1 | ds | TD-CP signed (pre-registered) | 0.885 | 0.013 | 4.043 | 6.014 | 0.195 | 0.108 | 0.171 | 0.177 | -0.217 |
| corn | mp6 | m5 | 1 | ds | TD-CP absolute scores | 0.880 | 0.014 | 3.995 | 5.989 | 0.195 | 0.108 | 0.171 | 0.177 | -0.217 |
| corn | mp6 | m5 | 1 | ds | TD-CP+ (jackknife+) | 0.919 | 0.011 | 4.513 | 5.456 | 0.195 | 0.108 | 0.171 | 0.177 | -0.217 |
| corn | mp6 | m5 | 1 | ds | Weighted CP (covariate shift) | 0.779 | 0.015 | ∞ | ∞ | 0.195 | 0.108 | 0.171 | 0.177 | -0.217 |
| corn | mp6 | m5 | 1 | pds | Gaussian TD (parametric) | 0.895 | 0.011 | 7.527 | 11.885 | 0.413 | 0.108 | 0.387 | 0.383 | -0.134 |
| corn | mp6 | m5 | 1 | pds | Leverage PI (classical) | 0.577 | 0.023 | 3.068 | 15.676 | 0.413 | 0.108 | 0.387 | 0.383 | -0.134 |
| corn | mp6 | m5 | 1 | pds | Naive CP (primary residuals) | 0.467 | 0.025 | 1.971 | 22.957 | 0.413 | 0.108 | 0.387 | 0.383 | -0.134 |
| corn | mp6 | m5 | 1 | pds | Pooled CP (k labelled) | 0.623 | 0.020 | 3.261 | 16.822 | 0.413 | 0.108 | 0.387 | 0.383 | -0.134 |
| corn | mp6 | m5 | 1 | pds | Target CP (k labelled) | 0.930 | 0.009 | 9.654 | 12.855 | 0.413 | 0.108 | 0.387 | 0.383 | -0.134 |
| corn | mp6 | m5 | 1 | pds | Target CP+ (k labelled) | 0.939 | 0.008 | 10.457 | 12.752 | 0.413 | 0.108 | 0.387 | 0.383 | -0.134 |
| corn | mp6 | m5 | 1 | pds | TD-CP signed (pre-registered) | 0.890 | 0.011 | 8.047 | 12.911 | 0.413 | 0.108 | 0.387 | 0.383 | -0.134 |
| corn | mp6 | m5 | 1 | pds | TD-CP absolute scores | 0.922 | 0.010 | 9.170 | 12.724 | 0.413 | 0.108 | 0.387 | 0.383 | -0.134 |
| corn | mp6 | m5 | 1 | pds | TD-CP+ (jackknife+) | 0.940 | 0.008 | 10.032 | 12.454 | 0.413 | 0.108 | 0.387 | 0.383 | -0.134 |
| corn | mp6 | m5 | 1 | pds | Weighted CP (covariate shift) | 0.691 | 0.019 | ∞ | ∞ | 0.413 | 0.108 | 0.387 | 0.383 | -0.134 |
| corn | mp6 | m5 | 2 | ds | Gaussian TD (parametric) | 0.872 | 0.015 | 3.146 | 4.780 | 0.425 | 0.160 | 0.447 | 0.392 | -0.152 |
| corn | mp6 | m5 | 2 | ds | Leverage PI (classical) | 0.602 | 0.016 | 1.315 | 5.595 | 0.425 | 0.160 | 0.447 | 0.392 | -0.152 |
| corn | mp6 | m5 | 2 | ds | Naive CP (primary residuals) | 0.526 | 0.016 | 1.056 | 6.697 | 0.425 | 0.160 | 0.447 | 0.392 | -0.152 |
| corn | mp6 | m5 | 2 | ds | Pooled CP (k labelled) | 0.668 | 0.018 | 1.528 | 5.529 | 0.425 | 0.160 | 0.447 | 0.392 | -0.152 |
| corn | mp6 | m5 | 2 | ds | Target CP (k labelled) | 0.907 | 0.013 | 3.697 | 5.005 | 0.425 | 0.160 | 0.447 | 0.392 | -0.152 |
| corn | mp6 | m5 | 2 | ds | Target CP+ (k labelled) | 0.925 | 0.011 | 4.263 | 4.963 | 0.425 | 0.160 | 0.447 | 0.392 | -0.152 |
| corn | mp6 | m5 | 2 | ds | TD-CP signed (pre-registered) | 0.877 | 0.014 | 3.320 | 4.900 | 0.425 | 0.160 | 0.447 | 0.392 | -0.152 |
| corn | mp6 | m5 | 2 | ds | TD-CP absolute scores | 0.890 | 0.014 | 3.497 | 4.948 | 0.425 | 0.160 | 0.447 | 0.392 | -0.152 |
| corn | mp6 | m5 | 2 | ds | TD-CP+ (jackknife+) | 0.922 | 0.012 | 4.033 | 4.729 | 0.425 | 0.160 | 0.447 | 0.392 | -0.152 |
| corn | mp6 | m5 | 2 | ds | Weighted CP (covariate shift) | 0.704 | 0.015 | ∞ | ∞ | 0.425 | 0.160 | 0.447 | 0.392 | -0.152 |
| corn | mp6 | m5 | 2 | pds | Gaussian TD (parametric) | 0.882 | 0.010 | 4.758 | 7.225 | 0.742 | 0.160 | 0.698 | 0.682 | -0.044 |
| corn | mp6 | m5 | 2 | pds | Leverage PI (classical) | 0.514 | 0.020 | 1.814 | 11.015 | 0.742 | 0.160 | 0.698 | 0.682 | -0.044 |
| corn | mp6 | m5 | 2 | pds | Naive CP (primary residuals) | 0.394 | 0.021 | 1.056 | 15.915 | 0.742 | 0.160 | 0.698 | 0.682 | -0.044 |
| corn | mp6 | m5 | 2 | pds | Pooled CP (k labelled) | 0.585 | 0.017 | 2.049 | 11.107 | 0.742 | 0.160 | 0.698 | 0.682 | -0.044 |
| corn | mp6 | m5 | 2 | pds | Target CP (k labelled) | 0.907 | 0.010 | 5.867 | 7.753 | 0.742 | 0.160 | 0.698 | 0.682 | -0.044 |
| corn | mp6 | m5 | 2 | pds | Target CP+ (k labelled) | 0.941 | 0.007 | 6.489 | 7.310 | 0.742 | 0.160 | 0.698 | 0.682 | -0.044 |
| corn | mp6 | m5 | 2 | pds | TD-CP signed (pre-registered) | 0.876 | 0.011 | 4.999 | 7.499 | 0.742 | 0.160 | 0.698 | 0.682 | -0.044 |
| corn | mp6 | m5 | 2 | pds | TD-CP absolute scores | 0.897 | 0.010 | 5.531 | 7.571 | 0.742 | 0.160 | 0.698 | 0.682 | -0.044 |
| corn | mp6 | m5 | 2 | pds | TD-CP+ (jackknife+) | 0.931 | 0.008 | 6.168 | 7.067 | 0.742 | 0.160 | 0.698 | 0.682 | -0.044 |
| corn | mp6 | m5 | 2 | pds | Weighted CP (covariate shift) | 0.680 | 0.016 | ∞ | ∞ | 0.742 | 0.160 | 0.698 | 0.682 | -0.044 |
| corn | mp6 | m5 | 3 | ds | Gaussian TD (parametric) | 0.881 | 0.014 | 3.938 | 5.559 | 0.854 | 0.375 | 0.894 | 0.772 | -0.121 |
| corn | mp6 | m5 | 3 | ds | Leverage PI (classical) | 0.656 | 0.016 | 1.898 | 6.096 | 0.854 | 0.375 | 0.894 | 0.772 | -0.121 |
| corn | mp6 | m5 | 3 | ds | Naive CP (primary residuals) | 0.592 | 0.016 | 1.586 | 7.252 | 0.854 | 0.375 | 0.894 | 0.772 | -0.121 |
| corn | mp6 | m5 | 3 | ds | Pooled CP (k labelled) | 0.706 | 0.017 | 2.098 | 6.184 | 0.854 | 0.375 | 0.894 | 0.772 | -0.121 |
| corn | mp6 | m5 | 3 | ds | Target CP (k labelled) | 0.888 | 0.015 | 4.651 | 6.198 | 0.854 | 0.375 | 0.894 | 0.772 | -0.121 |
| corn | mp6 | m5 | 3 | ds | Target CP+ (k labelled) | 0.923 | 0.012 | 5.297 | 6.156 | 0.854 | 0.375 | 0.894 | 0.772 | -0.121 |
| corn | mp6 | m5 | 3 | ds | TD-CP signed (pre-registered) | 0.888 | 0.012 | 4.185 | 5.689 | 0.854 | 0.375 | 0.894 | 0.772 | -0.121 |
| corn | mp6 | m5 | 3 | ds | TD-CP absolute scores | 0.896 | 0.013 | 4.305 | 5.776 | 0.854 | 0.375 | 0.894 | 0.772 | -0.121 |
| corn | mp6 | m5 | 3 | ds | TD-CP+ (jackknife+) | 0.934 | 0.010 | 4.973 | 5.654 | 0.854 | 0.375 | 0.894 | 0.772 | -0.121 |
| corn | mp6 | m5 | 3 | ds | Weighted CP (covariate shift) | 0.729 | 0.014 | ∞ | ∞ | 0.854 | 0.375 | 0.894 | 0.772 | -0.121 |
| corn | mp6 | m5 | 3 | pds | Gaussian TD (parametric) | 0.900 | 0.010 | 5.331 | 7.328 | 1.272 | 0.375 | 1.258 | 1.163 | -0.126 |
| corn | mp6 | m5 | 3 | pds | Leverage PI (classical) | 0.594 | 0.019 | 2.245 | 10.684 | 1.272 | 0.375 | 1.258 | 1.163 | -0.126 |
| corn | mp6 | m5 | 3 | pds | Naive CP (primary residuals) | 0.490 | 0.020 | 1.586 | 14.158 | 1.272 | 0.375 | 1.258 | 1.163 | -0.126 |
| corn | mp6 | m5 | 3 | pds | Pooled CP (k labelled) | 0.653 | 0.017 | 2.574 | 10.223 | 1.272 | 0.375 | 1.258 | 1.163 | -0.126 |
| corn | mp6 | m5 | 3 | pds | Target CP (k labelled) | 0.917 | 0.010 | 6.305 | 7.938 | 1.272 | 0.375 | 1.258 | 1.163 | -0.126 |
| corn | mp6 | m5 | 3 | pds | Target CP+ (k labelled) | 0.942 | 0.008 | 6.992 | 7.864 | 1.272 | 0.375 | 1.258 | 1.163 | -0.126 |
| corn | mp6 | m5 | 3 | pds | TD-CP signed (pre-registered) | 0.892 | 0.010 | 5.582 | 7.929 | 1.272 | 0.375 | 1.258 | 1.163 | -0.126 |
| corn | mp6 | m5 | 3 | pds | TD-CP absolute scores | 0.913 | 0.010 | 6.078 | 7.805 | 1.272 | 0.375 | 1.258 | 1.163 | -0.126 |
| corn | mp6 | m5 | 3 | pds | TD-CP+ (jackknife+) | 0.945 | 0.007 | 6.766 | 7.608 | 1.272 | 0.375 | 1.258 | 1.163 | -0.126 |
| corn | mp6 | m5 | 3 | pds | Weighted CP (covariate shift) | 0.704 | 0.015 | ∞ | ∞ | 1.272 | 0.375 | 1.258 | 1.163 | -0.126 |
| corn | mp6 | mp5 | 0 | ds | Gaussian TD (parametric) | 0.870 | 0.013 | 2.985 | 4.573 | 0.322 | 0.169 | 0.298 | 0.280 | -0.154 |
| corn | mp6 | mp5 | 0 | ds | Leverage PI (classical) | 0.734 | 0.016 | 1.748 | 4.583 | 0.322 | 0.169 | 0.298 | 0.280 | -0.154 |
| corn | mp6 | mp5 | 0 | ds | Naive CP (primary residuals) | 0.666 | 0.017 | 1.463 | 5.536 | 0.322 | 0.169 | 0.298 | 0.280 | -0.154 |
| corn | mp6 | mp5 | 0 | ds | Pooled CP (k labelled) | 0.737 | 0.017 | 1.774 | 5.030 | 0.322 | 0.169 | 0.298 | 0.280 | -0.154 |
| corn | mp6 | mp5 | 0 | ds | Target CP (k labelled) | 0.871 | 0.016 | 3.364 | 4.863 | 0.322 | 0.169 | 0.298 | 0.280 | -0.154 |
| corn | mp6 | mp5 | 0 | ds | Target CP+ (k labelled) | 0.921 | 0.012 | 3.881 | 4.616 | 0.322 | 0.169 | 0.298 | 0.280 | -0.154 |
| corn | mp6 | mp5 | 0 | ds | TD-CP signed (pre-registered) | 0.879 | 0.012 | 3.173 | 4.662 | 0.322 | 0.169 | 0.298 | 0.280 | -0.154 |
| corn | mp6 | mp5 | 0 | ds | TD-CP absolute scores | 0.883 | 0.012 | 3.209 | 4.537 | 0.322 | 0.169 | 0.298 | 0.280 | -0.154 |
| corn | mp6 | mp5 | 0 | ds | TD-CP+ (jackknife+) | 0.933 | 0.009 | 3.672 | 4.282 | 0.322 | 0.169 | 0.298 | 0.280 | -0.154 |
| corn | mp6 | mp5 | 0 | ds | Weighted CP (covariate shift) | 0.793 | 0.014 | ∞ | ∞ | 0.322 | 0.169 | 0.298 | 0.280 | -0.154 |
| corn | mp6 | mp5 | 0 | pds | Gaussian TD (parametric) | 0.908 | 0.009 | 3.302 | 4.358 | 0.334 | 0.169 | 0.334 | 0.283 | -0.100 |
| corn | mp6 | mp5 | 0 | pds | Leverage PI (classical) | 0.755 | 0.018 | 1.838 | 4.514 | 0.334 | 0.169 | 0.334 | 0.283 | -0.100 |
| corn | mp6 | mp5 | 0 | pds | Naive CP (primary residuals) | 0.671 | 0.022 | 1.463 | 6.258 | 0.334 | 0.169 | 0.334 | 0.283 | -0.100 |
| corn | mp6 | mp5 | 0 | pds | Pooled CP (k labelled) | 0.750 | 0.016 | 1.815 | 5.110 | 0.334 | 0.169 | 0.334 | 0.283 | -0.100 |
| corn | mp6 | mp5 | 0 | pds | Target CP (k labelled) | 0.920 | 0.011 | 3.988 | 4.950 | 0.334 | 0.169 | 0.334 | 0.283 | -0.100 |
| corn | mp6 | mp5 | 0 | pds | Target CP+ (k labelled) | 0.932 | 0.010 | 4.288 | 4.953 | 0.334 | 0.169 | 0.334 | 0.283 | -0.100 |
| corn | mp6 | mp5 | 0 | pds | TD-CP signed (pre-registered) | 0.913 | 0.009 | 3.576 | 4.645 | 0.334 | 0.169 | 0.334 | 0.283 | -0.100 |
| corn | mp6 | mp5 | 0 | pds | TD-CP absolute scores | 0.926 | 0.008 | 3.749 | 4.644 | 0.334 | 0.169 | 0.334 | 0.283 | -0.100 |
| corn | mp6 | mp5 | 0 | pds | TD-CP+ (jackknife+) | 0.934 | 0.009 | 4.043 | 4.729 | 0.334 | 0.169 | 0.334 | 0.283 | -0.100 |
| corn | mp6 | mp5 | 0 | pds | Weighted CP (covariate shift) | 0.808 | 0.014 | ∞ | ∞ | 0.334 | 0.169 | 0.334 | 0.283 | -0.100 |
| corn | mp6 | mp5 | 1 | ds | Gaussian TD (parametric) | 0.895 | 0.011 | 3.297 | 4.645 | 0.161 | 0.108 | 0.143 | 0.126 | -0.112 |
| corn | mp6 | mp5 | 1 | ds | Leverage PI (classical) | 0.815 | 0.013 | 2.271 | 4.254 | 0.161 | 0.108 | 0.143 | 0.126 | -0.112 |
| corn | mp6 | mp5 | 1 | ds | Naive CP (primary residuals) | 0.750 | 0.016 | 1.971 | 5.088 | 0.161 | 0.108 | 0.143 | 0.126 | -0.112 |
| corn | mp6 | mp5 | 1 | ds | Pooled CP (k labelled) | 0.800 | 0.014 | 2.196 | 4.795 | 0.161 | 0.108 | 0.143 | 0.126 | -0.112 |
| corn | mp6 | mp5 | 1 | ds | Target CP (k labelled) | 0.895 | 0.012 | 3.563 | 4.925 | 0.161 | 0.108 | 0.143 | 0.126 | -0.112 |
| corn | mp6 | mp5 | 1 | ds | Target CP+ (k labelled) | 0.921 | 0.011 | 4.092 | 4.886 | 0.161 | 0.108 | 0.143 | 0.126 | -0.112 |
| corn | mp6 | mp5 | 1 | ds | TD-CP signed (pre-registered) | 0.918 | 0.010 | 3.619 | 4.765 | 0.161 | 0.108 | 0.143 | 0.126 | -0.112 |
| corn | mp6 | mp5 | 1 | ds | TD-CP absolute scores | 0.905 | 0.011 | 3.521 | 4.721 | 0.161 | 0.108 | 0.143 | 0.126 | -0.112 |
| corn | mp6 | mp5 | 1 | ds | TD-CP+ (jackknife+) | 0.934 | 0.010 | 4.007 | 4.709 | 0.161 | 0.108 | 0.143 | 0.126 | -0.112 |
| corn | mp6 | mp5 | 1 | ds | Weighted CP (covariate shift) | 0.835 | 0.013 | ∞ | ∞ | 0.161 | 0.108 | 0.143 | 0.126 | -0.112 |
| corn | mp6 | mp5 | 1 | pds | Gaussian TD (parametric) | 0.910 | 0.008 | 3.493 | 4.765 | 0.171 | 0.108 | 0.149 | 0.128 | -0.101 |
| corn | mp6 | mp5 | 1 | pds | Leverage PI (classical) | 0.813 | 0.015 | 2.291 | 4.628 | 0.171 | 0.108 | 0.149 | 0.128 | -0.101 |
| corn | mp6 | mp5 | 1 | pds | Naive CP (primary residuals) | 0.763 | 0.018 | 1.971 | 5.812 | 0.171 | 0.108 | 0.149 | 0.128 | -0.101 |
| corn | mp6 | mp5 | 1 | pds | Pooled CP (k labelled) | 0.813 | 0.013 | 2.249 | 5.144 | 0.171 | 0.108 | 0.149 | 0.128 | -0.101 |
| corn | mp6 | mp5 | 1 | pds | Target CP (k labelled) | 0.926 | 0.010 | 4.494 | 5.523 | 0.171 | 0.108 | 0.149 | 0.128 | -0.101 |
| corn | mp6 | mp5 | 1 | pds | Target CP+ (k labelled) | 0.929 | 0.009 | 4.729 | 5.593 | 0.171 | 0.108 | 0.149 | 0.128 | -0.101 |
| corn | mp6 | mp5 | 1 | pds | TD-CP signed (pre-registered) | 0.930 | 0.007 | 3.854 | 5.030 | 0.171 | 0.108 | 0.149 | 0.128 | -0.101 |
| corn | mp6 | mp5 | 1 | pds | TD-CP absolute scores | 0.924 | 0.007 | 4.001 | 5.105 | 0.171 | 0.108 | 0.149 | 0.128 | -0.101 |
| corn | mp6 | mp5 | 1 | pds | TD-CP+ (jackknife+) | 0.933 | 0.007 | 4.251 | 5.065 | 0.171 | 0.108 | 0.149 | 0.128 | -0.101 |
| corn | mp6 | mp5 | 1 | pds | Weighted CP (covariate shift) | 0.819 | 0.013 | ∞ | ∞ | 0.171 | 0.108 | 0.149 | 0.128 | -0.101 |
| corn | mp6 | mp5 | 2 | ds | Gaussian TD (parametric) | 0.880 | 0.013 | 2.444 | 3.608 | 0.336 | 0.160 | 0.332 | 0.299 | -0.094 |
| corn | mp6 | mp5 | 2 | ds | Leverage PI (classical) | 0.686 | 0.015 | 1.268 | 3.850 | 0.336 | 0.160 | 0.332 | 0.299 | -0.094 |
| corn | mp6 | mp5 | 2 | ds | Naive CP (primary residuals) | 0.610 | 0.017 | 1.056 | 4.628 | 0.336 | 0.160 | 0.332 | 0.299 | -0.094 |
| corn | mp6 | mp5 | 2 | ds | Pooled CP (k labelled) | 0.706 | 0.017 | 1.345 | 4.062 | 0.336 | 0.160 | 0.332 | 0.299 | -0.094 |
| corn | mp6 | mp5 | 2 | ds | Target CP (k labelled) | 0.904 | 0.013 | 2.917 | 3.875 | 0.336 | 0.160 | 0.332 | 0.299 | -0.094 |
| corn | mp6 | mp5 | 2 | ds | Target CP+ (k labelled) | 0.926 | 0.010 | 3.356 | 3.910 | 0.336 | 0.160 | 0.332 | 0.299 | -0.094 |
| corn | mp6 | mp5 | 2 | ds | TD-CP signed (pre-registered) | 0.892 | 0.012 | 2.599 | 3.659 | 0.336 | 0.160 | 0.332 | 0.299 | -0.094 |
| corn | mp6 | mp5 | 2 | ds | TD-CP absolute scores | 0.894 | 0.013 | 2.665 | 3.707 | 0.336 | 0.160 | 0.332 | 0.299 | -0.094 |
| corn | mp6 | mp5 | 2 | ds | TD-CP+ (jackknife+) | 0.920 | 0.011 | 3.082 | 3.701 | 0.336 | 0.160 | 0.332 | 0.299 | -0.094 |
| corn | mp6 | mp5 | 2 | ds | Weighted CP (covariate shift) | 0.724 | 0.015 | ∞ | ∞ | 0.336 | 0.160 | 0.332 | 0.299 | -0.094 |
| corn | mp6 | mp5 | 2 | pds | Gaussian TD (parametric) | 0.897 | 0.010 | 2.053 | 2.703 | 0.290 | 0.160 | 0.260 | 0.236 | -0.060 |
| corn | mp6 | mp5 | 2 | pds | Leverage PI (classical) | 0.765 | 0.017 | 1.308 | 2.889 | 0.290 | 0.160 | 0.260 | 0.236 | -0.060 |
| corn | mp6 | mp5 | 2 | pds | Naive CP (primary residuals) | 0.682 | 0.021 | 1.056 | 3.858 | 0.290 | 0.160 | 0.260 | 0.236 | -0.060 |
| corn | mp6 | mp5 | 2 | pds | Pooled CP (k labelled) | 0.753 | 0.016 | 1.268 | 3.177 | 0.290 | 0.160 | 0.260 | 0.236 | -0.060 |
| corn | mp6 | mp5 | 2 | pds | Target CP (k labelled) | 0.908 | 0.013 | 2.509 | 3.075 | 0.290 | 0.160 | 0.260 | 0.236 | -0.060 |
| corn | mp6 | mp5 | 2 | pds | Target CP+ (k labelled) | 0.925 | 0.011 | 2.703 | 3.084 | 0.290 | 0.160 | 0.260 | 0.236 | -0.060 |
| corn | mp6 | mp5 | 2 | pds | TD-CP signed (pre-registered) | 0.912 | 0.009 | 2.232 | 2.795 | 0.290 | 0.160 | 0.260 | 0.236 | -0.060 |
| corn | mp6 | mp5 | 2 | pds | TD-CP absolute scores | 0.911 | 0.010 | 2.238 | 2.796 | 0.290 | 0.160 | 0.260 | 0.236 | -0.060 |
| corn | mp6 | mp5 | 2 | pds | TD-CP+ (jackknife+) | 0.925 | 0.008 | 2.445 | 2.795 | 0.290 | 0.160 | 0.260 | 0.236 | -0.060 |
| corn | mp6 | mp5 | 2 | pds | Weighted CP (covariate shift) | 0.779 | 0.013 | ∞ | ∞ | 0.290 | 0.160 | 0.260 | 0.236 | -0.060 |
| corn | mp6 | mp5 | 3 | ds | Gaussian TD (parametric) | 0.880 | 0.013 | 3.286 | 4.581 | 0.711 | 0.375 | 0.715 | 0.602 | -0.062 |
| corn | mp6 | mp5 | 3 | ds | Leverage PI (classical) | 0.723 | 0.014 | 1.805 | 4.622 | 0.711 | 0.375 | 0.715 | 0.602 | -0.062 |
| corn | mp6 | mp5 | 3 | ds | Naive CP (primary residuals) | 0.666 | 0.015 | 1.586 | 5.330 | 0.711 | 0.375 | 0.715 | 0.602 | -0.062 |
| corn | mp6 | mp5 | 3 | ds | Pooled CP (k labelled) | 0.752 | 0.016 | 1.990 | 4.769 | 0.711 | 0.375 | 0.715 | 0.602 | -0.062 |
| corn | mp6 | mp5 | 3 | ds | Target CP (k labelled) | 0.909 | 0.013 | 3.868 | 4.897 | 0.711 | 0.375 | 0.715 | 0.602 | -0.062 |
| corn | mp6 | mp5 | 3 | ds | Target CP+ (k labelled) | 0.933 | 0.010 | 4.425 | 4.999 | 0.711 | 0.375 | 0.715 | 0.602 | -0.062 |
| corn | mp6 | mp5 | 3 | ds | TD-CP signed (pre-registered) | 0.900 | 0.011 | 3.522 | 4.617 | 0.711 | 0.375 | 0.715 | 0.602 | -0.062 |
| corn | mp6 | mp5 | 3 | ds | TD-CP absolute scores | 0.902 | 0.012 | 3.525 | 4.629 | 0.711 | 0.375 | 0.715 | 0.602 | -0.062 |
| corn | mp6 | mp5 | 3 | ds | TD-CP+ (jackknife+) | 0.930 | 0.010 | 4.062 | 4.667 | 0.711 | 0.375 | 0.715 | 0.602 | -0.062 |
| corn | mp6 | mp5 | 3 | ds | Weighted CP (covariate shift) | 0.755 | 0.014 | ∞ | ∞ | 0.711 | 0.375 | 0.715 | 0.602 | -0.062 |
| corn | mp6 | mp5 | 3 | pds | Gaussian TD (parametric) | 0.896 | 0.009 | 2.537 | 3.375 | 0.596 | 0.375 | 0.493 | 0.436 | -0.005 |
| corn | mp6 | mp5 | 3 | pds | Leverage PI (classical) | 0.811 | 0.013 | 1.815 | 3.465 | 0.596 | 0.375 | 0.493 | 0.436 | -0.005 |
| corn | mp6 | mp5 | 3 | pds | Naive CP (primary residuals) | 0.761 | 0.015 | 1.586 | 4.143 | 0.596 | 0.375 | 0.493 | 0.436 | -0.005 |
| corn | mp6 | mp5 | 3 | pds | Pooled CP (k labelled) | 0.803 | 0.013 | 1.799 | 3.736 | 0.596 | 0.375 | 0.493 | 0.436 | -0.005 |
| corn | mp6 | mp5 | 3 | pds | Target CP (k labelled) | 0.926 | 0.011 | 3.181 | 3.806 | 0.596 | 0.375 | 0.493 | 0.436 | -0.005 |
| corn | mp6 | mp5 | 3 | pds | Target CP+ (k labelled) | 0.932 | 0.009 | 3.356 | 3.899 | 0.596 | 0.375 | 0.493 | 0.436 | -0.005 |
| corn | mp6 | mp5 | 3 | pds | TD-CP signed (pre-registered) | 0.919 | 0.008 | 2.801 | 3.467 | 0.596 | 0.375 | 0.493 | 0.436 | -0.005 |
| corn | mp6 | mp5 | 3 | pds | TD-CP absolute scores | 0.909 | 0.008 | 2.716 | 3.443 | 0.596 | 0.375 | 0.493 | 0.436 | -0.005 |
| corn | mp6 | mp5 | 3 | pds | TD-CP+ (jackknife+) | 0.920 | 0.008 | 2.869 | 3.499 | 0.596 | 0.375 | 0.493 | 0.436 | -0.005 |
| corn | mp6 | mp5 | 3 | pds | Weighted CP (covariate shift) | 0.825 | 0.011 | ∞ | ∞ | 0.596 | 0.375 | 0.493 | 0.436 | -0.005 |
| tablets | inst1 | inst2 | 0 | ds | Gaussian TD (parametric) | 0.916 | 0.006 | 3.643 | 4.580 | 4.753 | 3.372 | 3.862 | 3.751 | -0.143 |
| tablets | inst1 | inst2 | 0 | ds | Leverage PI (classical) | 0.791 | 0.006 | 2.418 | 4.663 | 4.753 | 3.372 | 3.862 | 3.751 | -0.143 |
| tablets | inst1 | inst2 | 0 | ds | Naive CP (primary residuals) | 0.768 | 0.006 | 2.303 | 4.871 | 4.753 | 3.372 | 3.862 | 3.751 | -0.143 |
| tablets | inst1 | inst2 | 0 | ds | Pooled CP (k labelled) | 0.772 | 0.006 | 2.323 | 4.845 | 4.753 | 3.372 | 3.862 | 3.751 | -0.143 |
| tablets | inst1 | inst2 | 0 | ds | Target CP (k labelled) | 0.920 | 0.008 | 4.173 | 5.082 | 4.753 | 3.372 | 3.862 | 3.751 | -0.143 |
| tablets | inst1 | inst2 | 0 | ds | Target CP+ (k labelled) | 0.936 | 0.007 | 4.382 | 5.063 | 4.753 | 3.372 | 3.862 | 3.751 | -0.143 |
| tablets | inst1 | inst2 | 0 | ds | TD-CP signed (pre-registered) | 0.906 | 0.006 | 3.558 | 4.585 | 4.753 | 3.372 | 3.862 | 3.751 | -0.143 |
| tablets | inst1 | inst2 | 0 | ds | TD-CP absolute scores | 0.910 | 0.006 | 3.638 | 4.644 | 4.753 | 3.372 | 3.862 | 3.751 | -0.143 |
| tablets | inst1 | inst2 | 0 | ds | TD-CP+ (jackknife+) | 0.928 | 0.006 | 3.803 | 4.533 | 4.753 | 3.372 | 3.862 | 3.751 | -0.143 |
| tablets | inst1 | inst2 | 0 | ds | Weighted CP (covariate shift) | 0.736 | 0.018 | ∞ | ∞ | 4.753 | 3.372 | 3.862 | 3.751 | -0.143 |
| tablets | inst1 | inst2 | 0 | pds | Gaussian TD (parametric) | 0.914 | 0.007 | 6.285 | 8.009 | 7.802 | 3.372 | 8.330 | 6.944 | -0.076 |
| tablets | inst1 | inst2 | 0 | pds | Leverage PI (classical) | 0.599 | 0.009 | 2.557 | 10.426 | 7.802 | 3.372 | 8.330 | 6.944 | -0.076 |
| tablets | inst1 | inst2 | 0 | pds | Naive CP (primary residuals) | 0.555 | 0.009 | 2.303 | 11.505 | 7.802 | 3.372 | 8.330 | 6.944 | -0.076 |
| tablets | inst1 | inst2 | 0 | pds | Pooled CP (k labelled) | 0.571 | 0.009 | 2.379 | 11.233 | 7.802 | 3.372 | 8.330 | 6.944 | -0.076 |
| tablets | inst1 | inst2 | 0 | pds | Target CP (k labelled) | 0.937 | 0.007 | 7.358 | 8.646 | 7.802 | 3.372 | 8.330 | 6.944 | -0.076 |
| tablets | inst1 | inst2 | 0 | pds | Target CP+ (k labelled) | 0.958 | 0.005 | 8.293 | 9.001 | 7.802 | 3.372 | 8.330 | 6.944 | -0.076 |
| tablets | inst1 | inst2 | 0 | pds | TD-CP signed (pre-registered) | 0.896 | 0.007 | 6.186 | 8.248 | 7.802 | 3.372 | 8.330 | 6.944 | -0.076 |
| tablets | inst1 | inst2 | 0 | pds | TD-CP absolute scores | 0.917 | 0.007 | 6.390 | 8.094 | 7.802 | 3.372 | 8.330 | 6.944 | -0.076 |
| tablets | inst1 | inst2 | 0 | pds | TD-CP+ (jackknife+) | 0.945 | 0.005 | 7.227 | 8.149 | 7.802 | 3.372 | 8.330 | 6.944 | -0.076 |
| tablets | inst1 | inst2 | 0 | pds | Weighted CP (covariate shift) | 0.672 | 0.012 | ∞ | ∞ | 7.802 | 3.372 | 8.330 | 6.944 | -0.076 |
| tablets | inst1 | inst2 | 1 | ds | Gaussian TD (parametric) | 0.915 | 0.003 | 2.926 | 3.857 | 1.088 | 1.019 | 0.461 | 0.420 | -0.081 |
| tablets | inst1 | inst2 | 1 | ds | Leverage PI (classical) | 0.887 | 0.004 | 2.628 | 3.834 | 1.088 | 1.019 | 0.461 | 0.420 | -0.081 |
| tablets | inst1 | inst2 | 1 | ds | Naive CP (primary residuals) | 0.881 | 0.004 | 2.591 | 3.863 | 1.088 | 1.019 | 0.461 | 0.420 | -0.081 |
| tablets | inst1 | inst2 | 1 | ds | Pooled CP (k labelled) | 0.882 | 0.004 | 2.595 | 3.862 | 1.088 | 1.019 | 0.461 | 0.420 | -0.081 |
| tablets | inst1 | inst2 | 1 | ds | Target CP (k labelled) | 0.910 | 0.008 | 3.590 | 4.564 | 1.088 | 1.019 | 0.461 | 0.420 | -0.081 |
| tablets | inst1 | inst2 | 1 | ds | Target CP+ (k labelled) | 0.914 | 0.008 | 3.628 | 4.564 | 1.088 | 1.019 | 0.461 | 0.420 | -0.081 |
| tablets | inst1 | inst2 | 1 | ds | TD-CP signed (pre-registered) | 0.910 | 0.003 | 2.869 | 3.837 | 1.088 | 1.019 | 0.461 | 0.420 | -0.081 |
| tablets | inst1 | inst2 | 1 | ds | TD-CP absolute scores | 0.908 | 0.003 | 2.850 | 3.854 | 1.088 | 1.019 | 0.461 | 0.420 | -0.081 |
| tablets | inst1 | inst2 | 1 | ds | TD-CP+ (jackknife+) | 0.914 | 0.004 | 2.893 | 3.834 | 1.088 | 1.019 | 0.461 | 0.420 | -0.081 |
| tablets | inst1 | inst2 | 1 | ds | Weighted CP (covariate shift) | 0.885 | 0.005 | ∞ | ∞ | 1.088 | 1.019 | 0.461 | 0.420 | -0.081 |
| tablets | inst1 | inst2 | 1 | pds | Gaussian TD (parametric) | 0.918 | 0.004 | 3.517 | 4.446 | 1.196 | 1.019 | 0.698 | 0.524 | -0.075 |
| tablets | inst1 | inst2 | 1 | pds | Leverage PI (classical) | 0.861 | 0.011 | 2.646 | 4.628 | 1.196 | 1.019 | 0.698 | 0.524 | -0.075 |
| tablets | inst1 | inst2 | 1 | pds | Naive CP (primary residuals) | 0.853 | 0.012 | 2.591 | 4.783 | 1.196 | 1.019 | 0.698 | 0.524 | -0.075 |
| tablets | inst1 | inst2 | 1 | pds | Pooled CP (k labelled) | 0.856 | 0.012 | 2.604 | 4.746 | 1.196 | 1.019 | 0.698 | 0.524 | -0.075 |
| tablets | inst1 | inst2 | 1 | pds | Target CP (k labelled) | 0.912 | 0.009 | 4.382 | 5.375 | 1.196 | 1.019 | 0.698 | 0.524 | -0.075 |
| tablets | inst1 | inst2 | 1 | pds | Target CP+ (k labelled) | 0.917 | 0.009 | 4.596 | 5.508 | 1.196 | 1.019 | 0.698 | 0.524 | -0.075 |
| tablets | inst1 | inst2 | 1 | pds | TD-CP signed (pre-registered) | 0.912 | 0.004 | 3.439 | 4.456 | 1.196 | 1.019 | 0.698 | 0.524 | -0.075 |
| tablets | inst1 | inst2 | 1 | pds | TD-CP absolute scores | 0.912 | 0.004 | 3.569 | 4.560 | 1.196 | 1.019 | 0.698 | 0.524 | -0.075 |
| tablets | inst1 | inst2 | 1 | pds | TD-CP+ (jackknife+) | 0.916 | 0.004 | 3.722 | 4.634 | 1.196 | 1.019 | 0.698 | 0.524 | -0.075 |
| tablets | inst1 | inst2 | 1 | pds | Weighted CP (covariate shift) | 0.868 | 0.009 | ∞ | ∞ | 1.196 | 1.019 | 0.698 | 0.524 | -0.075 |
| tablets | inst1 | inst2 | 2 | ds | Gaussian TD (parametric) | 0.921 | 0.010 | 2.082 | 2.727 | 9.042 | 4.093 | 9.877 | 7.984 | -0.092 |
| tablets | inst1 | inst2 | 2 | ds | Leverage PI (classical) | 0.639 | 0.014 | 0.855 | 3.407 | 9.042 | 4.093 | 9.877 | 7.984 | -0.092 |
| tablets | inst1 | inst2 | 2 | ds | Naive CP (primary residuals) | 0.501 | 0.013 | 0.609 | 4.235 | 9.042 | 4.093 | 9.877 | 7.984 | -0.092 |
| tablets | inst1 | inst2 | 2 | ds | Pooled CP (k labelled) | 0.517 | 0.013 | 0.635 | 4.130 | 9.042 | 4.093 | 9.877 | 7.984 | -0.092 |
| tablets | inst1 | inst2 | 2 | ds | Target CP (k labelled) | 0.943 | 0.009 | 2.504 | 2.953 | 9.042 | 4.093 | 9.877 | 7.984 | -0.092 |
| tablets | inst1 | inst2 | 2 | ds | Target CP+ (k labelled) | 0.927 | 0.009 | 2.715 | 3.227 | 9.042 | 4.093 | 9.877 | 7.984 | -0.092 |
| tablets | inst1 | inst2 | 2 | ds | TD-CP signed (pre-registered) | 0.896 | 0.011 | 2.018 | 2.828 | 9.042 | 4.093 | 9.877 | 7.984 | -0.092 |
| tablets | inst1 | inst2 | 2 | ds | TD-CP absolute scores | 0.918 | 0.010 | 2.166 | 2.818 | 9.042 | 4.093 | 9.877 | 7.984 | -0.092 |
| tablets | inst1 | inst2 | 2 | ds | TD-CP+ (jackknife+) | 0.905 | 0.010 | 2.351 | 3.028 | 9.042 | 4.093 | 9.877 | 7.984 | -0.092 |
| tablets | inst1 | inst2 | 2 | ds | Weighted CP (covariate shift) | 0.534 | 0.017 | ∞ | ∞ | 9.042 | 4.093 | 9.877 | 7.984 | -0.092 |
| tablets | inst1 | inst2 | 2 | pds | Gaussian TD (parametric) | 0.928 | 0.005 | 1.880 | 2.354 | 8.409 | 4.093 | 8.650 | 7.311 | -0.118 |
| tablets | inst1 | inst2 | 2 | pds | Leverage PI (classical) | 0.691 | 0.011 | 0.896 | 2.753 | 8.409 | 4.093 | 8.650 | 7.311 | -0.118 |
| tablets | inst1 | inst2 | 2 | pds | Naive CP (primary residuals) | 0.526 | 0.010 | 0.609 | 3.646 | 8.409 | 4.093 | 8.650 | 7.311 | -0.118 |
| tablets | inst1 | inst2 | 2 | pds | Pooled CP (k labelled) | 0.542 | 0.010 | 0.633 | 3.553 | 8.409 | 4.093 | 8.650 | 7.311 | -0.118 |
| tablets | inst1 | inst2 | 2 | pds | Target CP (k labelled) | 0.930 | 0.008 | 2.150 | 2.594 | 8.409 | 4.093 | 8.650 | 7.311 | -0.118 |
| tablets | inst1 | inst2 | 2 | pds | Target CP+ (k labelled) | 0.957 | 0.005 | 2.439 | 2.715 | 8.409 | 4.093 | 8.650 | 7.311 | -0.118 |
| tablets | inst1 | inst2 | 2 | pds | TD-CP signed (pre-registered) | 0.896 | 0.007 | 1.786 | 2.434 | 8.409 | 4.093 | 8.650 | 7.311 | -0.118 |
| tablets | inst1 | inst2 | 2 | pds | TD-CP absolute scores | 0.923 | 0.006 | 1.910 | 2.402 | 8.409 | 4.093 | 8.650 | 7.311 | -0.118 |
| tablets | inst1 | inst2 | 2 | pds | TD-CP+ (jackknife+) | 0.948 | 0.004 | 2.169 | 2.489 | 8.409 | 4.093 | 8.650 | 7.311 | -0.118 |
| tablets | inst1 | inst2 | 2 | pds | Weighted CP (covariate shift) | 0.657 | 0.012 | ∞ | ∞ | 8.409 | 4.093 | 8.650 | 7.311 | -0.118 |
| tablets | inst2 | inst1 | 0 | ds | Gaussian TD (parametric) | 0.926 | 0.006 | 3.839 | 4.677 | 4.750 | 3.570 | 4.048 | 3.714 | -0.203 |
| tablets | inst2 | inst1 | 0 | ds | Leverage PI (classical) | 0.818 | 0.005 | 2.569 | 4.509 | 4.750 | 3.570 | 4.048 | 3.714 | -0.203 |
| tablets | inst2 | inst1 | 0 | ds | Naive CP (primary residuals) | 0.795 | 0.006 | 2.440 | 4.698 | 4.750 | 3.570 | 4.048 | 3.714 | -0.203 |
| tablets | inst2 | inst1 | 0 | ds | Pooled CP (k labelled) | 0.797 | 0.006 | 2.455 | 4.684 | 4.750 | 3.570 | 4.048 | 3.714 | -0.203 |
| tablets | inst2 | inst1 | 0 | ds | Target CP (k labelled) | 0.906 | 0.010 | 4.092 | 5.138 | 4.750 | 3.570 | 4.048 | 3.714 | -0.203 |
| tablets | inst2 | inst1 | 0 | ds | Target CP+ (k labelled) | 0.925 | 0.008 | 4.316 | 5.054 | 4.750 | 3.570 | 4.048 | 3.714 | -0.203 |
| tablets | inst2 | inst1 | 0 | ds | TD-CP signed (pre-registered) | 0.919 | 0.006 | 3.795 | 4.712 | 4.750 | 3.570 | 4.048 | 3.714 | -0.203 |
| tablets | inst2 | inst1 | 0 | ds | TD-CP absolute scores | 0.921 | 0.006 | 3.790 | 4.671 | 4.750 | 3.570 | 4.048 | 3.714 | -0.203 |
| tablets | inst2 | inst1 | 0 | ds | TD-CP+ (jackknife+) | 0.939 | 0.005 | 3.955 | 4.576 | 4.750 | 3.570 | 4.048 | 3.714 | -0.203 |
| tablets | inst2 | inst1 | 0 | ds | Weighted CP (covariate shift) | 0.795 | 0.014 | ∞ | ∞ | 4.750 | 3.570 | 4.048 | 3.714 | -0.203 |
| tablets | inst2 | inst1 | 0 | pds | Gaussian TD (parametric) | 0.912 | 0.009 | 7.992 | 10.494 | 9.812 | 3.570 | 10.897 | 9.088 | -0.108 |
| tablets | inst2 | inst1 | 0 | pds | Leverage PI (classical) | 0.536 | 0.010 | 2.786 | 14.590 | 9.812 | 3.570 | 10.897 | 9.088 | -0.108 |
| tablets | inst2 | inst1 | 0 | pds | Naive CP (primary residuals) | 0.487 | 0.010 | 2.440 | 16.299 | 9.812 | 3.570 | 10.897 | 9.088 | -0.108 |
| tablets | inst2 | inst1 | 0 | pds | Pooled CP (k labelled) | 0.499 | 0.010 | 2.512 | 16.000 | 9.812 | 3.570 | 10.897 | 9.088 | -0.108 |
| tablets | inst2 | inst1 | 0 | pds | Target CP (k labelled) | 0.934 | 0.009 | 9.755 | 11.636 | 9.812 | 3.570 | 10.897 | 9.088 | -0.108 |
| tablets | inst2 | inst1 | 0 | pds | Target CP+ (k labelled) | 0.964 | 0.005 | 11.049 | 11.879 | 9.812 | 3.570 | 10.897 | 9.088 | -0.108 |
| tablets | inst2 | inst1 | 0 | pds | TD-CP signed (pre-registered) | 0.893 | 0.009 | 7.931 | 10.957 | 9.812 | 3.570 | 10.897 | 9.088 | -0.108 |
| tablets | inst2 | inst1 | 0 | pds | TD-CP absolute scores | 0.925 | 0.008 | 8.402 | 10.535 | 9.812 | 3.570 | 10.897 | 9.088 | -0.108 |
| tablets | inst2 | inst1 | 0 | pds | TD-CP+ (jackknife+) | 0.954 | 0.006 | 9.584 | 10.634 | 9.812 | 3.570 | 10.897 | 9.088 | -0.108 |
| tablets | inst2 | inst1 | 0 | pds | Weighted CP (covariate shift) | 0.653 | 0.015 | ∞ | ∞ | 9.812 | 3.570 | 10.897 | 9.088 | -0.108 |
| tablets | inst2 | inst1 | 1 | ds | Gaussian TD (parametric) | 0.918 | 0.003 | 2.992 | 3.902 | 1.094 | 1.030 | 0.461 | 0.439 | -0.128 |
| tablets | inst2 | inst1 | 1 | ds | Leverage PI (classical) | 0.888 | 0.005 | 2.655 | 3.861 | 1.094 | 1.030 | 0.461 | 0.439 | -0.128 |
| tablets | inst2 | inst1 | 1 | ds | Naive CP (primary residuals) | 0.880 | 0.005 | 2.601 | 3.907 | 1.094 | 1.030 | 0.461 | 0.439 | -0.128 |
| tablets | inst2 | inst1 | 1 | ds | Pooled CP (k labelled) | 0.880 | 0.005 | 2.601 | 3.906 | 1.094 | 1.030 | 0.461 | 0.439 | -0.128 |
| tablets | inst2 | inst1 | 1 | ds | Target CP (k labelled) | 0.910 | 0.008 | 3.650 | 4.632 | 1.094 | 1.030 | 0.461 | 0.439 | -0.128 |
| tablets | inst2 | inst1 | 1 | ds | Target CP+ (k labelled) | 0.916 | 0.008 | 3.703 | 4.600 | 1.094 | 1.030 | 0.461 | 0.439 | -0.128 |
| tablets | inst2 | inst1 | 1 | ds | TD-CP signed (pre-registered) | 0.914 | 0.003 | 2.976 | 3.911 | 1.094 | 1.030 | 0.461 | 0.439 | -0.128 |
| tablets | inst2 | inst1 | 1 | ds | TD-CP absolute scores | 0.915 | 0.003 | 2.977 | 3.908 | 1.094 | 1.030 | 0.461 | 0.439 | -0.128 |
| tablets | inst2 | inst1 | 1 | ds | TD-CP+ (jackknife+) | 0.921 | 0.003 | 3.022 | 3.879 | 1.094 | 1.030 | 0.461 | 0.439 | -0.128 |
| tablets | inst2 | inst1 | 1 | ds | Weighted CP (covariate shift) | 0.879 | 0.010 | ∞ | ∞ | 1.094 | 1.030 | 0.461 | 0.439 | -0.128 |
| tablets | inst2 | inst1 | 1 | pds | Gaussian TD (parametric) | 0.919 | 0.003 | 4.043 | 5.135 | 1.379 | 1.030 | 0.917 | 0.714 | -0.074 |
| tablets | inst2 | inst1 | 1 | pds | Leverage PI (classical) | 0.826 | 0.014 | 2.704 | 5.710 | 1.379 | 1.030 | 0.917 | 0.714 | -0.074 |
| tablets | inst2 | inst1 | 1 | pds | Naive CP (primary residuals) | 0.811 | 0.016 | 2.601 | 6.093 | 1.379 | 1.030 | 0.917 | 0.714 | -0.074 |
| tablets | inst2 | inst1 | 1 | pds | Pooled CP (k labelled) | 0.815 | 0.015 | 2.624 | 6.016 | 1.379 | 1.030 | 0.917 | 0.714 | -0.074 |
| tablets | inst2 | inst1 | 1 | pds | Target CP (k labelled) | 0.925 | 0.008 | 5.118 | 6.115 | 1.379 | 1.030 | 0.917 | 0.714 | -0.074 |
| tablets | inst2 | inst1 | 1 | pds | Target CP+ (k labelled) | 0.931 | 0.008 | 5.436 | 6.251 | 1.379 | 1.030 | 0.917 | 0.714 | -0.074 |
| tablets | inst2 | inst1 | 1 | pds | TD-CP signed (pre-registered) | 0.912 | 0.004 | 4.055 | 5.255 | 1.379 | 1.030 | 0.917 | 0.714 | -0.074 |
| tablets | inst2 | inst1 | 1 | pds | TD-CP absolute scores | 0.920 | 0.003 | 4.160 | 5.227 | 1.379 | 1.030 | 0.917 | 0.714 | -0.074 |
| tablets | inst2 | inst1 | 1 | pds | TD-CP+ (jackknife+) | 0.926 | 0.004 | 4.470 | 5.328 | 1.379 | 1.030 | 0.917 | 0.714 | -0.074 |
| tablets | inst2 | inst1 | 1 | pds | Weighted CP (covariate shift) | 0.849 | 0.011 | ∞ | ∞ | 1.379 | 1.030 | 0.917 | 0.714 | -0.074 |
| tablets | inst2 | inst1 | 2 | ds | Gaussian TD (parametric) | 0.911 | 0.010 | 2.144 | 2.784 | 9.375 | 4.284 | 10.162 | 8.251 | -0.049 |
| tablets | inst2 | inst1 | 2 | ds | Leverage PI (classical) | 0.616 | 0.012 | 0.872 | 3.555 | 9.375 | 4.284 | 10.162 | 8.251 | -0.049 |
| tablets | inst2 | inst1 | 2 | ds | Naive CP (primary residuals) | 0.492 | 0.011 | 0.651 | 4.330 | 9.375 | 4.284 | 10.162 | 8.251 | -0.049 |
| tablets | inst2 | inst1 | 2 | ds | Pooled CP (k labelled) | 0.506 | 0.011 | 0.673 | 4.239 | 9.375 | 4.284 | 10.162 | 8.251 | -0.049 |
| tablets | inst2 | inst1 | 2 | ds | Target CP (k labelled) | 0.937 | 0.010 | 2.601 | 3.075 | 9.375 | 4.284 | 10.162 | 8.251 | -0.049 |
| tablets | inst2 | inst1 | 2 | ds | Target CP+ (k labelled) | 0.928 | 0.010 | 2.797 | 3.351 | 9.375 | 4.284 | 10.162 | 8.251 | -0.049 |
| tablets | inst2 | inst1 | 2 | ds | TD-CP signed (pre-registered) | 0.887 | 0.011 | 2.093 | 2.923 | 9.375 | 4.284 | 10.162 | 8.251 | -0.049 |
| tablets | inst2 | inst1 | 2 | ds | TD-CP absolute scores | 0.909 | 0.011 | 2.239 | 2.892 | 9.375 | 4.284 | 10.162 | 8.251 | -0.049 |
| tablets | inst2 | inst1 | 2 | ds | TD-CP+ (jackknife+) | 0.899 | 0.011 | 2.412 | 3.143 | 9.375 | 4.284 | 10.162 | 8.251 | -0.049 |
| tablets | inst2 | inst1 | 2 | ds | Weighted CP (covariate shift) | 0.511 | 0.015 | ∞ | ∞ | 9.375 | 4.284 | 10.162 | 8.251 | -0.049 |
| tablets | inst2 | inst1 | 2 | pds | Gaussian TD (parametric) | 0.928 | 0.006 | 1.912 | 2.443 | 8.578 | 4.284 | 8.557 | 7.222 | -0.132 |
| tablets | inst2 | inst1 | 2 | pds | Leverage PI (classical) | 0.705 | 0.018 | 0.913 | 3.034 | 8.578 | 4.284 | 8.557 | 7.222 | -0.132 |
| tablets | inst2 | inst1 | 2 | pds | Naive CP (primary residuals) | 0.579 | 0.019 | 0.651 | 3.791 | 8.578 | 4.284 | 8.557 | 7.222 | -0.132 |
| tablets | inst2 | inst1 | 2 | pds | Pooled CP (k labelled) | 0.590 | 0.018 | 0.669 | 3.717 | 8.578 | 4.284 | 8.557 | 7.222 | -0.132 |
| tablets | inst2 | inst1 | 2 | pds | Target CP (k labelled) | 0.940 | 0.006 | 2.304 | 2.702 | 8.578 | 4.284 | 8.557 | 7.222 | -0.132 |
| tablets | inst2 | inst1 | 2 | pds | Target CP+ (k labelled) | 0.957 | 0.004 | 2.550 | 2.828 | 8.578 | 4.284 | 8.557 | 7.222 | -0.132 |
| tablets | inst2 | inst1 | 2 | pds | TD-CP signed (pre-registered) | 0.892 | 0.009 | 1.834 | 2.561 | 8.578 | 4.284 | 8.557 | 7.222 | -0.132 |
| tablets | inst2 | inst1 | 2 | pds | TD-CP absolute scores | 0.925 | 0.007 | 1.989 | 2.490 | 8.578 | 4.284 | 8.557 | 7.222 | -0.132 |
| tablets | inst2 | inst1 | 2 | pds | TD-CP+ (jackknife+) | 0.950 | 0.004 | 2.225 | 2.559 | 8.578 | 4.284 | 8.557 | 7.222 | -0.132 |
| tablets | inst2 | inst1 | 2 | pds | Weighted CP (covariate shift) | 0.705 | 0.014 | ∞ | ∞ | 8.578 | 4.284 | 8.557 | 7.222 | -0.132 |
