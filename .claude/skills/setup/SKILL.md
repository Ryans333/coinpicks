---
name: setup
description: Guided one-time setup for the CoinPicks AI Altcoin Research Engine. Use when the user says "set up", "get started", "install", "begin", drops the engine zip in, or it's their first time. Installs uv, registers the data server at user (global) scope so tools load in every session, confirms the bundled methodology, and runs a first scan. The framework ships IN the zip - nothing is scraped from Skool.
---

# Setup the CoinPicks AI Altcoin Research Engine

**First, present `SOP.md`** as the user's starter checklist, then work it top to bottom — doing every step you can automatically and marking each item ✅ done / ❌ needs them / ⏭️ optional. Run the **FIRST-TIME SETUP** sequence in the root `CLAUDE.md` as the detailed "how," step by step, checking in with the user. Do not paste all steps at once. Summary:

**⚠️ This engine does NOT score. Never output Narrative /31, Team /10, or any points tally — research is angle-first prose. See `doctrine/HOW-RESEARCH-ACTUALLY-WORKS.md`.**

0. **Show the SOP. Check the one prerequisite:** is **Claude for Chrome** installed + logged in (needed for the live Diamond DB + LinkedIn team research)? Community login is OPTIONAL — the methodology + examples ship in the zip. Then ask about **bypass permissions** (optional, smoother).
1. Detect OS. Do NOT ask them to install Python.
2. Install `uv` if missing (the only thing to install; it auto-provides Python 3.12 + the server's packages). On Windows, watch for the stale-symlink error and clear it if it appears.
3. **Register the data server at USER (global) scope** so the data tools load in EVERY session (the key fix for the silent "tools never loaded" failure). Prefer `claude mcp add coinpicks-data --scope user -- <uv> run --python 3.12 --quiet --with "mcp[cli]>=1.2,<2" --with "httpx>=0.27" python "<ABS server.py path>"`. If it already exists, repoint it to the current folder. If no `claude` CLI, carefully add/update the entry under the top-level `mcpServers` in `~/.claude.json` (back it up first). The server is **already bundled** in the zip (`mcp-server/server.py`) — nothing to download.
3b. **Market data needs no keys.** GeckoTerminal, CoinGecko (public tier), DexScreener, DefiLlama, on-chain RPC and TON all work with no key and no signup. Do not ask for any key to make the engine run. (CoinMarketCap is off by default; optional free key in TROUBLESHOOT for heavy users.)

3c. **X (Twitter) key — the one key worth offering, and it is OPTIONAL.** Founder and social
    research is the half of the Team system that market data cannot answer: whether the
    account posting as the project IS the project, who the founder actually is, and what they
    have said lately. That runs on the member's OWN X API key via the `social-research` skill.
    Walk it, do not skip it, and do not oversell it:
    - Say what it buys: verified project handle, founder tracing, and their recent posts, in
      the Team section of every report. Without it, Team rests on LinkedIn and primary sources
      and the report says the social checks were skipped.
    - Say what it costs BEFORE they sign up: X bills per read from the first call. A free X
      account plus an app at https://developer.x.com plus a few dollars of pay-per-use credit
      is the whole requirement. **No X Premium.** The skill caps itself at $1.50 per coin and
      resolves handles from free sources first, so most lookups cost nothing.
    - Where it goes: `X_BEARER_TOKEN=...` in the `.env` at the engine root. **They paste it
      into the file themselves. It never goes in chat, and you never read it back.**
    - **SKIPPING IS A REAL ANSWER.** If they decline, or want to decide later, record it and
      move on immediately. Everything else works. Never make this feel required, and never ask
      a second time.
4. Have the user **fully quit and reopen Claude Code once**, then confirm by calling `mcp__coinpicks-data__cg_global` — ideally from a folder that is NOT the engine folder, to prove the global TOOL registration works everywhere. Don't proceed until it works. Then tell the member plainly: the tools are global, but the METHOD lives in this folder — open Claude Code in the engine folder to do research.
5. **Methodology is already loaded** — it ships in the zip (`framework/COINPICKS-METHOD.md` + `doctrine/` + `examples/`). Nothing to scrape. Just confirm it's ready. (OPTIONAL: if the user wants the latest course version, follow `framework/FRAMEWORK-SETUP.md` to pull it from their community via the browser — a refresh, never required.)
6. Prove it with `cg_global` FIRST ("run cg_global for me") - total market cap plus BTC
   dominance, one call, and the endpoint least likely to be rate limited. Only once that
   returns, run a real scan (e.g. trending on Solana) to show it working. A `429` on the
   trending call is THROTTLING, not a broken install: wait a few seconds and retry, and never
   let it read as a failed setup.

Then hand off to the standing research behavior in `CLAUDE.md` — which begins by reading `doctrine/HOW-RESEARCH-ACTUALLY-WORKS.md` (angle-driven, no numeric scoring, never disqualify on team). Keep it plain-language and friendly.
