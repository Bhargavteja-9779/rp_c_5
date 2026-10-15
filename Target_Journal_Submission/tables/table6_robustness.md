**Table 6. Robustness and generalisation experiments (alpha = 0.10)**

| experiment | condition | transfer | method | scenarios | mean_coverage | pct_valid | median_IS_sd |
|---|---|---|---|---|---|---|---|
| biased_standards | standards from lower half of y | ds | Gaussian TD (parametric) | 30 | 0.824 | 20.000 | 5.154 |
| biased_standards | standards from lower half of y | ds | Naive CP (primary residuals) | 30 | 0.529 | 6.667 | 6.873 |
| biased_standards | standards from lower half of y | ds | Target CP (k labelled) | 30 | 0.843 | 26.667 | 5.201 |
| biased_standards | standards from lower half of y | ds | Target CP+ (k labelled) | 30 | 0.880 | 60.000 | 5.156 |
| biased_standards | standards from lower half of y | ds | TD-CP signed (pre-specified) | 30 | 0.825 | 23.333 | 5.252 |
| biased_standards | standards from lower half of y | ds | TD-CP absolute scores | 30 | 0.839 | 30.000 | 5.155 |
| biased_standards | standards from lower half of y | ds | TD-CP+ (jackknife+) | 30 | 0.876 | 60.000 | 5.003 |
| biased_standards | standards from lower half of y | pds | Gaussian TD (parametric) | 30 | 0.894 | 80.000 | 7.791 |
| biased_standards | standards from lower half of y | pds | Naive CP (primary residuals) | 30 | 0.461 | 0.000 | 14.127 |
| biased_standards | standards from lower half of y | pds | Target CP (k labelled) | 30 | 0.918 | 96.667 | 8.161 |
| biased_standards | standards from lower half of y | pds | Target CP+ (k labelled) | 30 | 0.942 | 100.000 | 8.133 |
| biased_standards | standards from lower half of y | pds | TD-CP signed (pre-specified) | 30 | 0.887 | 60.000 | 8.379 |
| biased_standards | standards from lower half of y | pds | TD-CP absolute scores | 30 | 0.913 | 93.333 | 8.027 |
| biased_standards | standards from lower half of y | pds | TD-CP+ (jackknife+) | 30 | 0.939 | 100.000 | 7.773 |
| k_sensitivity | k=15 | ds | Gaussian TD (parametric) | 30 | 0.893 | 66.667 | 3.741 |
| k_sensitivity | k=15 | ds | Naive CP (primary residuals) | 30 | 0.655 | 0.000 | 4.283 |
| k_sensitivity | k=15 | ds | Target CP (k labelled) | 30 | 0.929 | 96.667 | 4.100 |
| k_sensitivity | k=15 | ds | Target CP+ (k labelled) | 30 | 0.951 | 100.000 | 4.050 |
| k_sensitivity | k=15 | ds | TD-CP signed (pre-specified) | 30 | 0.913 | 90.000 | 3.762 |
| k_sensitivity | k=15 | ds | TD-CP absolute scores | 30 | 0.902 | 86.667 | 3.681 |
| k_sensitivity | k=15 | ds | TD-CP+ (jackknife+) | 30 | 0.932 | 100.000 | 3.457 |
| k_sensitivity | k=15 | pds | Gaussian TD (parametric) | 30 | 0.906 | 96.667 | 6.108 |
| k_sensitivity | k=15 | pds | Naive CP (primary residuals) | 30 | 0.532 | 0.000 | 10.711 |
| k_sensitivity | k=15 | pds | Target CP (k labelled) | 30 | 0.940 | 100.000 | 7.013 |
| k_sensitivity | k=15 | pds | Target CP+ (k labelled) | 30 | 0.951 | 100.000 | 6.946 |
| k_sensitivity | k=15 | pds | TD-CP signed (pre-specified) | 30 | 0.920 | 100.000 | 6.585 |
| k_sensitivity | k=15 | pds | TD-CP absolute scores | 30 | 0.913 | 100.000 | 6.106 |
| k_sensitivity | k=15 | pds | TD-CP+ (jackknife+) | 30 | 0.922 | 100.000 | 5.927 |
| k_sensitivity | k=20 | ds | Gaussian TD (parametric) | 30 | 0.901 | 86.667 | 3.281 |
| k_sensitivity | k=20 | ds | Naive CP (primary residuals) | 30 | 0.712 | 6.667 | 3.773 |
| k_sensitivity | k=20 | ds | Target CP (k labelled) | 30 | 0.897 | 86.667 | 3.331 |
| k_sensitivity | k=20 | ds | Target CP+ (k labelled) | 30 | 0.920 | 100.000 | 3.212 |
| k_sensitivity | k=20 | ds | TD-CP signed (pre-specified) | 30 | 0.925 | 93.333 | 3.503 |
| k_sensitivity | k=20 | ds | TD-CP absolute scores | 30 | 0.911 | 93.333 | 3.338 |
| k_sensitivity | k=20 | ds | TD-CP+ (jackknife+) | 30 | 0.937 | 100.000 | 3.238 |
| k_sensitivity | k=20 | pds | Gaussian TD (parametric) | 30 | 0.919 | 100.000 | 4.838 |
| k_sensitivity | k=20 | pds | Naive CP (primary residuals) | 30 | 0.610 | 0.000 | 6.767 |
| k_sensitivity | k=20 | pds | Target CP (k labelled) | 30 | 0.914 | 100.000 | 4.942 |
| k_sensitivity | k=20 | pds | Target CP+ (k labelled) | 30 | 0.919 | 100.000 | 4.936 |
| k_sensitivity | k=20 | pds | TD-CP signed (pre-specified) | 30 | 0.940 | 100.000 | 5.355 |
| k_sensitivity | k=20 | pds | TD-CP absolute scores | 30 | 0.928 | 100.000 | 4.901 |
| k_sensitivity | k=20 | pds | TD-CP+ (jackknife+) | 30 | 0.932 | 100.000 | 4.889 |
| k_sensitivity | k=30 | ds | Gaussian TD (parametric) | 30 | 0.902 | 66.667 | 3.062 |
| k_sensitivity | k=30 | ds | Naive CP (primary residuals) | 30 | 0.752 | 3.333 | 3.462 |
| k_sensitivity | k=30 | ds | Target CP (k labelled) | 30 | 0.903 | 93.333 | 2.977 |
| k_sensitivity | k=30 | ds | Target CP+ (k labelled) | 30 | 0.916 | 100.000 | 2.910 |
| k_sensitivity | k=30 | ds | TD-CP signed (pre-specified) | 30 | 0.945 | 100.000 | 3.527 |
| k_sensitivity | k=30 | ds | TD-CP absolute scores | 30 | 0.922 | 100.000 | 3.175 |
| k_sensitivity | k=30 | ds | TD-CP+ (jackknife+) | 30 | 0.936 | 100.000 | 3.125 |
| k_sensitivity | k=30 | pds | Gaussian TD (parametric) | 30 | 0.909 | 93.333 | 4.055 |
| k_sensitivity | k=30 | pds | Naive CP (primary residuals) | 30 | 0.672 | 0.000 | 6.366 |
| k_sensitivity | k=30 | pds | Target CP (k labelled) | 30 | 0.906 | 100.000 | 4.145 |
| k_sensitivity | k=30 | pds | Target CP+ (k labelled) | 30 | 0.908 | 100.000 | 4.141 |
| k_sensitivity | k=30 | pds | TD-CP signed (pre-specified) | 30 | 0.950 | 100.000 | 4.527 |
| k_sensitivity | k=30 | pds | TD-CP absolute scores | 30 | 0.929 | 100.000 | 4.250 |
| k_sensitivity | k=30 | pds | TD-CP+ (jackknife+) | 30 | 0.931 | 100.000 | 4.231 |
| k_sensitivity | k=5 | ds | Gaussian TD (parametric) | 30 | 0.814 | 13.333 | 8.385 |
| k_sensitivity | k=5 | ds | Naive CP (primary residuals) | 30 | 0.419 | 0.000 | 13.891 |
| k_sensitivity | k=5 | ds | Target CP (k labelled) | 30 | 1.000 | 100.000 | ∞ |
| k_sensitivity | k=5 | ds | Target CP+ (k labelled) | 30 | 1.000 | 100.000 | ∞ |
| k_sensitivity | k=5 | ds | TD-CP signed (pre-specified) | 30 | 0.784 | 6.667 | 8.318 |
| k_sensitivity | k=5 | ds | TD-CP absolute scores | 30 | 0.811 | 10.000 | 8.119 |
| k_sensitivity | k=5 | ds | TD-CP+ (jackknife+) | 30 | 0.875 | 46.667 | 7.431 |
| k_sensitivity | k=5 | pds | Gaussian TD (parametric) | 30 | 0.846 | 23.333 | 14.994 |
| k_sensitivity | k=5 | pds | Naive CP (primary residuals) | 30 | 0.357 | 0.000 | 28.823 |
| k_sensitivity | k=5 | pds | Target CP (k labelled) | 30 | 1.000 | 100.000 | ∞ |
| k_sensitivity | k=5 | pds | Target CP+ (k labelled) | 30 | 1.000 | 100.000 | ∞ |
| k_sensitivity | k=5 | pds | TD-CP signed (pre-specified) | 30 | 0.782 | 10.000 | 17.459 |
| k_sensitivity | k=5 | pds | TD-CP absolute scores | 30 | 0.868 | 50.000 | 14.953 |
| k_sensitivity | k=5 | pds | TD-CP+ (jackknife+) | 30 | 0.950 | 100.000 | 13.813 |
| k_sensitivity | k=8 | ds | Gaussian TD (parametric) | 30 | 0.884 | 53.333 | 5.440 |
| k_sensitivity | k=8 | ds | Naive CP (primary residuals) | 30 | 0.545 | 3.333 | 6.840 |
| k_sensitivity | k=8 | ds | Target CP (k labelled) | 30 | 1.000 | 100.000 | ∞ |
| k_sensitivity | k=8 | ds | Target CP+ (k labelled) | 30 | 1.000 | 100.000 | ∞ |
| k_sensitivity | k=8 | ds | TD-CP signed (pre-specified) | 30 | 0.875 | 53.333 | 5.536 |
| k_sensitivity | k=8 | ds | TD-CP absolute scores | 30 | 0.893 | 66.667 | 5.622 |
| k_sensitivity | k=8 | ds | TD-CP+ (jackknife+) | 30 | 0.926 | 100.000 | 5.631 |
| k_sensitivity | k=8 | pds | Gaussian TD (parametric) | 30 | 0.904 | 86.667 | 8.832 |
| k_sensitivity | k=8 | pds | Naive CP (primary residuals) | 30 | 0.432 | 0.000 | 15.971 |
| k_sensitivity | k=8 | pds | Target CP (k labelled) | 30 | 1.000 | 100.000 | ∞ |
| k_sensitivity | k=8 | pds | Target CP+ (k labelled) | 30 | 1.000 | 100.000 | ∞ |
| k_sensitivity | k=8 | pds | TD-CP signed (pre-specified) | 30 | 0.887 | 60.000 | 9.253 |
| k_sensitivity | k=8 | pds | TD-CP absolute scores | 30 | 0.923 | 100.000 | 9.847 |
| k_sensitivity | k=8 | pds | TD-CP+ (jackknife+) | 30 | 0.952 | 100.000 | 9.927 |
| kennard_stone | KS selection | ds | Gaussian TD (parametric) | 30 | 0.915 | 90.000 | 4.379 |
| kennard_stone | KS selection | ds | Naive CP (primary residuals) | 30 | 0.573 | 3.333 | 5.515 |
| kennard_stone | KS selection | ds | Target CP (k labelled) | 30 | 0.939 | 100.000 | 4.915 |
| kennard_stone | KS selection | ds | Target CP+ (k labelled) | 30 | 0.958 | 100.000 | 5.075 |
| kennard_stone | KS selection | ds | TD-CP signed (pre-specified) | 30 | 0.917 | 86.667 | 4.515 |
| kennard_stone | KS selection | ds | TD-CP absolute scores | 30 | 0.925 | 100.000 | 4.515 |
| kennard_stone | KS selection | ds | TD-CP+ (jackknife+) | 30 | 0.950 | 100.000 | 4.539 |
| kennard_stone | KS selection | pds | Gaussian TD (parametric) | 30 | 0.941 | 100.000 | 6.516 |
| kennard_stone | KS selection | pds | Naive CP (primary residuals) | 30 | 0.482 | 0.000 | 11.080 |
| kennard_stone | KS selection | pds | Target CP (k labelled) | 30 | 0.963 | 100.000 | 8.163 |
| kennard_stone | KS selection | pds | Target CP+ (k labelled) | 30 | 0.972 | 100.000 | 8.423 |
| kennard_stone | KS selection | pds | TD-CP signed (pre-specified) | 30 | 0.936 | 100.000 | 6.879 |
| kennard_stone | KS selection | pds | TD-CP absolute scores | 30 | 0.951 | 100.000 | 7.228 |
| kennard_stone | KS selection | pds | TD-CP+ (jackknife+) | 30 | 0.962 | 100.000 | 7.582 |
| no_standardisation | no transfer | none | Gaussian TD (parametric) | 30 | 0.903 | 80.000 | 2.284 |
| no_standardisation | no transfer | none | Naive CP (primary residuals) | 30 | 0.283 | 0.000 | 26.110 |
| no_standardisation | no transfer | none | Target CP (k labelled) | 30 | 0.912 | 100.000 | 5.685 |
| no_standardisation | no transfer | none | Target CP+ (k labelled) | 30 | 0.912 | 100.000 | 5.685 |
| no_standardisation | no transfer | none | TD-CP signed (pre-specified) | 30 | 0.917 | 90.000 | 2.351 |
| no_standardisation | no transfer | none | TD-CP absolute scores | 30 | 0.921 | 100.000 | 5.606 |
| no_standardisation | no transfer | none | TD-CP+ (jackknife+) | 30 | 0.921 | 100.000 | 5.606 |
| noise | noise=0.005 | pds | Gaussian TD (parametric) | 30 | 0.899 | 73.333 | 9.427 |
| noise | noise=0.005 | pds | Naive CP (primary residuals) | 30 | 0.406 | 0.000 | 22.157 |
| noise | noise=0.005 | pds | Target CP (k labelled) | 30 | 0.920 | 100.000 | 10.114 |
| noise | noise=0.005 | pds | Target CP+ (k labelled) | 30 | 0.948 | 100.000 | 9.928 |
| noise | noise=0.005 | pds | TD-CP signed (pre-specified) | 30 | 0.888 | 56.667 | 9.875 |
| noise | noise=0.005 | pds | TD-CP absolute scores | 30 | 0.915 | 100.000 | 10.031 |
| noise | noise=0.005 | pds | TD-CP+ (jackknife+) | 30 | 0.945 | 100.000 | 9.517 |
| noise | noise=0.01 | pds | Gaussian TD (parametric) | 30 | 0.899 | 80.000 | 10.183 |
| noise | noise=0.01 | pds | Naive CP (primary residuals) | 30 | 0.365 | 0.000 | 26.642 |
| noise | noise=0.01 | pds | Target CP (k labelled) | 30 | 0.923 | 100.000 | 10.552 |
| noise | noise=0.01 | pds | Target CP+ (k labelled) | 30 | 0.952 | 100.000 | 10.503 |
| noise | noise=0.01 | pds | TD-CP signed (pre-specified) | 30 | 0.888 | 53.333 | 10.467 |
| noise | noise=0.01 | pds | TD-CP absolute scores | 30 | 0.918 | 100.000 | 10.235 |
| noise | noise=0.01 | pds | TD-CP+ (jackknife+) | 30 | 0.948 | 100.000 | 9.851 |
| noise | noise=0.02 | pds | Gaussian TD (parametric) | 30 | 0.907 | 93.333 | 10.307 |
| noise | noise=0.02 | pds | Naive CP (primary residuals) | 30 | 0.339 | 0.000 | 28.515 |
| noise | noise=0.02 | pds | Target CP (k labelled) | 30 | 0.931 | 100.000 | 10.692 |
| noise | noise=0.02 | pds | Target CP+ (k labelled) | 30 | 0.957 | 100.000 | 10.969 |
| noise | noise=0.02 | pds | TD-CP signed (pre-specified) | 30 | 0.895 | 73.333 | 10.539 |
| noise | noise=0.02 | pds | TD-CP absolute scores | 30 | 0.926 | 100.000 | 10.206 |
| noise | noise=0.02 | pds | TD-CP+ (jackknife+) | 30 | 0.953 | 100.000 | 10.141 |
| official_split | IDRC official split | ds | Gaussian TD (parametric) | 6 | 0.918 | 66.667 | 3.688 |
| official_split | IDRC official split | ds | Naive CP (primary residuals) | 6 | 0.780 | 33.333 | 3.855 |
| official_split | IDRC official split | ds | Target CP (k labelled) | 6 | 0.921 | 66.667 | 4.989 |
| official_split | IDRC official split | ds | Target CP+ (k labelled) | 6 | 0.924 | 100.000 | 4.856 |
| official_split | IDRC official split | ds | TD-CP signed (pre-specified) | 6 | 0.907 | 66.667 | 3.590 |
| official_split | IDRC official split | ds | TD-CP absolute scores | 6 | 0.913 | 66.667 | 3.572 |
| official_split | IDRC official split | ds | TD-CP+ (jackknife+) | 6 | 0.916 | 100.000 | 3.558 |
| official_split | IDRC official split | pds | Gaussian TD (parametric) | 6 | 0.918 | 66.667 | 3.686 |
| official_split | IDRC official split | pds | Naive CP (primary residuals) | 6 | 0.826 | 33.333 | 3.527 |
| official_split | IDRC official split | pds | Target CP (k labelled) | 6 | 0.919 | 83.333 | 5.124 |
| official_split | IDRC official split | pds | Target CP+ (k labelled) | 6 | 0.929 | 100.000 | 5.130 |
| official_split | IDRC official split | pds | TD-CP signed (pre-specified) | 6 | 0.908 | 66.667 | 3.587 |
| official_split | IDRC official split | pds | TD-CP absolute scores | 6 | 0.912 | 83.333 | 3.577 |
| official_split | IDRC official split | pds | TD-CP+ (jackknife+) | 6 | 0.924 | 83.333 | 3.582 |
| parsimonious_pls | PLS, 1-SE rule | ds | Gaussian TD (parametric) | 30 | 0.888 | 56.667 | 4.238 |
| parsimonious_pls | PLS, 1-SE rule | ds | Naive CP (primary residuals) | 30 | 0.621 | 6.667 | 4.701 |
| parsimonious_pls | PLS, 1-SE rule | ds | Target CP (k labelled) | 30 | 0.904 | 90.000 | 4.589 |
| parsimonious_pls | PLS, 1-SE rule | ds | Target CP+ (k labelled) | 30 | 0.927 | 100.000 | 4.621 |
| parsimonious_pls | PLS, 1-SE rule | ds | TD-CP signed (pre-specified) | 30 | 0.892 | 76.667 | 4.268 |
| parsimonious_pls | PLS, 1-SE rule | ds | TD-CP absolute scores | 30 | 0.900 | 90.000 | 4.260 |
| parsimonious_pls | PLS, 1-SE rule | ds | TD-CP+ (jackknife+) | 30 | 0.927 | 100.000 | 4.270 |
| parsimonious_pls | PLS, 1-SE rule | pds | Gaussian TD (parametric) | 30 | 0.907 | 93.333 | 6.027 |
| parsimonious_pls | PLS, 1-SE rule | pds | Naive CP (primary residuals) | 30 | 0.576 | 6.667 | 9.916 |
| parsimonious_pls | PLS, 1-SE rule | pds | Target CP (k labelled) | 30 | 0.921 | 100.000 | 6.752 |
| parsimonious_pls | PLS, 1-SE rule | pds | Target CP+ (k labelled) | 30 | 0.938 | 100.000 | 6.640 |
| parsimonious_pls | PLS, 1-SE rule | pds | TD-CP signed (pre-specified) | 30 | 0.905 | 86.667 | 6.265 |
| parsimonious_pls | PLS, 1-SE rule | pds | TD-CP absolute scores | 30 | 0.920 | 100.000 | 6.188 |
| parsimonious_pls | PLS, 1-SE rule | pds | TD-CP+ (jackknife+) | 30 | 0.937 | 100.000 | 6.302 |
| pds_window | PDS window 11 | pds | Gaussian TD (parametric) | 30 | 0.891 | 66.667 | 10.566 |
| pds_window | PDS window 11 | pds | Naive CP (primary residuals) | 30 | 0.404 | 0.000 | 24.508 |
| pds_window | PDS window 11 | pds | Target CP (k labelled) | 30 | 0.920 | 96.667 | 11.451 |
| pds_window | PDS window 11 | pds | Target CP+ (k labelled) | 30 | 0.950 | 100.000 | 11.219 |
| pds_window | PDS window 11 | pds | TD-CP signed (pre-specified) | 30 | 0.881 | 50.000 | 11.253 |
| pds_window | PDS window 11 | pds | TD-CP absolute scores | 30 | 0.910 | 83.333 | 11.215 |
| pds_window | PDS window 11 | pds | TD-CP+ (jackknife+) | 30 | 0.946 | 100.000 | 10.519 |
| pds_window | PDS window 3 | pds | Gaussian TD (parametric) | 30 | 0.906 | 93.333 | 6.135 |
| pds_window | PDS window 3 | pds | Naive CP (primary residuals) | 30 | 0.536 | 0.000 | 9.824 |
| pds_window | PDS window 3 | pds | Target CP (k labelled) | 30 | 0.922 | 100.000 | 6.723 |
| pds_window | PDS window 3 | pds | Target CP+ (k labelled) | 30 | 0.944 | 100.000 | 6.708 |
| pds_window | PDS window 3 | pds | TD-CP signed (pre-specified) | 30 | 0.903 | 86.667 | 6.444 |
| pds_window | PDS window 3 | pds | TD-CP absolute scores | 30 | 0.922 | 100.000 | 6.463 |
| pds_window | PDS window 3 | pds | TD-CP+ (jackknife+) | 30 | 0.942 | 100.000 | 6.429 |
| pds_window | PDS window 7 | pds | Gaussian TD (parametric) | 30 | 0.907 | 100.000 | 9.370 |
| pds_window | PDS window 7 | pds | Naive CP (primary residuals) | 30 | 0.437 | 0.000 | 18.937 |
| pds_window | PDS window 7 | pds | Target CP (k labelled) | 30 | 0.929 | 100.000 | 10.180 |
| pds_window | PDS window 7 | pds | Target CP+ (k labelled) | 30 | 0.952 | 100.000 | 9.934 |
| pds_window | PDS window 7 | pds | TD-CP signed (pre-specified) | 30 | 0.898 | 76.667 | 9.997 |
| pds_window | PDS window 7 | pds | TD-CP absolute scores | 30 | 0.924 | 100.000 | 10.007 |
| pds_window | PDS window 7 | pds | TD-CP+ (jackknife+) | 30 | 0.950 | 100.000 | 9.647 |
| preprocessing | snv_sg1 | ds | Gaussian TD (parametric) | 30 | 0.894 | 76.667 | 3.704 |
| preprocessing | snv_sg1 | ds | Naive CP (primary residuals) | 30 | 0.684 | 0.000 | 4.209 |
| preprocessing | snv_sg1 | ds | Target CP (k labelled) | 30 | 0.904 | 86.667 | 3.926 |
| preprocessing | snv_sg1 | ds | Target CP+ (k labelled) | 30 | 0.923 | 100.000 | 3.848 |
| preprocessing | snv_sg1 | ds | TD-CP signed (pre-specified) | 30 | 0.902 | 80.000 | 3.832 |
| preprocessing | snv_sg1 | ds | TD-CP absolute scores | 30 | 0.905 | 93.333 | 3.709 |
| preprocessing | snv_sg1 | ds | TD-CP+ (jackknife+) | 30 | 0.925 | 96.667 | 3.674 |
| preprocessing | snv_sg1 | pds | Gaussian TD (parametric) | 30 | 0.918 | 90.000 | 2.758 |
| preprocessing | snv_sg1 | pds | Naive CP (primary residuals) | 30 | 0.762 | 13.333 | 2.967 |
| preprocessing | snv_sg1 | pds | Target CP (k labelled) | 30 | 0.922 | 100.000 | 3.062 |
| preprocessing | snv_sg1 | pds | Target CP+ (k labelled) | 30 | 0.932 | 100.000 | 3.078 |
| preprocessing | snv_sg1 | pds | TD-CP signed (pre-specified) | 30 | 0.930 | 100.000 | 2.877 |
| preprocessing | snv_sg1 | pds | TD-CP absolute scores | 30 | 0.927 | 100.000 | 2.815 |
| preprocessing | snv_sg1 | pds | TD-CP+ (jackknife+) | 30 | 0.936 | 100.000 | 2.838 |
| ridge_model | ridge | pds | Gaussian TD (parametric) | 30 | 0.905 | 96.667 | 8.606 |
| ridge_model | ridge | pds | Naive CP (primary residuals) | 30 | 0.438 | 0.000 | 21.259 |
| ridge_model | ridge | pds | Target CP (k labelled) | 30 | 0.927 | 100.000 | 9.461 |
| ridge_model | ridge | pds | Target CP+ (k labelled) | 30 | 0.946 | 100.000 | 9.204 |
| ridge_model | ridge | pds | TD-CP signed (pre-specified) | 30 | 0.896 | 76.667 | 9.120 |
| ridge_model | ridge | pds | TD-CP absolute scores | 30 | 0.924 | 100.000 | 9.444 |
| ridge_model | ridge | pds | TD-CP+ (jackknife+) | 30 | 0.945 | 100.000 | 9.163 |
| simulated | severity=1 | ds | Gaussian TD (parametric) | 7 | 0.897 | 85.714 | 4.017 |
| simulated | severity=1 | ds | Naive CP (primary residuals) | 7 | 0.564 | 14.286 | 5.047 |
| simulated | severity=1 | ds | Target CP (k labelled) | 7 | 0.910 | 85.714 | 4.614 |
| simulated | severity=1 | ds | Target CP+ (k labelled) | 7 | 0.922 | 100.000 | 4.620 |
| simulated | severity=1 | ds | TD-CP signed (pre-specified) | 7 | 0.886 | 71.429 | 4.074 |
| simulated | severity=1 | ds | TD-CP absolute scores | 7 | 0.903 | 85.714 | 4.214 |
| simulated | severity=1 | ds | TD-CP+ (jackknife+) | 7 | 0.916 | 100.000 | 4.395 |
| simulated | severity=1 | pds | Gaussian TD (parametric) | 7 | 0.911 | 100.000 | 1.347 |
| simulated | severity=1 | pds | Naive CP (primary residuals) | 7 | 0.895 | 100.000 | 1.353 |
| simulated | severity=1 | pds | Target CP (k labelled) | 7 | 0.914 | 100.000 | 1.432 |
| simulated | severity=1 | pds | Target CP+ (k labelled) | 7 | 0.918 | 100.000 | 1.440 |
| simulated | severity=1 | pds | TD-CP signed (pre-specified) | 7 | 0.922 | 100.000 | 1.426 |
| simulated | severity=1 | pds | TD-CP absolute scores | 7 | 0.915 | 100.000 | 1.362 |
| simulated | severity=1 | pds | TD-CP+ (jackknife+) | 7 | 0.918 | 100.000 | 1.361 |
| simulated | severity=2 | ds | Gaussian TD (parametric) | 7 | 0.896 | 85.714 | 3.938 |
| simulated | severity=2 | ds | Naive CP (primary residuals) | 7 | 0.564 | 14.286 | 5.350 |
| simulated | severity=2 | ds | Target CP (k labelled) | 7 | 0.911 | 85.714 | 4.688 |
| simulated | severity=2 | ds | Target CP+ (k labelled) | 7 | 0.919 | 100.000 | 4.691 |
| simulated | severity=2 | ds | TD-CP signed (pre-specified) | 7 | 0.887 | 71.429 | 3.998 |
| simulated | severity=2 | ds | TD-CP absolute scores | 7 | 0.903 | 85.714 | 4.115 |
| simulated | severity=2 | ds | TD-CP+ (jackknife+) | 7 | 0.915 | 100.000 | 4.330 |
| simulated | severity=2 | pds | Gaussian TD (parametric) | 7 | 0.914 | 100.000 | 1.581 |
| simulated | severity=2 | pds | Naive CP (primary residuals) | 7 | 0.856 | 42.857 | 1.627 |
| simulated | severity=2 | pds | Target CP (k labelled) | 7 | 0.920 | 100.000 | 1.681 |
| simulated | severity=2 | pds | Target CP+ (k labelled) | 7 | 0.924 | 100.000 | 1.711 |
| simulated | severity=2 | pds | TD-CP signed (pre-specified) | 7 | 0.925 | 100.000 | 1.656 |
| simulated | severity=2 | pds | TD-CP absolute scores | 7 | 0.917 | 100.000 | 1.593 |
| simulated | severity=2 | pds | TD-CP+ (jackknife+) | 7 | 0.921 | 100.000 | 1.591 |
| simulated | severity=3 | ds | Gaussian TD (parametric) | 7 | 0.900 | 85.714 | 3.982 |
| simulated | severity=3 | ds | Naive CP (primary residuals) | 7 | 0.546 | 14.286 | 5.884 |
| simulated | severity=3 | ds | Target CP (k labelled) | 7 | 0.913 | 85.714 | 4.692 |
| simulated | severity=3 | ds | Target CP+ (k labelled) | 7 | 0.923 | 100.000 | 4.685 |
| simulated | severity=3 | ds | TD-CP signed (pre-specified) | 7 | 0.893 | 85.714 | 4.064 |
| simulated | severity=3 | ds | TD-CP absolute scores | 7 | 0.904 | 85.714 | 4.139 |
| simulated | severity=3 | ds | TD-CP+ (jackknife+) | 7 | 0.915 | 100.000 | 4.371 |
| simulated | severity=3 | pds | Gaussian TD (parametric) | 7 | 0.915 | 100.000 | 2.333 |
| simulated | severity=3 | pds | Naive CP (primary residuals) | 7 | 0.741 | 28.571 | 2.884 |
| simulated | severity=3 | pds | Target CP (k labelled) | 7 | 0.921 | 100.000 | 2.501 |
| simulated | severity=3 | pds | Target CP+ (k labelled) | 7 | 0.927 | 100.000 | 2.593 |
| simulated | severity=3 | pds | TD-CP signed (pre-specified) | 7 | 0.917 | 100.000 | 2.449 |
| simulated | severity=3 | pds | TD-CP absolute scores | 7 | 0.920 | 100.000 | 2.344 |
| simulated | severity=3 | pds | TD-CP+ (jackknife+) | 7 | 0.924 | 100.000 | 2.391 |
