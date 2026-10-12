---
name: bid-output-scrubber
description: Final scan of client-facing documents for forbidden content: supplier names, individual names, margins, headcount, internal rates, engineering line items and banned terms.
---
## When to use
Last step before the two-document pair check on every client-facing document.

## Inputs
Rendered client document, forbidden lists from the company profile, proposal rules.

## Steps
1. Scan for supplier names, precedent project names, individual names, licensed-engineer names, headcount, margin percentages, internal cost rates, cash-flow rationale, superseded terms and addresses, competitor lead times.
2. Scan for a separate engineering line item, banned payment terms and dead terms.
3. Scan for em-dashes, unfilled placeholder tokens and emojis.
4. Check required scope mentions (for example deck).
5. Visual pass on every page: overflow, clipped tables, orphaned headers.
6. List each hit with location. Block, do not auto-fix silently.

## Outputs
Scrub report: PASS or list of blocking hits.

## Gates
Block severity: leaks of internal information, placeholders, banned terms. Warn severity: style. No override.
