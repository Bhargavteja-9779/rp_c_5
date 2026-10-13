"""Expand the YAML configuration into the list of jobs for every experiment."""
from __future__ import annotations

from tdcp.experiments.runner import Job


def _scenarios(cfg: dict):
    for ds, d in cfg["datasets"].items():
        for prim, sec in d["pairs"]:
            for prop in d["properties"]:
                yield ds, prim, sec, prop, d["n_test"]


def build_jobs(cfg: dict, mode: str) -> dict[str, list[Job]]:
    jobs: dict[str, list[Job]] = {}
    m = cfg["main"]
    R = m["reps"][mode]
    jobs["main"] = [
        Job("main", ds, p, s, prop, tr, seed, k=m["k"], n_test=nt, alphas=tuple(m["alphas"]))
        for ds, p, s, prop, nt in _scenarios(cfg) for tr in m["transfers"] for seed in range(R)
    ]
    E = cfg["experiments"]
    e = E["k_sensitivity"]
    jobs["k_sensitivity"] = [
        Job("k_sensitivity", ds, p, s, prop, tr, seed, k=k, n_test=nt)
        for k in e["k"] for ds, p, s, prop, nt in _scenarios(cfg) for tr in e["transfers"] for seed in range(e["reps"][mode])
    ]
    e = E["kennard_stone"]
    jobs["kennard_stone"] = [
        Job("kennard_stone", ds, p, s, prop, tr, seed, n_test=nt, selection="kennard_stone")
        for ds, p, s, prop, nt in _scenarios(cfg) for tr in e["transfers"] for seed in range(e["reps"][mode])
    ]
    e = E["preprocessing"]
    jobs["preprocessing"] = [
        Job("preprocessing", ds, p, s, prop, tr, seed, n_test=nt, preprocess=e["preprocess"])
        for ds, p, s, prop, nt in _scenarios(cfg) for tr in e["transfers"] for seed in range(e["reps"][mode])
    ]
    e = E["ridge_model"]
    jobs["ridge_model"] = [
        Job("ridge_model", ds, p, s, prop, tr, seed, n_test=nt, model=e["model"])
        for ds, p, s, prop, nt in _scenarios(cfg) for tr in e["transfers"] for seed in range(e["reps"][mode])
    ]
    e = E["noise"]
    jobs["noise"] = [
        Job("noise", ds, p, s, prop, tr, seed, n_test=nt, noise=lvl)
        for lvl in e["levels"] for ds, p, s, prop, nt in _scenarios(cfg) for tr in e["transfers"] for seed in range(e["reps"][mode])
    ]
    e = E["no_standardisation"]
    jobs["no_standardisation"] = [
        Job("no_standardisation", ds, p, s, prop, tr, seed, n_test=nt)
        for ds, p, s, prop, nt in _scenarios(cfg) for tr in e["transfers"] for seed in range(e["reps"][mode])
    ]
    e = E["official_split"]
    jobs["official_split"] = [
        Job("official_split", "tablets", p, s, prop, tr, seed, protocol="official")
        for p, s in cfg["datasets"]["tablets"]["pairs"] for prop in cfg["datasets"]["tablets"]["properties"]
        for tr in e["transfers"] for seed in range(e["reps"][mode])
    ]
    e = E["simulated"]
    jobs["simulated"] = [
        Job("simulated", ds, e["primary"][ds], f"sim{sev}", prop, tr, seed, n_test=cfg["datasets"][ds]["n_test"])
        for sev in e["severities"] for ds in cfg["datasets"] for prop in cfg["datasets"][ds]["properties"]
        for tr in e["transfers"] for seed in range(e["reps"][mode])
    ]
    return jobs
