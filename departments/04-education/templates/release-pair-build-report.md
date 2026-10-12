# Release Pair

## Part 1: Public (scrubbed)
Version {{VERSION}} | Release notes: see `release-notes.md` | Listing copy: see `store-listing.md`

## Part 2: Internal build report (never public)
Version {{VERSION}} (must equal Part 1)
Commit reference {{COMMIT_REF}}
Test counts: unit {{UNIT_COUNT}} | instrumented {{INSTRUMENTED_COUNT}} | vectors {{VECTOR_COUNT}} | failures {{FAILURES}}
Stability: crash-free {{CRASH_FREE_RATE}} | ANR {{ANR_RATE}}
AI spend this build cycle: {{AI_SPEND}}
Known issues: {{KNOWN_ISSUES}}
Parity result (two solver implementations): {{PARITY_RESULT}}
QA sign-off: {{QA_SIGNOFF}} on {{DATE}}

## Cross-leak scan
Result {{PASS_FAIL}}. Any internal field found in Part 1 is a FAIL.
