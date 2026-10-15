**Table 3. TD-CP vs comparators: paired Wilcoxon over scenarios (Holm-adjusted)**

| reference | metric | comparator | n_scenarios | median_ref | median_comp | median_diff | ci95_low | ci95_high | rank_biserial | p_value | p_holm | ref_better_fraction |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| td_cp_plus | abs_gap | Naive CP (primary residuals) | 60 | 0.032 | 0.333 | -0.302 | -0.365 | -0.230 | -0.999 | 0.000 | 0.000 | 0.983 |
| td_cp_plus | abs_gap | Leverage PI (classical) | 60 | 0.032 | 0.254 | -0.234 | -0.269 | -0.159 | -0.997 | 0.000 | 0.000 | 0.967 |
| td_cp_plus | abs_gap | Weighted CP (covariate shift) | 60 | 0.032 | 0.269 | -0.235 | -0.280 | -0.201 | -1.000 | 0.000 | 0.000 | 1.000 |
| td_cp_plus | abs_gap | Gaussian TD (parametric) | 60 | 0.032 | 0.017 | 0.015 | 0.009 | 0.022 | 0.587 | 0.000 | 0.001 | 0.250 |
| td_cp_plus | abs_gap | TD-CP signed (pre-specified) | 60 | 0.032 | 0.015 | 0.016 | 0.008 | 0.022 | 0.658 | 0.000 | 0.000 | 0.200 |
| td_cp_plus | abs_gap | TD-CP absolute scores | 60 | 0.032 | 0.016 | 0.018 | 0.014 | 0.023 | 0.779 | 0.000 | 0.000 | 0.150 |
| td_cp_plus | abs_gap | TD-CP w/o cross-fitting | 60 | 0.032 | 0.161 | -0.115 | -0.192 | -0.087 | -0.983 | 0.000 | 0.000 | 0.933 |
| td_cp_plus | abs_gap | TD-sum (union bound) | 60 | 0.032 | 0.069 | -0.035 | -0.042 | -0.030 | -0.951 | 0.000 | 0.000 | 0.883 |
| td_cp_plus | abs_gap | Target CP (k labelled) | 60 | 0.032 | 0.016 | 0.019 | 0.012 | 0.022 | 0.723 | 0.000 | 0.000 | 0.133 |
| td_cp_plus | abs_gap | Target CP+ (k labelled) | 60 | 0.032 | 0.032 | -0.002 | -0.005 | 0.001 | -0.196 | 0.188 | 1.000 | 0.600 |
| td_cp_plus | abs_gap | Target t-interval (k labelled) | 60 | 0.032 | 0.018 | 0.020 | 0.015 | 0.022 | 0.766 | 0.000 | 0.000 | 0.117 |
| td_cp_plus | abs_gap | Pooled CP (k labelled) | 60 | 0.032 | 0.235 | -0.202 | -0.223 | -0.146 | -0.999 | 0.000 | 0.000 | 0.983 |
| td_cp_plus | is_norm | Naive CP (primary residuals) | 60 | 4.864 | 6.614 | -1.711 | -2.995 | -1.187 | -1.000 | 0.000 | 0.000 | 1.000 |
| td_cp_plus | is_norm | Leverage PI (classical) | 60 | 4.864 | 5.586 | -0.512 | -1.264 | -0.280 | -0.804 | 0.000 | 0.000 | 0.767 |
| td_cp_plus | is_norm | Weighted CP (covariate shift) | 60 | 4.864 | 1000000.000 | -999995.136 | -999995.416 | -999994.544 | -1.000 | 0.000 | 0.000 | 1.000 |
| td_cp_plus | is_norm | Gaussian TD (parametric) | 60 | 4.864 | 4.773 | 0.094 | 0.024 | 0.148 | 0.395 | 0.008 | 0.063 | 0.367 |
| td_cp_plus | is_norm | TD-CP signed (pre-specified) | 60 | 4.864 | 4.965 | -0.125 | -0.198 | -0.034 | -0.626 | 0.000 | 0.000 | 0.700 |
| td_cp_plus | is_norm | TD-CP absolute scores | 60 | 4.864 | 5.027 | -0.114 | -0.213 | -0.073 | -0.718 | 0.000 | 0.000 | 0.767 |
| td_cp_plus | is_norm | TD-CP w/o cross-fitting | 60 | 4.864 | 6.516 | -0.561 | -0.866 | -0.353 | -0.804 | 0.000 | 0.000 | 0.783 |
| td_cp_plus | is_norm | TD-sum (union bound) | 60 | 4.864 | 5.911 | -1.026 | -1.113 | -0.953 | -1.000 | 0.000 | 0.000 | 1.000 |
| td_cp_plus | is_norm | Target CP (k labelled) | 60 | 4.864 | 5.302 | -0.382 | -0.482 | -0.309 | -0.992 | 0.000 | 0.000 | 0.967 |
| td_cp_plus | is_norm | Target CP+ (k labelled) | 60 | 4.864 | 5.069 | -0.252 | -0.280 | -0.234 | -1.000 | 0.000 | 0.000 | 1.000 |
| td_cp_plus | is_norm | Target t-interval (k labelled) | 60 | 4.864 | 5.073 | -0.121 | -0.235 | -0.027 | -0.417 | 0.005 | 0.044 | 0.683 |
| td_cp_plus | is_norm | Pooled CP (k labelled) | 60 | 4.864 | 5.413 | -1.013 | -1.299 | -0.545 | -1.000 | 0.000 | 0.000 | 1.000 |
| td_cp | abs_gap | Naive CP (primary residuals) | 60 | 0.015 | 0.333 | -0.319 | -0.393 | -0.251 | -1.000 | 0.000 | 0.000 | 1.000 |
| td_cp | abs_gap | Leverage PI (classical) | 60 | 0.015 | 0.254 | -0.226 | -0.291 | -0.185 | -0.999 | 0.000 | 0.000 | 0.983 |
| td_cp | abs_gap | Weighted CP (covariate shift) | 60 | 0.015 | 0.269 | -0.256 | -0.280 | -0.224 | -1.000 | 0.000 | 0.000 | 1.000 |
| td_cp | abs_gap | Gaussian TD (parametric) | 60 | 0.015 | 0.017 | -0.001 | -0.005 | 0.005 | 0.071 | 0.632 | 1.000 | 0.533 |
| td_cp | abs_gap | TD-CP absolute scores | 60 | 0.015 | 0.016 | 0.002 | -0.002 | 0.006 | 0.225 | 0.130 | 0.912 | 0.433 |
| td_cp | abs_gap | TD-CP w/o cross-fitting | 60 | 0.015 | 0.161 | -0.133 | -0.207 | -0.110 | -0.998 | 0.000 | 0.000 | 0.983 |
| td_cp | abs_gap | TD-sum (union bound) | 60 | 0.015 | 0.069 | -0.056 | -0.063 | -0.050 | -0.857 | 0.000 | 0.000 | 0.917 |
| td_cp | abs_gap | Target CP (k labelled) | 60 | 0.015 | 0.016 | 0.002 | -0.005 | 0.005 | 0.116 | 0.433 | 1.000 | 0.467 |
| td_cp | abs_gap | Target CP+ (k labelled) | 60 | 0.015 | 0.032 | -0.014 | -0.019 | -0.006 | -0.666 | 0.000 | 0.000 | 0.783 |
| td_cp | abs_gap | Target t-interval (k labelled) | 60 | 0.015 | 0.018 | 0.003 | -0.001 | 0.007 | 0.202 | 0.174 | 1.000 | 0.400 |
| td_cp | abs_gap | Pooled CP (k labelled) | 60 | 0.015 | 0.235 | -0.197 | -0.227 | -0.160 | -1.000 | 0.000 | 0.000 | 1.000 |
| td_cp | is_norm | Naive CP (primary residuals) | 60 | 4.965 | 6.614 | -1.588 | -2.522 | -1.212 | -0.997 | 0.000 | 0.000 | 0.967 |
| td_cp | is_norm | Leverage PI (classical) | 60 | 4.965 | 5.586 | -0.498 | -1.083 | -0.191 | -0.754 | 0.000 | 0.000 | 0.750 |
| td_cp | is_norm | Weighted CP (covariate shift) | 60 | 4.965 | 1000000.000 | -999995.035 | -999995.383 | -999994.311 | -1.000 | 0.000 | 0.000 | 1.000 |
| td_cp | is_norm | Gaussian TD (parametric) | 60 | 4.965 | 4.773 | 0.132 | 0.102 | 0.193 | 0.970 | 0.000 | 0.000 | 0.050 |
| td_cp | is_norm | TD-CP absolute scores | 60 | 4.965 | 5.027 | -0.000 | -0.041 | 0.028 | -0.121 | 0.414 | 1.000 | 0.500 |
| td_cp | is_norm | TD-CP w/o cross-fitting | 60 | 4.965 | 6.516 | -0.402 | -0.774 | -0.211 | -0.714 | 0.000 | 0.000 | 0.733 |
| td_cp | is_norm | TD-sum (union bound) | 60 | 4.965 | 5.911 | -0.937 | -1.082 | -0.692 | -0.997 | 0.000 | 0.000 | 0.983 |
| td_cp | is_norm | Target CP (k labelled) | 60 | 4.965 | 5.302 | -0.218 | -0.280 | -0.164 | -0.973 | 0.000 | 0.000 | 0.950 |
| td_cp | is_norm | Target CP+ (k labelled) | 60 | 4.965 | 5.069 | -0.186 | -0.269 | -0.042 | -0.544 | 0.000 | 0.002 | 0.683 |
| td_cp | is_norm | Target t-interval (k labelled) | 60 | 4.965 | 5.073 | -0.028 | -0.071 | 0.023 | 0.012 | 0.935 | 1.000 | 0.600 |
| td_cp | is_norm | Pooled CP (k labelled) | 60 | 4.965 | 5.413 | -0.776 | -1.160 | -0.465 | -0.993 | 0.000 | 0.000 | 0.967 |
