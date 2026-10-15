"""Calibration models on primary-instrument spectra.

``PLS1`` is a NIPALS implementation that stores the regression vector for every
number of latent variables, so that K-fold cross-validation over 1..A_max
components needs a single fit per fold. ``fit_calibration`` selects the
complexity by minimum RMSECV and returns out-of-fold residuals, which serve as
the conformal calibration scores of the primary instrument.
"""
from __future__ import annotations

from dataclasses import dataclass

import numpy as np
from sklearn.decomposition import PCA
from sklearn.linear_model import Ridge
from sklearn.model_selection import KFold


class PLS1:
    def __init__(self, n_components: int):
        self.n_components = n_components

    def fit(self, X: np.ndarray, y: np.ndarray) -> "PLS1":
        self.x_mean_ = X.mean(axis=0)
        self.y_mean_ = float(y.mean())
        E = X - self.x_mean_
        f = y - self.y_mean_
        A = min(self.n_components, X.shape[0] - 1, X.shape[1])
        p_dim = X.shape[1]
        W = np.zeros((p_dim, A))
        P = np.zeros((p_dim, A))
        q = np.zeros(A)
        for a in range(A):
            w = E.T @ f
            nw = np.linalg.norm(w)
            if nw < 1e-14:
                A = a
                break
            w /= nw
            t = E @ w
            tt = t @ t
            P[:, a] = E.T @ t / tt
            q[a] = (f @ t) / tt
            W[:, a] = w
            E = E - np.outer(t, P[:, a])
            f = f - q[a] * t
        W, P, q = W[:, :A], P[:, :A], q[:A]
        self.n_components_ = A
        # coefficient path: B[:, a-1] is the regression vector with a components
        self.coef_path_ = np.zeros((p_dim, A))
        for a in range(1, A + 1):
            R = W[:, :a] @ np.linalg.inv(P[:, :a].T @ W[:, :a])
            self.coef_path_[:, a - 1] = R @ q[:a]
        self.R_ = W @ np.linalg.inv(P.T @ W)
        self.train_scores_ = (X - self.x_mean_) @ self.R_
        return self

    def predict(self, X: np.ndarray, n_components: int | None = None) -> np.ndarray:
        a = self.n_components_ if n_components is None else n_components
        return (X - self.x_mean_) @ self.coef_path_[:, a - 1] + self.y_mean_

    def predict_path(self, X: np.ndarray) -> np.ndarray:
        return (X - self.x_mean_) @ self.coef_path_ + self.y_mean_

    def scores(self, X: np.ndarray, n_components: int | None = None) -> np.ndarray:
        a = self.n_components_ if n_components is None else n_components
        return ((X - self.x_mean_) @ self.R_)[:, :a]

    def leverage(self, X: np.ndarray, n_components: int | None = None) -> np.ndarray:
        """Leverage of new spectra relative to the training scores (without the 1/n term)."""
        a = self.n_components_ if n_components is None else n_components
        T = self.train_scores_[:, :a]
        G = np.linalg.inv(T.T @ T)
        S = self.scores(X, a)
        return np.einsum("ij,jk,ik->i", S, G, S)


@dataclass
class Calibration:
    """A fitted primary-instrument calibration and its cross-validated residuals."""

    kind: str
    model: object
    n_components: int  # PLS latent variables (or 0 for ridge)
    cv_residuals: np.ndarray  # y_i - f_{-fold(i)}(x_i)
    rmsecv: float
    feature_fn: object  # x -> low-dimensional features used by weighted CP

    def predict(self, X: np.ndarray) -> np.ndarray:
        if self.kind == "pls":
            return self.model.predict(X, self.n_components)
        return self.model.predict(X)

    def leverage(self, X: np.ndarray) -> np.ndarray | None:
        if self.kind == "pls":
            return self.model.leverage(X, self.n_components)
        return None


def _folds(n: int, n_folds: int, seed: int):
    return KFold(n_splits=min(n_folds, n), shuffle=True, random_state=seed).split(np.arange(n))


def fit_calibration(X: np.ndarray, y: np.ndarray, kind: str, max_components: int, n_folds: int, seed: int) -> Calibration:
    n = X.shape[0]
    if kind in ("pls", "pls_1se"):
        A = min(max_components, n - n // n_folds - 2)
        oof = np.zeros((n, A))
        fold_id = np.zeros(n, dtype=int)
        for fi, (tr, te) in enumerate(_folds(n, n_folds, seed)):
            fold_id[te] = fi
            m = PLS1(A).fit(X[tr], y[tr])
            path = m.predict_path(X[te])
            oof[te, : path.shape[1]] = path
            if path.shape[1] < A:  # rank-deficient fold: carry the last available solution forward
                oof[te, path.shape[1]:] = path[:, -1:]
        rmse = np.sqrt(((oof - y[:, None]) ** 2).mean(axis=0))
        a_best = int(np.argmin(rmse)) + 1
        if kind == "pls_1se":  # one-standard-error rule on fold-wise MSE (more parsimonious model)
            fm = np.array([((oof[fold_id == f] - y[fold_id == f, None]) ** 2).mean(axis=0) for f in np.unique(fold_id)])
            se = fm[:, a_best - 1].std(ddof=1) / np.sqrt(fm.shape[0])
            a_best = int(np.flatnonzero(fm.mean(axis=0) <= fm[:, a_best - 1].mean() + se)[0]) + 1
        model = PLS1(A).fit(X, y)
        a_best = min(a_best, model.n_components_)
        res = y - oof[:, a_best - 1]
        return Calibration("pls", model, a_best, res, float(np.sqrt(np.mean(res**2))), lambda Z, m=model, a=a_best: m.scores(Z, a))
    if kind == "ridge":
        alphas = np.logspace(-6, 2, 17)
        Xc_scale = np.trace((X - X.mean(0)).T @ (X - X.mean(0))) / X.shape[1]
        oof = np.zeros((n, len(alphas)))
        for tr, te in _folds(n, n_folds, seed):
            for j, a in enumerate(alphas):
                oof[te, j] = Ridge(alpha=a * Xc_scale).fit(X[tr], y[tr]).predict(X[te])
        rmse = np.sqrt(((oof - y[:, None]) ** 2).mean(axis=0))
        j = int(np.argmin(rmse))
        model = Ridge(alpha=alphas[j] * Xc_scale).fit(X, y)
        res = y - oof[:, j]
        pca = PCA(n_components=min(10, n - 1)).fit(X)
        return Calibration("ridge", model, 0, res, float(np.sqrt(np.mean(res**2))), pca.transform)
    raise ValueError(kind)
