"""Scaling of interval computation with master-set size n, standards k and test-set size (synthetic scores).

Writes ../../results/scaling.csv and ../../figures/figS1_scaling.(png|pdf). Single-threaded timings;
the median of 5 repetitions is reported. Inputs are random numbers because the cost of the interval
step does not depend on the data values.
"""
from __future__ import annotations

import os

os.environ.setdefault("OMP_NUM_THREADS", "1")

import sys
import time
from pathlib import Path

import numpy as np
import pandas as pd

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "src"))
from tdcp.intervals.methods import td_cp, td_cp_plus  # noqa: E402


def bench(fn, reps=5):
    ts = []
    for _ in range(reps):
        t = time.perf_counter(); fn(); ts.append(time.perf_counter() - t)
    return float(np.median(ts))


def main():
    rng = np.random.default_rng(0)
    rows = []
    n_test = 100
    for n in (50, 200, 1000, 5000):
        for k in (5, 10, 30):
            r, d = rng.normal(size=n), rng.normal(size=k)
            yhat = rng.normal(size=n_test)
            loo = yhat[:, None] + 0.01 * rng.normal(size=(n_test, k))
            rows.append(dict(n=n, k=k, n_test=n_test, method="td_cp (signed)", seconds=bench(lambda: td_cp(r, d, n_test, 0.1))))
            rows.append(dict(n=n, k=k, n_test=n_test, method="td_cp_plus", seconds=bench(lambda: td_cp_plus(r, d, loo, yhat, 0.1))))
    df = pd.DataFrame(rows)
    df["ms_per_test_sample"] = 1000 * df.seconds / df.n_test
    root = HERE.parents[1]
    df.to_csv(root / "results" / "scaling.csv", index=False)
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots(figsize=(3.6, 2.8))
    for (m, k), g in df.groupby(["method", "k"]):
        ax.plot(g.n, g.ms_per_test_sample, marker="o" if "plus" in m else "s", lw=1.5,
                color={5: "#2a78d6", 10: "#eb6834", 30: "#1baf7a"}[k], ls="-" if "plus" in m else "--", label=f"{m}, k={k}")
    ax.set_xscale("log"); ax.set_yscale("log"); ax.set_xlabel("master-set size n"); ax.set_ylabel("ms per test sample")
    ax.legend(fontsize=5.5, frameon=False); ax.grid(True, color="#e4e3df", lw=0.5)
    fig.tight_layout(); fig.savefig(root / "figures" / "figS1_scaling.png", dpi=600); fig.savefig(root / "figures" / "figS1_scaling.pdf")
    print(df.round(5).to_string())


if __name__ == "__main__":
    main()
