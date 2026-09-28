# TOKEN VALUE ACCRUAL FRAMEWORK

**Status: LIVING DOCTRINE. Born 2026-07-30.** This is the TOKEN-level sibling of the Chain-Purpose
Valuation Framework. It was not written from theory: it was derived from a same-day audit of nine
live CoinPicks entries (CARDS, VVV, BNB, SOL, DOGE, TIG, REPLY, NOICE, RAIL) in which every trap
below was found in a real entry, plus a tenth worked case (CAP) run the same day. Any session
writing or refreshing a value-accrual claim in any tier DB reads this first.

Companion doctrine:
- `framework/CHAIN-PURPOSE-VALUATION-FRAMEWORK.md`
- `Hedge-Fund-DB/CHAIN-PURPOSE-VALUATION-EXAMPLES.md`

---

## WHERE THE BOUNDARY IS (chain framework vs this one)

**The chain framework answers:** what real-world segment does this chain replace, how much of that
segment's revenue can it siphon, and what does the network net after issuance. It values the
BUSINESS of a chain.

**This framework answers:** does the holder of THIS token have a claim on THIS business, and how
many dollars actually reach them. It values the CLAIM.

They compose, they do not overlap. For an L1 gas asset, run the chain framework to size the pie,
then run this one to ask whether the token is even a fork. For an app token (a DEX, a lending
protocol, a game, a collectibles market), skip the chain framework and run this one directly
against the app's own revenue. Per the 2026-07-30 correction in the chain examples file: when a
token has BOTH an income leg and a required-reserve leg, the two legs ADD, minus the overlap.
Nothing in this file changes that. This file is the discipline for the income leg.

---

## THE HEADLINE QUESTION

> **The business can be real and the token can still be a claim on nothing.**

This was the recurring finding of the 2026-07-30 audit. Collector Crypt really sells packs. Venice
really sells AI subscriptions. Binance really runs the biggest exchange on earth. Dogecoin really
has a brand. None of that, by itself, puts one dollar in a token holder's pocket.

The test, run before anything else: **if the business doubled tomorrow, name the specific mechanism
that forces one more dollar to reach a holder of this token.** If you cannot name the mechanism, the
number is zero, and the entry says so plainly. "The team would probably buy back more" is not a
mechanism. A contract address, a formula, or a standing on-chain flow is a mechanism.

---

## THE METHOD (run these seven steps on any token)

All figures in USD first, token amounts second. Trailing twelve months unless stated. The output is
ONE bottom-line number, not a range and not a blended percentage (the author's one-clear-number rule).
When an input must be estimated, pick one number from a sourced proxy and label it MY ESTIMATE.

**Step 1. Name the business and its NET revenue.**
One sentence: what does this business sell, and what does it keep after paying out what it owes
users. Gross volume is not revenue. Pack sales that are 90% instantly paid back out are not
revenue. If the project only publishes a gross number, find or estimate the net and label it.

**Step 2. Name the mechanism type** from the taxonomy below. If the honest answer is "governance"
or "points," the accrual read is over: write $0 and move to issuance.

**Step 3. Place the claim on the CLAIM STRENGTH LADDER** below. The mechanism type says HOW value
would move. The rung says WHETHER anyone can count on it.

**Step 4. Measure what was actually delivered, trailing twelve months, in USD.**
Measured means: on-chain burn/buyback totals you (or a source you can Ctrl+F) counted, or a
DefiLlama holders-revenue figure with a published methodology. Promised, projected, and "since
inception" cumulative numbers do not go in this step. Watch the one-time vs recurring split: a
single event (an unclaimed-airdrop burn, a launch-week buyback) gets stripped out or dated, never
annualized.

**Step 5. Subtract annual issuance, in USD.**
Mandatory, carried over from the chain framework. Annual issuance = new tokens entering circulation
per year (staking emissions, ecosystem/foundation distributions, vesting unlocks actually
unlocking) times current price. Use the measured trailing number where supply history exists; where
the token is young, use the published schedule for the next twelve months and label it SCHEDULED.
Net accrual, never gross. A token paying holders $30M while printing $1.7B is negative, and the
entry says negative.

**Step 6. Write the bottom line.** One sentence, one number:
"Net value accrual to [TICKER] holders: [USD amount] per year ([delivered USD] via [mechanism],
minus [issuance USD] of new supply), on the [rung name] rung."

**Step 7. Sanity-check against the market cap.** State the ratio in plain words ("the market is
paying $58M for a claim currently worth $0 per year"). No verdict language, no "overvalued," just
the arithmetic sitting next to the price. The reader makes the call.

---

## MECHANISM TAXONOMY (step 2)

| # | Mechanism | What it is | Is it accrual? |
|---|---|---|---|
| 1 | **Supply shrink (burn)** | Fees or revenue destroy tokens, verifiable at a burn address | Yes, if funded by recurring revenue, not one-time events |
| 2 | **Cash distribution** | Fee share, dividends, or buyback-and-distribute reaching holders/stakers | Yes, the cleanest form |
| 3 | **Must-hold / must-stake demand** | Using the network REQUIRES holding or staking the token (gas, base reserves, operator bonds) | Yes, but it is the reserve leg: size it as required dollars locked, not as income, and do not double count fees paid in the token |
| 4 | **Fee discount** | Holding the token makes the product cheaper | Weak: value accrues to the USER, not the holder, unless the discount forces material holding |
| 5 | **Pure governance** | Voting rights only | **Not accrual.** A vote that could someday create accrual is an option, not a flow. Write $0 today |
| 6 | **Loyalty / points** | Status, allowlists, cosmetics | **Not accrual.** Write $0 |

Honest note that goes in entries: types 5 and 6 are not value accrual at all. Saying "governance
token" in the What-the-token-does callout without saying "no cash flow reaches holders today" is
the polite version of hiding the zero.

---

## THE CLAIM STRENGTH LADDER (step 3)

From strongest to nothing. Two tokens with the same mechanism type can sit rungs apart, and the
rung matters more than the mechanism.

**Rung 1: CONTRACTUAL AND ENFORCEABLE.** The flow is written into deployed contract code or an
enforceable structure; no one's ongoing goodwill is required. Example from the audit: **RAIL**,
real protocol-level deductions, roughly $13.0M all-time and roughly $322K in 30 days per DefiLlama.
The comparatively clean case of the nine.

**Rung 2: FORMULA-BASED BUT DISCRETIONARY.** A published formula produces the number, but a company
or foundation chooses to keep honoring it and could stop. Example: **BNB.** Roughly 6.0M BNB burned
in twelve months, roughly $4.4B, about 4.3% of supply, which is enormous, but since December 2021
the Auto-Burn is a formula executed from Binance's own holdings. Nothing forces it to continue.
Real money, revocable promise: name both halves.

**Rung 3: ANNOUNCED INTENT.** Words in docs or blog posts, no formula, no schedule, executed
ad hoc or not at all. Examples: **CARDS** (roughly $1.4M of buybacks, about 3.4% of net revenue,
no published formula, while ops wallets off-ramped roughly $45.7M USDC) and **CAP** (docs sentence:
"Revenue generated will be used to conduct discretionary buybacks," nothing live). Intent is a
fact worth recording. It is not a flow.

**Rung 4: NOTHING.** No burn, no distribution, no requirement, no stated intent, or a mechanism
whose documentation has gone dark. Examples: **DOGE** (no burn, no fee capture, no staking,
uncapped supply, roughly $370M per year of new issuance: a claim on nothing but future demand) and
**NOICE** (the old index-asset/buyback design's docs now 404; an unpublished mechanism is scored as
no mechanism until it is republished).

---

## NAMED TRAPS (step-by-step recognition list, each from a real entry)

1. **THE GROSS-VS-NET TRAP (CARDS, Silver).** The entry cited "$146.9M Q1 revenue." That was GROSS
pack sales, and roughly 90% is instantly paid back to users as pulls; net was roughly $43M against
roughly $635M gross all-time. Always ask what the business KEEPS. Marketplaces, pack-sellers,
casinos, and exchanges all quote gross first.

2. **THE ONE-TIME-VS-RECURRING TRAP (VVV, Gold).** The entry implied 42.68% of supply burned
through usage. Roughly 32.5M of that was a single unclaimed-airdrop burn in March 2025;
revenue-funded burns since November 2025 total roughly 217K VVV. Date every burn, strip one-time
events, and only annualize the recurring residue.

3. **THE EQUITY-VS-TOKEN TRAP (VVV, Gold).** Venice's $1B Series A is equity in the company. Token
holders do not own the company. Corporate fundraising, corporate revenue, and corporate valuation
are facts about the BUSINESS; they enter the token's math only through a mechanism from the
taxonomy. If the company wins and the token has no claim, the token can still go to zero.

4. **THE WHICH-LEG-ACTUALLY-PAYS TRAP (BNB, Gold).** BNB has a chain leg (gas burn) and an exchange
leg (Auto-Burn from Binance). The exchange leg outweighs the chain leg roughly 350x. When a token
touches multiple businesses, attribute the accrual to the leg that actually pays, and rate THAT
leg's claim strength. A great chain story attached to a discretionary corporate promise is still a
discretionary corporate promise.

5. **THE DISCRETIONARY-VS-CONTRACTUAL TRAP (BNB and CARDS).** Both do real buybacks/burns; neither
is enforceable. BNB is rung 2 (formula, revocable), CARDS is rung 3 (no formula at all). The trap
is writing "buyback and burn" in an entry as if the words themselves were a contract. Always state
the rung.

6. **THE ISSUANCE-SWAMP TRAP (SOL, Gold).** Roughly $32.4M per year reaches holders while roughly
$1.75B per year is minted. Net NEGATIVE roughly $1.72B per year. Skipping step 5 turns an
unambiguously negative asset into a mildly positive one. This is why the subtraction is mandatory.

7. **THE ZERO CASE (DOGE, Gold).** Sometimes the honest answer is a flat zero with negative
issuance on top (roughly $370M per year minted, uncapped). Write it. A zero stated plainly is more
useful to the reader than a paragraph of maybes.

8. **THE PROMISED-VS-MEASURED TRAP (TIG, Gold).** The entire thesis is IP licensing revenue. The
licensing scoreboard is 0 of 6, and the commercial license defers to a rate card with no percentage
in it. A thesis about future revenue is a legitimate thing to hold in a tier DB, but step 4 records
what was DELIVERED, and for TIG that is $0 so far. Keep thesis and measurement in separate
sentences.

9. **THE DESCRIBED-BUT-UNVERIFIED TRAP (REPLY, Silver).** The mechanism is documented but its live
status is unverified. Per doctrine, "unverified" is a label, not a negative score, but an entry may
not present a described mechanism as a measured flow. Say "documented, live status unverified" and
put $0 in step 4 until verified.

10. **THE MECHANISM-WENT-DARK TRAP (NOICE, demoted to Bronze).** Docs that described the accrual
design now 404. Treat dead documentation as a change event: re-verify, downgrade the rung to
nothing until republished, and date the observation.

11. **THE PRODUCT-YIELD-VS-TOKEN-ACCRUAL TRAP (CAP, Silver, added from the 2026-07-30 worked
example).** In stablecoin and yield protocols, the yield paid to DEPOSITORS is a product feature
and a cost of doing business, not token accrual. Cap's borrowers paid roughly $358K of fees in 30
days, but roughly $344K of that went to stcUSD stakers and restaker delegators (the product), the
protocol kept roughly $14.2K, and $0 reached CAP holders. Never let a protocol's headline
fee/yield number stand in for the token's number. DefiLlama's fees-vs-revenue-vs-holders-revenue
split is the fast check.

**The benchmark, not a trap: RAIL.** Real protocol deductions, roughly $13.0M all-time, roughly
$322K per 30 days per DefiLlama. This is what a live, verifiable, contract-level flow looks like at
small scale. Compare candidates against it.

---

## WHAT MAKES A CLAIM VERIFIABLE (step 4 discipline)

**Counts as VERIFIED:**
- On-chain burn addresses and dead addresses you can read a balance from, with dated deltas
- Buyback wallets traced on chain (and, for the skeptic pass, ops wallets traced the other way:
  the CARDS $45.7M USDC off-ramp was found this way)
- DefiLlama fees/revenue/holders-revenue with its published per-protocol methodology string
- First-party docs pages that exist NOW (fetch them; a 404 is a finding, see trap 10)
- Platform leaderboards read live on the platform itself, never from a tweet

**Counts as CLAIMED (label it, never promote it):**
- Aggregator "total burned" numbers with no address to check
- Project blog posts and tweets about buybacks with no tx links
- "Since inception" cumulative figures with no time axis
- the author's or anyone's recollection (label as recollection; a cheap targeted search of the official
  X API often resolves these, per the 2026-07-22 Pollak/Kerbrat lesson)

Anything that cannot be sourced gets omitted, not invented (standing rule). Label every number
verified vs claimed vs MY ESTIMATE.

---

## HOW THIS SHOWS UP IN ENTRIES

- The Overview's value-accrual sentence (mandatory per the author's 2026-07-22 rule) states the
  mechanism AND the rung in plain language, or states plainly that nothing reaches holders today.
- The full seven-step arithmetic goes in a dated, labeled block in the entry (Extra area), showing
  the issuance subtraction explicitly.
- No selling language anywhere in it. The block is arithmetic sitting next to a price.

---

## LESSON LOG (append when the author corrects this file; date each entry)

- 2026-07-30. Born from the nine-entry audit plus the CAP worked example, same day as the
  chain-purpose framework was captured. First worked application: the CAP Silver entry.
