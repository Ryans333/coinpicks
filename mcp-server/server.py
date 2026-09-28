#!/usr/bin/env -S uv run --quiet
# /// script
# requires-python = ">=3.10"
# dependencies = ["mcp[cli]>=1.2,<2", "httpx>=0.27"]
# ///
"""
coinpicks-data MCP server.

Wraps free + (optional) paid crypto data APIs into clean, deterministic tools
for the coinpicks-research skill.

Data sources covered:
  - CoinGecko (free public API)
  - GeckoTerminal (free public API)
  - DexScreener (free public API)
  - CoinMarketCap (requires CMC_API_KEY env var, graceful degradation if missing)
  - Ethereum + Base direct RPC (public endpoints, no key)
  - TON via TON Center API (free tier, no key)

Run as: `uv run server.py` (or register with Claude Code, see README).
"""

from __future__ import annotations

import asyncio
import json
import os
from pathlib import Path
import random
import time
from typing import Any

import httpx
from mcp.server.fastmcp import FastMCP

# ============================================================
# Bases / config
# ============================================================

CG_BASE = "https://api.coingecko.com/api/v3"
GT_BASE = "https://api.geckoterminal.com/api/v2"
DS_BASE = "https://api.dexscreener.com"
CMC_BASE = "https://pro-api.coinmarketcap.com/v1"
TON_BASE = "https://toncenter.com/api/v3"
DL_BASE = "https://api.llama.fi"
DL_COINS_BASE = "https://coins.llama.fi"

GT_HEADERS = {"Accept": "application/json;version=20230302"}

# ---------------------------------------------------------------------------
# .env LOADER (2026-08-29). env.example tells the member to copy it to `.env` and paste their
# keys in. Until now nothing read that file: the server used os.environ only, so a member who
# followed the instruction got NOTHING, silently, forever — a key that is never read produces
# no error, the tools just stay off exactly as if no key existed. Found in a pre-ship audit.
#
# Real environment variables WIN over the file, so registering keys in the MCP `env` block
# (the route TROUBLESHOOT.md documents) still takes precedence and nothing that worked before
# changes. Hand-parsed on purpose: no new dependency for six lines of work.
def _load_dotenv() -> None:
    here = Path(globals().get("__file__", "server.py")).resolve().parent
    for candidate in (here.parent / ".env", Path.cwd() / ".env"):
        try:
            if not candidate.is_file():
                continue
            for raw in candidate.read_text(encoding="utf-8").splitlines():
                line = raw.strip()
                if not line or line.startswith("#") or "=" not in line:
                    continue
                k, _, v = line.partition("=")
                k, v = k.strip(), v.strip().strip('"').strip("'")
                # never clobber a real env var, and never set an empty placeholder
                if k and v and k not in os.environ:
                    os.environ[k] = v
            return
        except Exception:
            continue          # an unreadable .env is "no keys", never a crash


_load_dotenv()

CMC_KEY = os.environ.get("CMC_API_KEY", "")
CMC_HEADERS = {"X-CMC_PRO_API_KEY": CMC_KEY} if CMC_KEY else None

# CoinGecko keys (optional but recommended). The keyless tier is only ~10-15 calls/min
# shared per IP, which parallel agents blow through instantly. A FREE "Demo" key lifts
# that to ~30/min + 10k/month. You can set ONE or MULTIPLE comma-separated keys in
# COINGECKO_API_KEY; we rotate across them round-robin to multiply the rate limit.
# Demo keys (free) use the demo header. Set COINGECKO_PRO=1 only for a paid Pro key.
_cg_raw = os.environ.get("COINGECKO_API_KEY", "") or os.environ.get("CG_API_KEY", "")
CG_KEYS = [k.strip() for k in _cg_raw.split(",") if k.strip()]
CG_PRO = os.environ.get("COINGECKO_PRO", "").lower() in ("1", "true", "yes")
if CG_PRO and CG_KEYS:
    CG_BASE = "https://pro-api.coingecko.com/api/v3"
_cg_rr = 0


def _cg_headers() -> dict | None:
    if not CG_KEYS:
        return None
    global _cg_rr
    key = CG_KEYS[_cg_rr % len(CG_KEYS)]
    _cg_rr += 1
    return {"x-cg-pro-api-key": key} if CG_PRO else {"x-cg-demo-api-key": key}


# Per-host minimum spacing between requests, so parallel agents don't burst one endpoint
# into 429s. CoinGecko keyless is the tightest; each key lets us poll faster, and more
# keys = more throughput (rotated above), so we tighten the interval as keys are added.
# PACING FROM REAL USAGE, not from a guess (2026-08-29). These numbers come from the author's
# own usage log across 2,394 logged calls on the same server, which is the only evidence that
# actually counts here:
#   api.coingecko.com     @ 4.0s -> 1,136 calls,   1% retries,  4 x 429   HEALTHY, leave it
#   api.geckoterminal.com @ 2.2s ->   428 calls, 102% retries, 66 x 429   TOO FAST
# A single burst test on one IP suggested CoinGecko needed 8.0s; 1,136 real calls say it does
# not, and the bigger sample wins. GeckoTerminal was the host actually drowning the whole time.
# Retries consume quota too, so a 102% retry rate means the EFFECTIVE request rate was about
# double the nominal one - which is why 2.2s (27/min nominal) kept crossing a 30/min ceiling.
_cg_interval = 1.0 if len(CG_KEYS) >= 2 else (2.0 if CG_KEYS else 4.0)
_HOST_MIN_INTERVAL = {
    "api.coingecko.com": _cg_interval,
    "pro-api.coingecko.com": 1.0,
    "api.geckoterminal.com": 4.0,   # was 2.2 -> 102% retry rate in real use; see note above
}
_host_locks: dict[str, asyncio.Lock] = {}
_host_last: dict[str, float] = {}

# Usage telemetry: one appended line per external call, so you can see how much
# you hit each data website and when you're nearing a rate limit. Lives at the
# project root as usage.log.jsonl. Set COINPICKS_USAGE_LOG=0 to disable.
USAGE_LOG = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "usage.log.jsonl"
)
USAGE_ON = os.environ.get("COINPICKS_USAGE_LOG", "1").lower() not in ("0", "false", "no")

EVM_RPCS = {
    "ethereum": "https://eth.llamarpc.com",
    "eth": "https://eth.llamarpc.com",
    "base": "https://mainnet.base.org",
}

KNOWN_NETWORKS = [
    "eth", "base", "solana", "bsc", "arbitrum", "polygon_pos", "avax",
    "optimism", "ton", "sui", "ftm", "cro", "linea", "blast", "mantle",
    "berachain", "celo", "scroll", "zksync", "hyperliquid",
]

mcp = FastMCP("coinpicks-data")

_client: httpx.AsyncClient | None = None


async def client() -> httpx.AsyncClient:
    global _client
    if _client is None:
        _client = httpx.AsyncClient(timeout=30.0)
    return _client


def _host_of(url: str) -> str:
    try:
        return url.split("/")[2]
    except IndexError:
        return url


# ADAPTIVE PACING (2026-08-29). The shipped intervals are a guess at each free tier's real
# ceiling, and the ceiling moves: it is per-IP, shared, and varies by time of day. Rather than
# keep hammering at a speed we have just been told is too fast, a 429 PERMANENTLY widens this
# host's interval for the rest of the session (1.6x, capped at 30s). The run gets slower and
# it FINISHES, instead of exhausting retries and handing the member an error on a request the
# engine advertises it can do. Reset when the process restarts.
_HOST_BACKOFF: dict[str, float] = {}


def _widen_interval(host: str) -> float:
    base = _HOST_MIN_INTERVAL.get(host, 1.0) or 1.0
    cur = _HOST_BACKOFF.get(host, base)
    new = min(cur * 1.6, 30.0)
    _HOST_BACKOFF[host] = new
    return new


async def _throttle(host: str) -> None:
    """Space out requests to a host so concurrent callers don't burst into 429s."""
    interval = max(_HOST_MIN_INTERVAL.get(host, 0.0), _HOST_BACKOFF.get(host, 0.0))
    if interval <= 0:
        return
    lock = _host_locks.setdefault(host, asyncio.Lock())
    async with lock:
        wait = interval - (time.monotonic() - _host_last.get(host, 0.0))
        if wait > 0:
            await asyncio.sleep(wait)
        _host_last[host] = time.monotonic()


def _retry_delay(resp, attempt: int) -> float:
    """Honor Retry-After if present, else exponential backoff with jitter."""
    ra = resp.headers.get("Retry-After")
    if ra:
        try:
            return float(ra)
        except ValueError:
            pass
    return min(2 ** attempt, 16) + random.uniform(0, 0.75)


_RETRY_STATUS = {429, 500, 502, 503, 504}


def _path_of(url: str) -> str:
    try:
        after_host = url.split("//", 1)[1].split("/", 1)[1]
        return "/" + after_host.split("?", 1)[0]
    except IndexError:
        return "/"


def _record_usage(host: str, path: str, status: int, retries: int) -> None:
    """Append one usage line. Never let telemetry break a research call."""
    if not USAGE_ON:
        return
    try:
        rec = {
            "ts": time.time(),
            "date": time.strftime("%Y-%m-%d"),
            "host": host,
            "path": path,
            "status": status,
            "retries": retries,
        }
        with open(USAGE_LOG, "a") as f:
            f.write(json.dumps(rec) + "\n")
    except Exception:
        pass


async def _get(url: str, headers: dict | None = None, params: dict | None = None) -> Any:
    c = await client()
    host = _host_of(url)
    if "coingecko.com" in host:
        cgh = _cg_headers()
        if cgh:
            headers = {**(headers or {}), **cgh}
    retries = 0
    for attempt in range(5):
        await _throttle(host)
        r = await c.get(url, headers=headers, params=params)
        if r.status_code in _RETRY_STATUS and attempt < 4:
            retries += 1
            if r.status_code == 429:
                _widen_interval(host)      # slow down for good, not just for this retry
            await asyncio.sleep(_retry_delay(r, attempt))
            continue
        _record_usage(host, _path_of(url), r.status_code, retries)
        # EXHAUSTED-RETRY MESSAGE (2026-08-29). raise_for_status() surfaced a raw httpx
        # traceback -- "Client error '429 Too Many Requests' for url ..." -- straight to the
        # buyer, which reads as broken software rather than as a rate limit. It is an honest
        # failure and it should say what it is, and what actually fixes it.
        if r.status_code == 429:
            keyed = "coingecko.com" in host and bool(CG_KEYS)
            raise RuntimeError(
                f"Rate limited by {host} after {retries} retries. This is throttling, not a broken "
                f"install. The engine already slowed itself to {_HOST_BACKOFF.get(host, 0):.0f}s "
                f"between calls and this request is still bigger than the free tier allows. "
                + ("Wait about a minute and ask again, or narrow the request to fewer coins."
                   if keyed else
                   "Wait about a minute and ask again, narrow the request to fewer coins, or "
                   "add a FREE CoinGecko Demo key (coingecko.com/en/api) to roughly quadruple "
                   "the allowance -- see TROUBLESHOOT.md. Nothing is wrong with the engine.")
            )
        r.raise_for_status()
        return r.json()


async def _post(url: str, headers: dict | None = None, json_body: dict | None = None) -> Any:
    c = await client()
    host = _host_of(url)
    retries = 0
    for attempt in range(5):
        await _throttle(host)
        r = await c.post(url, headers=headers, json=json_body)
        if r.status_code in _RETRY_STATUS and attempt < 4:
            retries += 1
            await asyncio.sleep(_retry_delay(r, attempt))
            continue
        _record_usage(host, _path_of(url), r.status_code, retries)
        r.raise_for_status()
        return r.json()


def _to_float(v) -> float | None:
    if v is None:
        return None
    try:
        return float(v)
    except (TypeError, ValueError):
        return None


# ============================================================
# CoinGecko
# ============================================================

@mcp.tool()
async def search_coin(query: str) -> dict:
    """
    CoinGecko: resolve a ticker or name to coin IDs.
    Returns top 5 matches with id, symbol, name, market_cap_rank.
    Use this BEFORE get_coin() to find the right CG slug.
    """
    data = await _get(f"{CG_BASE}/search", params={"query": query})
    coins = data.get("coins", [])[:5]
    return {
        "matches": [
            {
                "id": c["id"],
                "symbol": c["symbol"],
                "name": c["name"],
                "market_cap_rank": c.get("market_cap_rank"),
            }
            for c in coins
        ]
    }


@mcp.tool()
async def get_coin(coin_id: str) -> dict:
    """
    CoinGecko: full coin data — market data, links, categories, top exchanges, contracts.
    coin_id is the CG slug (e.g. 'sogni-ai', 'jupiter-exchange-solana', 'render-token').
    """
    data = await _get(
        f"{CG_BASE}/coins/{coin_id}",
        params={
            "localization": "false",
            "tickers": "true",
            "community_data": "false",
            "developer_data": "false",
            "sparkline": "false",
        },
    )
    md = data.get("market_data", {}) or {}
    tickers = data.get("tickers", []) or []
    return {
        "id": data.get("id"),
        "symbol": data.get("symbol"),
        "name": data.get("name"),
        "categories": data.get("categories"),
        "platforms": data.get("platforms"),
        "links": {
            "homepage": (data.get("links", {}) or {}).get("homepage"),
            "twitter": (data.get("links", {}) or {}).get("twitter_screen_name"),
            "telegram": (data.get("links", {}) or {}).get("telegram_channel_identifier"),
            "whitepaper": (data.get("links", {}) or {}).get("whitepaper"),
        },
        "market_data": {
            "current_price_usd": _to_float((md.get("current_price") or {}).get("usd")),
            "market_cap_usd": _to_float((md.get("market_cap") or {}).get("usd")),
            "market_cap_rank": md.get("market_cap_rank"),
            "fdv_usd": _to_float((md.get("fully_diluted_valuation") or {}).get("usd")),
            "total_volume_24h_usd": _to_float((md.get("total_volume") or {}).get("usd")),
            "circulating_supply": md.get("circulating_supply"),
            "total_supply": md.get("total_supply"),
            "max_supply": md.get("max_supply"),
            "ath_usd": _to_float((md.get("ath") or {}).get("usd")),
            "ath_date": (md.get("ath_date") or {}).get("usd"),
            "ath_change_pct": _to_float((md.get("ath_change_percentage") or {}).get("usd")),
            "price_change_24h_pct": _to_float(md.get("price_change_percentage_24h")),
            "price_change_7d_pct": _to_float(md.get("price_change_percentage_7d")),
            "price_change_30d_pct": _to_float(md.get("price_change_percentage_30d")),
            "price_change_1y_pct": _to_float(md.get("price_change_percentage_1y")),
        },
        "top_exchanges": [
            {
                "exchange": (t.get("market") or {}).get("name"),
                "pair": f"{(t.get('base') or '')}/{(t.get('target') or '')}",
                "volume_24h_usd": _to_float(t.get("converted_volume", {}).get("usd")),
            }
            for t in tickers[:10]
        ],
    }


@mcp.tool()
async def coin_markets_by_category(category: str, per_page: int = 50, sort: str = "market_cap_desc") -> dict:
    """
    CoinGecko: list top coins in a category, sorted by market cap or other.
    Example categories: 'base-ecosystem', 'ton-ecosystem', 'real-world-assets-rwa',
    'decentralized-finance-defi', 'depin', 'ai-agents'.
    """
    data = await _get(
        f"{CG_BASE}/coins/markets",
        params={
            "vs_currency": "usd",
            "category": category,
            "order": sort,
            "per_page": min(per_page, 250),
            "page": 1,
            "sparkline": "false",
            "price_change_percentage": "1h,24h,7d,30d",
        },
    )
    return {
        "category": category,
        "count": len(data),
        "coins": [
            {
                "id": c.get("id"),
                "symbol": (c.get("symbol") or "").upper(),
                "name": c.get("name"),
                "mcap": _to_float(c.get("market_cap")),
                "price": _to_float(c.get("current_price")),
                "volume_24h": _to_float(c.get("total_volume")),
                "change_24h_pct": _to_float(c.get("price_change_percentage_24h_in_currency")),
                "change_7d_pct": _to_float(c.get("price_change_percentage_7d_in_currency")),
                "change_30d_pct": _to_float(c.get("price_change_percentage_30d_in_currency")),
            }
            for c in data
        ],
    }


@mcp.tool()
async def cg_global() -> dict:
    """CoinGecko: total crypto market cap, BTC dominance, DeFi share. Macro context."""
    data = await _get(f"{CG_BASE}/global")
    d = data.get("data") or {}
    return {
        "active_cryptocurrencies": d.get("active_cryptocurrencies"),
        "markets": d.get("markets"),
        "total_market_cap_usd": _to_float((d.get("total_market_cap") or {}).get("usd")),
        "total_volume_24h_usd": _to_float((d.get("total_volume") or {}).get("usd")),
        "btc_dominance_pct": _to_float((d.get("market_cap_percentage") or {}).get("btc")),
        "eth_dominance_pct": _to_float((d.get("market_cap_percentage") or {}).get("eth")),
        "market_cap_change_24h_pct": _to_float(d.get("market_cap_change_percentage_24h_usd")),
    }


# ============================================================
# GeckoTerminal — DEX pools, screening
# ============================================================

@mcp.tool()
async def network_list() -> dict:
    """List GeckoTerminal chain IDs commonly used."""
    return {"networks": KNOWN_NETWORKS}


def _format_pool(pool: dict, network: str) -> dict:
    a = pool.get("attributes", {}) or {}
    rel = pool.get("relationships", {}) or {}
    base = ((rel.get("base_token") or {}).get("data") or {}).get("id", "")
    quote = ((rel.get("quote_token") or {}).get("data") or {}).get("id", "")
    dex = ((rel.get("dex") or {}).get("data") or {}).get("id", "")
    return {
        "address": a.get("address"),
        "name": a.get("name"),
        "dex": dex,
        "base_token": base,
        "quote_token": quote,
        "reserve_usd": _to_float(a.get("reserve_in_usd")),
        "volume_24h_usd": _to_float((a.get("volume_usd") or {}).get("h24")),
        "price_change_24h_pct": _to_float((a.get("price_change_percentage") or {}).get("h24")),
        "price_change_1h_pct": _to_float((a.get("price_change_percentage") or {}).get("h1")),
        "transactions_24h": (a.get("transactions") or {}).get("h24"),
        "base_token_price_usd": _to_float(a.get("base_token_price_usd")),
        "pool_created_at": a.get("pool_created_at"),
        "url": f"https://www.geckoterminal.com/{network}/pools/{a.get('address')}",
    }


@mcp.tool()
async def get_pools_for_token(network: str, token_address: str) -> dict:
    """
    GeckoTerminal: all DEX pools for a token, sorted by liquidity.
    network: 'base', 'eth', 'solana', 'bsc', 'arbitrum', 'ton', etc.
    """
    data = await _get(
        f"{GT_BASE}/networks/{network}/tokens/{token_address}/pools",
        headers=GT_HEADERS,
        params={"page": 1},
    )
    return {"pools": [_format_pool(p, network) for p in data.get("data", [])]}


@mcp.tool()
async def trending_pools(network: str = "base", duration: str = "24h") -> dict:
    """
    GeckoTerminal: trending pools on a chain.
    duration: '5m', '1h', '6h', '24h'.
    """
    data = await _get(
        f"{GT_BASE}/networks/{network}/trending_pools",
        headers=GT_HEADERS,
        params={"page": 1, "duration": duration},
    )
    return {
        "network": network,
        "duration": duration,
        "pools": [_format_pool(p, network) for p in data.get("data", [])],
    }


@mcp.tool()
async def new_pools(network: str = "base") -> dict:
    """GeckoTerminal: brand-new pools on a chain. Catches launches BEFORE they trend."""
    data = await _get(
        f"{GT_BASE}/networks/{network}/new_pools",
        headers=GT_HEADERS,
        params={"page": 1},
    )
    return {
        "network": network,
        "pools": [_format_pool(p, network) for p in data.get("data", [])],
    }


@mcp.tool()
async def screen_pools(
    network: str = "base",
    min_liquidity_usd: float = 0,
    max_liquidity_usd: float = 1_000_000_000,
    min_volume_24h_usd: float = 0,
    min_price_change_24h_pct: float = -100,
    max_price_change_24h_pct: float = 10000,
    sort: str = "h24_price_change_percentage_desc",
    pages: int = 10,
) -> dict:
    """
    GeckoTerminal: filter DEX pools by criteria. Bulk-screening workhorse.
    sort: 'h24_price_change_percentage_desc' (default), 'h24_volume_usd_desc',
          'h24_tx_count_desc', 'pool_created_at_desc'.

    Note: GeckoTerminal only sorts server-side by volume / tx_count / creation. For any
    other sort (e.g. price change) we fetch by volume across many pages, UNION the
    trending + new-pool feeds (so fresh gainers are not missed), then filter and sort
    client-side. This is why a '+300% in 24h' screen actually works.
    """
    # GeckoTerminal's free tier hard-caps pagination at page 10 (20 pools/page = 200 max
    # per network); page 11+ returns 401 (needs the paid Analyst plan). So we use the full
    # free depth by default and clamp here. Trending + new pools (below) extend coverage.
    pages = min(max(1, pages), 10)
    # Sorts GeckoTerminal accepts server-side. Anything else -> fetch by volume, sort here.
    GT_SERVER_SORTS = {"h24_volume_usd_desc", "h24_tx_count_desc", "pool_created_at_desc"}
    fetch_sort = sort if sort in GT_SERVER_SORTS else "h24_volume_usd_desc"

    raw: list = []
    for page in range(1, max(1, pages) + 1):
        try:
            data = await _get(
                f"{GT_BASE}/networks/{network}/pools",
                headers=GT_HEADERS,
                params={"page": page, "sort": fetch_sort},
            )
        except httpx.HTTPStatusError:
            break
        items = data.get("data", []) or []
        if not items:
            break
        raw.extend(items)

    # Union trending + new pools so fresh, fast movers that aren't top-by-volume are caught.
    for ep in ("trending_pools", "new_pools"):
        try:
            d = await _get(f"{GT_BASE}/networks/{network}/{ep}", headers=GT_HEADERS)
            raw.extend(d.get("data", []) or [])
        except httpx.HTTPStatusError:
            pass

    _STABLES = {"USDT", "USDC", "DAI", "EURC", "FRAX", "LUSD", "USDE", "USDS",
                "TUSD", "USDB", "PYUSD", "GUSD", "FDUSD", "USD0", "SUSD", "CRVUSD"}
    seen: set = set()
    matches = []
    for p in raw:
        pid = p.get("id") or (p.get("attributes", {}) or {}).get("address")
        if pid in seen:
            continue
        seen.add(pid)
        attrs = p.get("attributes", {}) or {}
        # Drop stable/stable pairs: their price-change is a decimal-math artifact
        # (e.g. USDT/USDC reporting +1085%), which pollutes momentum screens.
        sides = [s.strip().upper() for s in (attrs.get("name") or "").split("/")]
        if len(sides) == 2 and sides[0] in _STABLES and sides[1] in _STABLES:
            continue
        try:
            tvl = float(attrs.get("reserve_in_usd") or 0)
            vol_24h = float((attrs.get("volume_usd") or {}).get("h24") or 0)
            price_change_24h = float((attrs.get("price_change_percentage") or {}).get("h24") or 0)
        except (TypeError, ValueError):
            continue
        if not (min_liquidity_usd <= tvl <= max_liquidity_usd):
            continue
        if vol_24h < min_volume_24h_usd:
            continue
        if not (min_price_change_24h_pct <= price_change_24h <= max_price_change_24h_pct):
            continue
        m = _format_pool(p, network)
        m["_pc24"], m["_vol24"] = price_change_24h, vol_24h
        matches.append(m)

    if sort == "h24_volume_usd_desc":
        matches.sort(key=lambda x: x.get("_vol24", 0), reverse=True)
    elif sort != "pool_created_at_desc":  # default + price-change sorts -> by 24h price change
        matches.sort(key=lambda x: x.get("_pc24", 0), reverse=True)
    for m in matches:
        m.pop("_pc24", None)
        m.pop("_vol24", None)

    return {
        "network": network,
        "criteria": {
            "liquidity_range_usd": [min_liquidity_usd, max_liquidity_usd],
            "min_volume_24h_usd": min_volume_24h_usd,
            "price_change_24h_range_pct": [min_price_change_24h_pct, max_price_change_24h_pct],
            "sort": sort,
            "pages_scanned": pages,
            "sources": "pools(paged) + trending_pools + new_pools, deduped",
            "pools_examined": len(seen),
        },
        "match_count": len(matches),
        "pools": matches,
    }


@mcp.tool()
async def pool_ohlcv(network: str, pool_address: str, timeframe: str = "day", limit: int = 30) -> dict:
    """
    GeckoTerminal: OHLCV candles. Computes intra-window pump %.
    timeframe: 'day', 'hour', 'minute'.
    """
    data = await _get(
        f"{GT_BASE}/networks/{network}/pools/{pool_address}/ohlcv/{timeframe}",
        headers=GT_HEADERS,
        params={"aggregate": 1, "limit": min(limit, 1000), "currency": "usd"},
    )
    attrs = (data.get("data") or {}).get("attributes") or {}
    candles = attrs.get("ohlcv_list") or []
    if not candles:
        return {"network": network, "pool": pool_address, "candles": []}
    highs = [c[2] for c in candles if c[2] is not None]
    lows = [c[3] for c in candles if c[3] is not None]
    pump_pct = ((max(highs) - min(lows)) / min(lows) * 100) if (highs and lows and min(lows) > 0) else None
    return {
        "network": network,
        "pool": pool_address,
        "timeframe": timeframe,
        "candle_count": len(candles),
        "first_open_usd": candles[-1][1] if candles else None,
        "last_close_usd": candles[0][4] if candles else None,
        "max_high_usd": max(highs) if highs else None,
        "min_low_usd": min(lows) if lows else None,
        "intra_window_pump_pct": pump_pct,
        "candles": candles[:limit],
    }


# ============================================================
# DexScreener
# ============================================================

@mcp.tool()
async def dexscreener_token(token_address: str, chain_filter: str = "") -> dict:
    """
    DexScreener: all pairs for a token across all DEXes/chains.
    chain_filter: optionally restrict to one chain ('base', 'ethereum', 'solana', 'bsc', 'ton', etc.).
    """
    data = await _get(f"{DS_BASE}/latest/dex/tokens/{token_address}")
    pairs = data.get("pairs") or []
    if chain_filter:
        pairs = [p for p in pairs if p.get("chainId", "").lower() == chain_filter.lower()]
    return {
        "chain_filter": chain_filter or "all",
        "pair_count": len(pairs),
        "pairs": [
            {
                "chain": p.get("chainId"),
                "dex": p.get("dexId"),
                "pair_address": p.get("pairAddress"),
                "base_symbol": (p.get("baseToken") or {}).get("symbol"),
                "quote_symbol": (p.get("quoteToken") or {}).get("symbol"),
                "price_usd": _to_float(p.get("priceUsd")),
                "price_change_24h_pct": _to_float((p.get("priceChange") or {}).get("h24")),
                "liquidity_usd": _to_float((p.get("liquidity") or {}).get("usd")),
                "volume_24h_usd": _to_float((p.get("volume") or {}).get("h24")),
                "fdv": _to_float(p.get("fdv")),
                "mcap": _to_float(p.get("marketCap")),
                "url": p.get("url"),
            }
            for p in pairs[:15]
        ],
    }


@mcp.tool()
async def dexscreener_search(query: str) -> dict:
    """DexScreener: search across all pairs by token name, symbol, or address."""
    data = await _get(f"{DS_BASE}/latest/dex/search", params={"q": query})
    pairs = (data.get("pairs") or [])[:15]
    return {
        "query": query,
        "pair_count": len(pairs),
        "pairs": [
            {
                "chain": p.get("chainId"),
                "dex": p.get("dexId"),
                "base_symbol": (p.get("baseToken") or {}).get("symbol"),
                "base_name": (p.get("baseToken") or {}).get("name"),
                "base_address": (p.get("baseToken") or {}).get("address"),
                "price_usd": _to_float(p.get("priceUsd")),
                "liquidity_usd": _to_float((p.get("liquidity") or {}).get("usd")),
                "volume_24h_usd": _to_float((p.get("volume") or {}).get("h24")),
                "fdv": _to_float(p.get("fdv")),
                "url": p.get("url"),
            }
            for p in pairs
        ],
    }


@mcp.tool()
async def dexscreener_trending_boosted() -> dict:
    """DexScreener: tokens with active 'boosts' — proxy for trending attention."""
    try:
        data = await _get(f"{DS_BASE}/token-boosts/top/v1")
        items = data if isinstance(data, list) else []
        return {
            "count": len(items),
            "boosted": [
                {
                    "chain": it.get("chainId"),
                    "address": it.get("tokenAddress"),
                    "amount": it.get("amount"),
                    "total_amount": it.get("totalAmount"),
                    "url": it.get("url"),
                }
                for it in items[:25]
            ],
        }
    except Exception as e:
        return {"error": str(e)}


# ============================================================
# CoinMarketCap (requires CMC_API_KEY env var)
# ============================================================

@mcp.tool()
async def cmc_status() -> dict:
    """Check if CoinMarketCap API key is configured."""
    if not CMC_KEY:
        return {
            "configured": False,
            "message": "CMC_API_KEY env var not set. Sign up at https://coinmarketcap.com/api/ (free tier = 10,000 calls/month, 30/min).",
        }
    return {"configured": True, "key_prefix": CMC_KEY[:6] + "..."}


@mcp.tool()
async def cmc_quote(symbol: str) -> dict:
    """CMC: latest quote (price, mcap, volume, supply) for a symbol. Requires CMC_API_KEY."""
    if not CMC_KEY:
        return {"error": "CMC_API_KEY not set. Run cmc_status() for instructions."}
    data = await _get(
        f"{CMC_BASE}/cryptocurrency/quotes/latest",
        headers=CMC_HEADERS,
        params={"symbol": symbol.upper(), "convert": "USD"},
    )
    return data


@mcp.tool()
async def cmc_listings(limit: int = 100, sort: str = "market_cap") -> dict:
    """CMC: top N coins. sort: 'market_cap', 'volume_24h', 'percent_change_24h'. Requires CMC_API_KEY."""
    if not CMC_KEY:
        return {"error": "CMC_API_KEY not set. Run cmc_status() for instructions."}
    data = await _get(
        f"{CMC_BASE}/cryptocurrency/listings/latest",
        headers=CMC_HEADERS,
        params={"limit": min(limit, 5000), "sort": sort, "convert": "USD"},
    )
    return data


# ============================================================
# EVM chain RPC (Ethereum + Base)
# ============================================================

async def _evm_call(chain: str, method: str, params: list) -> Any:
    rpc = EVM_RPCS.get(chain.lower())
    if not rpc:
        raise ValueError(f"Unknown EVM chain: {chain}. Use one of: {list(EVM_RPCS.keys())}")
    j = await _post(rpc, json_body={"jsonrpc": "2.0", "method": method, "params": params, "id": 1})
    if "error" in j:
        raise RuntimeError(j["error"])
    return j["result"]


@mcp.tool()
async def evm_block_number(chain: str = "base") -> dict:
    """EVM RPC: latest block number. chain: 'ethereum' or 'base'."""
    hex_block = await _evm_call(chain, "eth_blockNumber", [])
    return {"chain": chain, "block_number": int(hex_block, 16)}


@mcp.tool()
async def evm_get_balance(chain: str, address: str) -> dict:
    """EVM RPC: native ETH balance for an address. chain: 'ethereum' or 'base'."""
    hex_balance = await _evm_call(chain, "eth_getBalance", [address, "latest"])
    wei = int(hex_balance, 16)
    return {"chain": chain, "address": address, "balance_wei": str(wei), "balance_eth": wei / 1e18}


def _decode_string(hex_data: str) -> str | None:
    try:
        if not hex_data or hex_data == "0x":
            return None
        data = bytes.fromhex(hex_data[2:])
        if len(data) >= 96:
            length = int.from_bytes(data[32:64], "big")
            return data[64:64 + length].decode("utf-8", errors="replace")
        return data.rstrip(b"\x00").decode("utf-8", errors="replace")
    except Exception:
        return None


def _decode_uint(hex_data: str) -> int | None:
    try:
        if not hex_data or hex_data == "0x":
            return None
        return int(hex_data, 16)
    except Exception:
        return None


@mcp.tool()
async def erc20_token_info(chain: str, token_address: str) -> dict:
    """
    EVM RPC: read ERC-20 metadata (name, symbol, decimals, totalSupply) from chain.
    chain: 'ethereum' or 'base'. Returns ground-truth on-chain values.
    """
    selectors = {
        "name": "0x06fdde03",
        "symbol": "0x95d89b41",
        "decimals": "0x313ce567",
        "total_supply": "0x18160ddd",
    }

    async def _call(sel: str):
        return await _evm_call(chain, "eth_call", [{"to": token_address, "data": sel}, "latest"])

    results = await asyncio.gather(
        *[_call(sel) for sel in selectors.values()],
        return_exceptions=True,
    )
    name_raw, symbol_raw, decimals_raw, supply_raw = results

    name = _decode_string(name_raw) if not isinstance(name_raw, Exception) else None
    symbol = _decode_string(symbol_raw) if not isinstance(symbol_raw, Exception) else None
    decimals = _decode_uint(decimals_raw) if not isinstance(decimals_raw, Exception) else None
    supply_raw_int = _decode_uint(supply_raw) if not isinstance(supply_raw, Exception) else None

    return {
        "chain": chain,
        "address": token_address,
        "name": name,
        "symbol": symbol,
        "decimals": decimals,
        "total_supply_raw": str(supply_raw_int) if supply_raw_int is not None else None,
        "total_supply": (supply_raw_int / (10 ** decimals)) if (decimals and supply_raw_int) else None,
    }


@mcp.tool()
async def erc20_balance_of(chain: str, token_address: str, holder_address: str) -> dict:
    """EVM RPC: an address's balance of a specific ERC-20 token."""
    holder_clean = holder_address.lower().replace("0x", "")
    padded = holder_clean.rjust(64, "0")
    data = f"0x70a08231{padded}"
    hex_bal = await _evm_call(chain, "eth_call", [{"to": token_address, "data": data}, "latest"])
    raw = _decode_uint(hex_bal) or 0
    decimals_raw = await _evm_call(chain, "eth_call", [{"to": token_address, "data": "0x313ce567"}, "latest"])
    decimals = _decode_uint(decimals_raw) or 18
    return {
        "chain": chain,
        "token": token_address,
        "holder": holder_address,
        "balance_raw": str(raw),
        "balance": raw / (10 ** decimals),
        "decimals": decimals,
    }


# ============================================================
# TON (TON Center)
# ============================================================

@mcp.tool()
async def ton_account(address: str) -> dict:
    """TON: account info (balance, status, code/data hashes) for a TON address."""
    data = await _get(f"{TON_BASE}/account", params={"address": address})
    return data


@mcp.tool()
async def ton_jetton_master(jetton_master_address: str) -> dict:
    """TON: jetton metadata (TON's ERC-20 equivalent): total supply, mintable, admin."""
    data = await _get(f"{TON_BASE}/jetton/masters", params={"address": jetton_master_address})
    return data


@mcp.tool()
async def ton_jetton_wallets(owner_address: str, limit: int = 20) -> dict:
    """TON: list jetton wallets owned by a TON address (what tokens the address holds)."""
    data = await _get(
        f"{TON_BASE}/jetton/wallets",
        params={"owner_address": owner_address, "limit": min(limit, 100)},
    )
    return data


# ============================================================
# DefiLlama — live protocol revenue, TVL, fees data
# ============================================================

@mcp.tool()
async def defillama_protocols(limit: int = 50, category_filter: str = "") -> dict:
    """
    DefiLlama: top protocols ranked by TVL. THE source for live protocol-level TVL.
    category_filter: optionally filter by category. DefiLlama's real values include
                     'Dexs' (note the spelling, NOT 'Dexes' - it is the biggest category
                     at ~2000 protocols), 'Yield', 'Lending', 'Derivatives',
                     'Liquid Staking', 'Launchpad', 'CDP', 'Bridge'. Common misspellings
                     are auto-corrected, and an unmatched filter returns the list of
                     valid categories instead of silently returning nothing.
    Returns name, slug, chain(s), TVL, mcap, change_1d, change_7d, change_1m, category.
    """
    data = await _get(f"{DL_BASE}/protocols")
    items = data if isinstance(data, list) else []
    # SILENT-ZERO GUARD (2026-08-29). The docstring used to say 'Dexes'; DefiLlama's actual
    # value is 'Dexs'. The docstring is what an assistant reads to pick arguments, so the
    # single largest category (~2000 protocols) returned an empty list and the assistant
    # confidently reported "no DEX protocols found". A filter matching nothing must SAY so.
    filter_note = None
    if category_filter:
        live = sorted({(p.get("category") or "") for p in items if p.get("category")})
        want = category_filter.strip().lower()
        ALIAS = {"dexes": "dexs", "dex": "dexs"}
        want = ALIAS.get(want, want)
        match = next((c for c in live if c.lower() == want), None)
        if match is None:
            near = [c for c in live if c.lower().startswith(want[:4])]
            match = near[0] if len(near) == 1 else None
        if match is None:
            return {"category_filter": category_filter, "count": 0, "protocols": [],
                    "error": f"no DefiLlama category matches {category_filter!r}. That is a bad "
                             f"filter value, NOT an absence of protocols. Valid values below.",
                    "valid_categories": live}
        if match.lower() != category_filter.strip().lower():
            filter_note = f"interpreted {category_filter!r} as {match!r}"
        items = [p for p in items if (p.get("category") or "") == match]
    items = items[:min(limit, 500)]
    return {
        "category_filter": category_filter or "all",
        **({"note": filter_note} if filter_note else {}),
        "count": len(items),
        "protocols": [
            {
                "name": p.get("name"),
                "slug": p.get("slug"),
                "category": p.get("category"),
                "chains": p.get("chains"),
                "tvl_usd": _to_float(p.get("tvl")),
                "mcap_usd": _to_float(p.get("mcap")),
                "change_1d_pct": _to_float(p.get("change_1d")),
                "change_7d_pct": _to_float(p.get("change_7d")),
                "change_1m_pct": _to_float(p.get("change_1m")),
                "url": p.get("url"),
            }
            for p in items
        ],
    }


@mcp.tool()
async def defillama_protocol(slug: str) -> dict:
    """
    DefiLlama: detailed data for a specific protocol by slug.
    slug examples: 'aave', 'jupiter-aggregator', 'collector-crypt', 'raydium', 'hyperliquid'.
    Returns TVL by chain, current TVL, mcap, category, audits, and full protocol metadata.
    """
    data = await _get(f"{DL_BASE}/protocol/{slug}")
    chain_tvls = data.get("chainTvls", {}) or {}
    current_tvl_by_chain = {
        chain: (chain_tvls.get(chain, {}) or {}).get("tvl", [{}])[-1].get("totalLiquidityUSD")
        if isinstance((chain_tvls.get(chain, {}) or {}).get("tvl"), list) and (chain_tvls.get(chain, {}) or {}).get("tvl")
        else None
        for chain in list(chain_tvls.keys())[:15]
    }
    return {
        "name": data.get("name"),
        "slug": data.get("slug") or slug,
        "category": data.get("category"),
        "description": (data.get("description") or "")[:500],
        "url": data.get("url"),
        "twitter": data.get("twitter"),
        "audits": data.get("audits"),
        "audit_links": data.get("audit_links"),
        "chains": data.get("chains"),
        "current_tvl_total_usd": _to_float(data.get("currentChainTvls", {}).get("total") if data.get("currentChainTvls") else None),
        "current_tvl_by_chain": data.get("currentChainTvls"),
        "mcap_usd": _to_float(data.get("mcap")),
        "fdv_usd": _to_float(data.get("fdv")),
        "github": data.get("github"),
        "tokens": data.get("tokens"),
    }


@mcp.tool()
async def defillama_chains() -> dict:
    """
    DefiLlama: TVL ranked by chain. Macro view of where DeFi capital sits.
    Useful for "which chains are growing/shrinking" reads.
    """
    data = await _get(f"{DL_BASE}/v2/chains")
    items = data if isinstance(data, list) else []
    items = sorted(items, key=lambda x: x.get("tvl") or 0, reverse=True)[:50]
    return {
        "count": len(items),
        "chains": [
            {
                "name": c.get("name"),
                "chain_id": c.get("chainId"),
                "tvl_usd": _to_float(c.get("tvl")),
                "token_symbol": c.get("tokenSymbol"),
                "gecko_id": c.get("gecko_id"),
                "cmc_id": c.get("cmcId"),
            }
            for c in items
        ],
    }


@mcp.tool()
async def defillama_fees(protocol_slug: str) -> dict:
    """
    DefiLlama: live fee + revenue data for a protocol.
    Returns 24h fees, 7d fees, 30d fees, daily revenue, plus the breakdown.
    The DEFINITIVE source for "how much does this protocol actually earn?"
    """
    data = await _get(f"{DL_BASE}/summary/fees/{protocol_slug}")
    return {
        "name": data.get("name"),
        "category": data.get("category"),
        "fees_24h_usd": _to_float(data.get("total24h")),
        "fees_7d_usd": _to_float(data.get("total7d")),
        "fees_30d_usd": _to_float(data.get("total30d")),
        "fees_1y_usd": _to_float(data.get("total1y")),
        "fees_all_time_usd": _to_float(data.get("totalAllTime")),
        "revenue_24h_usd": _to_float(data.get("dailyRevenue")),
        "revenue_7d_usd": _to_float(data.get("total7dRevenue")) if data.get("total7dRevenue") else None,
        "average_24h_fees_usd": _to_float(data.get("average1y")),
        "url": data.get("url"),
        "twitter": data.get("twitter"),
        "chains": data.get("chains"),
    }


@mcp.tool()
async def defillama_dex_volume(protocol_slug: str) -> dict:
    """
    DefiLlama: live DEX volume for a protocol.
    For DEXes / aggregators / perps venues. Returns 24h, 7d, 30d volume.
    """
    data = await _get(f"{DL_BASE}/summary/dexs/{protocol_slug}")
    return {
        "name": data.get("name"),
        "category": data.get("category"),
        "volume_24h_usd": _to_float(data.get("total24h")),
        "volume_7d_usd": _to_float(data.get("total7d")),
        "volume_30d_usd": _to_float(data.get("total30d")),
        "volume_1y_usd": _to_float(data.get("total1y")),
        "volume_all_time_usd": _to_float(data.get("totalAllTime")),
        "url": data.get("url"),
        "twitter": data.get("twitter"),
        "chains": data.get("chains"),
    }


# ============================================================
# Entrypoint
# ============================================================

if __name__ == "__main__":
    mcp.run()
