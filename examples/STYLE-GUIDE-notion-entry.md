# CoinPicks research-entry style guide (the rules behind the gold standard)

This is how a finalized CoinPicks research entry should read. Mirror this **tone, language level, structure, and team-section format** whenever you write a full research report. The companion golden example is `GOLDEN-zama-notion-entry.md`; the full live set is the public CoinPicks Diamond Investment Database (read via the Claude for Chrome browser):
`https://coinpicks.notion.site/diamonddatabase?v=27e82822b7b780409672000cc47c0665`

## Style rules (what makes this the standard)

### 1. Plain language with analogies — for people without crypto/tech background

If a section uses a technical term, define it inline or replace it with an analogy:

| Don't say | Say instead |
|---|---|
| "offchain coprocessor architecture and threshold decryption" | "developers write normal smart contract code (Solidity, the standard language) and the privacy layer works underneath — kind of like how website developers don't need to understand HTTPS for their site to be secure, it just works" |
| "compute directly on encrypted data without ever decrypting it" | "lets the blockchain process your data while it stays locked in a sealed box the whole time" |
| "Total Value Shielded (TVS)" | "value locked into encrypted transactions" |
| "MEV bots can front-run any visible transaction" | "automated bots can spy on pending trades and jump ahead of regular users" |
| "FHE-enabled Ethereum Virtual Machine" | (just say "FHE" once, defined as "Fully Homomorphic Encryption — math that lets you do math on locked data") |

Every entry must include **at least one analogy** in the Overview section. The Zama one — *"postcard vs sealed envelope"* — is the template. Pick something everyday-people-relatable.

### 1a. "What $TICKER does" callout — required in every Overview

Right before the **Analogy** line, every Overview must include a labeled callout that says **What $TICKER does:** in **1–2 sentences max**. This explains the actual mechanics of the token — what it's used for and the most likely way value flows to it.

Pattern by token type:
- **Gas / utility tokens:** "Every transaction on X pays fees in TICKER, and those fees get burned, shrinking total supply as the network is used more."
- **Governance / DAO tokens:** "TICKER is the governance token — holders vote on Y, and the most likely path for value to accrue is through future proposals directing profits toward buybacks and burns."
- **Staking / yield tokens:** "Stake TICKER to receive Z (compute, fees, voting power); a portion of revenue buys TICKER off the open market and burns it."
- **Platform base currencies:** "Every X launched on the platform is paired against TICKER for liquidity, so demand for X flows through TICKER."

Examples from the gold-standard entries:
- **$ZAMA:** "Every confidential transaction on Zama's network pays fees in ZAMA, and those fees get permanently destroyed (burned)..."
- **$DEUS (XMAQUINA):** "Governance token of the DAO; the most likely path for value to accrue is through future proposals directing profits from the DAO's robotics-company investments toward DEUS token buybacks and burns."
- **$RAIN:** "Every trade across the Rain network pays a 2.5% fee that automatically buys RAIN off the open market and burns it..."
- **$VVV:** "Stake VVV → get a proportional share of Venice's total AI compute capacity..."

### 2. State facts. Never sell.

**Cut anything that reads like a pitch deck.** Specifically, ban these phrases (and equivalents):

- "transition from research curiosity to investable narrative"
- "the strongest part of the thesis" (in narrative scoring sections — this is fine for **Smart Money** but not maturity/lineage/mutation)
- "positioned to be a 100x category"
- "asymmetric opportunity"
- "the moment to position"
- "this is the bet"
- "front-running the trend"
- Anything that implies the reader should buy / sounds like financial advice

Replace with neutral facts: dates, partnerships, raise amounts, what the product does, who's using it.

### 3. Narrative scoring: keep Smart Money strong, soften the rest

Smart Money section is the place to show concrete institutional/whale signals — VC names, partnerships, listings. Maturity/Communication/Lineage/Mutation should read like a news brief, not a pitch.

### 4. Team section: one sentence per person, with PAST metrics

Each team member's bullet must:
- Be **one sentence** (long sentence OK, but one)
- Cite a **past project they worked on** (NOT the current crypto project being reviewed)
- Lead with a **financial metric** if it exists (acquisition price, valuation, funding raised, revenue)
- If no financial metric exists, use an **adoption metric** (users, developers, downloads, academic citations, employees managed, clients served)
- For academic founders: **citation count** counts as adoption (Pascal Paillier has 13,185 citations → "research cited over 13,000 times")
- Include sourced links with **Ctrl+F-able quotes** ("over 23,000 developers")

Zama's two team examples are the template:

> **Dr. Rand Hindi:** Previously founded **Snips**, a privacy-focused voice AI platform that was **acquired by Sonos for $37.5M in November 2019** and had built a community of **over 23,000 developers** before the acquisition; PhD in Bioinformatics from University College London.

> **Dr. Pascal Paillier:** Invented the **Paillier cryptosystem in 1999** (one of the most widely used encryption schemes ever — his research has been **cited over 13,000 times** across academia, and the 1999 paper alone is cited in **2,333+ academic surveys**), previously CEO of CryptoExperts (cryptography consulting firm), and **awarded the IACR Fellowship in 2025**, the cryptography field's highest honor.

Each person gets 2-3 sourced links underneath the sentence, each with a Ctrl+F-able quote.

### 5. Don't invent numbers

If a metric can't be sourced, omit it. Don't fill in "estimated" or "approximate" or "likely." The reader can tell when numbers are real.

### 6. Yellow-highlight every H1 section header

Every `# ` heading in the entry must be wrapped in `<span color="yellow_bg">...</span>` so the section dividers render with a yellow background in Notion. This is what visually separates the major sections in the canonical Zama entry.

Apply highlighting to these H1s:
- `# <span color="yellow_bg">[\$TICKER Chart Link](url)</span>`
- `# <span color="yellow_bg">**Liquidity: <tier>**</span>`
- `# <span color="yellow_bg">**Overview**</span><span color="yellow_bg">:</span>` (Overview's colon goes in its own span — that's how the canonical Zama entry stores it)
- `# <span color="yellow_bg">**Exclusivity Factor:**</span>`
- `# <span color="yellow_bg">Narrative Scoring:</span>`
- `# <span color="yellow_bg">Team:</span>`
- `# <span color="yellow_bg">Want to Know More?</span>`

Do NOT highlight:
- H3 sub-headers like `### **Narrative Maturity Score**` (per-score sections inside Narrative Scoring)
- H3 sub-headers like `### CEO and Co-founder: **Dr. Rand Hindi**` (per-person sections inside Team)
- The `### Extra:` block

### 7. Liquidity section is minimal — no volume, no TVL, no CEX listings

The Liquidity section is **two lines, period**:
- The H1 heading: `# <span color="yellow_bg">**Liquidity: <tier>**</span>`
- One line below it: either `[Biggest DEX Liquidity Pool](url)` (a single GeckoTerminal pool URL) OR, if the coin is mostly CEX-traded, a one-line italic note like `*XLM is mostly a CEX token*`

The two patterns from the canonical examples:

Zama (has a DEX pool):
```
# **Liquidity: Medium**
[Biggest DEX Liquidity Pool](https://www.geckoterminal.com/bsc/pools/0xb39978347f071b74076be26d1445e2eccafe3557d2cdbc17e6c74d3ea883a4e0)
```

Stellar (mostly CEX):
```
# **Liquidity: High**
[Biggest DEX Liquidity Pool](https://www.geckoterminal.com/cro/pools/0xb1d227d14d19151b915c395692dddf9ccdeadee3)
*XLM is mostly a CEX token*
```

**Do NOT include in this section:**
- TVL or pool reserve dollar figures
- 24-hour trading volume numbers
- Specific CEX venue names or pair volumes (CEX listings belong in **Smart Money Compatibility**, not Liquidity)
- Multiple DEX pool URLs (the section is called *Biggest* DEX Liquidity Pool — pick one)
- Comparative venue lists ("top venues by volume…")

If the section is more than two lines, it's bloated. Cut.

## Structure to preserve (Notion DB entry layout)

```
# <span color="yellow_bg">[$TICKER Chart Link](url)</span>
---
# <span color="yellow_bg">**Liquidity: <tier>**</span>
[Biggest DEX Liquidity Pool]
---
# <span color="yellow_bg">**Overview**</span><span color="yellow_bg">:</span>
<3-4 sentences in plain language>

**What $TICKER does:** <1-2 sentence callout>

**Analogy:** *<everyday-life analogy>*
---
# <span color="yellow_bg">**Exclusivity Factor:**</span>
- **Ease of Use:** <plain explanation, real-world signal of who's using it>
- **Hair-on-Fire:** <the unmet need in plain language + dollar/user signal of demand>
- **Exclusivity Factor:** <the rare unduplicatable thing>
---
# <span color="yellow_bg">Narrative Scoring:</span>
### **Narrative Maturity Score**
### **Smart Money Compatibility Score**
### **Narrative Communication Score**
### **Narrative Lineage Score**
### **Narrative Mutation Score**
---
# <span color="yellow_bg">Team:</span>
### Role and Co-founder: **Name**
<one-sentence past-project summary with metrics>
<sourced links with Ctrl+F quotes>
---
# <span color="yellow_bg">Want to Know More?</span>
---
### Extra:
<bullet list of recent milestones, key dates, dilution / token details>
```

## When to invoke this style

Any time you write a full CoinPicks research report (or the user asks to "make me a full research report using the CoinPicks strategy"). Match this style without re-asking. The live gold-standard set is the public Diamond Investment Database link above.
