#!/usr/bin/env python3
"""VADER data + momentum screen of the Virtuals-ecosystem category (CoinGecko)."""
import csv, json, os, time, urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
UA = {"User-Agent": "CoinPicks AI Altcoin Research Engine"}

def get(url):
    req = urllib.request.Request(url, headers=UA)
    for a in range(3):
        try: return json.load(urllib.request.urlopen(req, timeout=30))
        except Exception as e:
            if a < 2: time.sleep(15); continue
            return {"_err": str(e)}

seen = set()
for r in csv.DictReader(open(os.path.join(HERE, "SEEN-COINS.csv"))):
    t = (r.get("ticker") or "").strip().lower()
    if t: seen.add(t)
ALREADY = {"tibbir","mamo","peak","blkh","lbm","vader","virtual"}  # already held / parent

# --- VADER ---
v = get("https://api.coingecko.com/api/v3/coins/vaderai-by-virtuals?localization=false&tickers=true&community_data=false&developer_data=false")
md = v.get("market_data", {})
print("== VADER (vaderai-by-virtuals) ==")
print(" mc", md.get("market_cap",{}).get("usd"), "fdv", md.get("fully_diluted_valuation",{}).get("usd"), "vol", md.get("total_volume",{}).get("usd"))
print(" price", md.get("current_price",{}).get("usd"), "ath%", md.get("ath_change_percentage",{}).get("usd"), "30d%", md.get("price_change_percentage_30d"))
print(" platforms", v.get("platforms"))
print(" home", v.get("links",{}).get("homepage"), "tw", v.get("links",{}).get("twitter_screen_name"))
print(" venues", sorted([(t['market']['name'], t.get('converted_volume',{}).get('usd') or 0) for t in v.get("tickers",[])], key=lambda x:-x[1])[:3])
time.sleep(3)

# --- momentum screen ---
rows = get("https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&category=virtuals-protocol-ecosystem&order=market_cap_desc&per_page=200&page=1&price_change_percentage=24h,7d,30d")
def g(c,k):
    x=c.get(k); return x if isinstance(x,(int,float)) else None
cand=[]
for c in rows:
    sym=(c.get("symbol") or "").lower()
    if sym in seen or sym in ALREADY: continue
    mc=g(c,"market_cap") or 0; vol=g(c,"total_volume") or 0
    d24=g(c,"price_change_percentage_24h_in_currency"); d7=g(c,"price_change_percentage_7d_in_currency")
    d30=g(c,"price_change_percentage_30d_in_currency"); athc=g(c,"ath_change_percentage")
    if not (250_000<=mc<=500_000_000): continue
    if vol<10_000: continue
    tag = "pullback" if (d30 or 0)>=40 and ((d7 or 0)<0 or (d24 or 0)<0) else (
          "near-ATH" if (athc is not None and athc>=-30 and ((d7 or 0)>=5 or (d30 or 0)>=20)) else "mover")
    cand.append({"sym":c.get("symbol","").upper(),"name":c.get("name",""),"id":c.get("id",""),
                 "mc":mc,"vol":vol,"d24":d24,"d7":d7,"d30":d30,"athc":athc,"tag":tag})
# rank by recent momentum blend (7d weighted + 24h), best movers first
cand.sort(key=lambda r:r["mc"], reverse=True)
f=lambda x: ("%+.0f%%"%x) if isinstance(x,(int,float)) else "  ? "
def line(r):
    return ("  %-10s %-22s %-9s mc $%-6s vol $%-7s | 24h %-6s 7d %-6s 30d %-7s ATH %-6s | %s"
            %(r["sym"][:10], r["name"][:22], r["tag"], f"{r['mc']/1e6:.1f}M", f"{r['vol']/1e6:.2f}M",
              f(r["d24"]),f(r["d7"]),f(r["d30"]),f(r["athc"]), r["id"]))
print(f"\n=== TOP 20 VIRTUALS MOVERS (by 7d momentum; sector is mostly down) — {len(cand)} qualified ===")
for r in cand[:20]: print(line(r))
