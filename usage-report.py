#!/usr/bin/env python3
"""
Show which data websites the engine pulled from.

Per-request (what did my last question use?):
    uv run python usage-report.py --last        # your most recent request (auto-detected burst)
    uv run python usage-report.py --minutes 5   # everything in the last 5 minutes

Cumulative (how much overall?):
    uv run python usage-report.py               # all-time totals
    uv run python usage-report.py --today       # just today
    uv run python usage-report.py --days 7      # last N days

Reads usage.log.jsonl (written automatically by the data server on every call).
"""
import json
import os
import sys
import time
from collections import defaultdict

ROOT = os.path.dirname(os.path.abspath(__file__))
LOG = os.path.join(ROOT, "usage.log.jsonl")

HOST_NAME = {
    "api.coingecko.com": "CoinGecko",
    "pro-api.coingecko.com": "CoinGecko Pro",
    "api.geckoterminal.com": "GeckoTerminal",
    "api.dexscreener.com": "DexScreener",
    "pro-api.coinmarketcap.com": "CoinMarketCap",
    "toncenter.com": "TON Center",
    "eth.llamarpc.com": "Ethereum RPC",
    "mainnet.base.org": "Base RPC",
    "api.llama.fi": "DefiLlama",
    "coins.llama.fi": "DefiLlama",
}
FREE_LIMITS = {
    "api.coingecko.com": "keyless ~10-15/min + ~10k/mo",
    "pro-api.coingecko.com": "paid CoinGecko Pro key",
    "api.geckoterminal.com": "keyless ~30/min, no monthly cap",
    "api.dexscreener.com": "keyless ~300/min, no monthly cap",
    "pro-api.coinmarketcap.com": "free key ~30/min + ~10k/mo (optional)",
    "toncenter.com": "1/sec keyless, 10/sec with free key",
    "eth.llamarpc.com": "public RPC, best-effort",
    "mainnet.base.org": "public RPC, best-effort",
}
GAP_SECONDS = 120  # calls more than this far apart are treated as separate requests


def load():
    recs = []
    if not os.path.exists(LOG):
        return recs
    with open(LOG) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                recs.append(json.loads(line))
            except json.JSONDecodeError:
                continue
    recs.sort(key=lambda r: float(r.get("ts", 0) or 0))
    return recs


def last_request_cluster(recs):
    """Most recent contiguous burst of calls (split on gaps > GAP_SECONDS)."""
    if not recs:
        return []
    cluster = [recs[-1]]
    for r in reversed(recs[:-1]):
        if float(cluster[-1].get("ts", 0)) - float(r.get("ts", 0)) <= GAP_SECONDS:
            cluster.append(r)
        else:
            break
    return list(reversed(cluster))


def aggregate(recs):
    per = defaultdict(lambda: {"calls": 0, "rl": 0, "err": 0, "retries": 0, "last": 0.0})
    for r in recs:
        s = per[r.get("host", "?")]
        s["calls"] += 1
        s["retries"] += int(r.get("retries", 0) or 0)
        st = int(r.get("status", 0) or 0)
        if st == 429:
            s["rl"] += 1
        elif st >= 400:
            s["err"] += 1
        s["last"] = max(s["last"], float(r.get("ts", 0) or 0))
    return per


def print_compact(recs, label):
    if not recs:
        print(f"\n{label}: nothing logged.\n")
        return
    per = aggregate(recs)
    t0 = time.strftime("%H:%M:%S", time.localtime(float(recs[0].get("ts", 0))))
    t1 = time.strftime("%H:%M:%S", time.localtime(float(recs[-1].get("ts", 0))))
    total = sum(s["calls"] for s in per.values())
    rl = sum(s["rl"] for s in per.values())
    parts = [f"{HOST_NAME.get(h, h)} {s['calls']}" for h, s in sorted(per.items(), key=lambda kv: -kv[1]["calls"])]
    print(f"\n{label}  ({t0} -> {t1})")
    print("Sources this request: " + ", ".join(parts))
    print(f"Total: {total} calls" + (f" | rate-limited (429): {rl}" if rl else ""))
    print()


def print_detailed(recs, label):
    per = aggregate(recs)
    total = sum(s["calls"] for s in per.values())
    print(f"\nData-source usage  ({label})   total calls: {total}")
    print("=" * 78)
    if total == 0:
        print("Nothing in this window.\n")
        return
    for h, s in sorted(per.items(), key=lambda kv: -kv[1]["calls"]):
        last = time.strftime("%Y-%m-%d %H:%M", time.localtime(s["last"])) if s["last"] else "-"
        flag = "  <-- hitting limits" if s["rl"] else ""
        name = HOST_NAME.get(h, h)
        print(f"{name:16} {s['calls']:>7} calls | 429:{s['rl']:>4} | err:{s['err']:>3} | retries:{s['retries']:>4} | last {last}{flag}")
        if h in FREE_LIMITS:
            print(f"{'':16}   free tier: {FREE_LIMITS[h]}")
    print("=" * 78)
    if any(s["rl"] for s in per.values()):
        print("NOTE: 429s seen. Run fewer parallel agents (about 3-4) so you don't fight the free rate limits.")
    print()


def main():
    args = sys.argv[1:]
    recs = load()
    if not recs:
        print("No usage logged yet. Run some research first, then check back.")
        return

    if "--last" in args:
        print_compact(last_request_cluster(recs), "Your last request")
        return
    if "--minutes" in args:
        try:
            m = float(args[args.index("--minutes") + 1])
        except (ValueError, IndexError):
            m = 5.0
        cutoff = time.time() - m * 60
        print_compact([r for r in recs if float(r.get("ts", 0)) >= cutoff], f"Last {m:g} minutes")
        return
    if "--today" in args:
        today = time.strftime("%Y-%m-%d")
        print_detailed([r for r in recs if r.get("date") == today], "TODAY")
        return
    if "--days" in args:
        try:
            d = int(args[args.index("--days") + 1])
        except (ValueError, IndexError):
            d = 7
        cutoff = time.time() - d * 86400
        print_detailed([r for r in recs if float(r.get("ts", 0)) >= cutoff], f"LAST {d} DAYS")
        return
    print_detailed(recs, "ALL TIME")


if __name__ == "__main__":
    main()
