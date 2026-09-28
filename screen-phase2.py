#!/usr/bin/env python3
"""Phase-2 follow-up: pull the next batch from the hot-low-liq screen cache.

Run `uv run python screen-hot-lowliq.py` first. That creates `.screen-cache.json`,
which this script reads so it can return a second pass without refetching the full
CoinGecko universe.
"""
import csv, json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
cache_path = os.path.join(HERE, ".screen-cache.json")
if not os.path.exists(cache_path):
    print("No .screen-cache.json found yet.")
    print("Run this first: uv run python screen-hot-lowliq.py")
    print("Then rerun:      uv run python screen-phase2.py")
    sys.exit(0)

cache = json.load(open(cache_path))

seen = set()
for r in csv.DictReader(open(os.path.join(HERE, "SEEN-COINS.csv"))):
    t = (r.get("ticker") or "").strip().lower()
    if t: seen.add(t)

ALREADY_SHOWN = {  # the 24 from the first screen
 "the-original-doge","three-ws","konnect","aixdrop","deepnode","pod-the-squire","naws-ai",
 "talus","customer-service-xiao-he","depinsim","tsuki","manifesting","folks","oneoneone",
 "looped-hype","yellow","asset","chaos-3","tiger-alpha","unicorn-3-2","toescoin",
 "official-layoff-coin","c0mpute"}

BAD_KW = ("usd","stable","xstock","tokenized","etf","-ondo-","dai","eur","peg","yield",
          "bold","midas","treasur","tbill","money-market","pre-ipo","republic","wrapped","staked")
def bad(c):
    blob=(c.get("id","")+" "+c.get("name","")+" "+c.get("symbol","")).lower()
    return any(k in blob for k in BAD_KW)
def g(c,k):
    v=c.get(k); return v if isinstance(v,(int,float)) else None

out=[]
for c in cache:
    if (c.get("symbol") or "").lower() in seen: continue
    if c.get("id") in ALREADY_SHOWN: continue
    if bad(c): continue
    mc=g(c,"market_cap") or 0; vol=g(c,"total_volume") or 0
    d24=g(c,"price_change_percentage_24h_in_currency"); d7=g(c,"price_change_percentage_7d_in_currency")
    d30=g(c,"price_change_percentage_30d_in_currency"); athc=g(c,"ath_change_percentage")
    if not (300_000<=mc<=40_000_000): continue
    if vol<75_000 or vol>mc*8: continue
    moves=[abs(x) for x in (d24,d7,d30) if isinstance(x,(int,float))]
    if moves and max(moves)<6: continue
    tag=None
    if d30 is not None and d30>=40 and ((d7 or 0)<0 or (d24 or 0)<0): tag="ran+pulledback"
    elif athc is not None and athc>=-25 and ((d7 or 0)>=4 or (d30 or 0)>=15): tag="near-ATH"
    if not tag: continue
    out.append({"id":c.get("id"),"sym":(c.get("symbol") or "").upper(),"name":c.get("name",""),
                "mc":mc,"vol":vol,"d24":d24,"d7":d7,"d30":d30,"athc":athc,"tag":tag})

# blended sort: reward momentum, keep near-ATH and pullback mixed
out.sort(key=lambda r:(r["d30"] or 0)+ (50 if r["tag"]=="near-ATH" and (r["athc"] or -99)>=-12 else 0), reverse=True)
f=lambda x: ("%+.0f%%"%x) if isinstance(x,(int,float)) else "  ? "
print(f"fresh candidates (excl. ledger + 24 shown): {len(out)}\n")
for r in out[:18]:
    print("  %-11s %-24s %-14s mc $%-7s vol $%-7s | 24h %-6s 7d %-6s 30d %-7s ATH %-6s | %s"
          %(r["sym"][:11], r["name"][:24], r["tag"], f"{r['mc']/1e6:.1f}M", f"{r['vol']/1e6:.2f}M",
            f(r["d24"]),f(r["d7"]),f(r["d30"]),f(r["athc"]), r["id"]))
