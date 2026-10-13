"""Format verified references (Crossref/arXiv records) in the Elsevier numbered style."""
from __future__ import annotations

import json
from pathlib import Path

VERIFIED = Path(__file__).resolve().parents[1] / "code" / "scripts" / "references_verified.json"

ABBREV = {
    "Analytical Chemistry": "Anal. Chem.",
    "Chemometrics and Intelligent Laboratory Systems": "Chemometr. Intell. Lab. Syst.",
    "Applied Spectroscopy": "Appl. Spectrosc.",
    "Journal of Near Infrared Spectroscopy": "J. Near Infrared Spectrosc.",
    "Analytica Chimica Acta": "Anal. Chim. Acta",
    "Journal of the American Statistical Association": "J. Am. Stat. Assoc.",
    "The Annals of Statistics": "Ann. Stat.",
    "Foundations and Trends® in Machine Learning": "Found. Trends Mach. Learn.",
    "Food Chemistry": "Food Chem.",
    "Journal of Chemometrics": "J. Chemom.",
    "TrAC Trends in Analytical Chemistry": "TrAC Trends Anal. Chem.",
    "Technometrics": "Technometrics",
    "The Annals of Probability": "Ann. Probab.",
    "The Annals of Mathematical Statistics": "Ann. Math. Stat.",
    "Biometrics Bulletin": "Biometrics Bull.",
    "Comprehensive Psychology": "Compr. Psychol.",
    "Lecture Notes in Computer Science": "Lect. Notes Comput. Sci.",
}

MANUAL = {
    "holm1979": "S. Holm, A simple sequentially rejective multiple test procedure, Scand. J. Stat. 6 (1979) 65–70.",
    "astm_e1655": "ASTM E1655-17, Standard Practices for Infrared Multivariate Quantitative Analysis, ASTM International, West Conshohocken, PA, 2017.",
    "ich_q2r2": "International Council for Harmonisation, ICH Q2(R2) Guideline: Validation of Analytical Procedures, 2023.",
    "eigenvector_data": "Eigenvector Research Inc., Data sets: NIR spectra of corn samples; NIR shootout 2002 pharmaceutical tablets. https://eigenvector.com/resources/data-sets/ (accessed 13 October 2026).",
    "vovk2005": "V. Vovk, A. Gammerman, G. Shafer, Algorithmic Learning in a Random World, Springer, New York, 2005. https://doi.org/10.1007/b106715.",
}


OVERRIDES = {  # fields missing or incomplete in Crossref records, checked against the publisher versions
    "massart1990": {"pages": "1269–1283"},
    "wilcoxon1945": {"pages": "80–83"},
    "kerby2014": {"pages": ""},
    "papadopoulos2002": {"venue": "in: Machine Learning: ECML 2002, Lect. Notes Comput. Sci.", "volume": "2430"},
}


def _initials(given: str) -> str:
    parts = [p for p in given.replace("-", " -").split() if p]
    out = []
    for p in parts:
        if p.startswith("-"):
            out.append("-" + p[1:2] + ".")
        else:
            out.append(p[0] + ".")
    return "".join(out).replace(".-", ".-")


def _authors(rec: dict) -> str:
    names = []
    for a in rec.get("authors", "").split("; "):
        if not a.strip():
            continue
        if "," in a:
            fam, giv = [s.strip() for s in a.split(",", 1)]
            names.append(f"{_initials(giv)} {fam}".strip())
        else:  # arXiv "Given Family"
            bits = a.split()
            names.append(f"{_initials(' '.join(bits[:-1]))} {bits[-1]}")
    if len(names) > 6:
        names = names[:6] + ["et al."]
        return ", ".join(names[:-1]) + " " + names[-1]
    return ", ".join(names)


def format_reference(key: str, recs: dict) -> str:
    if key in MANUAL:
        return MANUAL[key]
    r = dict(recs[key], **OVERRIDES.get(key, {}))
    title = r["title"].rstrip(".")
    if r.get("arxiv"):
        return f"{_authors(r)}, {title}, arXiv preprint arXiv:{r['arxiv']} ({r['year']})."
    venue = ABBREV.get(r.get("venue", ""), r.get("venue", ""))
    vol = r.get("volume", "")
    pages = str(r.get("pages", "")).replace("-", "–")
    s = f"{_authors(r)}, {title}, {venue}"
    if vol:
        s += f" {vol}"
    s += f" ({r['year']})"
    if pages:
        s += f" {pages}"
    return s + f". https://doi.org/{r['doi']}."


def load_records() -> dict:
    return {r["key"]: r for r in json.loads(VERIFIED.read_text())}
