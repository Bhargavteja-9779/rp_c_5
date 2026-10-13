"""Interval-quality metrics."""
from __future__ import annotations

import numpy as np


def interval_metrics(y: np.ndarray, lo: np.ndarray, hi: np.ndarray, alpha: float) -> dict:
    """Coverage, mean width and mean interval (Winkler) score (Gneiting & Raftery, 2007)."""
    covered = (y >= lo) & (y <= hi)
    width = hi - lo
    finite = np.isfinite(width)
    with np.errstate(invalid="ignore"):
        score = width + (2 / alpha) * np.where(y < lo, lo - y, 0.0) + (2 / alpha) * np.where(y > hi, y - hi, 0.0)
    return {
        "coverage": float(covered.mean()),
        "width": float(width.mean()) if finite.all() else float("inf"),
        "interval_score": float(score.mean()) if finite.all() else float("inf"),
        "frac_infinite": float((~finite).mean()),
        "below_coverage": float((y < lo).mean()),
        "above_coverage": float((y > hi).mean()),
    }


def grouped_coverage(covered: np.ndarray, groups: np.ndarray, n_groups: int = 3) -> list[float]:
    return [float(covered[groups == g].mean()) if np.any(groups == g) else float("nan") for g in range(n_groups)]
