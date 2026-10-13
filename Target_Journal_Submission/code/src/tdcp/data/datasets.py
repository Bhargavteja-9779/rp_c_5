"""Download, verify and parse the public paired multi-instrument NIR datasets.

Both datasets are distributed by Eigenvector Research as PLS_Toolbox ``DataSet``
objects inside .mat files; they are parsed with ``scipy.io.loadmat`` without
MATLAB. Files are verified against the SHA-256 digests recorded on first use
(13 Oct 2026) so that every run uses byte-identical data.
"""
from __future__ import annotations

import hashlib
import io
import urllib.request
import zipfile
from dataclasses import dataclass, field
from pathlib import Path

import numpy as np
import scipy.io as sio

SOURCES = {
    "corn": {
        "url": "https://eigenvector.com/wp-content/uploads/2019/06/corn.mat_.zip",
        "sha256": "8a2d1a03648b6ad334caaafa5d8377bf945ba1477a5082c4963d705d07cca795",
        "member": "corn.mat",
    },
    "tablets": {
        "url": "https://eigenvector.com/wp-content/uploads/2019/06/nir_shootout_2002.mat_.zip",
        "sha256": "04c03a4314ab8e8f63e0ecc788b657b5d1b5450791ce465ad41ad90cb5d52125",
        "member": "nir_shootout_2002.mat",
    },
}


@dataclass
class PairedSpectra:
    """Spectra of the same physical samples on several instruments."""

    name: str
    spectra: dict[str, np.ndarray]  # instrument -> (n_samples, n_wavelengths)
    y: np.ndarray  # (n_samples, n_properties)
    properties: list[str]
    wavelengths: np.ndarray
    official_split: np.ndarray | None = None  # per-sample label, if the dataset has one
    notes: dict = field(default_factory=dict)

    @property
    def instruments(self) -> list[str]:
        return list(self.spectra)

    @property
    def n_samples(self) -> int:
        return self.y.shape[0]


def _download(name: str, raw_dir: Path) -> Path:
    src = SOURCES[name]
    raw_dir.mkdir(parents=True, exist_ok=True)
    zpath = raw_dir / Path(src["url"]).name
    if not zpath.exists():
        req = urllib.request.Request(src["url"], headers={"User-Agent": "Mozilla/5.0 (tdcp reproducibility script)"})
        with urllib.request.urlopen(req, timeout=120) as resp:
            zpath.write_bytes(resp.read())
    digest = hashlib.sha256(zpath.read_bytes()).hexdigest()
    if digest != src["sha256"]:
        raise RuntimeError(f"SHA-256 mismatch for {zpath}: {digest} != {src['sha256']}")
    return zpath


def _read_member(zpath: Path, member: str) -> dict:
    with zipfile.ZipFile(zpath) as zf:
        names = [n for n in zf.namelist() if n.endswith(member) and "__MACOSX" not in n]
        return sio.loadmat(io.BytesIO(zf.read(names[0])))


def _ds_data(obj) -> np.ndarray:
    return np.asarray(obj[0, 0]["data"], dtype=float)


def _ds_axis(obj, mode: int = 1) -> np.ndarray:
    return np.asarray(obj[0, 0]["axisscale"][mode, 0], dtype=float).ravel()


def _ds_labels(obj, mode: int = 1) -> list[str]:
    return [str(s).strip() for s in obj[0, 0]["label"][mode, 0]]


def load_corn(raw_dir: Path) -> PairedSpectra:
    d = _read_member(_download("corn", raw_dir), SOURCES["corn"]["member"])
    spectra = {inst: _ds_data(d[f"{inst}spec"]) for inst in ("m5", "mp5", "mp6")}
    return PairedSpectra(
        name="corn",
        spectra=spectra,
        y=_ds_data(d["propvals"]),
        properties=[p.lower() for p in _ds_labels(d["propvals"])],
        wavelengths=_ds_axis(d["m5spec"]),
        notes={"source": SOURCES["corn"]["url"]},
    )


def load_tablets(raw_dir: Path) -> PairedSpectra:
    d = _read_member(_download("tablets", raw_dir), SOURCES["tablets"]["member"])
    parts = ("calibrate", "validate", "test")
    spectra = {inst: np.vstack([_ds_data(d[f"{p}_{inst}"]) for p in parts]) for inst in ("1", "2")}
    y = np.vstack([_ds_data(d[f"{p}_Y"]) for p in parts])
    split = np.concatenate([[p] * _ds_data(d[f"{p}_Y"]).shape[0] for p in parts])
    return PairedSpectra(
        name="tablets",
        spectra={f"inst{k}": v for k, v in spectra.items()},
        y=y,
        properties=_ds_labels(d["calibrate_Y"]),
        wavelengths=_ds_axis(d["calibrate_1"]),
        official_split=split,
        notes={"source": SOURCES["tablets"]["url"]},
    )


LOADERS = {"corn": load_corn, "tablets": load_tablets}


def load(name: str, raw_dir: str | Path) -> PairedSpectra:
    return LOADERS[name](Path(raw_dir))
