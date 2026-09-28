# The CoinPicks Research Method (the 5 systems)

This is the CoinPicks research framework — the lens applied to every coin. It ships **inside this engine**, so you don't need to scrape it from anywhere to get started.

> **Read `doctrine/HOW-RESEARCH-ACTUALLY-WORKS.md` alongside this.** The course version of this framework attaches **numeric scores** to each system (Narrative /31, Team /10, an Exclusivity gate). **This engine does not use those numbers** — it applies these five systems as *qualitative lenses*, angle-first, in plain prose. The concepts below are what matter; the point tables have been intentionally removed. If anything here implies a score, ignore the score and keep the concept.

The five systems: **Core Strategy → Product / Exclusivity → Liquidity → Narrative (Demand) → Team.**

---

## 1. Core Strategy

Seek coins with **low liquidity relative to the current market cycle** that show a credible path to becoming **high-liquidity** positions. Liquidity reveals where capital is and where it's rotating next. The goal is to position early — before the repricing — in underexposed assets that have real fundamentals, credible infrastructure, and narrative alignment. This is the lens applied to every asset: anticipate where liquidity rotates next, rather than chasing momentum after the fact.

## 2. Product — the Exclusivity Factor

Product strength is the level of real innovation a project has actually built and the utility it creates in the real world. In crypto, **product = substance.** Evaluate it through three keys (qualitatively — no scoring):

- **Ease of Use** — When you actually use the product, does it work smoothly, simply, and effectively? Does it do what it claims, or is it clunky / vaporware?
- **Hair-on-Fire** — Does it solve an **urgent, painful** problem that users or an entire industry feel they must adopt *now*? Look for real evidence of demand (named users, customers, or industries actively needing it), not a gimmick.
- **Exclusivity Factor** — The "wow" trait. Does the project have a rare, **not-easily-duplicatable** edge — first-to-market, a legal win, world-class backing, an official integration/fork approval — such that clones are always second-best? Traits to look for: category-creating utility, obvious universal usefulness, "market gravity" (competitors copy it), and an emotional "this changes everything" punch.

If a project clearly fails all three (clunky, not urgent, easily copied), it's weak — move on. (Note: in the older course this was a numeric kill-gate; here it's a judgment call, not a math gate. Research what's interesting; let the write-up land it as strong or weak.)

## 3. Liquidity

Gauge liquidity two ways: the size of the **main liquidity pool**, and the **±2% depth** across exchanges. Compare it to the *pre-pump* liquidity of recent top performers to judge what "cheap" looks like in the current cycle. Then assign a simple tier — **Low / Medium / High** — by best judgment, not a formula.

- **Low liquidity = high volatility** — moves fast in both directions.
- **High liquidity = lower volatility** — moves more steadily.

How to assign the tier in practice: check the "Markets" tab on CoinGecko and sort by ±2% depth; find the main DEX pool (GeckoTerminal), checking the top few pools by liquidity since previews can be stale; use the biggest pool's size plus the ±2% depth to call it Low / Medium / High. If there's no DEX pool, judge by ±2% CEX depth alone (some coins are mostly CEX-traded — say so).

## 4. Narrative (Demand)

Demand is the market's desire to buy a project, driven primarily by **narrative**. In crypto, **story = value.** Assess the narrative through these lenses — **written as prose, never as point scores:**

- **Narrative Maturity** — How far along is this narrative in the market cycle? (Early = room to run; late/exhausted = be careful.)
- **Smart Money Compatibility** — Would serious capital — institutions, tier-1 VCs, named smart-money — actually flow into this? This is usually the strongest part of a thesis when it's present; show the concrete signals (partnerships, backers, listings).
- **Hair-on-Fire Innovation** — Is it solving an urgent, painful problem the market must adopt now? (This lives inside the narrative read here.)
- **Narrative Communication** — How well is the story being told? Clear messaging, credible public spokespeople, real press.
- **Narrative Lineage** — Is it clearly connected to a previously proven 100× trend (e.g., DePIN via Render, AI via Bittensor)?
- **Narrative Mutation** — Has the narrative evolved into a real-world trend or a new form?

**Evidence standard:** every claim gets a 1–2 sentence explanation backed by a source link with a Ctrl+F-able quote — `https://example.com "exact text on the page"`.

## 5. Team Credibility

Evaluate the **top 3–5 most important people** (founder + heads of product/marketing + any standout contributors or world-class advisors). The rules:

- **Past experience only — never the current project.** Most projects we research are still small and unproven, so the current project proves nothing about the team. Judge them on what they did *before*.
- **One sentence per person.** If you understand their background, you can say it in one sentence.
- **Lead with a financial metric** (acquisition price, valuation, funding raised, prior project's market cap or revenue), then an **adoption metric** (users, downloads, developers, citations) if available.
- **Every claim sourced** with a Ctrl+F-able quote (LinkedIn for employment history, the company's site, press releases).
- **X (Twitter) is the other half of this system, and it is where founders actually talk.**
  Verify the project's real account before quoting anything from it (impersonators are
  routine), then trace the founder and read what they have said lately. Run the
  `social-research` skill; it needs the member's own X key and says so when there isn't
  one, in which case this section rests on LinkedIn and primary sources and the report
  states that plainly. **Anonymous teams are a fact to report, never an automatic no.**
- **The founder matters most** — weight their track record heaviest in your judgment. (The course did this with a multiplier formula; here it's judgment, not arithmetic.)
- **Advisors** only count as a named team member when they are genuinely world-class *and* actually involved — otherwise skip them.

**Teams are weighted heavily but never a disqualifier.** A strong, credible, public team is a major plus. An anonymous or no-public-team coin is a **flagged risk** and, all else equal, a lower-conviction placement — but it is never auto-rejected just for the team.

---

## The deliverable
A full research report applies these five systems but reads like the gold-standard examples in `examples/` — angle-first, plain language, a "What $TICKER does" callout, an everyday analogy, the narrative lenses as prose, a one-sentence-per-person sourced team section, funding history with dates, and honest risks. **No numeric scores anywhere in the report.**
