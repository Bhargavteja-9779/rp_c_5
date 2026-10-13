#!/usr/bin/env python
"""Build Final_Manuscript.{md,docx,pdf}, highlights and the cover letter from result files.

Every number is read from ../results or ../tables via values.py; qualitative claims
are asserted against those numbers (claims.py) and the build fails if a claim is
not supported.
"""
from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from docx_writer import build_docx  # noqa: E402
from references import format_reference, load_records  # noqa: E402
import text_front as F  # noqa: E402
import text_results as R  # noqa: E402
from values import compute_values  # noqa: E402
from claims import check_claims  # noqa: E402

ROOT = HERE.parent
CITE = re.compile(r"\[(@[^\]]+)\]")


def number_citations(blocks):
    order: list[str] = []

    def repl(m):
        keys = [k.strip().lstrip("@") for k in m.group(1).split(";")]
        nums = []
        for k in keys:
            if k not in order:
                order.append(k)
            nums.append(order.index(k) + 1)
        nums = sorted(set(nums))
        # compress ranges: [1,2,3,5] -> 1–3,5
        out, start, prev = [], nums[0], nums[0]
        for x in nums[1:] + [None]:
            if x is not None and x == prev + 1:
                prev = x
                continue
            out.append(f"{start}–{prev}" if prev - start >= 2 else (f"{start},{prev}" if prev != start else f"{start}"))
            if x is not None:
                start = prev = x
        return "[" + ",".join(out) + "]"

    new = []
    for b in blocks:
        if b[0] in ("p", "plabel", "bullets", "numbered"):
            if b[0] == "bullets" or b[0] == "numbered":
                new.append((b[0], [CITE.sub(repl, s) for s in b[1]]))
            elif b[0] == "plabel":
                new.append((b[0], b[1], CITE.sub(repl, b[2])))
            else:
                new.append((b[0], CITE.sub(repl, b[1])))
        else:
            new.append(b)
    return new, order


def fill(blocks, V):
    out = []
    for b in blocks:
        if b[0] in ("p", "h1", "h2", "h3", "center", "title"):
            out.append((b[0], b[1].format(**V)))
        elif b[0] == "plabel":
            out.append((b[0], b[1], b[2].format(**V)))
        elif b[0] in ("bullets", "numbered"):
            out.append((b[0], [s.format(**V) for s in b[1]]))
        elif b[0] in ("fig",):
            out.append((b[0], b[1], b[2].format(**V)) + tuple(b[3:]))
        elif b[0] == "table":
            out.append((b[0], b[1], b[2].format(**V), (b[3] if len(b) > 3 else "").format(**V)))
        else:
            out.append(b)
    return out


def to_markdown(blocks) -> str:
    md = []
    for b in blocks:
        k = b[0]
        if k == "title":
            md.append(f"# {b[1]}\n")
        elif k == "h1":
            md.append(f"\n## {b[1]}\n")
        elif k == "h2":
            md.append(f"\n### {b[1]}\n")
        elif k == "h3":
            md.append(f"\n#### {b[1]}\n")
        elif k in ("p", "center"):
            md.append(b[1] + "\n")
        elif k == "plabel":
            md.append(f"**{b[1]}** {b[2]}\n")
        elif k == "bullets":
            md.extend(f"- {s}" for s in b[1]); md.append("")
        elif k == "numbered":
            md.extend(f"{i}. {s}" for i, s in enumerate(b[1], 1)); md.append("")
        elif k == "eq":
            md.append(f"$$ {b[1]} \\qquad ({b[2]}) $$\n")
        elif k == "fig":
            md.append(f"![{b[2][:40]}]({Path(b[1]).relative_to(ROOT).as_posix() if Path(b[1]).is_absolute() else b[1]})\n\n{b[2]}\n")
        elif k == "table":
            df = b[1]
            md.append(b[2] + "\n")
            md.append("| " + " | ".join(map(str, df.columns)) + " |")
            md.append("|" + "---|" * len(df.columns))
            for _, r in df.iterrows():
                md.append("| " + " | ".join(map(str, r.values)) + " |")
            if len(b) > 3 and b[3]:
                md.append("\n" + b[3])
            md.append("")
        elif k == "refs":
            md.extend(f"[{i}] {s}" for i, s in enumerate(b[1], 1))
        elif k == "pagebreak":
            md.append("\n---\n")
    return "\n".join(md) + "\n"


def main():
    V, T = compute_values(ROOT)
    check_claims(V)
    body = []
    body += [("title", F.TITLE), ("center", "Author One^{a,*}, Author Two^{b} [author names withheld — placeholder]"),
             ("center", "^{a} Affiliation placeholder; ^{b} Affiliation placeholder"),
             ("center", "^{*} Corresponding author: name, e-mail placeholder")]
    body += [("h1", "Highlights"), ("bullets", F.HIGHLIGHTS)]
    body += [("h1", "Abstract")] + [("plabel", k + ":", v) for k, v in F.ABSTRACT.items()]
    body += [("plabel", "Keywords:", "; ".join(F.KEYWORDS))]
    body += [("h1", "1. Introduction")] + F.INTRO
    body += [("fig", ROOT / "figures" / "fig1_workflow.png",
              "**Fig. 1.** TD-CP workflow. Residuals of the primary calibration (top) and reference-free transfer discrepancies of "
              "cross-fitted standardisation maps on the transfer standards (bottom) are combined into the interval for a new "
              "secondary-instrument spectrum. Schematic; no data are shown.")]
    body += [("h1", "2. Theory")] + F.THEORY
    body += [("h1", "3. Experimental")] + F.EXPERIMENTAL
    body += R.results_blocks(V, T, ROOT)
    body += [("h1", "5. Conclusions")] + R.CONCLUSIONS
    body += R.declarations()
    body = fill(body, V)
    body, order = number_citations(body)
    recs = load_records()
    refs = [format_reference(k, recs) for k in order]
    unused = sorted(set(recs) - set(order))
    body += [("h1", "References"), ("refs", refs)]
    (HERE / "Final_Manuscript.md").write_text(to_markdown(body))
    tmp = HERE / "_build"; tmp.mkdir(exist_ok=True)
    build_docx(body, HERE / "Final_Manuscript.docx", tmp)
    (HERE / "highlights.md").write_text("\n".join("- " + h for h in F.HIGHLIGHTS) + "\n")
    assert all(len(h) <= 85 for h in F.HIGHLIGHTS), [len(h) for h in F.HIGHLIGHTS]
    n_words = len(" ".join(F.ABSTRACT.values()).format(**V).split())
    print(f"abstract words: {n_words}; references: {len(refs)}; verified but uncited: {unused}")
    assert n_words <= 250, n_words
    try:
        subprocess.run(["soffice", "--headless", "--convert-to", "pdf", "--outdir", str(HERE), str(HERE / "Final_Manuscript.docx")],
                       check=True, capture_output=True, timeout=600)
    except Exception as e:  # PDF is optional
        print("PDF conversion failed:", e)


if __name__ == "__main__":
    main()
