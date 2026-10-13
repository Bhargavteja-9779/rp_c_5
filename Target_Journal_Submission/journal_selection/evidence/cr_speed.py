import sys,json,urllib.request,urllib.parse,statistics,datetime as dt,time
def get(u):
    for i in range(4):
        try: return json.loads(urllib.request.urlopen(urllib.request.Request(u,headers={"User-Agent":"research-script (mailto:none@example.org)"}),timeout=90).read())
        except Exception as e: err=e; time.sleep(2**i)
    raise err
def parse(v):
    for f in ("%d %B %Y","%Y-%m-%d","%d %b %Y","%B %d, %Y"):
        try: return dt.datetime.strptime(v.strip(),f).date()
        except: pass
def speed(name,issn):
    u="https://api.crossref.org/journals/%s/works?"%issn+urllib.parse.urlencode({"filter":"from-pub-date:2025-07-01,type:journal-article","rows":400,"select":"DOI,assertion"})
    items=get(u)["message"]["items"]; d=[]
    for it in items:
        a={x.get("name"):x.get("value") for x in it.get("assertion",[]) or []}
        r=parse(a.get("received","") or ""); c=parse(a.get("accepted","") or "")
        if r and c and 0<=(c-r).days<1500: d.append((c-r).days)
    if len(d)<10: return name,len(items),len(d)
    d.sort(); return name,len(items),dict(n=len(d),median=statistics.median(d),q1=d[len(d)//4],q3=d[3*len(d)//4],pct_le72=round(100*sum(v<=72 for v in d)/len(d),1))
for arg in sys.argv[1:]:
    n,i=arg.split("=")
    try: print(json.dumps(speed(n,i)))
    except Exception as e: print(n,"ERR",e)
    sys.stdout.flush()
