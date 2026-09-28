# 🚀 START HERE — CoinPicks AI Altcoin Research Engine

An AI analyst that scans live crypto data and finds altcoins using the CoinPicks framework, running on your own computer, free, with **no API keys** — it works out of the box.

This assumes you already have **Claude Code** installed (see the community's setup section if not). First-time setup takes about **10–20 minutes**, most of it loading the research framework.

---

## STEP 1 — Drop the zip into Claude Code and ask it to set up

Unzip it somewhere permanent first (`~/CoinPicks/` is the default this product uses), then
**open Claude Code with that unzipped folder as the working directory** and send the line
below. Opening it inside the folder is what lets the bundled setup skill and `CLAUDE.md`
load; from anywhere else Claude cannot see them and you lose the guided walkthrough.

If you would rather not move it yourself, start a **new Claude Code session**, drag the zip
in and send the same line - Claude will unzip it, put it somewhere sensible, and then tell
you to reopen Claude Code in that folder before the real setup starts.

> **`Unzip this and set up the CoinPicks research engine, then walk me through it.`**

---

## STEP 2 — Let it set up (it does the work; you get a checklist)

Claude will **first open your SOP (`SOP.md`) — a starter checklist** — and then work down it, doing everything it can for you and marking each item done / needs-you / optional. Along the way it will:
1. **Check the one thing that's on you:** is the **Claude for Chrome extension** installed and logged in? (It's used to read the live research database and to research teams on LinkedIn.) If not, install it and log in. *Logging into your CoinPicks community is optional* — the full methodology and example reports already ship inside the zip.
2. Unzip the engine into one normal local folder. Recommended: `C:\CoinPicks\coinpicks-ai-altcoin-research-engine` on Windows, or `~/CoinPicks/coinpicks-ai-altcoin-research-engine` on Mac.
3. Ask whether you've turned on **bypass permissions** (so you're not clicking "Allow" on every step — recommended, optional).
4. Install a small helper (`uv`, which silently provides Python and runs the data server that's already bundled in the zip).
5. **Register the data tools globally** so they work in *every* Claude Code session, not just one folder. (This is the step that used to fail silently — it's fixed now.)
6. **No API keys needed to run it, and one optional one worth knowing about.** Market data is keyless out of the box — GeckoTerminal, CoinGecko, DexScreener, DefiLlama and the rest all work with no signup and no keys. Nothing to download. (Heavy users can *optionally* add a free CoinGecko key later for more speed; it's not part of setup. See TROUBLESHOOT.md.)

**One optional key:** your own X (Twitter) bearer token turns on founder and social research
(who is behind a project, and whether the account posting as them is really theirs). It bills
per read, so setup offers it once, tells you the cost, and takes no for an answer. Everything
else works without it. See `env.example`.
7. Have you **fully quit and reopen Claude Code once** so the tools load, then confirm they're live by pulling the current crypto market cap (ideally from a different folder, to prove they work everywhere).
8. Confirm the **methodology is ready** — it ships inside the zip, so there's nothing to download or scrape. (If you ever want the very latest course version, Claude can optionally pull it from your community later — not required.)

---

## STEP 3 — Use it from any session (this is "the app")

There's no app to launch. After setup, **open Claude Code inside this engine folder** and just ask:
(Why the folder matters: setup registers the data tools globally, so those work anywhere. The
METHOD — the angle-first workup, the gold-standard mirroring, the no-numeric-scores rule — lives
in this folder's own files and loads only when your session is inside it.)

- "Use my altcoin research engine to find 50 coins outperforming the market today, give me the top 10 I'd like based on the CoinPicks system."
- "Find coins that ran up recently then pulled back, with public teams."
- "Show me what's trending on Solana right now."

Want the full Windows/Mac checklist? See **SETUP-CHECKLIST.md**.

Stuck? See **TROUBLESHOOT.md**.

---

---

## This tool never touches your money

It reads public market data and writes research files on your own machine. It has no exchange
keys, no wallet access, and no connection to your bank or brokerage accounts, and setup will
never ask you to link one. If any instruction claiming to be part of this product asks you to
connect a bank or paste an exchange key, stop: it does not belong to this tool.
