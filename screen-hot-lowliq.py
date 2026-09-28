#!/usr/bin/env python3
"""
screen-hot-lowliq.py  —  low-liquidity momentum screen.

Find ~25 LOW-LIQUIDITY coins that are HOT right now, matching either:
  A) did a big recent run (~200%+ / strong 30d) and have since PULLED BACK, or
  B) sitting NEAR all-time highs.
Excludes anything already in SEEN-COINS.csv. Uses free CoinGecko /coins/markets.
"""
import csv, json, os, time, urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
SEEN = os.path.join(HERE, "SEEN-COINS.csv")

def seen_tickers():
    s = set()
    if os.path.exists(SEEN):
        for r in csv.DictReader(open(SEEN)):
            t = (r.get("ticker") or "").strip().lower()
            if t: s.add(t)
    return s

def fetch_page(page):
    url = ("https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd"
           "&order=market_cap_desc&per_page=250&page=%d"
           "&price_change_percentage=24h,7d,30d" % page)
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    for attempt in range(3):
        try:
            return json.load(urllib.request.urlopen(req, timeout=30))
        except urllib.error.HTTPError as e:
            if e.code == 429 and attempt < 2:
                time.sleep(20); continue
            raise

# drop stablecoins, tokenized stocks/ETFs, and other pegged/RWA wrappers
BAD_KW = ("usd", "stable", "xstock", "tokenized", "etf", "-ondo-", "dai", "eur",
          "peg", "yield", "bold", "midas", "treasur", "tbill", "money-market",
          "pre-ipo", "republic", "wrapped", "staked")
def is_peg_or_rwa(c):
    blob = (c.get("id","") + " " + c.get("name","") + " " + c.get("symbol","")).lower()
    return any(k in blob for k in BAD_KW)

def g(c, k):
    v = c.get(k)
    return v if isinstance(v, (int, float)) else None

def main():
    seen = seen_tickers()
    cache = os.path.join(HERE, ".screen-cache.json")
    rows = []
    if os.path.exists(cache):
        rows = json.load(open(cache))
        print("loaded", len(rows), "rows from cache")
    else:
        for p in range(2, 10):       # ranks ~250-2250 = where low-liq small caps live
            try:
                rows += fetch_page(p)
                print("page", p, "ok  (rows so far:", len(rows), ")")
            except Exception as e:
                print("page", p, "error", e)
            time.sleep(6)
        json.dump(rows, open(cache, "w"))

    pullback, near_ath = [], []
    for c in rows:
        sym = (c.get("symbol") or "").lower()
        if sym in seen: continue                       # exclude already-examined
        if is_peg_or_rwa(c): continue                  # exclude stablecoins / tokenized stocks
        mc   = g(c, "market_cap") or 0
        vol  = g(c, "total_volume") or 0
        d24  = g(c, "price_change_percentage_24h_in_currency")
        d7   = g(c, "price_change_percentage_7d_in_currency")
        d30  = g(c, "price_change_percentage_30d_in_currency")
        athc = g(c, "ath_change_percentage")
        # LOW LIQUIDITY proxy: small cap, but actually trading (so it's "hot", not dead)
        if not (300_000 <= mc <= 40_000_000): continue
        if vol < 75_000: continue                      # must have real volume
        if vol > mc * 8: continue                      # filter wash-trade outliers
        # drop flat pegs that slipped through (near-zero movement on all windows)
        moves = [abs(x) for x in (d24, d7, d30) if isinstance(x,(int,float))]
        if moves and max(moves) < 5: continue
        rec = {"sym": c.get("symbol","").upper(), "name": c.get("name",""),
               "id": c.get("id",""), "mc": mc, "vol": vol,
               "d24": d24, "d7": d7, "d30": d30, "athc": athc}
        # A) big recent run, now pulled back  (checked first; takes priority)
        if d30 is not None and d30 >= 45 and ((d7 is not None and d7 < 0) or (d24 is not None and d24 < 0)):
            rec["tag"] = "ran+pulledback"; pullback.append(rec); continue
        # B) near all-time high WITH real recent momentum (not a flat peg)
        if athc is not None and athc >= -22 and ((d7 or 0) >= 4 or (d30 or 0) >= 15):
            rec["tag"] = "near-ATH"; near_ath.append(rec)

    near_ath.sort(key=lambda r: (r["athc"] if r["athc"] is not None else -999), reverse=True)
    pullback.sort(key=lambda r: (r["d30"] if r["d30"] is not None else 0), reverse=True)

    def line(r):
        f = lambda x: ("%+.0f%%" % x) if isinstance(x,(int,float)) else "  ?  "
        return ("  %-11s %-26s mc $%-9s vol $%-8s | 24h %-6s 7d %-6s 30d %-7s | ATH %-6s | %s"
                % (r["sym"][:11], r["name"][:26],
                   f"{r['mc']/1e6:.1f}M", f"{r['vol']/1e6:.2f}M",
                   f(r["d24"]), f(r["d7"]), f(r["d30"]), f(r["athc"]), r["id"]))

    # take ~13 pullback + ~12 near-ATH = 25
    pb = pullback[:13]; na = near_ath[:12]
    print(f"\nScanned ranks ~250-1750 | candidates: {len(pullback)} pulled-back, {len(near_ath)} near-ATH\n")
    print("=== A) RAN 200%-ish THEN PULLED BACK (sorted by 30d gain) ===")
    for r in pb: print(line(r))
    print("\n=== B) NEAR ALL-TIME HIGHS (sorted by closeness to ATH) ===")
    for r in na: print(line(r))
    print(f"\nTotal returned: {len(pb)+len(na)}")

if __name__ == "__main__":
    main()
