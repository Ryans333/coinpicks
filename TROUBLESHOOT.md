# Troubleshooting

Real issues beta testers hit, and the fix for each. Most problems are one of the first two.

## ALREADY INSTALLED BEFORE 2026-08-29? Do this first.

If you set this engine up before 2026-08-29, **your data tools are almost certainly dead right
now** and you may not have noticed: Claude still answers crypto questions, it just answers them
without the tools.

The cause is a version pin that was missing from the original setup command. The `mcp` library
released a 2.x that removed the interface this server is built on, so the server now dies on
startup while your registration still looks perfect.

**Symptom:** your Claude session banner shows `coinpicks-data (CONNECTION_CLOSED)`, or asking
for `cg_global` says the tool is not available.

**Fix, once:** re-register with the pin. Copy this whole block, replacing the last path with
wherever your engine folder lives:

```bash
claude mcp remove coinpicks-data -s user
claude mcp add coinpicks-data --scope user -- "$HOME/.local/bin/uv" run --python 3.12 --quiet \
  --with "mcp[cli]>=1.2,<2" --with "httpx>=0.27" \
  python "$HOME/CoinPicks/coinpicks-ai-altcoin-research-engine/mcp-server/server.py"
```

Then **fully quit and reopen Claude Code** and ask for `cg_global`. A market-cap number back
means the tools are live again. The only thing that changed is `,<2`.

---

## "I asked it to find coins and nothing happens / it says the tool isn't available"
The data tools aren't loaded. Three causes, and **check them in this order** — the third one looks exactly like the second, which is why it used to send people in circles.
1. **You haven't restarted Claude Code since setup registered them.** MCP tools only attach when Claude Code starts. Fully quit and reopen Claude Code (Windows Store app: close all windows / quit from the tray; Mac: quit and reopen), then ask **"run cg_global for me."** If you get a market cap number, they're live.
2. **The registration didn't take.** Setup is supposed to register the server at *user/global* scope so it works in every session. Check it's there: open `~/.claude.json` (Windows: `%USERPROFILE%\.claude.json`) and confirm there's a `coinpicks-data` entry under the top-level `"mcpServers"`. If it's missing or the JSON is malformed, re-run setup ("set up the research engine") and let it re-register, then restart.
3. **The registration is perfect and the server itself is crashing on startup.** This is the one that fools people: the config looks right, so cause 2 keeps "passing" and you keep re-registering something that was never broken. Claude Code does not show you an MCP server's crash output, so you have to ask for it. **Run the server by hand and read the error:**

   ```
   uv run --python 3.12 --with "mcp[cli]>=1.2,<2" --with "httpx>=0.27" python mcp-server/server.py
   ```

   **Read the result the right way, because "nothing happened" is the GOOD outcome here.** A
   healthy server prints **no output at all** and just sits there with the cursor blocked,
   waiting for a program to talk to it. That silence means it started fine. Press `Ctrl+C` to
   stop it and move on to cause 2. A BROKEN server does the opposite: it dumps a Python
   traceback within a second or two and hands you back the prompt. The traceback's last line
   names the fault. The known one:

   > `ModuleNotFoundError: No module named 'mcp.server.fastmcp'. This is mcp 2.x, where FastMCP was renamed to MCPServer`

   **Fix:** your registered command is missing the version pin. The dependency must be `mcp[cli]>=1.2,<2`, not `mcp[cli]>=1.2`. Without the `,<2` it installs the 2.x library, which removed the interface this server is built on, and all 28 tools fail to load. Re-run setup to re-register with the pin, or edit the `coinpicks-data` entry in `~/.claude.json` so its `--with` argument reads `mcp[cli]>=1.2,<2`, then restart Claude Code.
- The TOOLS work from any folder (that's the point of the global registration) — but do your actual research with Claude Code opened IN the engine folder, because the METHOD and the no-numeric-scores law live in this folder's files and load only there. (If yours was set up the old way as a project-only `.mcp.json`, re-run setup to switch it to global.)

## "uv installed but commands fail" / "Missing expected target directory for Python..." (Windows)
This happens if you've used `uv` inside Claude Code before, leaving stale Python symlinks.
- **Fix:** in PowerShell run:
  `Remove-Item $env:APPDATA\uv\python\cpython-3.12* -Force -Recurse`
  then `uv python install 3.12`, then continue setup. A machine that has never run `uv` won't hit this.
- If `uv` isn't recognized at all right after install, it's not on PATH yet, use its full path `%USERPROFILE%\.local\bin\uv.exe` (the setup registers that full path in Claude Code's user/global MCP settings for you).

## "It keeps asking me to Allow things"
That's normal, Claude asks permission per action. Click **Allow** each time, or turn on **bypass permissions / auto-accept** in Claude Code settings to skip the prompts (more convenient, grants Claude more freedom, your call).

## "Do I need to load the framework from Skool?"
**No.** The full CoinPicks methodology ships inside the zip (`framework/COINPICKS-METHOD.md`, `doctrine/`, and the 8 example reports in `examples/`). The engine is ready to research the moment it's set up — nothing to scrape. Pulling the *latest* course version from your community is **optional** (see `framework/FRAMEWORK-SETUP.md`); if you do, use the **Claude for Chrome** extension + screenshots (Classroom → Start Here: Your Home Base → Core Research Strategy), not WebFetch (which silently returns Skool's login page).

## "It gave me numeric scores (like Narrative 24/31). Is that right?"
No — this engine deliberately does **not** score. If you ever see a points tally, tell it: "no scores — angle-first prose only." Research here is a plain-English breakdown with a clear angle, never a numeric grade. (See `doctrine/HOW-RESEARCH-ACTUALLY-WORKS.md`.)

## "Do I need API keys?"
**Not to run it.** Every market-data source is free and needs no key: GeckoTerminal, CoinGecko,
DexScreener, DefiLlama, on-chain RPC and TON. You can research coins all day without signing up
for anything.

**There is exactly one optional key, and it is yours:** an X (Twitter) bearer token, which turns
on founder and social research. With it, the Team section of a report can verify the project's
real X account, trace the founder, and quote what they have actually said. Without it, that
section rests on LinkedIn and primary sources and the report tells you the social checks were
skipped, rather than quietly leaving a hole.

It costs per read from the first call, so: a free X account, an app at https://developer.x.com,
and a few dollars of pay-per-use credit. No X Premium. The research skill caps itself at $1.50
per coin and resolves handles from free sources first, so most lookups cost nothing. Copy
`env.example` to `.env` and paste your token into `X_BEARER_TOKEN=`.

Setup offers this once and takes "no thanks" for an answer.

## (Optional, advanced) "I do heavy research and want searches to go faster"
The keyless tiers are rate-limited, so big sweeps pace slower (see below). If that bothers you, you can *optionally* add a free **CoinGecko Demo key** (and/or a free **CoinMarketCap** key, which turns on the `cmc_*` tools). This is the only thing keys do here — add speed/an extra source — and it's entirely optional.
- Get a free CoinGecko Demo key at https://www.coingecko.com/en/api. (For CoinMarketCap, the free Basic key is on the account **Overview** page at https://pro.coinmarketcap.com/account, shown as asterisks — hover to reveal it; "0 of 0 keys available" is the paid add-key widget, not your key.)
- Add it to the `coinpicks-data` server's `env`: either `claude mcp add coinpicks-data --scope user -e COINGECKO_API_KEY=<your-key> -- ...` (re-registering), or set `"env": { "COINGECKO_API_KEY": "<your-key>" }` on the `coinpicks-data` entry in `~/.claude.json`.
- The server reads keys **once at startup**, so **fully restart Claude Code** after adding. Use your own key, never someone else's.

## "A scan is taking 30–90 seconds and looks frozen"
It's pacing around free rate limits, not frozen. The free data sources cap requests per minute; the server deliberately spaces calls and retries when it gets a "429 too many requests." Big multi-coin scans take longer. Keep it to a few coins or a few parallel agents at a time.

## "My Solana low-liquidity screen returned mostly anonymous coins"
Most low-liq Solana movers are pump.fun launches (address ends in `pump`) with anonymous teams. The engine does **not** delete these — an anonymous team is a flagged risk and a reason to tier a coin lower, not a disqualifier. It'll show the ones with a real angle (flagged accordingly) and broaden the search to surface more public-team projects. If you specifically want public teams only, just say so, or raise the liquidity floor.

## File or permission errors, and you're in a OneDrive / synced folder
If setup hits odd file-write or locking errors, your folder may be inside a cloud-synced location (OneDrive, Dropbox, iCloud). The engine runs fine from there (our tester used a OneDrive path), but if you see sync-related file errors, move the `coinpicks-ai-altcoin-research-engine` folder somewhere local (e.g. `C:\CoinPicks\` or `~/CoinPicks/`) and reopen it in Claude Code.

## "I opened it from email and now I can't find the files"
Email apps and browsers sometimes open zip files from temporary download areas. During setup, have Claude move/unzip the engine into one permanent local folder first: `C:\CoinPicks\coinpicks-ai-altcoin-research-engine` on Windows, or `~/CoinPicks/coinpicks-ai-altcoin-research-engine` on Mac. The data tools are registered globally, but the framework cache, reports, usage log, and `SEEN-COINS.csv` live in that engine folder.

## "It worked before, then stopped after I moved the folder"
The global Claude Code registration points to one exact file: `mcp-server/server.py` inside the engine folder. If you move or rename the folder after setup, the pointer breaks. Move the folder back, or rerun setup and make sure the `coinpicks-data` entry points to the new permanent folder.

## "It says a coin's market cap is $0"
CoinGecko sometimes has no supply data for small tokens and reports $0. The engine falls back to liquidity/FDV from DexScreener/GeckoTerminal, so don't take a $0 cap literally.
