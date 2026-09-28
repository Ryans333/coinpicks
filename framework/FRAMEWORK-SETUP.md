# OPTIONAL — Refreshing the framework from the community classroom

**You do NOT need this for a normal setup.** The full CoinPicks methodology already ships inside this zip:
- `framework/COINPICKS-METHOD.md` — the 5-system method (de-numbered)
- `doctrine/HOW-RESEARCH-ACTUALLY-WORKS.md` — how to apply it (angle-first, no scoring)
- `examples/` — 8 gold-standard reports + style guide

This file is **only** for the case where a member wants Claude to pull the *very latest* version of the Core Research Strategy lessons from their community classroom (e.g. the course was just updated). It requires Claude for Chrome + an active membership. Skip it otherwise — and never block setup on it.

> Note: the course version contains **numeric scoring** (Narrative /31, Team /10, an Exclusivity gate). This engine does NOT use those numbers — if you pull the course, treat the scoring scales as background only and keep researching angle-first per `doctrine/HOW-RESEARCH-ACTUALLY-WORKS.md`.

If you do refresh: **open the user's community in the browser, navigate directly to the Core Research Strategy section, and capture every page by SCREENSHOT. Do not use WebFetch, and do not rely on copy-paste.** Here's why the other methods fail:

- **WebFetch does NOT work for Skool.** Skool requires a logged-in session. WebFetch returns the public marketing/landing page instead of the course content, with **no error** — it silently gives you the wrong thing. Never use it for these pages.
- **Text extraction misses content.** Several pages in this section are **images with the words baked into the picture.** Pulling the rendered text (`document.body.innerText`) silently drops everything that's an image. That's why screenshots are the default, not a fallback.
- **Copy-paste is lossy.** Pasting drops the tables and images and it's easy to miss a page. Only as a last resort.

## Which community

The framework is the same across all three CoinPicks communities. The user belongs to one of:

- **CoinPicks Genesis**
- **CoinPicks Army**
- **CoinPicks Inner Circle**

During setup the user **pastes the link to their own community** into the chat. Use that exact link — don't go searching for a community. (If they haven't pasted it yet, ask them to copy the URL of whichever CoinPicks community they're a member of.)

## BROWSER + SCREENSHOT method (do this)

1. Make sure the **Claude for Chrome** extension is installed and enabled, and the user is **logged into their CoinPicks community** in that Chrome profile, with an active membership.
2. **Open the user's pasted community link** in the browser.
3. **Navigate directly — don't wander the classroom:**
   - Click the **Classroom** tab. (The tabs across the top are Community, Classroom, Calendar, Members, Map, Leaderboards, About — you only want **Classroom**.)
   - Open **"Start Here: Your Home Base."**
   - Scroll the lesson list on the **left** until you reach **Core Research Strategy.**
   - Everything inside the **Core Research Strategy** section IS the research framework. Go straight there.
4. **Screenshot every page in the Core Research Strategy section, in order.** Don't assume a fixed number of pages — the course changes; capture all of them. For each page:
   - Scroll the page fully (the content lazy-loads as you scroll).
   - **Take a screenshot** (these pages are images-with-text — a screenshot is what reliably captures them). Read the framework content from the screenshots.
   - **Do not click links inside a page while capturing** (e.g. an "Example Submission" link) — it navigates the browser away and you lose your place. If that happens, go back to the page URL and resume.
5. Save each page into this `framework/` folder as `01-...md`, `02-...md`, etc., in module order (include the screenshots / transcribed content).

> The framework you capture here is the **scoring rulebook**. The **example research reports** (the gold standard for what a finished report looks like) are a separate thing — the public Diamond Investment Database. See `examples/EXAMPLE-one-pager.md`.

If a page won't load or the extension isn't available, tell the user exactly what's blocking it instead of silently saving partial content.

## Completeness checklist (verify before moving on)

After saving, confirm each of these is actually present:

- [ ] **Core Strategy** page: the definition + the core strategy steps.
- [ ] **Product / Exclusivity** page: the exclusivity-factor definition with real examples.
- [ ] **Liquidity Analysis** page: the liquidity tiers with the dollar thresholds (Low / Medium / High).
- [ ] **Narrative** page(s): the narrative sub-sections (Maturity, Smart-Money Fit, Communication, Lineage, Mutation) with their content.
- [ ] **Team Credibility** page: the criteria.

If a box can't be checked, the framework is incomplete — re-capture before doing real research.

> The full method ships INSIDE this zip (`framework/COINPICKS-METHOD.md`, `doctrine/`, and the
> 8 gold-standard examples), so the engine applies it with no membership and no login. This
> page is only about pulling a NEWER version of the course if one exists.
