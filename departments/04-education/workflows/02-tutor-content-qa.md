# 02 Tutor Content QA

Owner: tutor-content-qa | Approver: {{OWNER}}

## Steps
1. Collect a sample: new regression set, curriculum QA log items, or a release candidate batch.
2. Run `../skills/tutor-content-qa/SKILL.md` on each item (correctness, step completeness, readability, explain-it-back).
3. GATE: missing practice variant or explain-it-back prompt = FAIL.
4. Triage failures: model prompt issue, solver domain gap, fact-base gap, readability issue.
5. Create a fix ticket per root cause; add a regression vector or sample for each fixed defect.
6. Re-run until clean.
7. SIGN-OFF: owner reviews the QA summary before any release candidate.

## Outputs
QA report, curriculum QA log update, new regression items.
