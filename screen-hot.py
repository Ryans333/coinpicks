#!/usr/bin/env python3
"""'Running hot' screen — broad. Strong recent momentum + real volume, any quality.
Sort by heat (7d, then 24h). Exclude ledger + already-shown + pegs/tokenized-stocks."""
import csv, json, os, time, urllib.request, urllib.error

HERE=os.path.dirname(os.path.abspath(__file__))
UA={"User-Agent":"CoinPicks AI Altcoin Research Engine"}
def get(url):
    req=urllib.request.Request(url,headers=UA)
    for a in range(4):
        try: return json.load(urllib.request.urlopen(req,timeout=40))
        except Exception as e:
            if a<3: time.sleep(18); continue
            return {"_err":str(e)}
def g(c,k):
    v=c.get(k); return v if isinstance(v,(int,float)) else None

seen=set()
for r in csv.DictReader(open(os.path.join(HERE,"SEEN-COINS.csv"))):
    t=(r.get("ticker") or "").strip().lower()
    if t: seen.add(t)
# Your own exclusions, by CoinGecko id, one per line, in an optional EXCLUDE.txt next to
# this script. Empty by default and deliberately so: this shipped carrying the author's
# personal skip-list of eight coins, which silently removed them from every buyer's results
# with no way to know. Your ledger is yours; the SEEN-COINS filter above already handles
# "I have looked at this before".
SHOWN=set()
_ex=os.path.join(HERE,"EXCLUDE.txt")
if os.path.exists(_ex):
    SHOWN={l.strip().lower() for l in open(_ex) if l.strip() and not l.startswith("#")}
BAD=("usd","stable","xstock","tokenized","etf","-ondo-","dai","eur","peg","yield",
     "bold","midas","treasur","tbill","money-market","pre-ipo","republic","wrapped","staked","reuro")
def bad(c):
    blob=(c.get("id","")+" "+c.get("name","")+" "+c.get("symbol","")).lower()
    return any(k in blob for k in BAD)

rows=[]
# TRACK WHAT WE ACTUALLY GOT. This used to print a confident "RUNNING HOT: N coins" summary
# whether it fetched 3,000 coins or 2,250: a tester saw 3 of 12 pages rate-limited, a quarter
# of the universe never fetched, and a clean-looking result. Partial results presented as
# complete are the one failure a screener must never have.
PAGES_OK, PAGES_ERR = [], []
for p in range(1,13):  # ranks ~1-3000
    d=get(f"https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=250&page={p}&price_change_percentage=24h,7d,30d")
    if isinstance(d,list):
        rows+=d; PAGES_OK.append(p); print(f"page {p} ok ({len(rows)})")
    else:
        PAGES_ERR.append(p); print(f"page {p} ERR ({d.get('_err','?')[:60] if isinstance(d,dict) else '?'})")
    time.sleep(6)

hot=[]
for c in rows:
    sym=(c.get("symbol") or "").lower()
    if sym in seen or c.get("id") in SHOWN or bad(c): continue
    mc=g(c,"market_cap") or 0; vol=g(c,"total_volume") or 0
    d24=g(c,"price_change_percentage_24h_in_currency"); d7=g(c,"price_change_percentage_7d_in_currency"); d30=g(c,"price_change_percentage_30d_in_currency")
    if not (300_000<=mc<=200_000_000): continue
    if vol<150_000: continue                 # must really be trading
    if vol>mc*20: continue                    # filter obvious wash
    if vol<mc*0.03: continue                  # must be active vs its cap
    hot_now = ((d7 or 0)>=40) or ((d24 or 0)>=20)
    if not hot_now: continue
    heat=max(d7 or 0,0)*0.6 + max(d24 or 0,0)*1.0   # weight 24h, include 7d
    hot.append({"sym":(c.get("symbol") or "").upper(),"name":c.get("name",""),"id":c.get("id",""),
                "mc":mc,"vol":vol,"d24":d24,"d7":d7,"d30":d30,"heat":heat})
hot.sort(key=lambda r:r["heat"],reverse=True)
f=lambda x: ("%+.0f%%"%x) if isinstance(x,(int,float)) else "  ?  "
_scanned = len(PAGES_OK)*250
if PAGES_ERR:
    print(f"\n⚠️  INCOMPLETE SCAN: {len(PAGES_ERR)} of 12 pages failed (pages {PAGES_ERR}).")
    print(f"    Scanned about {_scanned} of ~3000 coins. This is rate limiting on the free")
    print(f"    CoinGecko tier, not a broken install. Anything in the missing pages was never")
    print(f"    looked at. Wait a few minutes and rerun for the full universe.")
print(f"\n=== RUNNING HOT: {len(hot)} coins (excl ledger + shown + pegs) "
      f"[from {_scanned} of ~3000 coins scanned] ===")
print("  TICKER       NAME                   mc       vol      | 24h    7d     30d    | id")
for r in hot[:60]:
    print("  %-11s %-22s $%-7s $%-7s | %-6s %-6s %-6s | %s"
          %(r["sym"][:11], r["name"][:22], f"{r['mc']/1e6:.1f}M", f"{r['vol']/1e6:.2f}M",
            f(r["d24"]),f(r["d7"]),f(r["d30"]), r["id"]))
print(f"\n(total hot: {len(hot)})")
