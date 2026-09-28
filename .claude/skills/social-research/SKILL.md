---
name: social-research
description: Research a crypto project's X (Twitter) presence and trace its founder, using the member's own X API key. Use whenever the research asks "who is behind this", "who's the founder", "find their X page", "check their Twitter", "is this the real account", "what is the team saying", or when the Team system of the CoinPicks method needs social evidence a website does not give. Resolves the handle from FREE sources first, verifies the account really belongs to the token being researched, traces the founder, and reports the source-quality tier reached. Official X API only, read-only, with a hard per-run spend cap. Optional: without a key the research continues and says which checks were skipped.
---

# Social research: the X half of the Team system

The Team system in `framework/COINPICKS-METHOD.md` asks who is behind a project and whether
their track record is real. LinkedIn and the project's own site answer half of that. The other
half lives on X, where founders actually talk, and where a project's real account can be told
apart from the several impersonating it.

This skill is **optional**. Without an X key the rest of the research still runs; you simply
report which checks you could not do rather than guessing at them.

## FIRST: IS THERE A KEY?

The member's own bearer token lives in `.env` at the engine root as `X_BEARER_TOKEN`.

- **No key, or the file is absent?** Say so once, plainly: social checks are unavailable, the
  Team write-up will rest on LinkedIn and primary sources only, and the report must say that.
  Then continue. Do not stop the research and do not ask twice.
- **Key present?** Use it only in the Authorization header to the official API. **Never print
  it, echo it, paste it into chat, or copy it into a report.**

**Official X API only.** No scrapers, no mirrors, no unofficial endpoints. If the official
route cannot answer something, that is the answer.

## SPEND: THIS COSTS THE MEMBER REAL MONEY

X bills per read from the first call, so:

- **Free sources first, every time.** DexScreener and GeckoTerminal both publish a project's
  listed socials, and the engine already has tools for both. That resolves most handles for
  $0. Spend a read only on what free sources cannot answer.
- **Hard cap: $1.50 per coin** unless the member raises it for that run, out loud. Count as
  you go, stop at the cap, and report what you have.
- **Report the actual spend** at the end of every run, against the cap.
- Cache what you resolve so the same lookup is never paid for twice.

## THE JOB

1. **Resolve the handle from free sources.** The socials field on the pool or token page.
   Only spend if it is empty.
2. **Verify the account is really this token.** This is not optional and it comes before any
   quote. Evidence that counts: the account posting the contract address, the socials listed
   on the pool page, an exact name and ticker match. **If you cannot confirm it, stop and say
   so.** Quoting a founder from the wrong account is worse than having no social section.
3. **Trace the founder.** The project account and the person reposting each other beats
   anything a bio claims. Bios are free to write.
4. **Judge the account, do not score it.** Age, follower count, whether it is verified, whether
   there is a real name and face, and whether the project cross-confirms them. Write this as
   prose. **This engine never outputs numeric scores** — that law applies here too.
5. **Read what they actually say.** Newest first, dated, with links. A founder who has not
   posted in four months is a finding, not a blank.

## SOURCE-QUALITY TIER, always state which you reached

1. **Founder interview** (highest: long-form and unscripted)
2. **The founder's own posts**
3. **The project account**
4. **Other accounts talking about it** (lowest, and always note how big that account is)

A tier-4 result is a legitimate result. Saying so is the useful part.

## WHAT GOES IN THE REPORT

Under the Team section, in prose:

- The verified handle and how you verified it.
- The founder, what they are demonstrably behind, and what remains unconfirmed.
- The tier you reached.
- Anything absent: no X presence, a dormant account, an anonymous team. **Anonymous is a fact
  to report, not a verdict** — plenty of real projects run that way, and the reader decides.
- If there was no key: one line saying the social checks were skipped and why.

## HARD RULES

- **Never present a guess as fact.** Label what is verified and what is your read.
- **Never quote from an unverified account.**
- **No numeric scores**, here or anywhere in this engine.
- **Never exceed the cap**, and never hide what a run cost.
