# coinpicks-data MCP server

A local server that wraps live crypto data sources into 28 callable tools. This is what lets the AI actually find and verify coins instead of guessing. It runs on your machine; nothing leaves it except normal public API calls to market-data websites.

You do **not** install anything here by hand — `uv` runs it and auto-installs its Python packages. Setup (see the root `CLAUDE.md`) wires it up for you.

## 28 tools across the core sources

**CoinGecko (4)** — `search_coin`, `get_coin`, `coin_markets_by_category`, `cg_global`
**GeckoTerminal (6)** — `network_list`, `get_pools_for_token`, `trending_pools`, `new_pools`, `screen_pools`, `pool_ohlcv`
**DexScreener (3)** — `dexscreener_token`, `dexscreener_search`, `dexscreener_trending_boosted`
**Ethereum + Base RPC (4, keyless)** — `evm_block_number`, `evm_get_balance`, `erc20_token_info`, `erc20_balance_of`
**TON (3, keyless)** — `ton_account`, `ton_jetton_master`, `ton_jetton_wallets`
**DefiLlama (5, keyless)** — `defillama_protocols`, `defillama_protocol`, `defillama_chains`, `defillama_fees`, `defillama_dex_volume`
**CoinMarketCap (3, optional)** — `cmc_status`, `cmc_quote`, `cmc_listings` if the user later adds `CMC_API_KEY`

## Requirements
- **`uv`** (installed during setup) — that's the only thing. `uv` auto-downloads its own Python 3.12 and installs the server's packages, so you do **not** need to install Python yourself.

## Built-in rate-limit defense
The server spaces requests per host (CoinGecko keyless is the tightest) and retries with exponential backoff + honors `Retry-After` on 429/5xx, so parallel agents don't hard-fail on a single rate-limit hit.

## How it's registered
Setup registers this server at Claude Code's user/global scope. After one full Claude Code restart, the 28 tools load in any session as `mcp__coinpicks-data__<tool_name>`. A project-local `.mcp.json.template` is still included only as a fallback for advanced users who specifically want project scope.

## Test it manually
```bash
uv run --python 3.12 --with "mcp[cli]>=1.2,<2" --with "httpx>=0.27" python mcp-server/server.py
```
(or just ask Claude to call `cg_global` after setup — if it returns market data, you're connected.)
