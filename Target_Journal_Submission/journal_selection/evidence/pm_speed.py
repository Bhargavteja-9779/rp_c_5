import sys, json, time, urllib.request, urllib.parse, statistics, xml.etree.ElementTree as ET, datetime as dt
E="https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"
def get(url,data=None):
    err=None
    for i in range(4):
        try: return urllib.request.urlopen(url,data=data,timeout=90).read()
        except Exception as e: err=e; time.sleep(2**i)
    raise err
def speed(jour, n=400):
    q=f'"{jour}"[jour] AND ("2025/07/01"[dp] : "2026/09/30"[dp]) AND journal article[pt] NOT review[pt]'
    r=json.loads(get(E+"esearch.fcgi?"+urllib.parse.urlencode(dict(db="pubmed",term=q,retmax=n,retmode="json",sort="pub_date"))))
    ids=r["esearchresult"]["idlist"]; tot=r["esearchresult"]["count"]
    if not ids: return jour,tot,None
    x=get(E+"efetch.fcgi",urllib.parse.urlencode(dict(db="pubmed",id=",".join(ids),retmode="xml")).encode())
    root=ET.fromstring(x); d=[]
    for a in root.iter("PubmedArticle"):
        h={}
        for p in a.iter("PubMedPubDate"):
            try: h[p.get("PubStatus")]=dt.date(int(p.findtext("Year")),int(p.findtext("Month")),int(p.findtext("Day")))
            except: pass
        if "received" in h and "accepted" in h:
            v=(h["accepted"]-h["received"]).days
            if 0<=v<1500: d.append(v)
    if len(d)<10: return jour,tot,len(d)
    d.sort(); q1=d[len(d)//4]; q3=d[3*len(d)//4]
    return jour,tot,dict(n=len(d),median=statistics.median(d),q1=q1,q3=q3,mean=round(statistics.mean(d),1),pct_le72=round(100*sum(v<=72 for v in d)/len(d),1))
for j in sys.argv[1:]:
    try: print(json.dumps(speed(j)))
    except Exception as e: print(j,"ERR",e)
    sys.stdout.flush(); time.sleep(0.5)
