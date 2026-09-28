# Worked examples: coins that were passed on, and why

**This file does not filter anything.** It is a set of worked examples from the author's own
research: candidates that surfaced, got looked at, and were rejected. Read it the way you would
read the golden reports, as a demonstration of the standard being applied.

**It is deliberately NOT wired into discovery.** Your research must not skip a coin because it
appears here. Somebody else's pass, on a different date, at a different price, with a different
thesis, is not evidence about your trade. Several of these were passed for reasons that were
true then and may not be true now ("ugly chart", "team went quiet"), and at least one may well
be a good buy today.

What to take from it: the SHAPE of a rejection. Notice how often the kill reason is something
cheap to check early (dead volume behind big liquidity, a team that cannot be verified, a
narrative with no product), and how rarely it is something that needed deep work. That is the
lesson. The specific tickers are incidental.

---



**Purpose:** a running list so we never waste time re-researching or re-suggesting coins the author already passed on, that we checked and didn't add, or that I suggested and he ignored. This complements `SEEN-COINS.csv` (which is the Daily-100 discovery dedup ledger). 

**Maintenance rule (do this every session):** BEFORE any discovery run or before researching a coin, READ THIS FILE. Do not re-suggest or re-add anything in sections 1-5. After every session, APPEND new rejections/passes here with the date and reason. Section 6 (pre-TGE) is parked, not killed — those CAN be revisited when a token launches.

Started 2026-06-19.

---

## 1. Explicitly rejected / skipped by the author (do NOT re-add, do NOT re-suggest)

| Ticker | Name | Reason the author passed |
|---|---|---|
| SPEC | Spectral | Dead chart; team keeps posting about a different project ("The Grid") = treat as abandoned. |
| (n/a) | Almanak | Dead chart. |
| OM | MANTRA | "Switched their coins"; the author doesn't want it; also the 2025 price collapse. |
| ALEO | Aleo | Chart dumped/ugly; explicit "do not add ALEO, that's terrible." |
| TIA | Celestia | "Ugly chart, don't even check." (also a modular/rollup-adjacent infra name) |
| LBC | LBRY / Library Credits | No usable price chart; skipped. |
| (n/a) | "Kronos" | Not a separate coin — the author meant Cronos (CRO), which is ALREADY in Silver. Dedupe, not a new add. |

## 2. Checked / researched but NOT added (failed the dead-project rule or weak)

| Ticker | Name | Reason |
|---|---|---|
| FLT | Fluence | Founders all still in C-suite and shipping (pivoted to GPU/AI compute, sunset their rollup), BUT token fails the dead rule: ~$1.5M mcap, ~$88K/day vol, -99.8% from ATH. Team alive, token dead. Not added. |
| BMX | Boardwalk (Morphex) | ~$1.7M cap, ~$10K/day vol, anonymous team. Recommended Bronze/watch at best; not added. |
| MOE | Merchant Moe | LFJ / Trader-Joe-built DEX on Mantle, Mantle EcoFund-backed, but token ~$600/day vol = basically dead. Watch/pass; not added. |

## 3. DeFi-lane candidates the author passed (dead/weak charts) — keep out unless the thesis changes

the author reviewed a DeFi discovery lane and kept only **Kamino (KMNO)** and **Maple (SYRUP)**; he passed the rest for dead-looking charts:

| Ticker | Name | Note |
|---|---|---|
| DRIFT | Drift | Passed (dead-looking; also post-exploit recovery). |
| RESOLV | Resolv | Passed (~95% off ATH). |
| GEAR | Gearbox | Passed (micro-cap). |
| TERM | Term Finance | Passed (value capture unconfirmed). |
| SPECTRA | Spectra (ex-APWine) | DEAD by the rule (~$1.3M cap, ~$2.7K/day vol, once ~$0.25). This is the example the author used to define the dead-chart rule. |
| FLUID | Fluid (Instadapp) | Suggested (real revenue->buyback), but NOT added. |

## 4. Rollups / infra the author passed ("rollups are dead unless something crazy")

| Ticker | Name | Note |
|---|---|---|
| INIT | Initia | Passed (rollup framework; Terra lineage). |
| FUEL | Fuel | Passed (modular execution layer, micro-cap). |
| MOVE | Movement | DROPPED — founder fired over a market-maker / token-dump scandal. Do not add. |
| ES | Eclipse | DROPPED — founder exited, TVL collapsed ~95%. |

(Exceptions the author DID accept despite the rollups-dead rule: Aztec = privacy + Zac Williamson/PLONK; Monad and MegaETH = high-performance L1 / real-time L2 with Jump/Stanford/MIT founders + huge raises. Those are in Silver.)

## 5. Suggested in discovery but NOT actioned (he ignored / didn't pick) — don't re-suggest unless something changes

| Ticker | Name | Note |
|---|---|---|
| USUAL | Usual Money | Non-finance founder (ex-French MP Pierre Person); not picked. |
| ROAM | Roam | Founder goes by initials (fails the named-team bar); weak; not picked. |
| WXM | WeatherXM | Not picked. |
| DIMO | DIMO | Not picked. |
| BIGTIME | Big Time | Not picked. |
| OLAS | Olas / Autonolas | More established agent infra; not picked. |
| XPL | Plasma | the author thought it was already in the DB. It is NOT in any DB. He did not add it. If he ever wants it, it is a fresh add (ex-Goldman founder Paul Faecks, Founders Fund + Tether). |
| (skip) | Felix / Ethereal / Contango | Scout could not confirm a live token and/or named team at the time; skip unless re-verified. |

**Already in our DBs (dedupe pointers, NOT rejections) — these resurfaced in scouting:** RSR Reserve (Silver), POLYX Polymesh (Bronze), CRO Cronos (Silver), LA Lagrange (Silver).

## 6. PRE-TGE / NO LIVE TOKEN — parked, NOT rejected (revisit when a token launches)

These have strong named teams / tier-1 backing but no live tradeable token yet. Do not waste time on them now; re-evaluate at TGE.

- **AI / agents:** Hyperbolic (Variant + Polychain), Nous Research (Paradigm $50M at $1B), Prime Intellect (Founders Fund, Karpathy), Gradient Network (Pantera + Multicoin), Pluralis (USV + CoinFund), Nevermined (Ocean co-founder), Skyfire (ex-Ripple; a16z CSX + Coinbase Ventures), Payman (Visa, Coinbase Ventures, Circle).
- **Payments / stablecoins (equity-only or stablecoin-only, no governance token):** Bridge (Stripe-acquired), Agora/AUSD (Paradigm), Mesh, Coinflow, KAST, Codex, M0, Perena (ex-Solana stablecoin lead), Mansa, Fin, Bastion, Better Money.
- **RWA (fund-token / equity only, no liquid token):** Superstate (Robert Leshner), Dinari, Midas, Tradable, Backed Finance (xStocks, Kraken-acquired), Securitize.
- **DeFi / DePIN / infra (points or pre-TGE):** Ostium (RWA perps, General Catalyst), Seismic (a16z privacy), Daylight Energy (a16z + Framework $75M), PrismaX (a16z robotics data), BitRobot.

---

## How to use this file
- Discovery scouts: exclude sections 1-5 (and the `SEEN-COINS.csv` tickers) from results.
- Researching a single coin: if it's in sections 1-5, say so plainly it was already passed and why, instead of re-researching.
- Section 6: fair game to revisit, but only once they have a live, tradeable token.
- Append new entries here at the end of every session.

---

## 7. Killed in verification, 2026-07-27 top-50 "exciting right now" screen (do NOT re-suggest)

All 15 surfaced high on a mechanical 4-lens screen and were killed by the verification swarm. They were surfaced by a mechanical screen and then killed one by one on verification, which is the point of this file: a screen finds candidates, it does not find winners.

| Ticker | Name | Reason killed (2026-07-27) |
|---|---|---|
| RAVE | RaveDAO | ZachXBT documented a coordinated pump-and-dump 2026-04-18/20: three Gnosis Safes held ~90% of supply, ~$42M deposited to Bitget pre-pump and ~$32M withdrawn during the spike, -97% in 24h, ~$43M of liquidations. Permanent no. |
| VELVET | Velvet Capital | On-chain analysts flagged ~22M tokens moved to exchanges by team-linked wallets in June 2026 and distributed into FOMO buying, not addressed by the project. Down 78% in 30d. FDV far above sub-$1M protocol TVL. |
| SERV | OpenServ | GoPlus flags that the contract creator can disable sells, change fees, mint and transfer tokens. Owner-privileged contract. Recent pump rested on an unverified AI benchmark claim against an already-superseded model. |
| AEON | AEON | Wash-trading signature: ~$34K total DEX liquidity across all 6 BSC pairs against $109.9M reported 24h volume on a $15.9M cap. Hit ATH and was already 55% off it same day. |
| ESIM | Depinsim | DWF Labs named backer, team disclosed by first names only, 13.5% float against a $47M FDV, $14.4K pool liquidity vs $553K reported volume. |
| ESP | Espresso | Shared-sequencer / rollup confirmation layer = the excluded category, and nothing unusual vs other shared sequencers. No max supply cap. 17% float. |
| EPIC | Epic Chain | Own materials call it an EVM L2 sidechain (fails the rollup rule); June 2026 pivot is to travel/loyalty commerce, so its CoinGecko RWA tag is stale. Homepage 403s. |
| SUPERGEMMA | Supergemma4-26b | Name-borrows Google's Gemma with no live product, only a pseudonymous builder handle, top 10 wallets reportedly ~88% of supply. |
| BANK | Lorenzo Protocol | 24h volume ~40x main-pool liquidity, token-manipulation allegations surfaced days before its ATH followed by a sharp reversal, anonymous team. |
| AA | ARAI Token | Reported cap was FDV overstated 6.9x (real ~$3.9M), anonymous team, 86% off a Sept 2025 ATH despite a large recent pump. |
| UB | Unibase | 75% of a 10B supply locked, real FDV $1.31B, no token-level fee capture in its own docs, anonymous team. |
| CAS | Caspius | Own site and whitepaper 403, not on CoinGecko, anonymous, contract is a Virtuals AgentTokenV4 with tax, blacklist and owner controls intact. |
| WALLET | Robinhood Wallet | Zero website and zero socials across all 11 pairs; takes the literal name of Robinhood's real wallet app with no affiliation. Robinhood has stated it never launched a memecoin. |
| PEA | MinePea | 577 holders after 6 days, volume ~7x liquidity, anonymous, zero third-party coverage, "mining" mechanic unverified. |
| WEN | Wen Lambo | Claims to be "backed by Peter Saddington" only on its own site, with no statement from him anywhere. Unverified celebrity-backing claim. |
| APES | Apes Together Strong | Advertises an hourly $GME airdrop funded by trading fees with no proof it pays out. 4 days old, 383 holders. |
| DICKBUTT | Dickbutt | 92% off its 90-day high with no catalyst found = fails the AUTO-NO dead-chart rule. Bot-deployed via Clanker, meme creator publicly disavowed commercial use. |

**Parked, not killed (re-check if the flag clears):** KITSU (two competing official-looking websites, copycat risk unresolved), TYGR (unproven "original team" claim on Roaring Kitty's likeness), ANSEMCAT (self-disclaims affiliation), CLANKER (a prior named dev resigned May 2025 tied to a ~$350K Velodrome theft; the buyback mechanic itself is real), THE AUTHOR (Pollak called the creator-coin strategy "definitively wrong" 2026-07-15).

---

## 8. Killed 2026-07-29 — the Chinese-name BSC co-pump cluster (coordinated launch-and-rug farm)

Forensics: shared factory `0x839d0bd232c7b5ad87f6a352f16786f34241fd9b` (unverified, 528 contracts CREATEd) minted 4 of these via selector `0xedf8f2df`, wired the launch BNB into each throwaway deployer EOA itself, and every deployer swept proceeds to ONE collector EOA `0x8F3A9F465812b613684accF6137c25c178023FeA`. Identical 12,843-byte bytecode, identical 1,000,000,000,000 supply at 9 decimals, identical 6-transaction lifecycle. Verified on BSC RPC + BscScan.

| Ticker | Name | Reason killed (2026-07-29) |
|---|---|---|
| 长鑫科技 | 长鑫科技 (0x7cdb63f5...a8fd400f) | Takes the exact official listed name of CXMT ("Changxin Technology Group"), deployed Jul-27-2026 08:26 UTC = the day CXMT's $8.6B Shanghai STAR IPO popped +466%. Zero affiliation ($WALLET precedent). Also an EIP-1967 upgradeable proxy (impl `0xbfd8ab93...`) whose "Renounce Ownership" was theater: storage slot 0 still holds deployer `0x5f6fe3c9`. Obfuscated setter "Setmarotnj". 357,643 holders in 2 days = fabricated. |
| 长鑫科技 | 长鑫科技 (0x6d3518c9...05bdfab1) | Second contract, same impersonated CXMT name, launched a day later off the shared farm factory. Mid-cycle at time of review: LP added 35 hrs prior, deployer still holding 3.31 BNB. Its three factory siblings all had LP pulled ~2 days after adding it. |
| 玛卡巴卡 | 晚安 玛卡巴卡 (Goodnight Makka Pakka) | Farm factory token. ALREADY RUGGED: LP pulled and 4.32 BNB swept to the collector 61 days ago. Pool now holds 2.5829 tokens / 0.000000 WBNB. Codex reported $707,510 volume and $156,247 liquidity that do not exist. Also unlicensed use of a BBC "In the Night Garden" character. |
| 长征十号 | 中国火箭 (China Rocket / Long March 10) | Farm factory token. Impersonates China's state crewed-lunar rocket program (CASC). ALREADY RUGGED: LP pulled, 4.1195 BNB swept to the collector 16 days ago. Pool holds 2.4700 tokens / 0.000000 WBNB vs $204,681 of claimed volume. |
| ANSEM | The Black Bull (0xc6b3bfaf...631b37b, BSC) | Cross-chain TICKER-SQUAT of the real Solana $ANSEM/The Black Bull. Farm factory token, ALREADY RUGGED: LP pulled, 3.2495 BNB swept to the collector 20 days ago. Pool holds 2.3979 tokens / 0.000000 WBNB. NOT the token in the Luke Belmar hunt. DANGER: the Codex row glued CoinGecko id "the-black-bull" and the real token's $74,927,898 cap onto this dead BSC contract. |

**⚠️⚠️ MINT CORRECTION 2026-07-29 (this row originally named the WRONG Solana mint — verified and fixed same day):**
The real Solana **$ANSEM / The Black Bull is `9cRCn9rGT8V2imeM2BaKs13yhMEais3ruM3rPvTGpump`** — confirmed two independent ways: CoinGecko's `the-black-bull` record returns `platforms: {"solana":"9cRCn9rGT8V2imeM2BaKs13yhMEais3ruM3rPvTGpump"}`, and DexScreener shows that mint with **30 pairs, $4,426,891 summed liquidity, $9,478,248 24h volume, $175.6M cap, pool created 2026-06-16**, baseToken name "The Black Bull", symbol "ANSEM".
The mint previously written here, `ECqPq3aWiH6popDLETJLj6mydri5aVxQgxhQe21Mpump`, is a **DIFFERENT and essentially dead token**: baseToken name "blknoiz06", symbol "Ansem", **1 pair, $4,540 liquidity, $209 of 24h volume, $3,490 market cap**, created 2025-11-26. It is not the Luke Belmar hunt target.
**Why this mattered:** the author has an active position interest in the real $ANSEM, so acting on the original row would have bought a $3,490 token instead of a $175M one. **Lesson: when a doctrine row names a "real" contract to contrast against a decoy, the REAL address needs the same verification rigor as the decoy. A wrong good-address is more dangerous than a missing one, because it reads as vetted.** Note the two caps differ by source (CoinGecko circulating $74.9M vs DexScreener $175.6M, which uses total supply); both confirm a large real token, and the circulating figure is the honest one for sizing.
| 喵喵币 | 喵喵币 (Meow Meow Coin) / MMToken | Only cluster member with a real book ($2.08M liq, real USDT pair, not farm-launched), but killed on exit-ability: verified source exposes `setSlippageFees()` with `MAX_SLIPPAGE_FEE` = 5000 bps (50%) plus `setProfitTax()` that taxes selling at a profit, owner NOT renounced, and the deployer was calling Set Slippage Fee / Set Tiers on the live contract during review. Observed buys 4,917 vs sells 170 (28.9:1). Owner can set a 50% sell fee before you exit. |
| JOMO | Joy of Missing Out | Not farm-launched, but nothing to underwrite: 0.3 days old, 245 holders, no socials, anonymous. Fails the named-team bar. |
| TNOS | TNOS / Transnational Oil Supply | Same-ticker swarm: FOUR separate Solana pump.fun mints in under 12 hours, printed +75,412% to +178,629%. At most one is "real" and there is no way to tell which. Kill the ticker for sweep purposes. |

**Pipeline bug found, not a coin (fix before next sweep):** the sweep glues ONE CoinGecko record onto every same-ticker contract. BSC ANSEM inherited the real Solana token's $74.9M cap, and all five PIPEDOG rows across three chains carry the identical `cg_id: pipedog` and `mcap_circulating: 51,352,852`. This makes copycats read as the real asset. Market cap must be bound to the contract address, never the ticker.

**Reusable primitive added:** the Base `0xadf` case taught "shared deployer prefix = manufactured." This case extends it: **a shared FACTORY contract plus a shared proceeds-collection wallet is the same tell and is stronger evidence.** Trace both directions on any co-pumping cohort: back to who funded the deployer, and forward to where the BNB was swept.

## 9. Killed 2026-07-29 — 24h-momentum tail triage (do NOT re-suggest)

All four launch artifacts below fail on a HARD filter independently of their headline percentage. Their
four-figure 24h gains are measured off a near-zero launch price and are meaningless as momentum.

| Ticker | Name | Reason killed (2026-07-29) |
|---|---|---|
| SHITCOIN | shitcoin (Robinhood Chain, `0x49e34dBB35023D51F981558F54e5523FA9C44b03`) | Pure meme, no product, 0.9d old. Made its ATH in HOUR ONE and is 24.6% off it; sells beat buys 6,244 to 5,429; hourly volume fading $184K to $87K. Top 10 hold 63.9%. Six same-ticker copycats launched the same day. Only ~$1,900 sellable for a 3% move. |
| TROY | OpenTroy (Robinhood Chain, `0x35082b06d25c9fDB76284997Ed6F11ac44465b07`) | Contract IS official (verified via opentroy.org's own DexScreener pool link) but **bot-deployed via Clanker** (the flag that killed DICKBUTT 2026-07-27). Top 10 hold 82.3%; 1,668 buys against 3,289 sells in its first five hours. Already 40.2% off a five-hour-old high, hourly volume collapsed $216K to $19K. Three Base vanity copycats with null liquidity against $58-70K reported volume. |
| FRANK | Frank Ocean (Base, `0xD17ea9248FAC06071f3acd0572d2550CCf12a90F`) | **Cross-chain COPYCAT.** Origin is the Solana TikTok meme (`3aqXuwp6...pump`, 124,467 trades, 7,082 holders); the Base pool was created HOURS after that pumped, with no X and no website. 12,075 holders with top 10 at 0.0% on 234 lifetime trades = manufactured airdrop distribution. Origin token already -35% in 6h. |
| LOOP | Loop (Solana, `BvWXEh15zjKJQjBw9Q7mXBmdFx5oYdqwqmzF6g888888`) | Top 10 hold **93.47%**. Zero social identity on DexScreener AND GeckoTerminal. Surrounded by a five-mint fake-liquidity farm on Fluxbeam, each showing ~$919K liquidity against $6,574 volume and exactly 300 buys / 0 sells (the RAXOL decoy signature). Printed a 112x inside hour one; ALL $1.166M of daily volume was that hour; now 59.4% off it on $12K/hr. $14.06M FDV on nothing. |
| RWA | Real World Acquisitions (Base, `0x9784354d43c258082E7011e8c75512Ae1d3543ea`) | **NOT the author's Bronze entry — ticker collision only.** Bronze holds ($RWA) RWA Inc = `0xE2B1dc2D4A3b4E59FDF0c47B71A7A86391a8B35a`, rwa.inc, 364-day-old pool, CEO Kevin Yunai, and it was FLAT today (-2.7%). Today's mover has 104 holders, no X, no website; the `@RealWorldAcq` handle belongs to a THIRD same-name contract on Ethereum which is -53.5%/24h. $437K volume on 568 trades ($771 avg) among 104 wallets on a monotonic grind. |

**PARKED, not killed — PUMPCADE** (Solana, `Eg2ymQ2aQqjMcibnmTt8erC6Tvk9PVpJZCxvVPJz2agu`). The only tail name clearing
the named-team filter: founder **Harrison Leggio** (@PopPunkOnChain, co-founder g8keep, co-founder/CTO Gaslite),
**$1M pre-seed led by Pump.fun**, 4,370 holders, top 10 only 26.7%, best exit of the tail (~$13.4K for a 3% move).
Held back on MOMENTUM only: +41.6%/24h sits inside -23%/30d at 62% off ATH, which is a bounce not a pumped-and-held
chart. Two honest flags: the product is press-verified not first-party page-verified (cade.market is a "something is
coming" placeholder, pumpca.de has a TLS cert mismatch), and his prior project g8keep was delisted by CertiK after its
founder threatened legal action. Re-check on a 30-day trend flip or a mainnet launch.

**⚠️ NEW DETECTION SIGNATURE — currently passes every filter we run.** Base RWA and Base FRANK share a fingerprint
that is the INVERSE of the wash-farm profile we screen for: **sub-600 lifetime trades at a $700+ average ticket, no
socials, a near-monotonic price grind on flat hourly volume, sitting 1-3% off high, deployed on Base the same day,
both reusing a ticker/name that had just pumped on ANOTHER chain.** We screen for suspiciously HIGH turnover; this is
suspiciously LOW trade count at a suspiciously HIGH ticket size, which reads as a controlled mark-up rather than
retail discovery. Candidate research code.

**⚠️ POSSIBLE NOTION DUPLICATE (check, per the POD precedent):** the Bronze search surfaced THREE `($RWA) RWA Inc`
pages — `26582822-b7b7-813a…`, `2e182822-b7b7-81f4…` (titled "(1)"), and `25182822-b7b7-803c…`. Not opened, so not
confirmed as true duplicates rather than distinct tiers.
