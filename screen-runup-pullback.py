#!/usr/bin/env python3
"""
Screen: coins that RAN >=300% to a peak within ~this month, then PULLED BACK 30-80% off that peak.

Formula per coin (from 30d OHLCV):
  peak      = max high over last 30d
  pre_low   = min low from start of window up to (and incl.) the peak candle   <- the run-up base
  run_up    = peak/pre_low - 1                 keep if >= 3.00 (300%)
  current   = last close
  pullback  = 1 - current/peak                 keep if 0.30 <= pullback <= 0.80

Two stages so it's feasible:
  Stage 1 (cheap): markets pull -> candidates that hit ATH in last 31d AND are 30-80% below ATH (peak proxy).
  Stage 2 (OHLCV): verify the >=300% intramonth run-up on each candidate. Excludes SEEN-COINS ledger.
"""
import csv, json, os, time, datetime, urllib.request

HERE=os.path.dirname(os.path.abspath(__file__)); UA={"User-Agent":"CoinPicks AI Altcoin Research Engine"}
TODAY=datetime.date.today()
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
BAD=("usd","stable","xstock","tokenized","etf","-ondo-","dai","eur","peg","wrapped","staked","tether")
def bad(c):
    b=(c.get("id","")+" "+c.get("name","")+" "+c.get("symbol","")).lower()
    return any(k in b for k in BAD)

# ---- Stage 1: candidate universe ----
cands=[]
for p in range(1,16):
    rows=get(f"https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=250&page={p}&price_change_percentage=30d")
    if not isinstance(rows,list): print("stage1 page",p,"err"); continue
    for c in rows:
        if (c.get("symbol") or "").lower() in seen or bad(c): continue
        mc=g(c,"market_cap") or 0; vol=g(c,"total_volume") or 0
        athc=g(c,"ath_change_percentage"); athd=c.get("ath_date")
        if not (300_000<=mc<=150_000_000): continue
        if vol<50_000: continue
        if athc is None or not (-80<=athc<=-30): continue   # 30-80% below the high
        if not athd: continue
        try: ad=datetime.date.fromisoformat(athd[:10])
        except: continue
        if (TODAY-ad).days>31: continue                      # peak was THIS month
        cands.append({"id":c["id"],"sym":(c.get("symbol") or "").upper(),"name":c.get("name",""),
                      "mc":mc,"vol":vol,"athc":athc,"athd":athd[:10],"d30":g(c,"price_change_percentage_30d_in_currency")})
    time.sleep(4)
cands.sort(key=lambda x:-(x["d30"] or 0))
print(f"STAGE 1: {len(cands)} candidates (peaked in last 31d, 30-80% off high, not in ledger)")

# ---- Stage 2: verify >=300% run-up via OHLCV ----
hits=[]
CAP=70
for i,c in enumerate(cands[:CAP]):
    o=get(f"https://api.coingecko.com/api/v3/coins/{c['id']}/ohlc?vs_currency=usd&days=30")
    time.sleep(6)
    if not isinstance(o,list) or len(o)<5: continue
    highs=[x[2] for x in o]; lows=[x[3] for x in o]; closes=[x[4] for x in o]
    peak=max(highs); pk=highs.index(peak)
    pre_low=min(lows[:pk+1]) if pk>=0 else min(lows)
    if not pre_low or pre_low<=0: continue
    run_up=peak/pre_low-1
    current=closes[-1]
    pullback=1-current/peak if peak else 0
    if run_up>=3.0 and 0.30<=pullback<=0.80:
        c.update({"run_up":run_up,"pullback":pullback,"peak":peak,"current":current,"pre_low":pre_low})
        hits.append(c)
hits.sort(key=lambda x:-x["run_up"])

print(f"\nSTAGE 2: {len(hits)} confirmed (ran >=300% this month, now 30-80% off that peak)\n")
print("  TICKER     NAME                  mc       vol      | run-up  pullback  | peaked    | id")
for h in hits:
    print("  %-10s %-20s $%-7s $%-7s | %-7s %-8s | %-9s | %s"
          %(h["sym"][:10], h["name"][:20], f"{h['mc']/1e6:.1f}M", f"{h['vol']/1e6:.2f}M",
            f"+{h['run_up']*100:.0f}%", f"-{h['pullback']*100:.0f}%", h["athd"], h["id"]))
json.dump(hits, open(os.path.join(HERE,".runup-hits.json"),"w"))
print(f"\n(stage-2 capped at {CAP} candidates; {len(cands)} total stage-1)")
