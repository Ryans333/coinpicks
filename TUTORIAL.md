# CoinPicks AI Altcoin Research Engine — Operator's Manual

*A complete guide to running the same agentic research desk the author uses every day. Written to institutional standard: precise, security-first, no hype. This is a research instrument, not investment advice.*

---

## 0. What this actually is

Most people "research" altcoins by scrolling Twitter and trusting a stranger's chart. This replaces that with a disciplined, repeatable process: you describe what you want in plain English, and an AI analyst pulls live on-chain and market data, applies a fixed research framework, verifies the team against primary sources, and hands you a ranked shortlist with the thesis and the risks already attached.

It runs entirely on your own machine, and your data never leaves it. No key is required to
operate it: all of its market data is free and keyless. There is one optional key, your own X
(Twitter) bearer token, which turns on founder and social research in the Team section. It
stays in a local file, is only ever sent to X, and skipping it costs you nothing but that one
section's social checks.

You will use three things, in order, every session:
1. **Discovery** — find candidates from live data.
2. **Diligence** — judge them against the framework in prose, and verify the people.
3. **Disposition** — save the keepers, log everything, never repeat work.

The rest of this manual covers each in operating detail.

---

## 1. First-time setup (once per machine)

Full step-by-step lives in `START-HERE.md` and is automated by the engine itself. In short:

1. In a **new Claude Code session**, drag in the engine zip.
2. Send: **`Unzip this and set up the CoinPicks research engine.`**
3. Follow Claude's prompts (it checks in as it goes).

Claude first opens your **SOP** (a starter checklist) and checks the one prerequisite that's on you — the Claude for Chrome extension. Then it puts the engine in one permanent local folder (`C:\CoinPicks\...` on Windows or `~/CoinPicks/...` on Mac), installs `uv` (a single helper that silently provides Python and the data server that's bundled in the zip), **registers the data tools at global scope so they load in every Claude Code session** (not just one folder — this is what makes it work reliably), has you restart Claude Code once, and confirms the tools are live with a live proof scan. There are **no API keys** to set up — the engine needs no key to run. The methodology and example reports already ship inside the zip, so there's nothing to scrape. You do not install Python.

**Security posture (read this):**
- The data server runs locally and only makes outbound calls to public market-data APIs. Nothing about your machine is uploaded.
- The engine never asks for a wallet, a seed phrase, or a private key, and it never will. If anything ever prompts you for one, stop.
- It needs **no API keys to run** — every market-data source is free and keyless. One optional key (your own X bearer token) adds founder and social research. Nothing else to sign up for and no secret to store or leak. (If you ever optionally add a free CoinGecko key later for speed, it stays on your machine in your local Claude Code config.)
- This tool reads data. It does not trade, move funds, or touch an exchange account.

---

## 2. The data layer (what the engine sees)

The engine reads from live market-data sources through 28 local tools. You never call these by hand; the AI selects them. Knowing them helps you understand what it can and cannot know.

| Source | What it provides | Used for |
|---|---|---|
| CoinGecko | Market cap, price, categories, exchange listings | Narrative sweeps, macro context, chart links |
| GeckoTerminal | DEX pool liquidity, trending/new pools, candles | The core discovery engine (hot / low-liq / pulled-back) |
| DexScreener | Cross-chain pair lookups by token/address | Fast verification, trending/boosted tokens |
| DefiLlama | Protocol TVL, fees, revenue, DEX volume | DeFi fundamentals and "real usage" checks |
| Ethereum + Base RPC | On-chain token name/symbol/supply, balances | Ground truth (overrides aggregators if they disagree) |
| TON Center | TON account + jetton data | Any TON-native project |
| CoinMarketCap | Optional second coin database (top by mcap / volume / 24h gainers) | Off by default; works only if a user optionally adds a free `CMC_API_KEY`. Not part of setup. |

On-chain RPC is treated as the authority: if CoinGecko and the chain disagree on supply, the chain wins.

---

## 3. Discovery — finding candidates

You drive discovery by talking. There are no menus. The AI translates your plain-English request into the right combination of tool calls, then returns candidates. These are the patterns the system is built around. Use them verbatim or remix them.

### 3.1 The core screens
- **Run-up-then-pullback** (the workhorse): *"Find coins that ran 200%+ in the last month and have since pulled back 30 to 70 percent, public teams only."*
- **Hot, low liquidity**: *"Show me coins running hot right now with under $2M liquidity."*
- **Relative strength**: *"What's outperforming the broad market and BTC over the last week?"*
- **Near all-time-high**: *"Coins within 15% of their all-time high that are still actively traded."*
- **Deep drawdown, still alive**: *"Base coins 90% off their highs but still trading real volume."*
- **New launches**: *"What launched in the last few days on Base or Solana with real liquidity?"*

### 3.2 Narrative sweeps
- *"Find me AI-agent tokens under $50M cap with verifiable founders."*
- *"DePIN projects with real hardware networks and growing usage."*
- *"RWA / tokenization plays that partnered with a bank or government entity in the last 60 days."*
- *"DeFi protocols with real fee revenue that haven't pumped yet."*

### 3.3 Ecosystem-specific
- *"Top Virtuals Protocol agents that are actually outperforming, not dead."*
- *"Bittensor subnets (alpha tokens) outperforming TAO itself."*
- *"Solana tokens with a real product, not just a celebrity meme."*

### 3.4 Scale (the parallel desk)
For breadth, ask for a swarm: *"Research 100 coins. Use parallel discovery agents across trending Base, trending Solana, category sweeps, new launches, and recent ATH-makers. Dedupe, run the framework on each, and surface the top 10."* The AI fans out, collects candidates, removes anything already in your ledger, and returns a ranked set. This is the "hundreds of coins before breakfast" capability.

*Rate-limit note:* the free data sources have per-minute limits, so when running swarms keep it to about 3-4 parallel agents. The server automatically spaces requests and retries on rate-limit hits, so scans slow down gracefully instead of failing.

### 3.5 The optional shortcut scripts
The same common screens exist as scripts at the folder root (`screen-runup-pullback.py`, `screen-hot-lowliq.py`, `screen-relative.py`, `screen-virtuals.py`, `screen-hot.py`). Run any with `uv run python <name>`. `screen-phase2.py` is an advanced follow-up that reads the cache created by `screen-hot-lowliq.py`, so run that first. These scripts are a convenience, not a requirement; conversation is the primary interface.

---

## 4. Diligence — the CoinPicks 5-system framework

Discovery gives you names. The framework decides which names are real. The process is **angle-first** (see `doctrine/HOW-RESEARCH-ACTUALLY-WORKS.md`): find the one-sentence reason a coin could re-price, *then* build the evidence. The five systems (which ship inside the zip in `framework/COINPICKS-METHOD.md`) are what the evidence covers:

1. **Core Strategy** — what structural shift is this coin a bet on, and is that shift real?
2. **Product / Exclusivity** — is there a working product, and is there anything here that competitors cannot trivially copy?
3. **Liquidity Analysis** — how thin is the float, where is the real pool, and what does that mean for entry/exit and for how violently it can move?
4. **Narrative** — maturity, smart-money compatibility, communication, lineage, and mutation of the narrative the coin rides.
5. **Team Credibility** — who are the people, and what have they actually shipped before (past employers, sourced)?

The engine assembles the evidence so you judge from facts, not vibes, and it lands each coin in a **conviction read** rather than a numeric score. A strong public team is a big plus; an anonymous team is a flagged risk, not an automatic rejection. If the framework files aren't loaded, the engine can still list coins but will tell you it hasn't loaded the framework. Load it before doing real diligence.

---

## 5. Team verification (the part most people skip)

This is where the institutional discipline lives. The rules are absolute:

- **Credibility comes from PAST employers and shipped projects, never the current one.** "Our team is world-class" from the project's own site counts for nothing.
- **Every team claim needs a primary source with a Ctrl+F-able quote.** Format:
  `- [https://source-url](https://source-url) "exact phrase from the page"`
  If you cannot find a phrase on a real page that supports the claim, you do not write the claim.
- **No name-drops without a plain-English bio.** Never assume the reader knows who someone is. Say what they did and where, with the number that proves it.
- **Trust order** (full detail in `doctrine/SOURCE-QUALITY.md`): project docs, founder's own pages, LinkedIn, Hugging Face, GitHub, first-party press releases, and research registries are Tier 1. Crunchbase and aggregators are Tier 2 (often stale). News is Tier 3. Influencer videos and anonymous accounts are never cited.

### The "backed" test (mandatory)
Whenever a project claims to be "asset-backed," "treasury-backed," or "collateralized," verify the legal structure before repeating it. Ask the bankruptcy question: *if this company went bankrupt tomorrow, who legally owns the assets?* If the answer is "the bankruptcy estate" rather than "token holders through an SPV or trust," then it is marketing, not collateralization, and you say so.

---

## 6. The non-negotiable rules (always on)

These are enforced on every scan and every write-up. Full text in `doctrine/RESEARCH-RULES.md`.

1. Lead with the angle, in plain language. No shilling adjectives.
2. Teams are weighted heavily but never disqualifying — a strong public team is a big plus; an anonymous team is a flagged risk and a lower tier, not a rejection.
3. Past-employer credibility only, always sourced.
4. Funding history is analyzed with dates — flag old (2021-era) rounds as possible VC overhang; check for recent activity.
5. No numeric scores — conviction reads, not Narrative /31 or Team /10.
6. Never invent a number. Unsourced metric = omitted metric.
7. Multi-chain projects are not disqualified for a selected chain.
8. Verify every "backed" claim with the bankruptcy test.
9. This is research, not financial advice. No price predictions, no "buy this."
10. Dedupe everything (see next section).

---

## 7. Disposition — output, ledger, and never repeating work

### 7.1 The one-pager
Keepers get saved as a markdown one-pager in `reports/`. The format (see `examples/EXAMPLE-one-pager.md`) is: ticker / chain / liquidity, a 3 to 4 sentence angle that leads with the structural thesis, token utility, a sourced team section, institutional/VC signals, the honest risks, current market data, and a verdict of Pass / Watch / Worth deeper research.

### 7.2 The dedup ledger
Every coin you examine is appended to `SEEN-COINS.csv` via `update-seen-coins.py`. This is what lets you scan hundreds of coins a week without ever re-researching the same one. Before any large sweep, the engine excludes everything already in the ledger. Keyed by contract address first, then ticker, so two different projects that share a ticker are never confused.

### 7.3 Knowing your usage
The data server logs every external call to `usage.log.jsonl` automatically. Run a report anytime:
```
uv run python usage-report.py            # all-time
uv run python usage-report.py --today    # just today
uv run python usage-report.py --days 7   # last week
```
It shows, per website: total calls, how many got rate-limited (429), errors, retries, and last use, alongside each source's free-tier limit. If a source starts showing 429s, that is the signal to run fewer parallel agents. Nothing leaves your machine; the log is local and git-ignored.

### 7.4 Turning research into a thesis
The same machinery powers two higher-order outputs the author produces:
- **Case studies** ("why did $X gain 300%?"): reverse-engineer a move into catalyst, mechanics (float and liquidity displacement), market context, and the repeatable lesson. The discipline is the same: sourced facts, honest mechanics, no narrative-fitting.
- **Conviction write-ups**: a fully researched coin with the angle, the sourced team, and the risks, ready to share.

---

## 8. Operating rhythm (how a real session goes)

1. Open Claude Code **inside this engine folder** after setup (the method loads from this folder's files; the data tools alone work anywhere).
2. State your hunt in plain English (Section 3).
3. The engine returns candidates, ledger-deduped.
4. Pick the interesting ones; ask it to run the full framework and verify the teams (Sections 4 and 5).
5. It returns scored write-ups with sourced bios and risk flags.
6. Save keepers to `reports/`; everything examined lands in the ledger.
7. Repeat tomorrow without ever covering the same ground twice.

That is the entire system. Simplicity is the point: you bring the questions and the judgment; the engine brings the data, the discipline, and the speed.

---

## 9. Where to go next

- **Your own research database**: a companion tool helps you build your own tiered database of researched coins and connect it to Notion. Available through your CoinPicks community.

---

*Built for the CoinPicks community. Research only. Not financial advice. No price predictions. Verify everything; the engine shows its sources so you can.*
