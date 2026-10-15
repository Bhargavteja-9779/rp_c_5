"""Generate cover_letter.docx with numbers from the results (no hand-typed results)."""
from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from docx import Document  # noqa: E402
from docx.shared import Cm, Pt  # noqa: E402

import text_front as F  # noqa: E402
from values import compute_values  # noqa: E402


def main():
    V, _ = compute_values(HERE.parent)
    doc = Document()
    st = doc.styles["Normal"]; st.font.name = "Times New Roman"; st.font.size = Pt(11.5)
    for s in doc.sections:
        s.left_margin = s.right_margin = Cm(2.5)
    paras = [
        "[Corresponding author name, affiliation, address, e-mail — placeholder]",
        "[Date]",
        "The Editors\nAnalytica Chimica Acta",
        "Dear Editors,",
        f"We submit the research article “{F.TITLE}” for consideration in Analytica Chimica Acta.",
        "Calibration transfer between spectrometers is a long-standing topic in this journal, but transferred calibrations "
        "are still validated almost exclusively by point accuracy. We show that prediction intervals calibrated on the "
        f"primary instrument become strongly over-confident after transfer: at a nominal 90% level they covered only "
        f"{V['naive_cov_pds']} (PDS) and {V['naive_cov_ds']} (DS) of secondary-instrument samples across 30 public "
        "benchmark scenarios. We introduce transfer-discrepancy conformal prediction, which uses the transfer standards "
        "that PDS/DS already require — without needing their reference values — to produce sample-wise intervals. Its "
        f"jackknife+ form (TD-CP+) reached {V['plus_cov_pds']} and {V['plus_cov_ds']} coverage, being valid in "
        f"{V['plus_valid_pds']} and {V['plus_valid_ds']} of scenarios.",
        "We believe the work fits the journal's scope in chemometrics and data treatment: it introduces a new principle "
        "for quantifying uncertainty of transferred multivariate calibrations, with a quantifiable analytical benefit "
        "(valid uncertainty statements for method validation and release decisions on secondary instruments).",
        "We have tried to make the evidence easy to scrutinise. The analysis protocol was fixed before the experiments; one "
        "method variant (TD-CP+) was added after the pre-specified main experiment and is reported as such, together "
        "with the pre-specified method's shortfall. All code, configuration and result files are openly available, and a single "
        "command regenerates every number, table and figure. Both datasets are public.",
        "Related work: we cite a concurrent machine-learning preprint (arXiv:2609.10737) that transports conformal "
        "calibration through unlabelled paired data for classification; our construction, target task (regression "
        "intervals after chemometric standardisation) and evaluation differ, as discussed in the manuscript.",
        "The manuscript is original, has not been published previously and is not under consideration elsewhere. All "
        "authors have approved the submission. There are no competing interests. No human or animal subjects were "
        "involved. Generative AI was used extensively in preparing this work; this is disclosed in the manuscript's "
        "declaration, and the authors take full responsibility for the content.",
        "Suggested reviewers: [to be provided by the authors].",
        "Sincerely,\n[Corresponding author, on behalf of all authors]",
    ]
    for t in paras:
        doc.add_paragraph(t)
    doc.save(HERE / "cover_letter.docx")
    print("cover letter written")


if __name__ == "__main__":
    main()
