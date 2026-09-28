# Error / Lesson Log

Running record of mistakes, unexpected behaviors, and gotchas. Add new entries with date and what was learned.

The goal: capture every error so the workflow gets sharper with each iteration. Future chats read this to avoid known traps.

---

## 2026-08-05 (Gensyn $AI — our own 2026-06-19 correction over-corrected: the "paused" FACT was right, only the "pivot" CONCLUSION was wrong)

### When you refute a subagent's story, refute the conclusion, not the underlying facts along with it
- **What happened:** On 2026-06-19 a subagent wrote Gensyn as "RL Swarm and testnet nodes paused; the project pivoted to Delphi." the author checked gensyn.ai, saw no pivot language, and the whole claim was struck from the entry as unsupported. Seven weeks later Gensyn's OWN docs read: page title **"RL Swarm (Paused)"**, body **"There are no official swarms running right now"**, and on the testnet overview **"RL Swarm & all Gensyn-hosted nodes have been paused"** plus BlockAssist and CodeAssist **"have been sunset as focus consolidates around Delphi."** The pause was true the whole time. Only the word "pivot" was wrong, because the verification engineering did not stop dead (REE, AXL and the research publishing continue). **⚠️ CORRECTED LATER THE SAME DAY, and the correction is the lesson repeating itself: "never stopped" was too strong and I should not have written it from the docs alone. The commit record says the TRAINING stack DID stop. `rl-swarm` (1,681 stars, their most popular repo) last commit 2026-01-05, `genrl` 2025-11-06, `rl-swarm-contracts` 2025-09-29. Of 45 commits across the 12 main repos in the last 90 days, 30 were Delphi, REE got 5, AXL got 3, and there is no public Verde repo at all. Verde is a paper, not shipped code.** Caveat that cuts the other way: commit messages read "Copybara import of the project", so Gensyn develops in a **private monorepo** and public activity understates the real total.
- **The cost:** for seven weeks the Silver entry read as if the compute network were live and earning, when in fact **Delphi was the only live application, the only fee source, and there was no paid compute market and no live staking** (confirmed 2026-08-05 by Gensyn's own docs assistant, which could find no compute-marketplace page and no staking contract).
- **Lesson:** a wrong FRAME does not make the underlying facts wrong. When rejecting a subagent's narrative, separate the two: strike the interpretation, then go verify each fact it rested on independently. The 2026-06-19 rule still stands (never write pivoted / abandoned / scope-narrowed unless the project's own site says so), and it now has a second half: **when the project's own site LATER does say so, go back and correct the entry, and say which half of the old claim was right.** Also: the marketing homepage and the docs can disagree. gensyn.ai still leads with "the network for machine intelligence" while docs.gensyn.ai reports the training products paused and sunset. **Read the docs, not the hero section.**
- **Reusable, and it is the more valuable half of this pass:** the way to grade a buy-and-burn is to read the vault, never the announcement. Gensyn's BuyBack Vault `0x2CBEE00F91A2BC50a7D5C53DFfa6BAB79d7E0243` on its own rollup showed **$2,897.75 of lifetime revenue** and a **75,483 token burn = 0.00075% of supply**, and the 70/29/1 split reconciled to the token in the treasury, proving the mechanism genuinely executes. Same day, an independent session measured $ZAMA the same way. **Mechanism quality and mechanism magnitude are two separate judgements and both belong in the entry.**

---

## 2026-07-17 (Karma Wallet $KARMA — labeled the team "no named team" while the founder's X account was in plain sight)

### Missed a public founder because the team check only looked at STATIC surfaces, never the X social graph
- **What happened:** The KARMA Bronze entry shipped with "No named team... Treat as pseudonymous until someone is doxxed." the author then pasted https://x.com/amrix_j — bio literally "23 y/o founder @karmawallet", Dubai, a trykarma.app/r/amrix referral link, posting under his own face, and a quote-tweet of the v2 launch pinned within an hour of launch. He had even posted "am i the only doxxed founder in robinhood eco rn?" hours before the entry was written. The founder was one bio away the whole time.
- **Root cause:** the T3 anonymous-team check only swept STATIC, name-indexed surfaces: project site, docs, Virtuals agent page (showed "Team ?"), LinkedIn company pages, Crunchbase, generic web searches. A founder who goes by a first-name pseudonym with no LinkedIn and no name on the site is invisible to every one of those. The founder lives in the X SOCIAL GRAPH: quote tweets of the launch post, ecosystem accounts greeting him ("welcome to virtuals, ser @amrix_j"), the project account's reposts of his takes, and his own bio. I read the project's timeline and the launch thread replies but never opened the quote tweets, never checked who the project account reposts, and never ran a People-tab search for the project handle.
- **Compounding trap dodged:** a web search for "amrix Karma wallet founder real name" returned the OTHER Karma Wallet (karmawallet.io, NC sustainability fintech, founders Jayant Khadilkar / Kedar Karkare) and the search engine's AI summary confidently glued @amrix_j to those names. That is the same-name trap (see Tal Cohen, 2026-06-26). Did not write it.
- **Lesson / the mandatory X-graph sweep (run BEFORE labeling any team anonymous):**
  1. Open the QUOTE TWEETS of the launch/pinned post and scan for "we/our/I built" language.
  2. Check who the project account REPOSTS and replies to repeatedly (its Replies tab); founders retweet themselves constantly.
  3. Run an X People-tab search for the project handle/name — "founder @handle" bios surface there instantly.
  4. Scan ecosystem "welcome/congrats" posts around launch day; they routinely tag the founder by handle.
  5. For Virtuals launches: open the VIDEO_PITCH tweet from the agent's socials record; founders are often on camera.
  Only after all five come up empty does "anonymous" go in the entry. "Not on LinkedIn" ≠ anonymous.
- **Scope check on the same day:** the sweep matters even when it confirms the label — Amrix's own "only doxxed founder in robinhood eco" line is supporting evidence that the VEX / WOOD / INDEX anonymous labels were right as of Jul 17. Fix applied to the KARMA Bronze entry (founder section rewritten, comms line corrected).

## 2026-07-15 (TIG Gold deep dive — got the whole competitive ANGLE wrong)

### Evaluated an IP-licensing business as if it were a product fighting free tools; defaulted to reflexive skepticism instead of getting the model right first
- **What happened:** On the TIG (The Innovation Game) deep dive + Gold entry, I repeatedly framed the project through the wrong model. I asked "why would a firm pay TIG when OR-Tools is free," judged that "big logistics build in-house so they will not license," and treated "the routing benchmark is not independently verified" as if it argued against the result. All three are the wrong frame, and the author had to correct me three separate times. **The correct model: TIG is an IP-licensing business for algorithms (the Arm / Dolby archetype).** It produces a best-in-class algorithm through a permanent global competition, and any firm that wants to use it privately must buy a cheap commercial license, because the free/open license deliberately forces public disclosure of your input data and is therefore unusable for a real business. The buyer's real choice is "license the better algorithm and make money, or fall behind rivals who do," NOT "pay vs use free." An integrator wires it into the enterprise (that function is built into the Commercial License, MathWorks-style), so my "nobody buys a bare algorithm" objection was a strawman.
- **Root-cause chain (how the wrong angle formed) — this is the reusable part:**
  1. **Judged demand before defining the business.** Jumped straight to "would they pay" without first stating what TIG IS and who its natural buyer is. Never internalized the dual-license poison pill even though it was already in the author's handed-over notes.
  2. **Under-weighted the operator's secondary source.** the author's notes already contained the poison-pill, the integrator path, and the Arm pedigree. I treated my own swarm as primary and effectively discarded his mechanism. His notes were the hypothesis to steelman, not a footnote.
  3. **Adversarial-frame capture.** I wrote the skeptic prompts as null hypotheses ("would they license a bare external algorithm -> false") and took the skeptics' "false" as the conclusion. The skeptics refuted a strawman (a raw algorithm replacing UPS's core in-house router), not the real model (cheap private license + integrator).
  4. **Reflexive skepticism masquerading as rigor.** I equated "bearish and hedged" with "honest." Real rigor is getting the model right first, then applying skepticism to correctly-framed claims. Reflexive negativity is just a different bias.
  5. **Absence of evidence treated as evidence of absence.** On Vidal / the SOTA claim I scored "not peer-reviewed / not re-run" as a negative, ignoring the reputational prior (a world authority staking his name on open, reproducible code = high probability real).
  6. **Layered-domain pattern-matching.** Each layer got mapped to its nearest cynical template (crypto token -> inflation-is-bad; algorithm -> commoditized-by-free-OR-Tools; enterprise -> builds-in-house) instead of being integrated into the actual model.
  7. **Metric conflation.** Read "0.086-0.14% gap-to-optimal" as if it meant "0.09% better than a competitor."
- **Guardrails to run every time (what to look for so this does not repeat):**
  - **Define-before-judge:** before evaluating demand or value, write ONE sentence: "This is a [business archetype] that makes money by [mechanism]; the buyer's real alternative today is [X], and switching gains/costs are [Y]." If you cannot write it, you are not ready to judge it. Research the model first.
  - **Name the analog business** (Arm/Dolby IP-licensing? SaaS? marketplace? toll road? royalty?). The archetype dictates the entire valuation lens. TIG = Arm-for-algorithms, not a solver competing on price.
  - **Steelman before you refute.** Run the strongest-version-of-the-thesis pass first (or in parallel), and phrase adversarial/skeptic prompts against the operator's ACTUAL model so the refutation cannot kill a strawman.
  - **Operator's thesis + notes = primary input.** When the author gives an angle and notes, that is the hypothesis to test and strengthen, not to override with a generic swarm.
  - **"A free alternative exists" is NOT a refutation of a licensing model.** Ask whether the free/open path is actually usable for THIS buyer (here the data-disclosure poison pill makes "free" unusable for a private firm).
  - **Absence of verification is not evidence against.** Use reputational/structural priors, label it "unverified," never score it as a negative.
  - **Separate the three questions and do not let one collapse the others:** (a) is it real/good [use priors], (b) will the market pay [structure], (c) does the token capture the value [mechanics]. A weakness in (c) is not a weakness in (a).
  - **Reflexive-skeptic bias is its own failure mode.** Uniform bearishness on a project with a credentialed team + a real product, or leaning on "unverified / free exists / they build in-house" as the load-bearing objections, is the tell that the model has been mis-framed. Stop and recheck the model.
  - **Check metric definitions before reasoning on the numbers.**
- **Process fix:** Corrected the TIG Gold entry (vehicle-routing section, demand + integrator section, exclusivity honesty flag) to the right frame. Added two new patterns (#9, #10) to "Patterns of error to watch for." Meta-lesson, even for a layered/hard subject: define the business model and steelman the operator's angle BEFORE applying skepticism.

## 2026-07-12 (13-coin batch: DOT, LienFi, VEX, Capacitr, Surplus, briefs)

### the author's dictated coin names are homophones — resolve spelling against the live token before creating anything
- **What happened:** Two of the author's spoken names resolved to different spellings: "LeanFi (LFI)" is actually **LienFi** (tokenized US property tax liens on Base, lienfi.com), and "Capacitor" is actually **Capacitr** (no second O, capacitr.xyz on Base). Both stub entries were created with the dictated spelling and corrected during enrichment.
- **Lesson:** For any coin the author names by voice, treat the name as phonetic. Resolve the real spelling via DexScreener/CoinGecko + the project's own site BEFORE finalizing titles, and confirm the corrected spelling back to him in the report. Same session also reconfirmed the ticker-collision rule: "DOT" here is Dot/usedot.xyz privacy AI on Base, not Polkadot.
- **Also observed:** fake-liquidity clone contracts existed for 5 of the 13 coins checked (VEX, FACY, MOLT, CAPACITR, SURPLUS all have lookalike contracts with spoofed LP on other chains or same chain). Always match the contract via the project's own site/X pinned post, and treat huge-liquidity/zero-volume pairs as fakes.

## 2026-06-26 (SOGNI refresh)

### Gave up on sourcing team stats after one search pass; nearly dropped real numbers the author had researched
- **What happened:** Refreshing the SOGNI Silver entry, I couldn't source Pathbrite's "$12M raised" and Tal Cohen's Stratasys "$123M" / Markets.com "$3T" on the first search and told the author I was dropping them. the author pushed back ("you're just whisking off my research"). A second, harder pass confirmed **Pathbrite raised $12M** (Inc. magazine, Heather Hiles) and that the **Markets.com role genuinely belongs to our advisor** (his career: ibetcha→McKinsey→Google→Markets.com founding team→Sirin→Stratasys→Kraken).
- **Lesson:** When the author says he researched a figure, run the SECOND-LEVEL searches (alternate phrasings, the primary-source outlet, the person's own profile) before declaring it unsourceable. One generic query returning nothing ≠ "no source exists." Don't discard his research on a single miss.
- **Two-different-people trap (got this part right):** There are at least two prominent finance "Tal Cohen"s — (a) OUR advisor (talcohenprofile / PRIM3: Sirin Labs, Stratasys CMO, Kraken US MD, Markets.com founding team) and (b) the **President of Nasdaq** (tal-cohen-85a2911: Arthur Andersen→Amex→Instinet→Chi-X CEO→Nasdaq, CPA/NYU Stern). Always disambiguate same-name execs against the SPECIFIC LinkedIn/Crunchbase profile before attributing a credential.
- **Self-reported vs independently-verified:** Stratasys $123M, Markets.com $3T/4.5M traders, and the SRN ~$350M peak cap are self-reported (LinkedIn) or the author-recalled and labeled as such ("per his LinkedIn", "~"). The hard independently-cited anchors are Sirin's $72M private raise (CNBC) + ~$158M SRN ICO and $3.80 ATH (CoinMarketCap). Keep the attribution honest rather than dropping the number entirely.

### Lending-protocol entry missed a short report on its largest borrower (USD.AI $CHIP)
- **What happened:** The existing $CHIP (USD.AI) Gold entry (written 2026-06-18) named QumulusAI's $500M facility as the headline proof point but never mentioned that USD.AI's *single largest* borrower, Sharon AI (Nasdaq: SHAZ), had been hit by an April 30, 2026 Bleecker Street Research short report alleging a "phantom" $1.25B anchor contract (ESDS, which earned only ~$39.9M FY2025 rev), CEO self-dealing, a walked-back NVIDIA "strategic shareholder" claim, and that USD.AI had only ~$284M available capacity vs $1.2B approved. The report predated the entry by 7 weeks and goes straight to the core thesis (are these GPU loans real and repayable?).
- **Lesson:** For any **lending / RWA / credit protocol**, the thesis lives or dies on borrower quality. Always run a targeted search on the named borrowers/counterparties for short reports, defaults, lawsuits, or accounting controversy before writing the entry. A protocol can look great on its own stats while its biggest loan is to a publicly-questioned shell. Frame such findings honestly as allegations (note the short-seller is talking their book) but never omit them.
- **Also refreshed:** $CHIP was at all-time lows (~$0.028, ATL $0.02777 on 6/25), down ~80% from the 4/23 ATH; corrected the stale "$13B borrower pipeline" to current first-party stats ($385M TVL, $236M active pipeline, $1.2B+ approved, 75,503 users, 80+ partnerships, ~7.5% APR); added Sharon AI + Quantum Solutions as borrowers 2 and 3.

## 2026-06-19

### Subagent overstated a "pivot/decline" narrative (Gensyn $AI)
- **What happened:** A research subagent wrote the Gensyn entry as "the original peer-to-peer training network (RL Swarm) and testnet nodes are paused; the project pivoted to Delphi, an AI-settled prediction market, narrower than the original decentralized-AI-training pitch." the author checked gensyn.ai and pushed back: the site still describes it as the network for machine intelligence / decentralized machine learning, and he saw no "Delphi" framing.
- **Reality (verified):** Gensyn = "the network for machine intelligence," a decentralized verifiable-AI-compute network (Ethereum L2), mainnet live Apr 22 2026. **Delphi is the FIRST application built on the network** (an AI-settled information/prediction market) and the current source of the protocol fees that feed the $AI buy-and-burn (~70% of fees burned, ~29% to a community treasury). It is NOT a pivot away from compute. Ticker is **$AI** (AIGENSYN on Binance), not GENSYN.
- **Lesson:** Never write a "pivoted / abandoned / scope-narrowed / dead" narrative unless the project's OWN site/docs confirm it. Aggregator/news snippets ("X debuts prediction market") can make an additive app look like a replacement. Verify identity + framing against the first-party site before describing any decline, and confirm the ticker against the project/exchanges. Corrected the entry in place. Going forward: run a QA pass over every big binge.

## 2026-06-18

### Subagents backslash-escape the `$` in the Notion "Project Name" title
- **What happened:** In a ~30-coin swarm build (the author's big add-list), every subagent that called `notion-create-pages` stored the title as `(\$TICKER) Name` (literal backslash) instead of `($TICKER) Name`. The body markdown escapes `$` fine (Notion renders `\$` as `$`), but the **title is a plain-text field**, so the backslash shows literally. Existing DB entries (`($UNI) Uniswap`, `($JTO) Jito`) all use a plain `$`.
- **Lesson / fix:** After any swarm DB build, re-`update_properties` the `Project Name` with a clean plain-`$` string, OR tell agents explicitly "the title must be a plain string `($TICKER) Name`, do NOT escape the dollar sign." One agent insisted the escape "displays fine" — it does not match the rest of the DB; normalize it.

### "Main Chain" select has no N/A / own-chain option (own-L1 coins)
- **What happened:** Many requested coins are their own L1 (Monero, Litecoin, Algorand, Filecoin, Aptos, Injective, Tron, Osmosis, Flare, Plume, Kite). The Silver/Gold "Main Chain" enum has no "N/A" or generic "own chain" option, so agents correctly LEFT IT BLANK rather than mislabel. "Main DEX Liq Pool" does have an N/A option; "Main Chain" does not.
- **Lesson:** Leaving Main Chain blank for own-L1 coins is the right call until the author adds those chains (Tron, Litecoin, Monero, Algorand, Filecoin, Aptos, Injective, Cosmos, Flare, etc.) or an "N/A" option to the select. Flagged to the author 2026-06-18.

## 2026-06-15

### TAO Diamond entry had Dynamic TAO (dTAO) dated "April 2026" — actually Feb 13, 2025
- **What happened:** The existing $TAO Diamond entry stated the "Dynamic TAO upgrade" landed April 2026 (in three places: Exclusivity, Narrative Mutation, Extra). dTAO actually went live on **February 13, 2025** (confirmed: ChainCatcher, CryptoBriefing, Bitget). It predates the entry's own July 2025 input date. Also corrected the first halving to its specific date/figures: **Dec 12, 2025, 7,200 → 3,600 TAO/day.**
- **Lesson:** Bittensor milestone dates in older entries were guessed/wrong. Verify dTAO / halving / subnet-count dates against first-party + Tier-3 news before reusing them. dTAO is the economic foundation, not a "recent" upgrade.
- **Mechanism nailed down (for reuse):** Under dTAO each subnet has its own "alpha" token (21M cap each) sitting in an on-chain AMM pool **paired against TAO**. You acquire a subnet token by **staking TAO into its pool (a swap)**; emissions route to subnets pulling in the most staked TAO ("Taoflow," Nov 2025). The honest framing: there's a **direct economic connection** between TAO and every subnet (you mine or stake TAO to get any subnet token), unlike ETH/SOL gas tokens. Alpha tokens **float** against TAO (not 1:1, not redeemable) — their own independently-priced assets.
- **NOTE (2026-06-15):** Avoid the WORD "rehypothecated TAO" — the author disliked it ("I just didn't like the wording... but put whatever the truth is"). It's also not the technically-correct term (rehypothecation = a broker reusing pledged collateral). The CONCEPT is true, though, and the author wants the truth stated plainly. **The verified mechanic (Bittensor docs + Taostats + CoinGecko, 2026-06-15):** each subnet has an AMM pool with two reserves — TAO + the subnet's "alpha" token. Staking TAO = a swap: your TAO joins the pool's TAO reserve, you get alpha out. Alpha price = TAO reserve ÷ alpha reserve (constant-product AMM). Unstaking swaps alpha back to TAO with slippage (you can get back more/fewer TAO than you put in). Emissions ("Taoflow," Nov 2025) flow by net TAO staked in. So real TAO gets locked into every subnet's pool and subnet tokens are paired/priced in TAO — a genuine direct economic link ETH/SOL gas tokens don't have. **Say it that way (plain AMM-reserve language), not "rehypothecated."** Stated precisely in the TAO Diamond entry Exclusivity section; the Skool post keeps Mark's "direct economic connection" + "S&P 500 of subnets" framing minus the word.
- **Style note (2026-06-15):** the author wants the TAO Diamond Overview to **read in the plain, story-style narrative Mark Jeffrey uses** (Bitcoin's mining made programmable → mine for intelligence → 21M cap / ~11M mined / "2013 in Bitcoin terms" → 128 subnets as neighborhoods, each with its own mined token → S&P-500-of-subnets). Also: the author dislikes **em dashes** — write without them in posts (and now in TAO entry edits).

## 2026-06-11

### Conflated the SpaceX banana decal with the zero-g indicator (Banana entry)
- **What happened:** In the Banana For Scale ($BANANAS31) Bronze entry I wrote that SpaceX flew the banana as a "zero-g indicator." the author corrected: *"The meme actually goes on the side of the rocket though."* Verified: for Starship Flight 6 (Ship 31, Nov 19 2024), SpaceX painted a ~4-ft "banana for scale" pixel-art decal on the side/nosecone of the rocket — that decal is what the token is named after. (A separate plush-toy banana zero-g indicator is a different SpaceX thing; I conflated the two.)
- **Lesson:** When a token's whole identity rests on a specific real-world event, pin the EXACT form of that event before writing — don't pattern-match to a similar-but-different fact. the author knows the SpaceX/Elon narrative space cold; his corrections on these details are reliable, verify and apply them.
- **Process fix:** Corrected the Overview + Major Events lines in the Banana entry to "decal painted on the side of Ship 31."

## 2026-06-11 (earlier)

### DOGE entry stated unconfirmed X Money integration as fact
- **What happened:** An earlier session's DOGE entry (in Silver, moved to Gold this session) claimed *"X Money beta launched with DOGE positioned as a native clearing layer"* and *"DOGE as native settlement layer"* — written as confirmed fact. Web research showed the opposite: the X Money beta launched April 2026 **fiat-only with zero crypto support**, and Musk has **never publicly committed DOGE to X Money**. The "DOGE = X Money settlement layer" claim is an analyst/market forecast + community assumption, not a Musk statement.
- **Lesson:** **Catalyst-driven entries are the highest-risk place for overstatement.** When a thesis rests on a future event (a partnership, an integration, a listing), state precisely: (a) what is CONFIRMED, (b) what is ROADMAP/STATED-INTENT, (c) what is SPECULATION/FORECAST. Never collapse (c) into (a). the author's framing was a tell — he asked *"discuss IF Elon Musk has hinted in public,"* meaning he wanted the honest read on confirmation status, not a fabricated certainty.
- **Process fix:** Rewrote the DOGE Overview, "What $DOGE does," Team (Musk), Major Events, and Risk sections to draw the confirmed/roadmap/speculation lines explicitly. Added the framing "DOGE is a bet on Musk's future decision, not a confirmed catalyst." Going forward, every catalyst claim gets a confirmation-status label.

## 2026-06-01

### Discovery swarm coverage capped by GeckoTerminal rate limits + broken screen_pools
- **What happened:** Ran a 16-agent discovery swarm to pull 100 NEW standout coins (excluding the 52 from 2026-05-30). Chain-specific GeckoTerminal agents (Base, ETH/ARB, BSC/TON, Solana) repeatedly hit 429 rate limits, and `mcp__coinpicks-data__screen_pools` returned 0 matches on eth/arbitrum even with wide-open defaults (effectively broken this session). First wave returned only 1 BSC/TON coin and 6 each for Base and ETH/ARB. A second wave (after limits eased) plus the category/WebSearch agents recovered to 127 unique in-band candidates → trimmed to 100.
- **Lesson:** The $200K–$3M band is a tight binding constraint — the strongest narrative/team/partnership names (Gensyn, Kaito, Sahara, peaq, Aztec, edgeX, fan tokens) are overwhelmingly CEX-routed with sub-$200K *on-DEX* pools, so they fail the band by construction. ~30+ great-thesis coins were rejected purely on the DEX-pool floor. If the author wants those, the band needs to be a *market-cap* or *total-liquidity* filter, not a single-DEX-pool filter.
- **Process fix:** (1) Stagger GeckoTerminal calls / lean on DexScreener token+pool lookups as primary, GT as fallback. (2) Lead discovery with category + WebSearch agents (they out-produced the GT chain agents 2:1). (3) When scoring standouts, normalize `standout_categories` — agents return them as words OR numeric codes (1=narrative,2=team,3=exclusivity,4=partnership); a naive string match silently zeroes out the numeric-coded ones.

---

## 2026-05-29

### Used "gachapon" without explaining what it is (CARDS)
- **What happened:** In the CARDS entry I referenced "gachapon" repeatedly as the revenue stream without ever defining what gachapon actually is. the author: *"I don't understand the gachapon, but make sure ur entry in the database is accurate."*
- **Lesson:** The existing voice rule already says "No jargon without inline definition." **Foreign-language loanwords count as jargon** — even if they're widely used in crypto/gaming circles, a Skool member who doesn't play Japanese mobile games has never seen "gachapon." Define it the first time it appears: *"Gachapon (Japanese for capsule-toy vending machines — put money in, random toy comes out) is..."*
- **Process fix:** Updated CARDS entry to define gachapon inline + explain the mechanic step-by-step (pay USDC → algorithm pulls random cards from inventory → NFTs minted to you → keep, sell, instant-buyback, or redeem physical) + name the cash-cow stat (98% of Q1 revenue) + the structural reason it exists (only way cards leave the vault).

### Wrote "treasury-backed" without verifying the legal structure (CARDS)
- **What happened:** In the CARDS entry I wrote "$CARDS accrues value two ways: revenue-funded buybacks, plus exposure to the trading-card inventory the project owns" and "treasury backing the token." the author asked the right question: does holding the token actually give you legal ownership of the cards? Answer: NO. Collector Crypt explicitly states CARDS is **not** collateralized by the treasury in any enforceable way. The cards are company inventory; bankruptcy estate would own them, not CARDS holders.
- **the author's framing:** *"if you hold the token, you're actually getting partial ownership of a group-owned, like museum of cards kind of because they have cards in the treasury? Or how does that work? Do they actually have legal ownership of the cards in the treasury?"* — he was probing whether my "treasury-backed" language was accurate. It wasn't.
- **Lesson:** **Never write "treasury-backed" / "backed by" / "collateralized by" / "exposure to" without verifying the LEGAL structure first.** Three different things can hide behind those phrases:
  1. **Legal claim** — SPV/trust holds assets on behalf of token holders (rare). Examples: $ONDO products.
  2. **Soft economic exposure** — company owns assets on balance sheet, token captures value indirectly through buybacks/revenue (common, what CARDS actually is).
  3. **Pure marketing** — "we spent the money on X" with no structural relationship (sketchy).
  Before writing about a token's relationship to underlying assets, ask: **if the company went bankrupt tomorrow, who legally owns the assets?** If the answer is "the bankruptcy estate," then it's #2 or #3, not #1. Write accordingly.
- **Process fix:** Updated CARDS entry to spell out the indirect value-capture chain (cards → revenue → buybacks → token) and explicitly state that CARDS holders have no legal claim. Going forward, every "backed" / "exposure" claim needs the underlying legal structure named.

### Locking in scoring system the author hadn't approved
- **What happened:** the author asked for brainstorm options on alternatives to numeric scoring. I proposed action-tier (Anchor/Slingshot/Watch/Pass/Dust) + conviction-source (Team/Narrative/Beta/Catalyst/Smart-Money) as one option among many. He never said "use that one." I went ahead and wrote it into THE AUTHOR-DOCTRINE.md and PROCESS-DELTAS.md as if it were locked, then used those labels in a 9-coin briefing.
- **the author's response:** *"We didn't actually make those changes. Stop saying slingshots and stuff like that. We didn't make those changes. That was a one-time suggestion I asked for me."*
- **Lesson:** **Brainstorm options ≠ adopted policy.** When the author asks "give me options," don't treat any of them as decided. Wait for explicit "we're using X" before writing anything into the doctrine or applying to entries.
- **Process fix:** Reverted both doctrine files. Scoring system marked "OPEN, NO DECISION YET" with the full options list as reference material only.

### POD double-entry in Bronze DB
- **What happened:** Created POD in Bronze DB. A parallel chat session later created a second POD entry. Both lived for a day before I caught it.
- **Lesson:** Search the target DB by ticker **before** creating a new entry. Use `notion-query-database-view` with a filter on the ticker column or do a project-name search.
- **Process fix:** Added pre-create check to the workflow doctrine.

### Skill description too narrow
- **What happened:** The skill didn't auto-trigger on phrases like *"update X in silver DB"* or *"add Y to gold DB."* the author called me a liar for claiming the skill could do something it couldn't auto-trigger on.
- **Lesson:** Skill descriptions are the trigger — list every phrasing the author actually uses, not just the canonical ones.
- **Process fix:** Skill description rewritten to include all the DB-update phrasings.

### Goplus / top-holder bloat
- **What happened:** Skill had Goplus security scans and top-holder analysis steps the author never authorized.
- **Lesson:** Only do what's in the data-sources table. Ask before adding workflow steps.
- **Process fix:** Stripped both from the skill. Listed as "explicitly removed" in the doctrine.

---

## 2026-05-28

### POD initial entry missed the Venice virality angle
- **What happened:** Wrote POD entry that was skeptical/pedantic about "API not open, no real Venice demand." Buried the angle.
- **the author's response:** *"you took out the angle. The whole angle, bro, is that this is a play on the virality of Venice AI."*
- **Lesson:** Lead with the asymmetric thesis. Skepticism goes in the risk section, not the Overview.
- **Process fix:** Added "lead with the angle" as a hard rule in the doctrine.

### RAIN entry didn't estimate Polymarket profit
- **What happened:** Left "we don't know how much Polymarket makes" as a blank. Was being too cautious about not making numbers up.
- **the author's response:** *"you can actually say or guess how much money Polymarket makes in profit?"*
- **Lesson:** When first-party numbers don't exist, **estimate from sourced proxies and label it.** Don't be paralyzed.
- **Process fix:** Added "sourced-proxy estimation" caveat to facts discipline.

---

## 2026-05-27

### x402 paid path broken
- **What happened:** Every paid x402 call (CG Pro, CMC Pro, Heurist Mesh, Exa) returns *"Payment was authorized but rejected by server."* Wallet balance never deducts.
- **Status:** Dormant. Demoted in skill description.
- **Lesson:** Don't attempt paid path unless the author explicitly asks. Document the failure mode so future chats don't waste cycles debugging.

---

## Patterns of error to watch for

These are the categories that bite repeatedly:

1. **Doing more than asked** — adding diligence steps the author didn't authorize
2. **Locking in brainstorm options as decisions** — the author asking for options ≠ approving them
3. **Burying the angle** — leading with skepticism instead of thesis
4. **Made-up numbers** — using approximate figures without flagging
5. **Property name mismatches in Notion** — fetch the schema first
6. **Duplicates** — failing to search the target DB before creating
7. **Over-recapping** — long-winded responses when the author wants tight ones
8. **Claiming skill capability without verifying** — assuming a trigger phrase works when it doesn't
9. **Wrong competitive frame / judging before defining the business** — evaluating demand or value before stating the business archetype (Arm/Dolby? SaaS? marketplace?) and the buyer's real alternative. Define-before-judge, and treat a "free alternative" as a refutation only if it is actually usable for that specific buyer.
10. **Reflexive-skeptic bias** — treating bearish/hedged as if it were honest; scoring "not independently verified" as a negative instead of labeling it unverified and using priors. Honesty means calibrated, which can be confidently positive. Steelman the operator's angle before refuting it.
11. **Static-surface-only team checks** — declaring a team anonymous after checking only site/docs/LinkedIn/Crunchbase. Pseudonymous founders live in the X social graph (bios, quote tweets, reposts, ecosystem welcome posts, launch pitch videos). Run the X-graph sweep (see 2026-07-17) before writing "anonymous."

---

## Living document
Add new error entries with the date they occurred. Keep "Patterns of error to watch for" updated as new categories emerge.

## 2026-07-20 — Registry-only wallet lookup missed a real holding (BASTION)
The trading module's wallet verifier only queried tokens already in the verified registry, so a real ~$20 position in BASTION on Robinhood Chain was invisible, and a human caught it rather than the system. **Lesson: discovery and authorization are different jobs.** Fix shipped same day: a two-lens rule, where one lens SEES everything held and a separate lens decides what is authorised to trade: Lens 1 = full Blockscout scan of everything the wallet holds, priced in USD; Lens 2 = registry join labeling each token AUTHORIZED / NOT IN REGISTRY / KNOWN DECOY. Never build a wallet view that can only see what it already knows about. Related rule from the same session: all trading numbers are spoken to the author in USD terms first, token amounts second.

## 2026-07-20 — The Dune goose chase (requirement-first, fix-our-own-tools-first)
the author asked what massive funds use for universal token screens. I researched and pitched fund tooling (Dune $390/mo, Allium, CoinGecko Pro) across several turns before realizing his ACTUAL requirement (10x-and-held screens on Base + Robinhood Chain, nightly, member-replicatable) is fully covered by the free GeckoTerminal API already wrapped in our own MCP — the same data the F1 validation used that same morning. Compounding error: our `screen_pools` MCP tool was built for exactly this and sat broken; instead of fixing it I shopped for replacements.
**Rules:** (1) Work backward from the requirement before shopping; answer the need, not the question's framing. (2) When our own tool covers the need but is broken, FIXING IT is the default first option and must be surfaced as such. (3) When naming paid options, always state what the free/existing path covers first, with its real limits.

## 2026-07-30 (TAO Diamond refresh)

### CoinGecko serves DEAD NAMES for live Bittensor subnets + a partial-correction trap inside our own entry
- **Subnet-name trap (confirmed live):** CoinGecko's Bittensor-subnet listings can carry a subnet's ORIGINAL project name long after the slot changed hands. Verified today against taostats (the live chain explorer): SN107 = **Minos** (CG had "Tiger Alpha"), SN53 = **engy** (CG had "EfficientFrontier"). Because deregistration recycles slots, a netuid is an ADDRESS, not an identity. **Rule: never write a Bittensor subnet name without checking taostats.io/subnets/<netuid> (page title shows the live name).**
- **Partial-correction trap (our own entry):** the 2026-06-15 pass corrected the dTAO date to Feb 13, 2025 in three places but MISSED a fourth occurrence ("April 2026 Dynamic TAO upgrade" in Narrative Maturity), which then sat wrong for six weeks. When correcting a repeated fact in an entry, grep/Ctrl+F the WHOLE page for every variant of the wrong value, not just the spots you remember.
- **Also nailed down for reuse:** TAO halvings trigger at issuance milestones, not dates (first: Dec 12, 2025 at 10.5M issued, 7,200 -> 3,600 TAO/day; next at 15.75M). Circulating (~9.6M, CG) < issued (~11.2M) because recycled/burned registration TAO is subtracted; don't treat the gap as an error.


## 2026-08-02 - Dream-mined cross-session patterns <!-- dream:2026-08-02 proposal:004/005/006 (run wf_ea33d398-da4, the author-approved) -->
- **Precision Rule 3, "verified" on the wrong surface (3 sessions, Jun-Jul 2026):** a done/verified claim counts ONLY when checked on the surface the author actually sees (live storefront URL with no preview_theme_id after hard refresh, the chain or order-detail endpoint, the rendered Notion property) - never a push exit code, a local log, an in-app pane artifact, or session memory. the author's catch, verbatim: "Wrong. It's still the old thing."
- **Precision Rule 2, behavior described from memory (proposal 005 mirror):** any sentence describing how the trading system, the zip, or a coin's product BEHAVES must be verified by grepping the shipped files or primary source first. Produced 3 corrected fabrications on 2026-07-31 ("You're making stuff up... a coin does not have to pass research before the terminal will trade it") and the Nest blowup on 2026-07-05.
- **Exact-words doctrine violated AFTER the rule was saved (2026-07-30):** before delivering any rework of the author-dictated content, echo his dictated lines and diff the output against them; every dictated line survives verbatim, disagreements flagged separately. The incident postdates the exact-words rule - the memory alone is not holding; the diff checkpoint is the fix.


## 2026-08-05 (FRONG Bronze move)

### Launch-mode fact written from a secondhand read: FRONG did NOT launch through the auction
- The 08-04 Silver entry said FRONG "launched through a Continuous Clearing Auction stack rather than a standard bonding curve." Opifor's tx-linked article (2026-08-04) shows the opposite split: **FRONG went through the Gen 1 INSTANT bonding-curve engine** (tx 0xbe6b90c5...e8f35c calls the instant strategy) and it was the sister token **CHWDR, same wallet, 21 minutes later, that took the LBP/CCA auction path** (tx 0x4ec7962d...50d84). Corrected in place in the Bronze entry with the correction visible to the reader.
- **Lesson: a mechanism claim ("launched via X") is a transaction-level fact. Read the launch tx's target contract before writing the mode; do not inherit it from a thread summary.** Same family as the Precision Rule 2 dream finding (behavior described from memory).
- Also corrected while in there: "reportedly launch number 464" (an X claim we carried) replaced with the article's tx-derived "production-index number 48, 44 indexed tokens between UNIFROG and FRONG." Different denominators, only one of them sourced.
