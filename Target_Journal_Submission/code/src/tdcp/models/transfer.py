"""Instrument standardisation maps x_S -> x_P (secondary to primary).

* ``PDS``: piecewise direct standardisation (Wang, Veltkamp & Kowalski, 1991)
  with a window of 2w+1 secondary channels per primary channel, local ridge
  regression with intercept. At the spectral edges the window is shifted
  inwards so that every local model has the same width.
* ``DS``: direct standardisation via the Moore-Penrose pseudo-inverse of the
  centred secondary transfer spectra.
* ``Identity``: no standardisation (the primary model is applied directly).
"""
from __future__ import annotations

import numpy as np


class Identity:
    def fit(self, Xp: np.ndarray, Xs: np.ndarray) -> "Identity":
        return self

    def transform(self, Xs: np.ndarray) -> np.ndarray:
        return Xs


class DS:
    def __init__(self, rcond: float = 1e-6):
        self.rcond = rcond

    def fit(self, Xp: np.ndarray, Xs: np.ndarray) -> "DS":
        self.mp_, self.ms_ = Xp.mean(0), Xs.mean(0)
        self.F_ = np.linalg.pinv(Xs - self.ms_, rcond=self.rcond) @ (Xp - self.mp_)
        return self

    def transform(self, Xs: np.ndarray) -> np.ndarray:
        return (Xs - self.ms_) @ self.F_ + self.mp_


class PDS:
    def __init__(self, half_window: int = 2, ridge: float = 1e-6):
        self.w = half_window
        self.ridge = ridge

    def _windows(self, p: int) -> np.ndarray:
        m = 2 * self.w + 1
        starts = np.clip(np.arange(p) - self.w, 0, p - m)
        return starts[:, None] + np.arange(m)[None, :]  # (p, m)

    def fit(self, Xp: np.ndarray, Xs: np.ndarray) -> "PDS":
        p = Xp.shape[1]
        self.mp_, self.ms_ = Xp.mean(0), Xs.mean(0)
        A = (Xs - self.ms_)[:, self._windows(p)]  # (k, p, m)
        G = np.einsum("kpi,kpj->pij", A, A)  # (p, m, m)
        lam = self.ridge * np.trace(G, axis1=1, axis2=2)[:, None, None] + 1e-12
        G = G + lam * np.eye(G.shape[1])[None]
        rhs = np.einsum("kpi,kp->pi", A, Xp - self.mp_)  # (p, m)
        self.B_ = np.linalg.solve(G, rhs[..., None])[..., 0]  # (p, m)
        self.idx_ = self._windows(p)
        return self

    def transform(self, Xs: np.ndarray) -> np.ndarray:
        Z = (Xs - self.ms_)[:, self.idx_]  # (n, p, m)
        return np.einsum("npm,pm->np", Z, self.B_) + self.mp_


def make_transfer(name: str, cfg: dict | None = None):
    cfg = cfg or {}
    if name == "pds":
        return PDS(half_window=cfg.get("pds_half_window", 2), ridge=cfg.get("pds_ridge", 1e-6))
    if name == "ds":
        return DS(rcond=cfg.get("ds_rcond", 1e-6))
    if name == "none":
        return Identity()
    raise ValueError(name)
