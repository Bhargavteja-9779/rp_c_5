"""Spectral preprocessing and simulated instrument perturbations."""
from __future__ import annotations

import numpy as np
from scipy.ndimage import gaussian_filter1d
from scipy.signal import savgol_filter


def snv(X: np.ndarray) -> np.ndarray:
    """Standard normal variate (row-wise centring and scaling)."""
    mu = X.mean(axis=1, keepdims=True)
    sd = X.std(axis=1, ddof=1, keepdims=True)
    return (X - mu) / sd


def snv_sg1(X: np.ndarray, window: int = 11, poly: int = 2) -> np.ndarray:
    """SNV followed by a Savitzky-Golay first derivative."""
    return savgol_filter(snv(X), window_length=window, polyorder=poly, deriv=1, axis=1)


PREPROCESSORS = {"none": lambda X: X, "snv_sg1": snv_sg1}


def simulate_secondary(X: np.ndarray, severity: int, rng: np.random.Generator) -> np.ndarray:
    """Create a virtual secondary instrument from primary spectra.

    Severity levels combine (i) a wavelength-axis shift (channels, linear
    interpolation), (ii) band broadening (Gaussian kernel, channels),
    (iii) a multiplicative gain and a sloped additive baseline, and
    (iv) white noise relative to the mean per-channel SD of X.
    The perturbation is deterministic given severity except for the noise.
    """
    levels = {
        0: dict(shift=0.0, blur=0.0, gain=1.00, base=0.000, noise=0.000),
        1: dict(shift=0.5, blur=1.0, gain=1.02, base=0.005, noise=0.005),
        2: dict(shift=1.0, blur=2.0, gain=1.05, base=0.010, noise=0.010),
        3: dict(shift=2.0, blur=3.0, gain=1.10, base=0.020, noise=0.020),
    }
    p = levels[severity]
    n, m = X.shape
    grid = np.arange(m, dtype=float)
    Xs = np.array([np.interp(grid - p["shift"], grid, row) for row in X]) if p["shift"] else X.copy()
    if p["blur"]:
        Xs = gaussian_filter1d(Xs, sigma=p["blur"], axis=1, mode="nearest")
    scale = X.std(axis=0).mean()
    span = np.abs(X).mean()
    baseline = p["base"] * span * (1.0 + grid / m)
    Xs = p["gain"] * Xs + baseline
    if p["noise"]:
        Xs = Xs + rng.normal(0.0, p["noise"] * scale, size=Xs.shape)
    return Xs
