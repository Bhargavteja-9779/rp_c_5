import math
import sys
from pathlib import Path

import numpy as np
import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from tdcp.intervals import methods as M  # noqa: E402
from tdcp.models.regression import PLS1, fit_calibration  # noqa: E402
from tdcp.models.transfer import DS, PDS  # noqa: E402
from tdcp.experiments.runner import kennard_stone  # noqa: E402


def test_conformal_quantile_rank_and_infinity():
    s = np.arange(1, 10, dtype=float)  # n = 9
    assert M.conformal_quantile(s, 0.9) == 9.0  # ceil(10*0.9)=9
    assert M.conformal_quantile(s, 0.95) == math.inf  # ceil(9.5)=10 > 9
    assert M.conformal_quantile(s, 0.5) == 5.0


def test_naive_cp_is_valid_under_exchangeability():
    rng = np.random.default_rng(0)
    covs = []
    for _ in range(400):
        r = rng.standard_t(4, 50)
        lo, hi = M.naive_cp(r, 200, 0.1)
        y = rng.standard_t(4, 200)
        covs.append(np.mean((y >= lo) & (y <= hi)))
    assert abs(np.mean(covs) - 0.9) < 0.01


def test_td_cp_valid_for_independent_shifted_errors():
    """If target error = r + delta with independent components, TD-CP covers at ~1-alpha."""
    rng = np.random.default_rng(1)
    covs = []
    for _ in range(400):
        r = rng.normal(0, 1, 60)
        d = rng.normal(0.8, 1.5, 30)  # biased, wider discrepancy
        lo, hi = M.td_cp(r, d, 300, 0.1)
        y = rng.normal(0, 1, 300) + rng.normal(0.8, 1.5, 300)
        covs.append(np.mean((y >= lo) & (y <= hi)))
    assert np.mean(covs) >= 0.89
    # the naive interval ignores the discrepancy and under-covers
    lo, hi = M.naive_cp(rng.normal(0, 1, 60), 300, 0.1)
    y = rng.normal(0, 1, 300) + rng.normal(0.8, 1.5, 300)
    assert np.mean((y >= lo) & (y <= hi)) < 0.8


def test_td_cp_signed_bounds_are_asymmetric_with_bias():
    r = np.linspace(-1, 1, 41)
    d = np.full(10, 2.0)
    lo, hi = M.td_cp(r, d, 3, 0.1)
    assert lo[0] > 0.9 and hi[0] < 3.1


def test_td_cp_reduces_to_naive_when_delta_zero():
    rng = np.random.default_rng(2)
    r = rng.normal(size=99)
    lo, hi = M.td_cp(r, np.zeros(5), 1, 0.1)
    # two one-sided alpha/2 quantiles of the signed residuals
    s = np.sort(r)
    idx = math.ceil(0.95 * 100)
    assert hi[0] == pytest.approx(s[idx - 1]) and lo[0] == pytest.approx(s[99 - idx])


def test_weighted_cp_close_to_naive_without_shift():
    rng = np.random.default_rng(3)
    X = rng.normal(size=(300, 3))
    Z = rng.normal(size=(300, 3))
    r = rng.normal(size=300)
    lo, hi = M.weighted_cp(r, X, Z, 0.1)
    q = M.conformal_quantile(np.abs(r), 0.9)
    assert np.median(hi) == pytest.approx(q, rel=0.15)


def test_pls1_matches_sklearn():
    from sklearn.cross_decomposition import PLSRegression

    rng = np.random.default_rng(4)
    X = rng.normal(size=(60, 30))
    y = X[:, :3] @ np.array([1.0, -2.0, 0.5]) + 0.1 * rng.normal(size=60)
    for a in (1, 3, 6):
        ours = PLS1(a).fit(X, y).predict(X[:10])
        ref = PLSRegression(n_components=a, scale=False).fit(X, y).predict(X[:10]).ravel()
        np.testing.assert_allclose(ours, ref, rtol=1e-6, atol=1e-8)


def test_fit_calibration_returns_oof_residuals():
    rng = np.random.default_rng(5)
    X = rng.normal(size=(80, 40))
    y = X[:, 0] + 0.2 * rng.normal(size=80)
    cal = fit_calibration(X, y, "pls", 10, 10, 0)
    assert cal.cv_residuals.shape == (80,)
    assert 1 <= cal.n_components <= 10
    assert cal.rmsecv > 0.1  # out-of-fold residuals are not training residuals


def test_pds_and_ds_recover_linear_instrument_difference():
    rng = np.random.default_rng(6)
    grid = np.linspace(0, 1, 120)
    comps = np.array([np.exp(-((grid - c) / 0.05) ** 2) for c in (0.2, 0.45, 0.7)])
    C = rng.uniform(0.2, 1.0, size=(40, 3))
    Xp = C @ comps + 0.1
    Xs = 1.05 * Xp + 0.02 + 0.01 * grid  # gain + sloped baseline
    for T in (PDS(2), DS()):
        T.fit(Xp[:12], Xs[:12])
        err = np.abs(T.transform(Xs[12:]) - Xp[12:]).max()
        assert err < 1e-3, (type(T).__name__, err)


def test_kennard_stone_starts_with_most_distant_pair():
    X = np.array([[0.0], [1.0], [10.0], [5.0], [4.0]])
    sel = kennard_stone(X, 3)
    assert set(sel[:2]) == {0, 2} and sel[2] == 3


def test_interval_score_definition():
    from tdcp.evaluation.metrics import interval_metrics

    y = np.array([0.0, 2.0, -3.0])
    m = interval_metrics(y, np.full(3, -1.0), np.full(3, 1.0), 0.2)
    # widths 2; penalties: y=2 -> 10*(1)=10 ; y=-3 -> 10*2=20
    assert m["interval_score"] == pytest.approx((2 + 12 + 22) / 3)
    assert m["coverage"] == pytest.approx(1 / 3)


def test_td_cp_plus_reduces_to_abs_when_transfer_is_stable():
    rng = np.random.default_rng(7)
    r, d = rng.normal(size=60), rng.normal(0.3, 0.5, size=12)
    yhat = np.array([1.0, 2.0])
    loo = np.repeat(yhat[:, None], 12, axis=1)  # identical leave-one-out predictions
    lo_p, hi_p = M.td_cp_plus(r, d, loo, yhat, 0.1)
    lo_a, hi_a = M.td_cp_abs(r, d, 2, 0.1)
    np.testing.assert_allclose(hi_p, hi_a)
    # lower bound uses floor(alpha (n+1)k) -> same order statistic of |r+delta|
    np.testing.assert_allclose(lo_p, lo_a)


def test_target_cp_plus_valid_on_exchangeable_data():
    rng = np.random.default_rng(8)
    covs = []
    for _ in range(300):
        e = rng.normal(size=19)
        loo = rng.normal(0, 0.05, size=(100, 19))
        y = rng.normal(size=100)
        lo, hi = M.target_cp_plus(e, loo, np.zeros(100), 0.1)
        covs.append(np.mean((y >= lo) & (y <= hi)))
    assert np.mean(covs) >= 0.88
