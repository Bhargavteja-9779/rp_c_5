#!/usr/bin/env python
"""Reproduce every experiment, statistic, table and figure of the study.

    python run_all.py --mode quick   # pipeline check (few repetitions, ~minutes)
    python run_all.py --mode full    # full pre-registered study

Outputs (relative to this file): ../results, ../tables, ../figures.
"""
from __future__ import annotations

import argparse
import json
import logging
import os
import platform
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE / "src"))

import numpy as np  # noqa: E402
import pandas as pd  # noqa: E402
import yaml  # noqa: E402
from joblib import Parallel, delayed  # noqa: E402

from tdcp.data.datasets import load  # noqa: E402
from tdcp.experiments.plan import build_jobs  # noqa: E402
from tdcp.experiments.runner import run_job  # noqa: E402


def detect_hardware() -> dict:
    info = {"cpu_count": os.cpu_count(), "platform": platform.platform(), "python": platform.python_version(),
            "numpy": np.__version__}
    try:  # the study itself is CPU-only; accelerators are only reported
        import torch

        info["cuda"] = bool(torch.cuda.is_available())
        info["mps"] = bool(getattr(torch.backends, "mps", None) and torch.backends.mps.is_available())
    except Exception:  # torch is optional
        info["cuda"] = info["mps"] = None
    return info


def _run_chunk(jobs, datasets, cfg):
    out = []
    for j in jobs:
        out.extend(run_job(j, datasets[j.dataset], cfg))
    return out


def run_experiments(cfg: dict, mode: str, results_dir: Path, only: list[str] | None, n_jobs: int, log) -> None:
    datasets = {name: load(name, HERE / cfg["raw_dir"]) for name in cfg["datasets"]}
    plan = build_jobs(cfg, mode)
    for exp, jobs in plan.items():
        if only and exp not in only:
            continue
        out = results_dir / f"raw_{exp}.csv"
        t0 = time.time()
        chunks = [jobs[i : i + 20] for i in range(0, len(jobs), 20)]
        res = Parallel(n_jobs=n_jobs, verbose=0)(delayed(_run_chunk)(c, datasets, cfg) for c in chunks)
        df = pd.DataFrame([r for chunk in res for r in chunk])
        df.to_csv(out, index=False)
        log.info("experiment %-20s jobs=%5d rows=%6d time=%.1fs -> %s", exp, len(jobs), len(df), time.time() - t0, out.name)


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--mode", choices=["quick", "full"], default="quick")
    ap.add_argument("--config", default=str(HERE / "config" / "default.yaml"))
    ap.add_argument("--only", nargs="*", help="run only these experiments")
    ap.add_argument("--skip-experiments", action="store_true", help="only regenerate statistics/tables/figures")
    ap.add_argument("--n-jobs", type=int, default=-1)
    args = ap.parse_args(argv)

    cfg = yaml.safe_load(open(args.config))
    root = HERE
    results = (root / cfg["results_dir"] / ("quick" if args.mode == "quick" else "")).resolve()
    tables = (root / cfg["tables_dir"] / ("quick" if args.mode == "quick" else "")).resolve()
    figures = (root / cfg["figures_dir"] / ("quick" if args.mode == "quick" else "")).resolve()
    logs = results / "experiment_logs"
    for d in (results, tables, figures, logs):
        d.mkdir(parents=True, exist_ok=True)
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(message)s",
                        handlers=[logging.StreamHandler(), logging.FileHandler(logs / f"run_{args.mode}.log")])
    log = logging.getLogger("tdcp")
    hw = detect_hardware()
    log.info("mode=%s hardware=%s", args.mode, json.dumps(hw))
    (logs / "environment.json").write_text(json.dumps(hw, indent=2))

    if not args.skip_experiments:
        run_experiments(cfg, args.mode, results, args.only, args.n_jobs, log)

    from tdcp.statistics.analysis import analyse
    from tdcp.reporting.tables import dataset_table, make_tables
    from tdcp.visualization.figures import make_figures

    analyse(results, cfg, log)
    dataset_table(HERE / cfg["raw_dir"], tables)
    make_tables(results, tables, log)
    make_figures(results, figures, cfg, HERE / cfg["raw_dir"], log)
    log.info("done")


if __name__ == "__main__":
    main()
