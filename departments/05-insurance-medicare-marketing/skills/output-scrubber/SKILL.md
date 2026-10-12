---
name: output-scrubber
description: Six-rule final scrub of an outward document. Returns PASS, AUTO-FIX or BLOCK in a fixed execution order.
---
# Output scrubber

## When to use
Last step before principal approval, after the compliance gate.

## The six rules, in order
1. Commission data: no commission, override, margin or production number on the outward document.
2. PHI and PII: none; identities masked as initials plus last four of a record ID where an internal doc needs them.
3. Fabricated credentials or unverified claims: every license, certification, enrollment figure or statistic is sourced or removed.
4. Demonstration label present on every outward artifact until the engagement is live. No logos in demo status.
5. Prohibited Medicare language and missing disclaimers.
6. Two-document rule: an internal `-INT` memo exists for this outward piece.

## Steps
Run the deterministic validator on the outward document and on the internal memo (non-zero exit blocks export). Then apply the six rules by judgment. Then run visual QC on the exported PDF: overflow, orphan headings, leaked placeholders, wrong escapes, missing footer or label.

## Outputs
PASS, AUTO-FIX (list of mechanical changes) or BLOCK (reason), plus a one-line delivery summary.

## Gates
After any edit to the validator scripts, smoke-test both directions: a file that should pass and a file that should fail. Do not export on a non-zero exit.
