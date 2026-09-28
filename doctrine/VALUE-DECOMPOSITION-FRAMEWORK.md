# The Two-Demand Valuation Framework (Fundamental vs Speculative)

**Status: active methodology, added 2026-07-16 (origin: TIG deep dive). Part of the CoinPicks research system. Read alongside THE AUTHOR-DOCTRINE.md.**

## The idea (the author's, formalized)

A token's price is driven by supply and TWO kinds of demand that must be measured separately:

1. **Value-accrual demand (Fundamental, F)** = demand that exists because the token captures real economic value (fees, burns, buybacks, real staking yield, required collateral/utility). Defensible with data.
2. **Speculative demand (Speculative premium, S)** = demand from narrative, momentum, reflexivity, and hope not yet backed by realized value.

**Market Cap = F + S.  Price = (F + S) / Circulating Supply.**

## How to measure each

**F (compute it forward from real data).** Pick the accrual mechanism(s) the token actually has and value them:
- Fee/revenue capture via burn, buyback, or holder dividend: capitalize the token-capturing cash flow at a comparable multiple (royalty businesses ~10-20x; crypto comps lower, e.g. TAO ~7x emissions).
- Real (non-inflationary) staking yield: present value of the yield stream.
- Required collateral / gas / utility lockup: the token value that must be held to use the network.
- Transactional-only medium (no sink): the equation-of-exchange floor, M = PQ / V (annual throughput / velocity). Usually small; this is why sink-less tokens accrue little.
- **If none of these exist or are unconfirmed, F is only a small utility floor, effectively near zero.** Say so plainly.

**S (measure it backward as a residual).** You cannot reliably forecast speculation. At any snapshot:
- **S = observed Market Cap − F.**
- **Speculative Share = S / Market Cap.** This is the headline metric. Track it over time.

## How to forecast (scenario mode)

Forecast F under explicit scenarios (defensible). Treat S as a labeled assumption (a sentiment multiplier on a speculative base), never as a hidden number. The TIG model does this literally:
`Implied mcap = (multiple x fees x holder-capture%)  +  (sentiment x speculative base)`
The first term is F, the second is S. Keep them as separate, visible rows.

## The logging discipline (why this exists)

At each research snapshot for a tracked project, append one row to that project's decomposition log
(`~/Desktop/Altcoin-Research/valuations/<TICKER>-decomposition-log.csv`). Columns:
`date, ticker, price_usd, circ_supply, mcap_usd, fundamental_mcap_usd, fundamental_price, speculative_mcap_usd, speculative_price, speculative_share_pct, accrual_basis, realized_annual_revenue_usd, holder_capture_pct_assumed, multiple_assumed, notes`

Purpose (the author, 2026-07-16): build a uniform dataset so that years later, when a token has re-priced, we can look back and attribute how much of the move was fundamental value accrual vs speculation. The strategy may change; the data must be uniform and preserved.

## Category note (do not over-fit)

Some tokens have no value-accrual mechanism and can still be worth trading (pure speculative or reflexive plays). This framework does not say those are uninvestable; it just makes the split explicit so we always know which kind of bet we are making. For new, unproven models (never-seen-before designs), F today is usually ~0 and the entire price is a bet that F grows into it. That is a valid bet; label it as such.

## Proposed RESEARCH-CODE (awaiting the author's approval before writing to RESEARCH-CODES.md)

`V1 Fundamental/Speculative split` — for any token with a value-accrual claim, compute F from real data, take S as the residual vs market cap, report Speculative Share, and append a snapshot row to the project's decomposition log. Origin: TIG, 2026-07-16.
