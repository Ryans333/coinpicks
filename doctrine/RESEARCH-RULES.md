# Research Rules (always on)

These are not optional settings. The engine applies them to every scan and every write-up. **Read `HOW-RESEARCH-ACTUALLY-WORKS.md` first — it explains the angle-driven process these rules sit inside. If anything here conflicts with that file, that file wins.**

1. **Lead with the angle.** Before scoring or sorting anything, find the one-sentence reason a coin could re-price (smart-money partnership, founder track record, structural unlock, viral-parent beta, urgent customer pain). The angle drives the write-up; everything else supports it. If there's no real angle, say so plainly — don't pad a weak coin.

2. **Weight teams heavily, but never disqualify on team.** Strongly prefer projects with real, public, credible people who've shipped before — a clean founder track record pushes a coin up. But an anonymous or no-public-team coin is **NOT** eliminated: it gets a clearly stated risk flag and, all else equal, a lower conviction tier. Never silently drop a coin *just* because the team is anonymous. (This is a deliberate change from older versions that used a hard anonymous-team kill rule.)

3. **Team credibility comes from PAST employers and projects — never the current one.** "Founder worked at X" must be backed by a sourced, Ctrl+F-able quote from a real source (LinkedIn, the company's site, a press release). The current project's own claims about its team do not count as credibility.

4. **Funding history is analyzed, not just reported.** Always include the year/date and stage of every round — "$20M raised" with no date is useless. A round from the last bull run (e.g. 2021) is a risk to flag (early VCs may have exited or be a waiting overhang), not a plus. Check for *recent* funding activity separately from the lifetime total. Keep unlock-overhang and unlock-schedule risks.

5. **No name-drops without explanation.** Every person cited gets a plain-English bio with sourced metrics from their prior work. Never assume the reader knows who someone is.

6. **Never invent numbers.** Market cap, liquidity, revenue, TVL, funding, percentages — if it isn't sourced, leave it out. An honest "not found" beats a confident guess.

7. **Plain language, no hype.** No shilling adjectives, no "this is going to explode." Describe what it does and let the facts carry it. Don't dress up a weak chart as strong.

8. **Multi-chain projects are not disqualified** for a selected chain. If you filter for "Base" and a project is on Base + Ethereum + Solana, it still passes.

9. **This is research, not financial advice.** No price predictions, no "buy this." Surface the angle, the team, and the risks; the decision is yours.

10. **Verify "backed" claims** with the legal-structure / bankruptcy test in `SOURCE-QUALITY.md` before repeating any "asset-backed" or "treasury" language.

11. **Dedup everything.** Append every coin examined to `SEEN-COINS.csv` (via `update-seen-coins.py`) so the same coin is never re-researched from scratch.
