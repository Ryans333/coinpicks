# ⭐ THE CYCLE-PEAK EXTRAPOLATION FRAMEWORK
**the author's framework, dictated 2026-08-05. Raw words not shipped (read that first when this feels ambiguous).**
**the author: "I need you to save this somewhere where every single Claude agent will see it. This is extremely important."**

This is the THIRD framework in the set. Read the boundary carefully:
- **CHAIN-PURPOSE framework** values the BUSINESS.
- **TOKEN VALUE ACCRUAL framework** values the CLAIM on that business.
- **THIS framework fixes WHEN you measure**, because measuring either of the above at the bottom of a four-year cycle produces a systematically wrong answer.

---

## 0. HOW THIS FIRES — THE TRIGGER (added 2026-08-05 at the author's request: "I want it to be the default")

the author's definition of the class: **"coins that aren't necessarily being realistically priced based on their current usage."** That is a measurable condition, not a vibe, so it gets a measurable test.

### THE GAP TEST — run it on every mechanical-revenue coin, automatically

```bash
```

**If market cap divided by current annualised revenue is greater than 50x, the market is pricing a FUTURE rather than today's usage. The framework FIRES.** Judging that token on trough numbers will produce a wrong answer.
**If it is under 50x, current usage IS the story. Value it on present numbers and do NOT reach for a dream state.**

Calibration run 2026-08-05, and it discriminates cleanly:

| Token | Market cap / current revenue | Fires? |
|---|---|---|
| $ZAMA | **8,697x** | YES, hard |
| $MON Monad | **90x** | YES |
| $AAVE | **4x** | NO, judge on today |

That is the whole trigger. It needs no judgment call and no memory.

### It ALSO fires on any of these phrasings from the author
"what does this look like at the top" · "what about in a bull market" · "you're using bear market numbers" · "what's the dream state" · "run cycle peak" · "extrapolate this to the peak" · "what if crypto goes crazy again" · "is this priced on current usage" · "how much usage would it need."

### And it fires AUTOMATICALLY, without being asked, in these situations
- Any **tier-DB entry or repass** (`db-entry-researcher`) for a coin with a mechanical revenue line.
- Any **hedge-fund PDF report** in `Hedge-Fund-DB/PDF-Reports/`.
- **Any time a conclusion is about to be written that a token's accrual is hopeless, negative, or far from break-even.** If that verdict rests on current-cycle data and the gap test fires, the verdict is not finished. Run this first. *This is exactly the mistake made on $ZAMA on 2026-08-05.*

### The output is always the BREAK-EVEN SHARE
Never report "it is 2,222x from break-even." Report **"it needs X% of peak-cycle [driver] to break even, versus the category leader's Y% today."** The first is a dead end. The second is a decision.

## 1. THE TWO CATEGORIES (the author's split)

**Category A: MOMENTUM COINS.** Demand is already visible. Price is moving. Short-term. Judge these on what is happening now, because now IS the thesis.

**Category B: MECHANICAL-REVENUE COINS WITH NO MOMENTUM.** DeFi protocols, looping and yield protocols, and crypto-native infrastructure. the author's words: *"coins that have a mechanical revenue that they're bringing in somehow, mechanically speaking"* and *"decently solid fundamentally, but they just have zero momentum."*

**The whole framework applies to Category B only.** Applying it to a meme coin or a momentum name is an abuse of it.

## 2. THE CORE ERROR IT FIXES

A Category-B token's revenue is **derivative of crypto adoption itself**. the author on Zama: *"Zama is something that's built on something else, which is crypto. It's literally saying, hey, make your crypto private."*

So its revenue is a **cyclical** revenue line, and nobody values a cyclical business on trough earnings. You do not value a steel mill, a shipping line, or a semiconductor fab at the bottom of its cycle and call that fair value. **Crypto infrastructure is the same shape, and the cycle has repeated on a roughly four-year clock every time so far.** the author's examples: Ethereum usage exploding Jan-Feb 2018 then dying, exploding again Oct 2021 to early 2022 then dying, with protocol revenues *"deeply correlated, extremely correlated to the usage of Ethereum's chain."*

**Today's numbers are the STARTING POINT, not the ANCHOR.** the author: *"yes, we want to know where we're starting at, so today's numbers for a good starting point, but that's not where I should be magnetizing my future predictions."*

## 3. THE METHOD

**Step 1. Identify the driver.** What activity does this protocol's revenue actually ride on? DEX volume, lending balances, transaction counts, blockspace demand, stablecoin float. Name the single metric.

**Step 2. Measure that driver at the last cycle PEAK, not today.** Verified 2026-08-05, all from DefiLlama:

| Driver | Peak | Recent | **Cycle multiplier** |
|---|---|---|---|
| DEX volume, all chains | Oct-2025, \$588.1B/mo | Jul-2026, \$202.9B/mo | **2.90x** |
| DEX aggregator volume | Jan-2025, \$263.8B/mo | Jul-2026, \$78.8B/mo | **3.35x** |
| Protocol fees, all | Jan-2025, \$3.28B/mo | Jul-2026, \$1.72B/mo | **1.91x** |

**Step 3. Decide the protocol's SHARE of the driver at peak.**
- If the protocol **existed** last cycle, read its actual peak revenue. That is the honest anchor.
- If the protocol is **new** (Zama, most of what we look at), you cannot multiply its current revenue by the cycle multiplier, because it did not exist to be multiplied. **You must model an adoption SHARE instead**, and benchmark that share against the current leader in its category. State it as a scenario, never as a forecast.

**Step 4. Apply the protocol's CURRENT unit economics to that peak-level activity.** Fee per transaction, or basis points per dollar. Keep the unit economics fixed and scale only the volume.

**Step 5. Subtract issuance at the same moment.** This is the step everyone skips. **Issuance does not fall in a bull market.** If fees are token-denominated, the break-even is fully price-invariant: a higher price lifts the dollar value of the burn AND the issuance equally. State net accrual, never gross.

## 4. THE MANDATORY HAIRCUTS (this is what stops it becoming a hype machine)

**H1. TAKE RATES COMPRESS. Verified, not assumed.** Last cycle DEX volume rose **2.90x** but total protocol fees rose only **1.91x**. **Fee capture compressed by about 1.52x.** So extrapolating fees by a volume multiplier overstates the answer by roughly 1.5x. **Apply the haircut explicitly and show it.**

**H2. THE FEE TREADMILL.** Many protocols plan to cut per-unit fees as they scale (Zama's litepaper targets \$0.005/op, down from about \$0.05 today). Burn equals fee times volume, so **every fee cut raises the volume needed by the same multiple.** Check the docs for a planned fee decline before extrapolating.

**H3. SURVIVORSHIP.** The protocol has to still exist at the next peak. Check runway, unlock cliffs landing before the peak, and whether the category kills its losers. In RFQ, Clipper and AirSwap were real funded projects now doing literally \$0.

**H4. THE PEAK IS A MOMENT, NOT A LEVEL.** Peak-cycle revenue is a spike, not a run rate. A token that only clears break-even AT the peak spends most of the cycle diluting. Say which one you are describing.

**H5. NEW CATEGORIES USUALLY FAIL.** Modelling a new category going from zero to meaningful share is the highest-variance assumption in the whole method. Benchmark it against the category's current leader and say what share you are assuming out loud.

## 5. WHAT TO OUTPUT

Never a single number. Always: **(a)** today's measured baseline, **(b)** the peak-cycle scenario table across a range of adoption shares, **(c)** the break-even share stated plainly, **(d)** the haircuts applied, **(e)** the one metric to watch that tells you which scenario is happening.

**The most useful single output is the BREAK-EVEN SHARE**, because it converts an unanswerable question ("will this succeed?") into a checkable one ("does it need 0.4% or 40% of its market?").

## 6. WORKED EXAMPLE — \$ZAMA, 2026-08-05

**Driver:** DEX volume (the RFQ charges per dollar traded). **Issuance to beat: \$28,971,971/yr.**

| Share of peak DEX volume | Volume | Burn @10bps | vs issuance |
|---|---|---|---|
| 0.10% | \$7.1B | \$7.1M | short |
| 0.25% | \$17.6B | \$17.6M | short |
| **0.41%** | **\$29.0B** | **\$29.0M** | **BREAK-EVEN** |
| 1.00% | \$70.6B | \$70.6M | **2.4x positive** |
| 4.49% | \$317.0B | \$317.0M | **10.9x positive** |

**The punchline: break-even needs 0.41% of peak-cycle DEX volume at a normal 10bp fee.** Native Swap, today's leading RFQ venue, already runs at **4.49%** of current DEX volume. So Zama's RFQ needs roughly **one eleventh of the share the current category leader already has**, at cycle-peak volumes.

**With the H1 haircut applied (1.52x), break-even rises to about 0.62% of peak DEX volume. Still well under what the incumbent does today.**

**This inverted the conclusion.** Measured on trough data the Gateway toll is 2,222x from break-even and the honest verdict reads "hopeless." Measured properly at cycle peak on the correct driver, the RFQ path needs a sub-1% market share and the verdict is "a real, checkable bet with a defined trigger." **The trough-anchored answer was wrong, and it was wrong because of WHEN it measured, not because the arithmetic was bad.**

**The one metric to watch:** Zama Confidential RFQ volume after its stated September 2026 public launch. That single number tells you which row of the table you are living in.

---

## 7. WHEN NOT TO USE THIS

Do not use it on meme coins, momentum names, tokens with no mechanical revenue, or anything where the "revenue" is emissions being recycled. **A cyclical framework applied to a business with no cycle and no revenue is just a story generator.** If you cannot name the driver in Step 1 in one metric, stop.
