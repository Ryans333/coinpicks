# 📋 CoinPicks AI Altcoin Research Engine — Setup SOP & Starter Checklist

**Claude: the moment the user drops this zip in and asks to set up, present this SOP first, then work the checklist top to bottom — doing every step you can do for them automatically, and reporting each item as ✅ done / ❌ needs them / ⏭️ optional. Fill in the real status as you go; don't just paste a blank checklist.**

This is the one-page operating procedure for getting the engine running. Most of it Claude does for you. A couple of items only you can confirm.

---

## PART A — Claude does this automatically (you just watch)

- [ ] **Engine unzipped to a permanent folder** (`~/CoinPicks/...` on Mac, `C:\CoinPicks\...` on Windows). Not left inside a Downloads/Mail/AirDrop temp path.
- [ ] **`uv` installed** — one tiny helper that silently provides Python and runs the data server. (You do NOT install Python yourself.)
- [ ] **Data tools registered globally (user scope)** — the research data server (≈28 tools across CoinGecko, GeckoTerminal, DexScreener, DefiLlama, on-chain RPC, TON, CoinMarketCap) is **already bundled inside this zip** (`mcp-server/server.py`). Nothing to download separately. Claude registers it at **user/global scope** (in your `~/.claude.json`), which is the one thing that makes the tools load in *every* Claude Code session in *any* folder. This single global registration is the whole setup — you do NOT need a per-folder copy.
- [ ] **Claude Code restarted once, tools confirmed live FROM ANY FOLDER** — after the restart, Claude calls `cg_global` and gets back a live market-cap number. To prove the global registration really took, this check should pass from a folder that is NOT the engine folder (e.g. your home directory). If the number comes back there, the TOOLS are global. For research itself, open Claude Code IN the engine folder — the method and the no-scores law live in this folder's files and load only there.
- [ ] **Your "Altcoin Database" folder created** — Claude makes `~/Altcoin Database/` (Mac) or `%USERPROFILE%\Altcoin Database\` (Windows), ready to hold your saved research PDFs. This is your local version of the CoinPicks tiered databases.

## PART B — Your starter checklist (only you can confirm these)

- [ ] **Claude for Chrome extension — installed and logged in?**  ✅ YES / ❌ NO
  This is the one prerequisite that's on you. It's needed for two things: reading the live CoinPicks Diamond research database, and researching team members on LinkedIn. If you don't have it: install the Claude for Chrome extension and log into it. (You almost certainly already have it — it's expected for this engine.)
- [ ] **Logged into your CoinPicks community? (OPTIONAL.)**  ⏭️
  The full research methodology and 8 gold-standard example reports already ship **inside this zip** — you don't need to log in to use the engine. Logging into your community (Genesis / Army / Inner Circle) is only needed if you want Claude to pull the *very latest* course version or fresh database entries via the browser.

## NO API KEYS NEEDED — it works out of the box
You do **not** need to sign up for anything to run it, and no key is required for market data. (One optional key, your own X bearer token, adds founder and social research. Setup offers it once; skipping is fine.) Every data source the engine relies on is free and keyless:
| Source | Key needed? |
|---|---|
| GeckoTerminal (pool-level discovery + screening) | **No key** |
| CoinGecko (market data, categories, macro) | **No key** (public tier) |
| DexScreener, DefiLlama, on-chain RPC, TON | **No key** |
| CoinMarketCap | Off by default (optional — see below) |

The keyless tiers are rate-limited, so a big multi-coin sweep paces a little slower and the engine quietly slows down rather than failing. For normal use that's a non-issue.

*Optional, only if you ever do heavy daily research and want more speed:* you can add a free CoinGecko "Demo" key (and/or a free CoinMarketCap key) later — see `TROUBLESHOOT.md`. Not required, not part of setup.

---

## PART C — How this engine researches (so you know what you're getting)

This engine is built to research altcoins **the CoinPicks way**. Two things to understand up front:

### ⚠️ This engine does NOT score your reports. (Important.)
The CoinPicks course teaches a numeric scoring system (Narrative /31, Team /10, an Exclusivity gate). **This engine deliberately does not use those numbers.** It produces deep, plain-English research with a clear angle and an honest breakdown — never a points tally. If you ever see it spit out scores like "Narrative: 24/31," that's wrong; the method here is angle-first, prose, no numeric scoring. (Full reasoning in `doctrine/HOW-RESEARCH-ACTUALLY-WORKS.md`.)

### It researches angle-first, from a wide net of sources.
- **Find the angle first** — the one-sentence reason a coin could re-price — then build the evidence around it.
- **Discovery sweeps many keyless sources in parallel, then narrows:** CoinGecko (categories, market data, the tool for *monthly*-gain screens) + GeckoTerminal (pool screens/trending/new — the tool for liquidity-band and today's-movers screens) + DexScreener + DefiLlama + multiple web-search angles. A wide net widens variety and eases rate limits.
- **Team research leans on LinkedIn first** (past-employer history, with sourced quotes), plus the project's own site/docs, GitHub, and Hugging Face for AI founders.
- **Teams are weighted heavily but never disqualifying** — a strong public team is a big plus; an anonymous team is a flagged risk, not an auto-reject.
- **It reports its sources** at the end of every research answer.

### Your normal flow
1. **"Give me a full research breakdown of [token]."** Claude delivers the deepest breakdown it can **right in the chat** — the full CoinPicks 5-system research, matching the 8 gold-standard examples in `examples/` (angle-first, plain language, a "What $TICKER does" callout, an everyday analogy, the 5 narrative sections as prose, a sourced team section, funding history with dates, honest risks). **No scores. No questions first — you just get the breakdown.**
2. **If you like it: "add [token] to my Altcoin Database."** *Now* Claude asks you: **"What about this project excites you? (What's the angle?)"** Your answer becomes the lead of the report's Overview, then it writes the final report and **saves it as a PDF in your "Altcoin Database" folder** (`~/Altcoin Database/`) — your local version of the CoinPicks tiered databases. One clean PDF per coin you keep.

**Why the angle question fires at save (not before):** it's the angle every good CoinPicks write-up is built around, it becomes a running record of *what kind of setups excite you* (a data layer on your own taste), and it's a filter — if a project doesn't excite you, you simply don't add it.

---

## Where everything lives
- `doctrine/HOW-RESEARCH-ACTUALLY-WORKS.md` — the method (angle-first, no scoring, the recurring patterns). **Claude reads this before every research session.**
- `doctrine/RESEARCH-RULES.md`, `doctrine/SOURCE-QUALITY.md` — the always-on rules + which sources to trust and where to find team info.
- `framework/COINPICKS-METHOD.md` — the 5-system CoinPicks methodology, explained as concepts (de-numbered).
- `examples/` — 8 gold-standard reports + the style guide. Start with
  `EXAMPLE-one-pager.md`, which shows the shape every report follows.
- `CLAUDE.md` — the full operating instructions Claude follows.

When the checklist above is all ✅ (or ⏭️ by choice), you're done. Then use it like this, and the folder matters: **open Claude Code IN this engine folder** (`cd` into it, or open it in your editor and start Claude Code there) and ask for coins. The data tools work from anywhere after setup, but the METHOD — the angle-first workup, the gold-standard mirroring, the no-numeric-scores law — lives in this folder's own files and only loads when your session is inside it. Ask from a random folder and you get generic Claude with crypto tools.
