# Source Quality Guide

Where to find good info and how much to trust it. The engine cites Tier 1 first and treats lower tiers with more skepticism.

## Search broad, then narrow (do this every time)

The single biggest difference between weak results and strong ones is **how many different angles you search, not how hard you search one of them.** A discovery or research pass should pull from a wide spread of sources before it narrows, not lean on one or two. Don't stop at a single `screen_pools` call and a web search.

For **discovery** (finding candidates), sweep across all of these **in parallel** and merge the results, then narrow to the ones with a real angle. Spreading the sweep across sources also means you hit any one source's rate limit far less:
- **CoinGecko** (keyless) — `coin_markets_by_category` across the live narratives (AI agents, AI compute / DePIN, RWA / tokenization, the chain ecosystems), plus `cg_global` for macro. The main market-data + narrative source, and the only one that carries **30-day** change, so it's the tool for *monthly*-gain screens.
- **GeckoTerminal** (keyless) — `screen_pools` (bulk DEX-pool screener: filter by liquidity band + 24h move + volume), `trending_pools`, `new_pools`. The tool for liquidity-band and today's-movers screens. Note: pool data is 24h-only, and one pool's liquidity ≠ the coin's total liquidity.
- **DexScreener** (keyless) — `dexscreener_search`, `dexscreener_trending_boosted` for cross-chain pairs and what's being boosted right now.
- **DefiLlama** (keyless) — `defillama_protocols`, `defillama_fees`, `defillama_dex_volume` to find projects with *real usage and revenue*, not just price action.
- **WebSearch** — run **several differently-worded queries**, not one: the narrative ("best AI agent tokens 2026"), the catalyst ("[chain] ecosystem new launches partnership"), the smart-money angle ("[VC] portfolio recent crypto investment"), and recent news. Different phrasings surface different coins.
- **CoinMarketCap** — `cmc_listings` is a second coin database, but it is **off unless the user optionally added a free key**. Don't depend on it; treat it as a bonus cross-check when available.

**Match the tool to the ask:** monthly-gain screen → CoinGecko categories (it has 30d). Liquidity-band or today's-movers screen → GeckoTerminal `screen_pools`. And remember a raw screen is mostly noise (fresh anon pumps) until you run candidates through the strategy filter.

For **diligence** (vetting one coin), cross-check the same fact across sources rather than trusting the first hit: market data (CoinGecko + GeckoTerminal + DexScreener + on-chain RPC), team (LinkedIn + project site + GitHub + Hugging Face + first-party press), funding (Crunchbase + press releases + founder/VC posts, always with the date).

The point is **diversity of sources and query angles, then intelligent narrowing** — the wide net is what catches the strong, less-obvious coins. One source = one blind spot.

## Tier 1 — Trust, cite first
| Source | Best for |
|---|---|
| Project's own site / docs | Tokenomics, roadmap, official claims (quote directly) |
| Founder's X / personal site | Background, current focus |
| LinkedIn | Verifiable employment history (scroll to load full history) |
| Hugging Face | AI/ML founders — model adoption + co-author credits |
| GitHub | Code activity, commit recency/frequency |
| First-party press releases | Partnership announcements (e.g. a bank's own page) |
| arXiv / IACR | Research, citation counts |

## Tier 2 — Trust with verification
| Source | Best for | Quirk |
|---|---|---|
| CoinGecko | Market data, categories, chart link | Rate-limited ~30/min |
| GeckoTerminal | Pool-level liquidity | Use the largest USD-paired pool |
| DexScreener | Cross-chain pair lookups | Strong for by-address lookups |
| EVM RPC (Base/ETH) | On-chain truth (name/symbol/supply) | Overrides CG/CMC if they conflict |
| TON Center | TON jetton/account data | Required for TON-native projects |
| Crunchbase / PitchBook | Funding rounds | Often 6–12 months stale |
| Messari / TokenInsight | Research summaries | Check for sponsored disclosure |

## Tier 3 — Cross-check before citing
IQ.wiki (verify dates), analyst X threads (direction only), TheBlock/CoinDesk/Decrypt (check date). Reddit/Discord = vibes only, never facts.

## Tier 4 — Avoid / flag
Stale project Medium posts, PR-wire marketing copy, YouTube influencer recaps, anonymous accounts with no track record, project-written "About" sections.

## Citation format (mandatory)
Every team claim or hard fact needs a Ctrl+F-able quote:
```
- [https://example.com/page](https://example.com/page) "exact text from the page"
```
If the source has no phrase that supports the claim, find a different source.

## The "backed" / "treasury" test (mandatory)
When a project says it's "asset-backed," "treasury-backed," or "collateralized," verify the legal structure before repeating it:
1. Is there an SPV/trust that holds assets for token holders? (Rare — name it.)
2. Or does the company hold assets on its own balance sheet? (Then holders have **no** direct claim — write the indirect chain: assets → revenue → buybacks → token.)
3. Or is "backed" pure marketing with no structure? (Flag it.)

**Bankruptcy test:** if the company went bankrupt tomorrow, who legally owns the assets? If the answer is "the bankruptcy estate" rather than "token holders via SPV/trust," it is not real collateralization.
