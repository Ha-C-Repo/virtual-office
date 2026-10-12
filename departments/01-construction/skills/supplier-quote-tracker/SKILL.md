---
name: supplier-quote-tracker
description: Logs and compares supplier quotes internally. Never client-visible.
---
## When to use
Whenever a rate is unknown or a purchase exceeds the parallel-quote threshold.

## Inputs
Quote emails or sheets, material specification, quantity.

## Steps
1. Log each quote: material, quantity, unit, unit price (internal), lead time, expiration, reference, logged date.
2. Normalize units before comparing.
3. Flag expired or near-expiry quotes.
4. Compare at least three suppliers on price, lead time and terms for high-value items.
5. Feed the chosen price into the estimate as a quoted rate, with the basis recorded.

## Outputs
Quote log entries and a comparison table.

## Gates
Internal only. The scrubber blocks supplier names in client documents. Prices from feeds are LOW until a written quote exists.
