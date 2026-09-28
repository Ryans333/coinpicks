#!/usr/bin/env python3
"""
update-seen-coins.py — maintain the cumulative SEEN-COINS.csv ledger.

SEEN-COINS.csv is the master record of every coin examined by this engine.
Before a large scan, Claude should read it and skip anything already listed
(match on ticker OR contract address). After a scan, append the candidate set.

Usage (run from the engine folder):
    # Append a scan's merged candidates (JSON array of objects with ticker/name/chain/contract_address/source)
    python3 update-seen-coins.py --add reports/candidates.json --date 2026-06-25

    # Or append from a candidates-considered.csv
    python3 update-seen-coins.py --add reports/candidates-considered.csv --date 2026-06-25

    # Print the current skip list (comma-separated tickers) for pasting into agent prompts
    python3 update-seen-coins.py --skiplist
"""
import csv, json, os, sys, argparse

LEDGER = os.path.join(os.path.dirname(os.path.abspath(__file__)), "SEEN-COINS.csv")
FIELDS = ["ticker","name","chain","contract_address","first_seen_date","runs_seen","times_seen","last_source"]

def key(t, ca):
    ca = (ca or "").strip().lower()
    return ca if ca and ca not in ("","n/a","none","null","0x") else "TK:"+(t or "").strip().lower()

def load():
    m = {}
    if os.path.exists(LEDGER):
        for r in csv.DictReader(open(LEDGER)):
            m[key(r["ticker"], r["contract_address"])] = r
    return m

def save(master):
    rows = sorted(master.values(), key=lambda r:(r["first_seen_date"], r["ticker"].lower()))
    with open(LEDGER, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS); w.writeheader()
        for r in rows: w.writerow({k:r.get(k,"") for k in FIELDS})
    return len(rows)

def read_any(path):
    if path.endswith(".json"):
        data = json.load(open(path))
        return data if isinstance(data, list) else [data]
    return list(csv.DictReader(open(path)))

def add(path, date):
    master = load()
    for r in read_any(path):
        t = str(r.get("ticker","")).strip()
        if not t: continue
        ca = str(r.get("contract_address","")).strip()
        k = key(t, ca)
        src = str(r.get("source","") or r.get("discovery_signal","")).split(":")[0][:40]
        if k in master:
            m = master[k]
            runs = set(filter(None, m.get("runs_seen","").split("|"))); runs.add(date)
            m["runs_seen"] = "|".join(sorted(runs))
            m["times_seen"] = str(int(m.get("times_seen","1") or 1) + 1)
            if not m.get("contract_address") and ca: m["contract_address"] = ca
        else:
            master[k] = {"ticker":t,"name":str(r.get("name","")),"chain":str(r.get("chain","")),
                         "contract_address":ca,"first_seen_date":date,"runs_seen":date,
                         "times_seen":"1","last_source":src}
    n = save(master)
    print(f"SEEN-COINS.csv now holds {n} unique coins (added from {path}, run {date}).")

def skiplist():
    master = load()
    tics = sorted({r["ticker"].strip() for r in master.values() if r["ticker"].strip()})
    print(", ".join(tics))

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--add"); ap.add_argument("--date")
    ap.add_argument("--skiplist", action="store_true")
    a = ap.parse_args()
    if a.skiplist: skiplist()
    elif a.add and a.date: add(a.add, a.date)
    else: ap.print_help()
