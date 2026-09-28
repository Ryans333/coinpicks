# Windows + Mac Setup Checklist

Use this when you want to test the zip on a clean computer, or when a member asks "what should happen?"

## The Short Version

1. Download the zip to the computer.
2. Open a new Claude Code session.
3. Drag in the zip and send:
   `Unzip this and set up the CoinPicks research engine, then walk me through it.`
4. Claude opens the **SOP** (`SOP.md`) — your starter checklist — and works it. The one prerequisite on you: **Claude for Chrome** extension installed + logged in. (Community login is optional; the methodology ships in the zip.)
5. Let Claude move/unzip it into one permanent local folder:
   - Windows: `C:\CoinPicks\coinpicks-ai-altcoin-research-engine`
   - Mac: `~/CoinPicks/coinpicks-ai-altcoin-research-engine`
6. Let Claude install `uv` if needed.
7. Let Claude register the `coinpicks-data` server at user/global scope (the server is already bundled in the zip).
8. No key needed to RUN it — market data is keyless out of the box (GeckoTerminal, CoinGecko, DexScreener, DefiLlama, on-chain, TON all work with no key).
9. Fully quit and reopen Claude Code once.
10. Ask Claude to run `cg_global` (ideally from a different folder). If market cap and BTC dominance come back, the data tools are live everywhere.
11. Methodology is **already loaded** (ships in the zip — `framework/COINPICKS-METHOD.md`, `doctrine/`, `examples/`). Nothing to scrape. (Optional: Claude can pull the latest course version from your community later.)
12. Prove the tools first: "Run cg_global for me." (one call, hardest to rate limit.)
    Then the first real scan: "Show me what's trending on Solana right now."
    A 429 on that second one is throttling, not a broken install - wait and retry.

## What Saves Where

The engine uses two places on the computer:

| Place | What goes there | Why |
|---|---|---|
| Claude Code user/global MCP settings | The pointer to the local data server | So the tools work in every new Claude Code session |
| The engine folder | Framework files, reports, usage log, `SEEN-COINS.csv` | So the user's research history stays in one visible folder |

Do not leave the working engine inside an email attachment preview, browser temp folder, or random Downloads subfolder. Move it into the recommended permanent folder first.

Do not move or rename the engine folder after setup unless you rerun setup. The global Claude Code tool registration points to the exact `mcp-server/server.py` path inside this folder.

## Windows Notes

- Use PowerShell commands when installing `uv`.
- If `uv` installs but fails with `Missing expected target directory for Python minor version link`, run:
  `Remove-Item $env:APPDATA\uv\python\cpython-3.12* -Force -Recurse`
  then:
  `uv python install 3.12`
- If `uv` is not on PATH right away, use:
  `%USERPROFILE%\.local\bin\uv.exe`
- If the folder is under OneDrive and setup has file-locking problems, move it to:
  `C:\CoinPicks\coinpicks-ai-altcoin-research-engine`
- After setup, fully quit Claude Code. On Windows Store installs, close all Claude Code windows and quit it from the tray if it is still running.

## Mac Notes

- **If the zip arrived via Messages, AirDrop, or Mail:** save or drag it to Downloads or Desktop FIRST. Claude's tools cannot read files inside `~/Library/Messages/Attachments/` (macOS privacy blocks it), so setup stalls until the file is in a normal folder.
- **Older Macs only have Python 3.9** (too old for the engine). That's fine and expected — `uv` installs its own Python 3.12, so you never touch the system Python. `uv` is needed on Mac too; it is not a Windows-only thing.
- If `uv` is missing, Claude installs it with the official install command.
- If `uv` is not on PATH right away, use:
  `~/.local/bin/uv`
- Recommended permanent folder:
  `~/CoinPicks/coinpicks-ai-altcoin-research-engine`
- After setup, fully quit and reopen Claude Code.

## Pass / Fail Test

After reopening Claude Code, ask:

`run cg_global for me`

Pass:
- Claude returns total crypto market cap, 24h volume, BTC dominance, and ETH dominance.

Fail:
- Claude says the tool is not available.
- Claude tries to browse CoinGecko directly instead of calling the tool.
- Claude gives generic advice instead of live market data.

If it fails, open `TROUBLESHOOT.md` and work its causes IN ORDER before doing research. Do not
assume the registration is at fault: a perfectly valid registration in front of a server that
crashes on startup looks identical, and that assumption is what used to send people in circles.
