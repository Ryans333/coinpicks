# CoinPicks AI Altcoin Research Engine

An agentic altcoin research system you run on your own machine. Ask in plain English; it discovers coins from live data, applies the CoinPicks 5-system framework, verifies teams from real sources, and returns ranked picks with the angle and risks attached. **It researches angle-first and never assigns numeric scores.**

New here? Read **START-HERE.md** first. When you set up, Claude opens **SOP.md** — a starter checklist that walks you through everything.

---

## What's in this folder

| Path | What it is |
|---|---|
| `CLAUDE.md` | The brain. Claude Code reads this automatically and runs guided setup + research. |
| `SOP.md` | The setup SOP + starter checklist Claude shows you the moment you set up. |
| `START-HERE.md` | Quick start: drag the zip into Claude Code and set up. Read this first. |
| `SETUP-CHECKLIST.md` | Plain Windows + Mac setup checklist and pass/fail test. |
| `TUTORIAL.md` | The complete operator's manual — everything the system does, start to finish. |
| `TROUBLESHOOT.md` | Fixes for the common setup snags (tools not loading, Windows uv, the Skool framework step). |
| `mcp-server/` | The local data server (28 tools across the core market-data sources). |
| `framework/` | The CoinPicks 5-system method (`COINPICKS-METHOD.md`), shipped in the zip — ready to use, nothing to scrape. `FRAMEWORK-SETUP.md` is the optional "pull the latest from the community" path. |
| `screen-*.py` | Optional pre-built screens for the most common requests (run-up-then-pullback, hot low-liq, etc.). |
| `usage-report.py` | Shows how much you've used each data website (calls, rate-limit hits). Run `uv run python usage-report.py`. |
| `save-report.py` | Renders a finished research report to a clean PDF and files it in your **Altcoin Database** folder (`~/Altcoin Database/`) — your local version of the CoinPicks tiered databases. Claude runs this for you when you say "save this to my Altcoin Database." |
| `doctrine/` | Source-quality rules + the always-on research rules. |
| `reports/` | Where your saved one-pagers land. |
| `examples/` | Eight finalized golden reports to mirror (Sogni, Zama + the six Diamond DB coins) plus a style guide, and a pointer to the live public Diamond Investment Database. |
| `SEEN-COINS.csv` | Your personal dedup ledger so you never re-research the same coin. |

## Data sources
**No API keys needed to run it.** Every source it relies on is free and keyless. Which tool reads which website:

> **Optional speed-up, free, two minutes: a CoinGecko Demo key.** Setup does NOT ask for this
> one — the engine runs fine without it. Add it yourself only if your scans feel slow: the
> public tier allows about 6-8 calls a minute from your IP, and a big request ("find me 50
> coins outperforming this month") is bigger than that. Get it at
> https://www.coingecko.com/en/api and see TROUBLESHOOT.md, "I do heavy research and want
> searches to go faster", for where to put it.

| Website | Tools | Used for |
|---|---|---|
| **GeckoTerminal** | `screen_pools`, `trending_pools`, `new_pools`, `pool_ohlcv`, `get_pools_for_token` | The discovery engine: hot / low-liq / pulled-back screens, 30-day history |
| **CoinGecko** | `search_coin`, `get_coin`, `coin_markets_by_category`, `cg_global` | Narrative/category sweeps, market data, macro |
| **DexScreener** | `dexscreener_search`, `dexscreener_token`, `dexscreener_trending_boosted` | Fast cross-chain pair + token lookups |
| **DefiLlama** | `defillama_protocols` (discovery: rank by TVL, filter by category — note the value is `Dexs`), `defillama_chains` | Finding protocols with real usage. `defillama_fees` and `defillama_dex_volume` take ONE protocol slug, so they confirm a candidate you already have rather than finding one. |
| **Ethereum/Base RPC** | `evm_*`, `erc20_*` | On-chain truth (supply, balances) |
| **TON Center** | `ton_*` | TON-native projects |
| **CoinMarketCap** | `cmc_status`, `cmc_quote`, `cmc_listings` | Off by default (optional). Works only if a user chooses to add a free `CMC_API_KEY` later; not needed. |

The engine runs its market data with **no API keys** — nothing to sign up for. Setup walks you through exactly one optional key, your own X (Twitter) bearer token, which turns on founder and social research; skip it and everything else still works. The keyless tiers are rate-limited, so big multi-coin sweeps pace a little slower (the server spaces requests and retries automatically rather than failing). Heavy users can *optionally* add a free CoinGecko key later for more speed (see `TROUBLESHOOT.md`), but it is not part of setup.

**Heads up on rate limits:** these free sources cap requests per minute, so big multi-coin scans take a little while, the engine paces itself and retries automatically rather than failing. See `TROUBLESHOOT.md`.

## The kinds of questions it answers
- "Find coins that ran 200%+ in the last month then pulled back 30–70%, public teams only."
- "Low-liquidity (\$200K–\$2M) AI / DePIN plays under \$50M cap with verifiable founders."
- "Base coins 90% off their all-time highs but still actively trading."
- "DeFi protocols with real fee revenue that haven't pumped yet."
- "Which RWA projects partnered with a bank or government entity in the last 60 days?"
- "Run the full CoinPicks framework on these 25 coins and rank them."

## Pre-built screens (optional; run `uv run python <name>`)
- `screen-runup-pullback.py` — ran up big, then retraced.
- `screen-hot-lowliq.py` — hot movers, low liquidity.
- `screen-hot.py` — hot movers.
- `screen-relative.py` — **ecosystem-relative only, not a broad-market screen.** It compares
  TAO subnet tokens against TAO, and Virtuals ecosystem tokens against VIRTUAL. Useful for
  "which subnet is beating its parent", useless for "what is beating BTC".
- `screen-virtuals.py` — Virtuals-ecosystem agents.
- `screen-phase2.py` — advanced follow-up screen; run `screen-hot-lowliq.py` first so it has a cache to read.

## The always-on rules
- Leads with the angle, plain language, no hype.
- Teams weighted heavily but never disqualifying — a real public team is a big plus; an anonymous team is a flagged risk and a lower tier, not a rejection.
- Team credibility from **past** employers only, with sourced quotes.
- Funding history analyzed with dates (old rounds flagged as possible VC overhang).
- No numeric scores — conviction reads, not points.
- Never invents numbers; unsourced metrics are left out.
- Research only — not financial advice, no price predictions.

## Want your own research database?
A companion tool, **"Your Own Research Database,"** helps you build your own tiered Notion database of researched coins and connect it. Ask in your CoinPicks community for it.

---
*Built for the CoinPicks community. The methodology and example reports ship inside this engine; the latest course version can optionally be pulled from your community classroom.*
