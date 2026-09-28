#!/usr/bin/env python3
"""Relative-strength screens:
  - TAO subnet tokens vs TAO (bittensor-subnets category)
  - Virtuals tokens vs VIRTUAL (virtuals-protocol-ecosystem category)
Outperformer = beats the parent's % change over the window (30d primary, 7d shown)."""
import csv, json, os, time, urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
UA = {"User-Agent": "CoinPicks AI Altcoin Research Engine"}
def get(url):
    req = urllib.request.Request(url, headers=UA)
    for a in range(4):
        try: return json.load(urllib.request.urlopen(req, timeout=40))
        except Exception as e:
            if a < 3: time.sleep(18); continue
            return {"_err": str(e)}
def g(c,k):
    x=c.get(k); return x if isinstance(x,(int,float)) else None

held=set()
for r in csv.DictReader(open(os.path.join(HERE,"SEEN-COINS.csv"))):
    t=(r.get("ticker") or "").strip().lower()
    if t: held.add(t)

# parents
par = get("https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=bittensor,virtual-protocol&price_change_percentage=24h,7d,30d")
P={c["id"]:c for c in par} if isinstance(par,list) else {}
tao=P.get("bittensor",{}); vrt=P.get("virtual-protocol",{})
tao7=g(tao,"price_change_percentage_7d_in_currency"); tao30=g(tao,"price_change_percentage_30d_in_currency")
vrt7=g(vrt,"price_change_percentage_7d_in_currency"); vrt30=g(vrt,"price_change_percentage_30d_in_currency")
print(f"PARENT TAO: 7d {tao7} 30d {tao30} | mc {g(tao,'market_cap')}")
print(f"PARENT VIRTUAL: 7d {vrt7} 30d {vrt30} | mc {g(vrt,'market_cap')}")
time.sleep(4)

def screen(category, p7, p30, label, n=50):
    rows = get(f"https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&category={category}&order=market_cap_desc&per_page=120&page=1&price_change_percentage=24h,7d,30d")
    if not isinstance(rows,list):
        print(f"\n[{label}] ERROR: {str(rows)[:160]}"); return
    out=[]
    for c in rows:
        d7=g(c,"price_change_percentage_7d_in_currency"); d30=g(c,"price_change_percentage_30d_in_currency")
        d24=g(c,"price_change_percentage_24h_in_currency"); mc=g(c,"market_cap") or 0
        # relative vs parent: prefer 30d, fall back to 7d
        rel30 = (d30 - p30) if (d30 is not None and p30 is not None) else None
        rel7  = (d7 - p7) if (d7 is not None and p7 is not None) else None
        key = rel30 if rel30 is not None else (rel7 if rel7 is not None else -9999)
        out.append({"sym":(c.get("symbol") or "").upper(),"name":c.get("name",""),"id":c.get("id",""),
                    "mc":mc,"d24":d24,"d7":d7,"d30":d30,"rel7":rel7,"rel30":rel30,"key":key})
    out.sort(key=lambda r:r["key"], reverse=True)
    outperf=[r for r in out if r["key"]>0 and r["key"]>-9999]
    f=lambda x: ("%+.0f"%x) if isinstance(x,(int,float)) else " ? "
    print(f"\n=== {label} | {len(out)} tokens, {len(outperf)} OUTPERFORM parent (30d) ===")
    print("    TICKER     NAME                  mc      24h   7d    30d   | REL30 REL7  held?  id")
    for r in out[:n]:
        h = "HELD" if r["sym"].lower() in held else ""
        print("  %-10s %-20s $%-6s %-5s %-5s %-6s| %-5s %-5s %-5s %s"
              %(r["sym"][:10], r["name"][:20], f"{r['mc']/1e6:.1f}M", f(r["d24"]),f(r["d7"]),f(r["d30"]),
                f(r["rel30"]), f(r["rel7"]), h, r["id"]))
    time.sleep(4)

screen("bittensor-subnets", tao7, tao30, "TAO SUBNETS vs TAO")
screen("virtuals-protocol-ecosystem", vrt7, vrt30, "VIRTUALS vs VIRTUAL")
