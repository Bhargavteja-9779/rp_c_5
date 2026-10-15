# TD-CP: distribution-free prediction intervals for transferred NIR calibrations

This repository contains the code for the manuscript *"Distribution-free prediction intervals for multivariate calibrations transferred between spectrometers using unlabelled transfer standards"*, submitted to Analytica Chimica Acta.

Running `run_all.py` regenerates every number, table and figure in the manuscript from the public data.

## 1. Install (CPU only; no GPU needed)
```bash
python -m venv .venv && source .venv/bin/activate     # Python 3.13 (3.10+ should work)
pip install -r requirements.txt
# or: conda env create -f environment.yml && conda activate tdcp
```
The scripts detect the hardware (CPU/CUDA/MPS) and record it in `results/experiment_logs/environment.json`. The study uses only CPU linear algebra. The full run takes about 1 hour on 4 cores.

## 2. Data
Both datasets download automatically on first use, and each file is checked against its SHA-256 digest (`src/tdcp/data/datasets.py`):

| Dataset | Source | Content |
|---|---|---|
| Corn | Eigenvector Research, `corn.mat` | 80 corn samples measured on 3 NIR spectrometers (m5, mp5, mp6), 1100–2498 nm, 700 channels. Properties: moisture, oil, protein, starch |
| Tablets | Eigenvector Research, `nir_shootout_2002.mat` (IDRC 2002 shootout) | 655 tablets measured on 2 spectrometers, 600–1898 nm, 650 channels. Properties: weight, hardness, assay. Official calibrate/validate/test split: 155/40/460 |

If you cannot reach the Internet, place `corn.mat_.zip` and `nir_shootout_2002.mat_.zip` in `data/raw/`. The digests are listed in `datasets.py`. The raw data are not redistributed here. See the Eigenvector website for the terms of use.

## 3. Reproduce everything
```bash
python run_all.py --mode quick    # ~3 min: every experiment with 2–5 repetitions (pipeline check)
python run_all.py --mode full     # pre-registered study: 100 (or 50) repetitions per scenario
python run_all.py --mode full --skip-experiments   # rebuild statistics/tables/figures from saved raw results
python -m pytest -q tests         # unit tests
python ../manuscript/build_supplementary.py         # Supplementary_Material.docx
python ../manuscript/cover_letter.py                # cover_letter.docx
python ../manuscript/build_manuscript.py           # manuscript (Markdown + DOCX) with numbers read from ../results
```
Outputs:
- `../results/raw_<experiment>.csv`: one row per (split, method, α).
- `../results/raw_results.csv.gz`: all experiments combined.
- `../results/scenario_results.csv`: means per scenario.
- `../results/metrics.json`, `../results/statistics.json`, `../results/statistical_tests.csv`, `../results/validity_summary.csv`.
- `../tables/*.csv|md` and `../figures/*.png|pdf`.
- Logs: `../results/experiment_logs/`.

Quick-mode outputs go to `quick/` subfolders, so they never overwrite the full results.

## 4. What is computed
- `src/tdcp/models/regression.py`: PLS1 (NIPALS) fitted to primary spectra. The number of latent variables is chosen by minimum 10-fold RMSECV. Out-of-fold residuals r_i are the conformal calibration scores. A ridge variant is also provided.
- `src/tdcp/models/transfer.py`: PDS (window 5, local ridge), DS (pseudo-inverse) and identity.
- `src/tdcp/intervals/methods.py`: all interval methods:
  - **TD-CP (proposed)**: signed convolution of the r_i with the cross-fitted transfer discrepancies δ_j = f(x_j^P) − f(T_{−j}(x_j^S)). This needs **no reference values** on the secondary instrument.
  - Baselines: naive CP, the classical leverage interval, weighted CP (covariate shift) and Gaussian TD.
  - Methods that need labelled transfer standards: target CP and pooled CP.
  - Methods that need labelled standards also include the classical bias-corrected t-interval (M7).
  - Ablations: TD-CP without cross-fitting, with absolute scores, and the union-bound sum.
- Experiments (`config/default.yaml`): main, k_sensitivity, kennard_stone, biased_standards, preprocessing,
  parsimonious_pls, pds_window, ridge_model, noise, no_standardisation, official_split, simulated.
- `src/tdcp/experiments/`: the job plan (`plan.py`) and one split (`runner.py`). In each split, the test samples, the transfer standards and the master samples are disjoint physical samples. The primary-instrument spectra of test samples are used only for the diagnostics columns, never by any method.
- `src/tdcp/statistics/analysis.py`: scenario-level aggregation, two-sided Wilcoxon signed-rank tests across scenarios, Holm adjustment, rank-biserial effect sizes and bootstrap confidence intervals.

## 5. Configuration
Everything is set in `config/default.yaml`: scenarios, k, α levels, repetitions, hyperparameters and seeds. Seeds 0…R−1 are the split seeds and were fixed in advance (see `../supplementary/S1_topic_selection_and_preregistration.md`).

## 6. Using TD-CP on your own data
```python
from tdcp.models.regression import fit_calibration
from tdcp.models.transfer import PDS
from tdcp.intervals.methods import td_cp
cal = fit_calibration(Xp_master, y_master, "pls", max_components=15, n_folds=10, seed=0)
T = PDS(2).fit(Xp_std, Xs_std)                       # transfer standards (spectra only)
delta = [cal.predict(Xp_std[j:j+1])[0] -
         cal.predict(PDS(2).fit(np.delete(Xp_std, j, 0), np.delete(Xs_std, j, 0)).transform(Xs_std[j:j+1]))[0]
         for j in range(len(Xs_std))]
yhat = cal.predict(T.transform(Xs_new))
lo, hi = td_cp(cal.cv_residuals, np.array(delta), len(yhat), alpha=0.10)
intervals = np.c_[yhat + lo, yhat + hi]
```

## 7. Licence
Code: MIT. Data: see the original providers.
