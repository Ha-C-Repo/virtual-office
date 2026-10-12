---
name: spec-maturity-classifier
description: Classify a spec as napkin, draft, final or frozen and apply the matching contingency to estimates.
---
# Spec Maturity Classifier

## When to use
When estimating effort or deciding whether work can start.

## Classes
- Napkin: idea only. Highest contingency. Do not build.
- Draft: sections present, open questions remain. High contingency.
- Final: complete, reviewed, owner approved. Low contingency.
- Frozen: locked for a release. Zero contingency; changes need an amendment.

## Steps
1. Read the spec and its open-question log.
2. Assign a class with a one-line reason.
3. Apply contingency of {{CONTINGENCY_PCT_BY_CLASS}} to estimates.
4. Flag any build task that targets a napkin or draft spec.

## Outputs
Class, reason, contingency applied.

## Gates
Only final or frozen specs are implemented. Frozen specs change only by owner-approved amendment.
