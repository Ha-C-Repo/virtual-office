---
name: spec-completeness-check
description: Check a product spec for all required sections and testable criteria, and reconcile it against the source request.
---
# Spec Completeness Check

## When to use
Before a spec moves from draft to final, and before planning begins.

## Inputs
Spec (`../../templates/product-spec.md`), original request.

## Steps
1. Confirm each required section exists and is not empty: user story; numbered acceptance criteria; offline behavior; error and empty states; analytics events (counts only); privacy impact; solver/verification path; test plan; out-of-scope; open questions.
2. Each AC is testable: a test can pass or fail it without judgment.
3. Reconciliation table: each request item marked Covered, Missing or Ambiguous.
4. Missing or ambiguous items become open questions.

## Outputs
Completeness report and reconciliation table.

## Gates
A spec with Missing sections cannot be marked final.
