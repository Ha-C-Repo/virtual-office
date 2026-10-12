---
name: release-pair-check
description: Verify that each release has a public notes/listing copy and an internal build report with the same version and no cross-leak.
---
# Release Pair Check

## When to use
At the end of every release candidate.

## Inputs
Public release notes and listing copy, internal build report (`../../templates/release-pair-build-report.md`).

## Steps
1. Both artifacts exist and show the same version.
2. Internal report contains: version, commit reference, test counts, stability data, AI spend, known issues, QA sign-off.
3. Cross-leak scan: public copy has none of the internal fields (spend, vendor names, stability internals, integrity mechanics).
4. Internal report does not omit known issues that the public notes claim are fixed.
5. FAIL on any miss. Exit code non-zero blocks.

## Outputs
Pair report (pass/fail with lines).

## Gates
No release without a passing pair.
