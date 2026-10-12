---
name: competitor-analysis
description: Structured competitor teardown using free public sources. Produces a summary, a data table, positioning advantages, items to verify and a recommendation (bid, pass, reprice, differentiate, learn, avoid, gap). Use for any competitive question.
---

# Competitor analysis

## When to use
Pricing decisions, bid or no-bid, positioning, product gaps, market entry, app teardown.

## Inputs
Segment definition (core and adjacent), the decision to be made, approved free sources.

## Steps
1. Define two segments if relevant: core offering and adjacent services.
2. One file per competitor: identity placeholder `{{COMPETITOR_NAME}}`, version or date, sources, date retrieved.
3. Capture: offer and core loop, published pricing with date, claims they make, proof they show, compliance surface, retention mechanics, weaknesses seen in public reviews.
4. Tag each finding HIGH, MEDIUM or LOW. Web-fetched items are LOW until confirmed against a primary source.
5. Write the output: summary, data table, positioning advantages, items to verify, recommendation.
6. Separate fact from inference. Never present a competitor's claim as verified.

## Outputs
Teardown file per competitor, comparison table, recommendation with the human decision needed.

## Gates
Free public sources only. No scraping behind logins, no impersonation, no private data. No disparagement in anything outward; the finding stays internal. Dated; re-baseline when stale.

## Anti-patterns
Copying a competitor's wording. Treating review counts as quality. Recommending a paid tool without flagging cost.
