---
name: two-document-pair-check
description: Verifies that both the client document and its internal twin (suffix -GP) exist and match before delivery.
---
## When to use
Before sign-off on every bid.

## Inputs
Output folder, bid number.

## Steps
1. Confirm the client proposal PDF exists.
2. Confirm the internal margin report (`-GP`) exists with the same bid number and revision.
3. Confirm totals match across the pair.
4. Confirm the scrubber passed on the client side.
5. Confirm alternates (`-ALT`) each have their own pair where margins differ.

## Outputs
PASS or a list of missing or mismatched documents.

## Gates
A client document without its twin is a defect. Do not send.
