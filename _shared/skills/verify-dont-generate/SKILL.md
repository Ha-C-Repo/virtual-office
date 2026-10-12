---
name: verify-dont-generate
description: The gate that keeps the AI from producing system-of-record facts. Numbers, identifiers, dates, readings and statuses come from sources on file or deterministic calculators, never from the model. Use on any task that contains a figure, an ID, a date or a status.
---

# Verify, do not generate

## When to use
Any deliverable that states a price, quantity, rate, weight, count, reading, date, deadline, identifier, license or status. Also any extraction from a document.

## Principle
The model explains, drafts and checks. A source or a deterministic tool certifies. If neither is available, the output says so.

## Inputs
The claim to be stated, the source document or register, the calculator or script if one exists.

## Steps
1. List every claim that is a fact of record.
2. For each, find the source on file. Record the path or reference.
3. For arithmetic, use a calculator, script or spreadsheet. Run two independent paths for money. Stop if they diverge beyond tolerance; redo the work.
4. Tag each claim HIGH, MEDIUM or LOW (see `../confidence-tagging/SKILL.md`). Hearsay is never upgraded to an inspection.
5. Where no source exists, write a flag: "NEEDS_INPUT: <what and from whom>". Do not fill the field.
6. A numeric value in a structured output is a claim object: value, confidence, source or derivation. Flat numbers are rejected.
7. If a check fails, one correction attempt with the verifier's feedback. If it still fails, show the verified result only (or nothing) and log the case for review. Never show the failed draft as an answer.
8. Report the check actually run and its observed result.

## Outputs
Deliverable with sourced facts, a list of flags, and a verification note for the internal twin.

## Gates
- No source, no claim.
- Conflicting evidence is a defect to resolve, never averaged.
- Clean gates over LOW-confidence input still yield a LOW-confidence deliverable.
- The model never signs off its own number.
- Freshness: every input carries its age. Stale input is refused when a freshness window applies.

## Anti-patterns
Estimating "to be helpful". Reusing a number from memory. Letting a document's own summary replace reading the rows. Treating a model's confidence as evidence.
