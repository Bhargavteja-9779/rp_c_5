import sys
from pathlib import Path

import numpy as np
import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from tdcp.data.datasets import load  # noqa: E402

RAW = ROOT / "data" / "raw"


@pytest.mark.parametrize("name,n,p,props,insts", [
    ("corn", 80, 700, 4, 3),
    ("tablets", 655, 650, 3, 2),
])
def test_dataset_shapes(name, n, p, props, insts):
    d = load(name, RAW)  # downloads and verifies SHA-256 if needed
    assert d.y.shape == (n, props)
    assert len(d.instruments) == insts
    for X in d.spectra.values():
        assert X.shape == (n, p) and np.isfinite(X).all()


def test_tablet_official_split_sizes():
    d = load("tablets", RAW)
    vals, counts = np.unique(d.official_split, return_counts=True)
    assert dict(zip(vals, counts)) == {"calibrate": 155, "validate": 40, "test": 460}


def test_split_disjointness():
    from tdcp.experiments.runner import Job, _split

    d = load("corn", RAW)
    job = Job("t", "corn", "m5", "mp5", 0, "pds", 3, k=10, n_test=25)
    master, tr, test = _split(job, d, d.spectra["m5"], np.ones(80, bool), np.random.default_rng(3))
    assert len(set(master) & set(tr)) == 0 and len(set(master) & set(test)) == 0 and len(set(tr) & set(test)) == 0
    assert len(master) + len(tr) + len(test) == 80
