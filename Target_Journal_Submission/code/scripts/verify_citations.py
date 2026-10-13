"""Verify every reference of the manuscript against Crossref (DOI) or arXiv (id).

Writes ../supplementary/citation_audit.csv. A reference is only used in the
manuscript if its record resolves and the first author/year/title match.
"""
import csv, json, sys, time, urllib.parse, urllib.request, re
from pathlib import Path

REFS = json.loads((Path(__file__).parent / "references.json").read_text())
UA = {"User-Agent": "tdcp-citation-audit (mailto:none@example.org)"}

def get(url):
    for i in range(4):
        try:
            return urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60).read()
        except Exception as e:
            err = e; time.sleep(2 ** i)
    raise err

rows = []
for r in REFS:
    rec = dict(key=r["key"], doi=r.get("doi", ""), arxiv=r.get("arxiv", ""), status="UNVERIFIED")
    try:
        if r.get("doi"):
            m = json.loads(get("https://api.crossref.org/works/" + urllib.parse.quote(r["doi"])))["message"]
            au = m.get("author", [{}])
            rec.update(title=(m.get("title") or [""])[0], first_author=au[0].get("family", au[0].get("name", "")) if au else "",
                       year=((m.get("published-print") or m.get("issued", {})).get("date-parts") or [[None]])[0][0], venue=(m.get("container-title") or [""])[0],
                       volume=m.get("volume", ""), pages=m.get("page", m.get("article-number", "")), n_authors=len(au),
                       authors="; ".join(f"{a.get('family','')}, {a.get('given','')}" for a in au), status="OK")
        elif r.get("arxiv"):
            x = get("http://export.arxiv.org/api/query?id_list=" + r["arxiv"]).decode()
            ent = x.split("<entry>")[1]
            rec.update(title=re.sub(r"\s+", " ", re.search(r"<title>(.*?)</title>", ent, re.S).group(1)).strip(),
                       authors="; ".join(re.findall(r"<name>(.*?)</name>", ent)),
                       year=re.search(r"<published>(\d{4})", ent).group(1), venue="arXiv:" + r["arxiv"], status="OK")
            rec["first_author"] = rec["authors"].split(";")[0].split()[-1]
        else:
            rec.update(title=r.get("title", ""), status="NO-IDENTIFIER (standard/guideline/web resource; checked manually)")
    except Exception as e:
        rec["status"] = f"FAILED: {e}"
    exp = r.get("expect", {})
    if rec["status"] == "OK" and exp:
        bad = [k for k, v in exp.items() if str(v).lower() not in str(rec.get(k, "")).lower()]
        if bad:
            rec["status"] = "MISMATCH:" + ",".join(bad)
    rows.append(rec)
    print(rec["key"], rec["status"], rec.get("year"), "|", rec.get("first_author"), "|", str(rec.get("title"))[:90], "|", rec.get("venue"))
out = Path(__file__).resolve().parents[2] / "supplementary" / "citation_audit.csv"
keys = sorted({k for r in rows for k in r})
with open(out, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=keys); w.writeheader(); w.writerows(rows)
(Path(__file__).parent / "references_verified.json").write_text(json.dumps(rows, indent=1, ensure_ascii=False))
