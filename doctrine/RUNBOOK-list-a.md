# The momentum screen: finding coins that pumped and HELD

A mechanical screen for one specific shape: a token that ran hard, then held most of the run
instead of giving it back. It is a CANDIDATE FINDER, never a buy signal. Everything it returns
still has to survive the research method in `framework/COINPICKS-METHOD.md`.

> **This screen needs a Codex API key, which the engine does not ship with yet.** The spec
> below is the method, written out so you can run it by hand against any full-universe price
> source, or wire it up yourself. The criteria are what matter and they do not depend on the
> data provider.

## The spec (the author's confirmed words, do not reinterpret)

A token qualifies if ALL of:
1. **Pump**: peak price >= **11x** (= +1,000%) a **14-day-median pre-run base**, with the run
   (base end -> peak) inside a **<= 90-day window**.
2. **Peak recency**: the peak is within the **last 90 days** ("could be yesterday, could be 89
   days ago").
3. **Still holding**: current price >= **1.3x the run-start base** ("pulled back down no more than
   30% above where they started" = still >= 30% above base). Deep drawdowns from the PEAK are
   ALLOWED and welcome — do not filter on drawdown-from-peak.
4. **Launch-artifact guard**: the 14-day base window must NOT overlap the pool's first 14 trading
   days (kills fake 1000x readings off launch-price candles, e.g. the ANSEM artifact of the
   2026-07-21 GT-based run).

Floors: liquidity >= $50K, volume24 >= $25K. Exclusions: every ticker in
`cockpit/exclusions.json` holdings + dollarTrue, every contract in blacklist + triaged, plus
stablecoins and wrapped natives (symbol list + any symbol containing "USD").

## Data sources (use ALL; record per-token `sources`)

1. **PRIMARY — Codex.io GraphQL** `https://graph.codex.io/graphql`, header
   `Authorization: <your CODEX_API_KEY, from the .env in this folder>` (read the file, NEVER print
   the key). 121 networks verified 2026-07-21, including Robinhood Chain (4663) and Base (8453).
   Solana's Codex network id = **1399811149** (resolve fresh via `{ getNetworks { id name } }` if
   in doubt).
2. **DexScreener**: `api.dexscreener.com/token-boosts/top/v1` + `/token-boosts/latest/v1` for
   boosted tokens; resolve liq/vol via batch `api.dexscreener.com/tokens/v1/{chainId}/{a1,a2,...}`
   (30 addresses/call, pick highest-h24-volume pair per token, apply the same liq/vol floors).
3. **CoinGecko free trending**: `api.coingecko.com/api/v3/search/trending` — carries NO contract
   addresses, so use it for **symbol tags only** on already-found candidates.
4. **CMC via coinpicks-data MCP**: `cmc_listings(sort="percent_change_24h", limit=100)` (the MCP
   only supports market_cap / volume_24h / percent_change_24h sorts). Output is huge — it lands in
   a tool-results file; pass that file path to the script. Adds candidates with
   `percent_change_90d >= 900` or `percent_change_30d >= 900` AND a platform contract on our
   chains; all CMC symbols also become tags.
5. **GeckoTerminal**: check before using — it was **429-blocked from this machine** on 2026-07-21
   and was SKIPPED entirely (noted in `_meta`).

## Exact queries (Codex)

Networks screened: `[4663 robinhood, 8453 base, 1 eth, 1399811149 solana]`.

Screener (per network, top-volume, server-side floors):
```graphql
query F($nets:[Int!],$lim:Int!) {
  filterTokens(
    filters:{ liquidity:{gte:50000}, volume24:{gte:25000}, network:$nets },
    rankings:[{attribute:volume24, direction:DESC}],
    limit:$lim   # 175 used per network (budget guard; max 200/page)
  ) { results { priceUSD liquidity volume24 pair { address } token { address symbol name networkId } } }
}
```

Daily bars per candidate (215 days = 90d peak recency + 90d run + 14d base + 14d guard + slack):
```graphql
query B($s:String!,$f:Int!,$t:Int!){
  getBars(symbol:$s, from:$f, to:$t, resolution:"1D",
          removeLeadingNullValues:true, currencyCode:"USD"){ s t h c }
}
```
`$s` = `"<tokenAddress>:<networkId>"`; `$f` = now − 215d, `$t` = now. `removeLeadingNullValues`
means bar index == trading-day number, which is what the launch guard keys off.

## The math (as implemented)

For each candidate's cleaned daily bars (drop null/0 closes; h falls back to c):
- `launchedInWindow` = first bar starts > 3 days after the fetch window start. If true, the base
  window may only START at trading-day index >= 14 (guard). If false (pool older than 215d), the
  guard is satisfied by construction.
- For every base-end index `b`: `base = median(close[b-13 .. b])` (14 daily closes).
- Peak = max high over bars after `b` with `t <= t[b] + 90d` AND `t >= now − 90d`.
- Qualify: `peak/base >= 11` AND `current >= 1.3 × base` (current = live screener price if
  available, else last close). Keep the `b` that maximizes the multiple.
- Then: one contract per ticker (keep the highest-REAL-24h-volume contract = decoy preference),
  drop anything with big-liq/dead-volume fake-pool signature (floors re-applied), sort by
  pump_multiple desc, emit top 20.

## Budget accounting (Codex free tier 10K/mo, 5 rps)

Throttle: min 260ms between requests (~3.8 rps). Request count per run:
1 getNetworks (smoke) + 4 filterTokens + 1 getBars per surviving candidate (~700) ≈ **~700–750
total**, logged in `_meta.codex_requests_used`. Hard target < 2,000/run. DexScreener/CoinGecko/CMC
calls are outside Codex budget.

## What to record per token

File: `cockpit/suggested-numeric.json` — `{ _meta, tokens: [...] }`. The UI's `normalize()` picks
`ticker|symbol|sym`, `name`, `chain|network|net`, `gtNetwork`, `contract|token|address|mint`,
`pool|pairAddress`, `priceUsd|price|current_price`, `liquidityUsd|liquidity|liq`,
`vol24hUsd|volume24hUsd|vol24`, thesis from `why|oneLiner|thesis|...` — so every token carries BOTH
the analytical fields (pump_multiple, base_price, peak_price, current_price, current_vs_base_x,
drawdown_from_peak_pct, days_since_peak, run_days, liquidity_usd, volume24_usd, one_line_why) AND
the alias fields (`liq`, `vol24`, `price`, `why`). `gtNetwork` values: robinhood / base / eth /
solana (GeckoTerminal slugs, used to build chart links). **The UI junk-guards files with < 5
tokens** — never ship fewer than 5; pad the spec honestly in `_meta` instead of loosening it
silently.

## Running it by hand

You need one thing: a full-universe list of tokens with enough price history to measure a
14-day median base, the peak since, and where price sits now. Then apply the spec above token
by token. The output is a shortlist, and the shortlist is the beginning of the research, not
the end of it.


## Known limits (honesty, carried in _meta)

- Universe = per-network TOP-175-by-24h-volume above the floors + boosted/CMC merges. Tokens that
  pumped but now trade under $25K/day volume (or $50K liq) are invisible to this screen.
- CoinGecko trending contributes tags only (no contracts in that API).
- CMC's MCP tool can't sort by 90d change; the 24h-sort top-100 is scanned for 30/90d >= 900%
  entries instead — a partial view of CMC's universe.
- getBars uses the token's top pool as priced by Codex; `pool` in the output is the screener's
  pair address (may be null for CMC-sourced candidates).
