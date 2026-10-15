"""Publication figures, generated only from result files and the public data.

Colour follows the method (fixed categorical order); identity is never carried by
colour alone because every panel also labels methods on an axis or in a legend.
"""
from __future__ import annotations

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402
import pandas as pd  # noqa: E402
from matplotlib.patches import FancyBboxPatch  # noqa: E402

from tdcp.data.datasets import load  # noqa: E402
from tdcp.experiments.runner import Job, run_job  # noqa: E402
from tdcp.reporting.tables import METHOD_LABELS  # noqa: E402

COLORS = {
    "td_cp_plus": "#2a78d6", "td_cp": "#9fbbe0", "target_cp_plus": "#5fa35f", "naive_cp": "#eb6834", "leverage": "#1baf7a", "weighted_cp": "#eda100",
    "gauss_td": "#e87ba4", "target_cp": "#008300", "pooled_cp": "#6250d6", "td_cp_insample": "#e34948",
    "td_cp_abs": "#1a4f8f", "td_sum": "#8c8a83",
}
SHORT = {
    "naive_cp": "Naive CP", "leverage": "Leverage PI", "weighted_cp": "Weighted CP", "gauss_td": "Gauss-TD",
    "td_cp": "TD-CP\nsigned", "target_cp": "Target CP*", "pooled_cp": "Pooled CP*", "td_cp_insample": "TD-CP\nno cross-fit",
    "td_cp_abs": "TD-CP\nabs.", "td_sum": "TD-sum", "td_cp_plus": "TD-CP+", "target_cp_plus": "Target CP+*",
}
INK, MUTED = "#0b0b0b", "#52514e"


def _style():
    plt.rcParams.update({
        "font.family": "DejaVu Sans", "font.size": 8, "axes.titlesize": 9, "axes.labelsize": 8,
        "axes.edgecolor": MUTED, "axes.linewidth": 0.6, "xtick.color": MUTED, "ytick.color": MUTED,
        "axes.grid": True, "grid.color": "#e4e3df", "grid.linewidth": 0.5, "axes.axisbelow": True,
        "axes.spines.top": False, "axes.spines.right": False, "savefig.dpi": 600, "legend.frameon": False,
    })


def _save(fig, out: Path, name: str):
    fig.savefig(out / f"{name}.png", bbox_inches="tight", dpi=600)
    fig.savefig(out / f"{name}.pdf", bbox_inches="tight")
    plt.close(fig)


def fig_workflow(out: Path):
    """Schematic of the TD-CP construction (not a data figure)."""
    fig, ax = plt.subplots(figsize=(7.2, 2.9))
    ax.set_axis_off(); ax.set_xlim(0, 10); ax.set_ylim(0, 4)
    boxes = [
        (0.1, 2.5, 2.3, 1.2, "Primary instrument P\nlabelled master set\n$\\{(x_i^P,\\, y_i)\\}_{i=1}^{n}$", "#dbe8f8"),
        (0.1, 0.4, 2.3, 1.2, "Transfer standards\nmeasured on P and S\n$\\{(x_j^P,\\, x_j^S)\\}_{j=1}^{k}$  (no y)", "#fde3d6"),
        (3.0, 2.5, 2.4, 1.2, "PLS calibration $f$\nout-of-fold residuals\n$r_i = y_i - f_{-\\kappa(i)}(x_i^P)$", "#dbe8f8"),
        (3.0, 0.4, 2.4, 1.2, "Cross-fitted maps $T_{-j}$\nreference-free discrepancies\n$\\delta_j = f(x_j^P) - f(T_{-j}(x_j^S))$", "#fde3d6"),
        (6.0, 1.45, 1.9, 1.2, "Combine radii\n$|r_i + \\delta_j|$\n(n+1)-corrected\norder statistics", "#e9e6f8"),
        (8.3, 1.45, 1.6, 1.2, "New spectrum $x^S$:\nTD-CP+ interval\naround $f(T_{-j}(x^S))$", "#e1f2ea"),
    ]
    for x, y, w, h, txt, c in boxes:
        ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.03,rounding_size=0.08", fc=c, ec=MUTED, lw=0.6))
        ax.text(x + w / 2, y + h / 2, txt, ha="center", va="center", fontsize=6.6, color=INK)
    arrows = [((2.4, 3.1), (3.0, 3.1)), ((2.4, 1.0), (3.0, 1.0)), ((5.4, 3.1), (6.0, 2.3)), ((5.4, 1.0), (6.0, 1.8)), ((7.9, 2.05), (8.3, 2.05))]
    for a, b in arrows:
        ax.annotate("", xy=b, xytext=a, arrowprops=dict(arrowstyle="-|>", color=MUTED, lw=0.8))
    ax.text(5.0, 3.85, "$y - f(T(x^S)) = [y - f(x^P)] + [f(x^P) - f(T(x^S))] = r + \\delta$", ha="center", fontsize=8.5, color=INK)
    _save(fig, out, "fig1_workflow")


def fig_spectra(raw_dir: Path, out: Path):
    corn, tab = load("corn", raw_dir), load("tablets", raw_dir)
    fig, axes = plt.subplots(2, 2, figsize=(7.2, 4.4))
    cols = ["#2a78d6", "#eb6834", "#1baf7a"]
    for c, (d, title) in enumerate([(corn, "Corn (80 samples)"), (tab, "Pharmaceutical tablets (655 samples)")]):
        ref = None
        for i, inst in enumerate(d.instruments):
            m = d.spectra[inst].mean(0)
            axes[0, c].plot(d.wavelengths, m, lw=1.2, color=cols[i], label=inst)
            if ref is None:
                ref = m
            else:
                axes[1, c].plot(d.wavelengths, m - ref, lw=1.2, color=cols[i], label=f"{inst} − {d.instruments[0]}")
        axes[0, c].set_title(title); axes[0, c].set_ylabel("Mean absorbance (a.u.)"); axes[0, c].legend(fontsize=7)
        axes[1, c].set_xlabel("Wavelength (nm)"); axes[1, c].set_ylabel("Mean difference"); axes[1, c].legend(fontsize=7)
        axes[1, c].axhline(0, color=MUTED, lw=0.5)
    fig.tight_layout()
    _save(fig, out, "fig2_spectra")


def _box(ax, data, methods, ylabel, ref=None, log=False):
    vals = [data[data.method == m]["value"].replace(np.inf, np.nan).dropna().to_numpy() for m in methods]
    bp = ax.boxplot(vals, positions=range(len(methods)), widths=0.6, patch_artist=True, showfliers=False,
                    medianprops=dict(color=INK, lw=1))
    for p, m in zip(bp["boxes"], methods):
        p.set_facecolor(COLORS[m]); p.set_alpha(0.55); p.set_edgecolor(MUTED); p.set_linewidth(0.6)
    rng = np.random.default_rng(0)
    for i, v in enumerate(vals):
        ax.scatter(i + rng.uniform(-0.18, 0.18, v.size), v, s=6, color=COLORS[methods[i]], edgecolor="white", lw=0.3, zorder=3)
    if ref is not None:
        ax.axhline(ref, color=INK, lw=0.8, ls="--")
    ax.set_xticks(range(len(methods)), [SHORT[m] for m in methods], fontsize=7)
    ax.set_ylabel(ylabel)
    if log:
        ax.set_yscale("log")


def fig_main(scen: pd.DataFrame, out: Path):
    methods = ["naive_cp", "leverage", "weighted_cp", "gauss_td", "td_cp", "td_cp_abs", "td_cp_plus", "target_cp", "target_cp_plus"]
    main = scen[(scen.experiment == "main") & (scen.alpha == 0.1)]
    fig, axes = plt.subplots(2, 2, figsize=(7.2, 5.6), sharex=True)
    for c, tr in enumerate(["pds", "ds"]):
        g = main[main.transfer == tr]
        _box(axes[0, c], g.assign(value=g.coverage), methods, "Empirical coverage", ref=0.9)
        axes[0, c].set_title(f"{tr.upper()} transfer — coverage (nominal 0.90)")
        axes[0, c].set_ylim(-0.02, 1.02)
        _box(axes[1, c], g.assign(value=g.is_norm), methods, "Interval score / SD(y)", log=True)
        axes[1, c].set_title(f"{tr.upper()} transfer — interval score (lower is better)")
        axes[1, c].tick_params(axis="x", rotation=45)
    reps = int(main.reps.median())
    fig.text(0.01, 0.005, f"* requires reference values for the k transfer standards. Points = scenarios (mean of {reps} splits). "
             "Weighted CP is omitted from the score panels where its intervals were infinite.", fontsize=7, color=MUTED)
    fig.tight_layout(rect=(0, 0.02, 1, 1))
    _save(fig, out, "fig3_main_results")


def fig_ablation(scen: pd.DataFrame, out: Path):
    methods = ["td_cp_plus", "td_cp_abs", "td_cp", "td_cp_insample", "td_sum", "gauss_td", "naive_cp"]
    main = scen[(scen.experiment == "main") & (scen.alpha == 0.1)]
    fig, axes = plt.subplots(1, 2, figsize=(7.2, 2.8))
    _box(axes[0], main.assign(value=main.gap), methods, "Coverage − 0.90", ref=0.0)
    axes[0].set_title("Coverage gap (PDS and DS scenarios)")
    _box(axes[1], main.assign(value=main.is_norm), methods, "Interval score / SD(y)", log=True)
    axes[1].set_title("Interval score")
    for a in axes:
        a.tick_params(axis="x", rotation=45)
    fig.tight_layout()
    _save(fig, out, "fig4_ablation")


def _line_panel(ax, g, xcol, methods, ycol, ref=None):
    for m in methods:
        h = g[g.method == m].groupby(xcol)[ycol].agg(["mean", "std", "count"]).reset_index()
        if h.empty:
            continue
        se = h["std"] / np.sqrt(h["count"])
        ax.errorbar(h[xcol], h["mean"], yerr=1.96 * se, color=COLORS[m], lw=1.5, marker="o", ms=4, capsize=2, label=SHORT[m].replace("\n", " "))
    if ref is not None:
        ax.axhline(ref, color=INK, lw=0.8, ls="--")


def fig_k(scen: pd.DataFrame, out: Path):
    methods = ["naive_cp", "gauss_td", "td_cp", "td_cp_plus", "target_cp", "target_cp_plus"]
    g = scen[(scen.alpha == 0.1) & ((scen.experiment == "k_sensitivity") | (scen.experiment == "main"))]
    fig, axes = plt.subplots(2, 2, figsize=(7.2, 4.8), sharex=True)
    for c, tr in enumerate(["pds", "ds"]):
        h = g[g.transfer == tr]
        _line_panel(axes[0, c], h, "k", methods, "coverage", ref=0.9)
        axes[0, c].set_title(f"{tr.upper()}: coverage vs number of transfer standards")
        axes[0, c].set_ylabel("Mean coverage (±95% CI over scenarios)")
        h2 = h.replace(np.inf, np.nan)
        _line_panel(axes[1, c], h2, "k", methods, "is_norm")
        axes[1, c].set_yscale("log"); axes[1, c].set_xlabel("k (transfer standards)"); axes[1, c].set_ylabel("Interval score / SD(y)")
    axes[0, 0].legend(fontsize=7, ncol=2)
    fig.tight_layout()
    _save(fig, out, "fig5_k_sensitivity")


def fig_robust(scen: pd.DataFrame, out: Path):
    methods = ["naive_cp", "gauss_td", "td_cp", "td_cp_plus", "target_cp_plus"]
    s = scen[scen.alpha == 0.1]
    fig, axes = plt.subplots(1, 3, figsize=(7.2, 2.7), sharey=True)
    sim = s[s.experiment == "simulated"].assign(sev=lambda d: d.secondary.str[3:].astype(int))
    _line_panel(axes[0], sim, "sev", methods, "coverage", ref=0.9)
    axes[0].set_xlabel("Simulated shift severity"); axes[0].set_ylabel("Mean coverage"); axes[0].set_title("Virtual secondary instruments")
    noi = pd.concat([s[(s.experiment == "main") & (s.transfer == "pds")], s[s.experiment == "noise"]])
    _line_panel(axes[1], noi, "noise", methods, "coverage", ref=0.9)
    axes[1].set_xlabel("Added noise (× mean channel SD)"); axes[1].set_title("Noise on secondary (PDS)")
    other = s[s.experiment.isin(["main", "kennard_stone", "preprocessing", "ridge_model", "no_standardisation", "official_split"]) & s.method.isin(methods)]
    other = other[~((other.experiment == "main") & (other.transfer != "pds"))]
    labels = {"main": "random\n(main)", "kennard_stone": "KS\nselection", "preprocessing": "SNV+SG1",
              "ridge_model": "ridge\nmodel", "no_standardisation": "no\ntransfer", "official_split": "IDRC\nofficial"}
    order = list(labels)
    for i, m in enumerate(methods):
        means = [other[(other.experiment == e) & (other.method == m)].coverage.mean() for e in order]
        axes[2].scatter(np.arange(len(order)) + (i - 2) * 0.13, means, color=COLORS[m], s=18, label=SHORT[m], zorder=3)
    axes[2].axhline(0.9, color=INK, lw=0.8, ls="--")
    axes[2].set_xticks(range(len(order)), [labels[e] for e in order], fontsize=6.5)
    axes[2].set_title("Other conditions (mean over scenarios)")
    axes[0].legend(fontsize=6.5)
    fig.tight_layout()
    _save(fig, out, "fig6_robustness")


def fig_alpha(scen: pd.DataFrame, out: Path):
    methods = ["naive_cp", "leverage", "weighted_cp", "gauss_td", "td_cp", "td_cp_plus", "target_cp", "target_cp_plus"]
    g = scen[scen.experiment == "main"].assign(nominal=lambda d: 1 - d.alpha)
    fig, ax = plt.subplots(figsize=(3.4, 3.0))
    _line_panel(ax, g, "nominal", methods, "coverage")
    ax.plot([0.75, 1], [0.75, 1], color=INK, lw=0.8, ls="--")
    ax.set_xlabel("Nominal coverage 1 − α"); ax.set_ylabel("Mean empirical coverage")
    ax.legend(fontsize=6.5)
    fig.tight_layout()
    _save(fig, out, "fig7_alpha_calibration")


def fig_error(scen: pd.DataFrame, raw: pd.DataFrame, out: Path):
    main = raw[(raw.experiment == "main") & (raw.alpha == 0.1)]
    methods = ["naive_cp", "leverage", "gauss_td", "td_cp", "td_cp_plus", "target_cp_plus"]
    fig, axes = plt.subplots(1, 3, figsize=(7.2, 2.7))
    w = 0.13
    for i, m in enumerate(methods):
        h = main[main.method == m]
        vals = [h[c].mean() for c in ["cov_ylow", "cov_ymid", "cov_yhigh"]]
        axes[0].bar(np.arange(3) + (i - 2.5) * w, vals, width=w * 0.9, color=COLORS[m], label=SHORT[m])
    axes[0].axhline(0.9, color=INK, lw=0.8, ls="--"); axes[0].set_xticks(range(3), ["low y", "mid y", "high y"])
    axes[0].set_ylabel("Conditional coverage"); axes[0].set_title("By reference-value tertile"); axes[0].legend(fontsize=6)
    for i, m in enumerate(methods):
        h = main[main.method == m]
        vals = [h[c].mean() for c in ["cov_levlow", "cov_levmid", "cov_levhigh"]]
        axes[1].bar(np.arange(3) + (i - 2.5) * w, vals, width=w * 0.9, color=COLORS[m])
    axes[1].axhline(0.9, color=INK, lw=0.8, ls="--"); axes[1].set_xticks(range(3), ["low h", "mid h", "high h"])
    axes[1].set_title("By leverage tertile (test set)")
    s = scen[(scen.experiment == "main") & (scen.alpha == 0.1) & (scen.method == "td_cp")]
    for ds, mk in [("corn", "o"), ("tablets", "s")]:
        h = s[s.dataset == ds]
        axes[2].scatter(h.delta_test_sd / h.rmsecv, h.delta_cf_sd / h.rmsecv, marker=mk, s=14, color="#2a78d6" if ds == "corn" else "#eb6834", label=ds)
    lim = [0, max(axes[2].get_xlim()[1], axes[2].get_ylim()[1])]
    axes[2].plot(lim, lim, color=INK, lw=0.8, ls="--")
    axes[2].set_xlabel("SD(δ) on test samples / RMSECV"); axes[2].set_ylabel("SD(δ) cross-fitted / RMSECV")
    axes[2].set_title("Discrepancy estimate vs truth"); axes[2].legend(fontsize=6.5)
    fig.tight_layout()
    _save(fig, out, "fig8_error_analysis")


def fig_example(raw_dir: Path, cfg: dict, out: Path):
    corn = load("corn", raw_dir)
    job = Job("example", "corn", "m5", "mp6", 0, "pds", 0, n_test=25, alphas=(0.1,))
    _, det = run_job(job, corn, cfg, details=True)
    y, yh = det["y_test"], det["yhat"]
    o = np.argsort(y)
    fig, axes = plt.subplots(1, 2, figsize=(7.2, 2.8), sharey=True)
    for ax, m in zip(axes, ["naive_cp", "td_cp_plus"]):
        lo, hi = det["intervals"][m]
        cov = (y >= yh + lo) & (y <= yh + hi)
        ax.errorbar(np.arange(y.size), yh[o], yerr=[-lo[o], hi[o]], fmt="o", ms=3, color=COLORS[m], ecolor=COLORS[m], elinewidth=1, capsize=1.5, label="prediction ± interval")
        ax.scatter(np.arange(y.size), y[o], marker="x", s=14, color=INK, label="reference", zorder=4)
        ax.set_title(f"{SHORT[m]}: {cov.mean():.0%} of 25 covered")
        ax.set_xlabel("Test samples (sorted by reference)")
    axes[0].set_ylabel("Moisture (%)"); axes[0].legend(fontsize=6.5)
    fig.suptitle("Corn moisture, m5 → mp6, PDS with k = 10 standards, α = 0.10 (split seed 0)", fontsize=8, color=MUTED)
    fig.tight_layout()
    _save(fig, out, "fig9_example_intervals")


def fig_compute(scen: pd.DataFrame, out: Path):
    main = scen[(scen.experiment == "main") & (scen.alpha == 0.1) & (scen.method == "td_cp_plus")]
    g = main.groupby(["dataset", "transfer"])[["t_calibration", "t_transfer", "t_crossfit", "t_interval"]].mean()
    fig, ax = plt.subplots(figsize=(3.6, 2.6))
    labels = [f"{d}\n{t.upper()}" for d, t in g.index]
    x = np.arange(len(g)); w = 0.2
    for i, (c, col, lab) in enumerate([("t_calibration", "#2a78d6", "PLS calibration + CV"), ("t_transfer", "#eb6834", "transfer fit + predict"),
                                        ("t_crossfit", "#1baf7a", "cross-fitting (k refits)"), ("t_interval", "#6250d6", "interval (per method)")]):
        ax.bar(x + (i - 1.5) * w, g[c] * 1000, width=w * 0.9, color=col, label=lab)
    ax.set_yscale("log"); ax.set_xticks(x, labels, fontsize=7); ax.set_ylabel("Time per split (ms)"); ax.legend(fontsize=6)
    fig.tight_layout()
    _save(fig, out, "fig10_compute")


def graphical_abstract(scen: pd.DataFrame, out: Path):
    """Elsevier graphical abstract (13 x 5 cm), built from the main-experiment results."""
    main = scen[(scen.experiment == "main") & (scen.alpha == 0.1)]
    fig, ax = plt.subplots(figsize=(13 / 2.54, 5 / 2.54))
    methods = ["naive_cp", "leverage", "weighted_cp", "gauss_td", "td_cp_plus", "target_cp_plus"]
    x = np.arange(len(methods)); w = 0.38
    for i, (tr, hatch) in enumerate([("pds", None), ("ds", "//")]):
        vals = [main[(main.transfer == tr) & (main.method == m)].coverage.mean() for m in methods]
        ax.bar(x + (i - 0.5) * w, vals, width=w * 0.92, color=[COLORS[m] for m in methods], hatch=hatch, edgecolor="white", lw=0.4,
               label=tr.upper())
    ax.axhline(0.9, color=INK, lw=0.8, ls="--"); ax.text(len(methods) - 0.45, 0.915, "nominal 0.90", fontsize=6, ha="right")
    ax.set_xticks(x, [SHORT[m].replace("\n", " ") for m in methods], fontsize=6)
    ax.set_ylabel("Coverage on secondary\ninstrument (30 scenarios)", fontsize=6.5); ax.set_ylim(0, 1.05)
    ax.legend(fontsize=6, ncol=2, loc="upper left", title="plain: PDS, hatched: DS", title_fontsize=5.5)
    ax.set_title("Primary-instrument intervals under-cover after calibration transfer; TD-CP+ restores coverage "
                 "without reference values", fontsize=6.5)
    fig.tight_layout()
    fig.savefig(out / "graphical_abstract.png", dpi=600); fig.savefig(out / "graphical_abstract.pdf"); plt.close(fig)


def make_figures(results: Path, figures: Path, cfg: dict, raw_dir: Path, log) -> None:
    _style()
    scen = pd.read_csv(results / "scenario_results.csv")
    raw = pd.concat([pd.read_csv(f) for f in sorted(results.glob("raw_main.csv*"))], ignore_index=True)
    fig_workflow(figures)
    fig_spectra(raw_dir, figures)
    fig_main(scen, figures)
    fig_ablation(scen, figures)
    fig_alpha(scen, figures)
    fig_error(scen, raw, figures)
    fig_example(raw_dir, cfg, figures)
    fig_compute(scen, figures)
    graphical_abstract(scen, figures)
    if (scen.experiment == "k_sensitivity").any():
        fig_k(scen, figures)
    if (scen.experiment == "simulated").any():
        fig_robust(scen, figures)
    log.info("figures written to %s", figures)
