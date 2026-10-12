---
name: verify-dont-generate
description: Reviewer gate and rule set for confidence tagging, freshness windows and flag-instead-of-fill behavior. Applies to every routine and extraction.
---
# Verify, do not generate

## When to use
Before any routine acts on data, and before any output leaves the office.

## Rules
1. Never fabricate a reading, count, ID, yield, balance, date, permit number or policy text. Missing data returns a flag naming what is missing and who can supply it.
2. Confidence tag every extraction: high (read directly from a source of record), medium (inferred from a clear pattern), low (unclear). Low is routed to a human, not passed on.
3. Freshness window: stamp the age of each input. Refuse to act when older than its window. Default windows (adjust in `../../knowledge/rules.md`): live readings 24 hours; weekly counts 7 days; register-to-physical reconciliation 30 days; permit status 45 days; price schedule until superseded.
4. What a routine may never do: shorten a lock or hold period; discount below schedule; delete register entries; mark VERIFIED without a recent physical count; change a past entry.
5. Label any number not read from a source as ESTIMATED.

## Steps
Read the source; record input age; tag confidence; compare to the rule; output a value or a flag; log the check.

## Outputs
Value with confidence and source, or a flag.

## Gates
Human sign-off on any low-confidence item and on any action that spends money, ships goods, or sends external communication.
