---
name: voice-check-gate
description: Silent final gate that scans outgoing text against a kill list of banned patterns; auto-fixes minor issues and blocks critical ones.
---
# Voice Check Gate

## When to use
Last step before any text leaves the company (email, proposal, video script, notice, social post).

## Steps
1. Identify the surface: strict (customer contracts, notices), disciplined (sales, support), hands-off (internal notes).
2. Scan against the kill list: dash overuse, filler openers, "not just X, it is Y" constructions, three-adjective stacks, rhetorical closers, banned vocabulary, vague hedges.
3. Minor violation: fix silently. Critical violation (invented claim, wrong tone for a notice): block and report.
4. Clean text passes with no commentary.
5. A simple linter script may score text per surface bucket; treat the score as advisory.

## Gates
Human sign-off still applies after the gate. The gate does not replace approval.
