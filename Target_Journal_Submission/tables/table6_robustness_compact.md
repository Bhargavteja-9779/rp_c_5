**Table 6. Robustness and generalisation (alpha = 0.10): mean coverage**

| experiment | condition | transfer | naive_cov | gauss_cov | tdcp_signed_cov | tdcp_plus_cov | tdcp_plus_pct_valid | target_cp_plus_cov |
|---|---|---|---|---|---|---|---|---|
| biased_standards | standards from lower half of y | ds | 0.529 | 0.824 | 0.825 | 0.876 | 60.000 | 0.880 |
| biased_standards | standards from lower half of y | pds | 0.461 | 0.894 | 0.887 | 0.939 | 100.000 | 0.942 |
| kennard_stone | KS selection | ds | 0.573 | 0.915 | 0.917 | 0.950 | 100.000 | 0.958 |
| kennard_stone | KS selection | pds | 0.482 | 0.941 | 0.936 | 0.962 | 100.000 | 0.972 |
| no_standardisation | no transfer | none | 0.283 | 0.903 | 0.917 | 0.921 | 100.000 | 0.912 |
| noise | noise=0.005 | pds | 0.406 | 0.899 | 0.888 | 0.945 | 100.000 | 0.948 |
| noise | noise=0.01 | pds | 0.365 | 0.899 | 0.888 | 0.948 | 100.000 | 0.952 |
| noise | noise=0.02 | pds | 0.339 | 0.907 | 0.895 | 0.953 | 100.000 | 0.957 |
| official_split | IDRC official split | ds | 0.780 | 0.918 | 0.907 | 0.916 | 100.000 | 0.924 |
| official_split | IDRC official split | pds | 0.826 | 0.918 | 0.908 | 0.924 | 83.333 | 0.929 |
| parsimonious_pls | PLS, 1-SE rule | ds | 0.621 | 0.888 | 0.892 | 0.927 | 100.000 | 0.927 |
| parsimonious_pls | PLS, 1-SE rule | pds | 0.576 | 0.907 | 0.905 | 0.937 | 100.000 | 0.938 |
| pds_window | PDS window 11 | pds | 0.404 | 0.891 | 0.881 | 0.946 | 100.000 | 0.950 |
| pds_window | PDS window 3 | pds | 0.536 | 0.906 | 0.903 | 0.942 | 100.000 | 0.944 |
| pds_window | PDS window 7 | pds | 0.437 | 0.907 | 0.898 | 0.950 | 100.000 | 0.952 |
| preprocessing | snv_sg1 | ds | 0.684 | 0.894 | 0.902 | 0.925 | 96.667 | 0.923 |
| preprocessing | snv_sg1 | pds | 0.762 | 0.918 | 0.930 | 0.936 | 100.000 | 0.932 |
| ridge_model | ridge | pds | 0.438 | 0.905 | 0.896 | 0.945 | 100.000 | 0.946 |
| simulated | severity=1 | ds | 0.564 | 0.897 | 0.886 | 0.916 | 100.000 | 0.922 |
| simulated | severity=1 | pds | 0.895 | 0.911 | 0.922 | 0.918 | 100.000 | 0.918 |
| simulated | severity=2 | ds | 0.564 | 0.896 | 0.887 | 0.915 | 100.000 | 0.919 |
| simulated | severity=2 | pds | 0.856 | 0.914 | 0.925 | 0.921 | 100.000 | 0.924 |
| simulated | severity=3 | ds | 0.546 | 0.900 | 0.893 | 0.915 | 100.000 | 0.923 |
| simulated | severity=3 | pds | 0.741 | 0.915 | 0.917 | 0.924 | 100.000 | 0.927 |
