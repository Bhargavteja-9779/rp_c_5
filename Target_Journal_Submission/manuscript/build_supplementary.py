#!/usr/bin/env python
"""Build Supplementary_Material.docx from the theory note and machine-generated tables/figures."""
from __future__ import annotations

import sys
from pathlib import Path

import pandas as pd

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from docx_writer import build_docx  # noqa: E402
import text_front as F  # noqa: E402

ROOT = HERE.parent


def fmt(df: pd.DataFrame, nd: int = 3) -> pd.DataFrame:
    df = df.copy()
    for c in df.columns:
        if df[c].dtype.kind == "f":
            df[c] = df[c].map(lambda x: "∞" if x == float("inf") else ("–" if pd.isna(x) else f"{x:.{nd}f}"))
    return df


def md_blocks(path: Path):
    out = []
    for line in path.read_text().splitlines():
        t = line.strip()
        if not t:
            continue
        if t.startswith("# "):
            out.append(("h1", t[2:]))
        elif t.startswith("## "):
            out.append(("h2", t[3:]))
        elif t.startswith("### "):
            out.append(("h3", t[4:]))
        elif t.startswith("- "):
            out.append(("bullets", [t[2:].replace("**", "")]))
        else:
            out.append(("p", t.replace("**", "")))
    return out


def main():
    t = ROOT / "tables"
    B = [("title", "Supplementary Material"), ("center", F.TITLE)]
    B += md_blocks(ROOT / "supplementary" / "S4_theory.md")
    specs = [
        ("tableS1_per_scenario", "Table S1. Per-scenario results at α = 0.10 (main experiment; coverage_se = standard error over splits)."),
        ("tableS2_main_by_dataset", "Table S2. Main results at α = 0.10 by dataset."),
        ("tableS3_alpha_levels", "Table S3. Mean coverage and validity at nominal levels 0.80, 0.90 and 0.95."),
        ("tableS4_split_level_coverage", "Table S4. Split-level (training-conditional) coverage at α = 0.10."),
        ("tableS5_stratum_consistency", "Table S5. Fraction of scenarios in which TD-CP+ beats each comparator, by dataset × transfer stratum."),
        ("tableS6_validity_tolerance", "Table S6. Fraction of valid scenarios for tolerances 0–0.03 (α = 0.10)."),
    ]
    for name, cap in specs:
        B += [("pagebreak",), ("table", fmt(pd.read_csv(t / f"{name}.csv")), cap)]
    st = pd.read_csv(ROOT / "results" / "statistical_tests.csv")
    st = st[["reference", "metric", "comparator", "n_scenarios", "median_ref", "median_comp", "median_diff", "ci95_low",
             "ci95_high", "rank_biserial", "p_value", "p_holm"]]
    for c in ("median_ref", "median_comp", "median_diff", "ci95_low", "ci95_high"):
        st[c] = st[c].map(lambda x: "∞" if x > 1e5 else ("−∞" if x < -1e5 else x))
    st["p_value"] = st["p_value"].map(lambda p: "<0.001" if p < 0.001 else f"{p:.3f}")
    st["p_holm"] = st["p_holm"].map(lambda p: "<0.001" if p < 0.001 else f"{p:.3f}")
    B += [("pagebreak",), ("table", fmt(st), f"Table S7. All paired Wilcoxon signed-rank tests (scenario level, α = 0.10), Holm-adjusted over all {len(st)} tests.")]
    B += [("pagebreak",), ("table", fmt(pd.read_csv(t / "table6_robustness.csv")), "Table S9. Robustness and generalisation experiments, all reported methods (α = 0.10; valid in %, IS/SD median).")]
    B += [("pagebreak",), ("table", fmt(pd.read_csv(t / "table7_compute.csv"), 4), "Table S8. Mean wall-clock time per split (s), single core.")]
    B += [("fig", ROOT / "figures" / "fig7_alpha_calibration.png", "**Fig. S2.** Mean empirical versus nominal coverage (PDS and DS pooled); diagonal = perfect calibration.", 9.0)]
    B += [("fig", ROOT / "figures" / "fig10_compute.png", "**Fig. S3.** Computation time per split by stage (main experiment).", 9.0)]
    B += [("pagebreak",), ("fig", ROOT / "figures" / "figS1_scaling.png",
                           "**Fig. S1.** Time per test sample of the interval step versus master-set size n for k = 5, 10, 30 "
                           "(synthetic scores, single core; results/scaling.csv).", 10.0)]
    tmp = HERE / "_build"; tmp.mkdir(exist_ok=True)
    build_docx(B, HERE / "Supplementary_Material.docx", tmp, line_numbers=False)
    print("supplementary written")


if __name__ == "__main__":
    main()
