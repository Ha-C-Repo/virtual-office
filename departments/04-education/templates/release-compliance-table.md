# Release Compliance Table

Release {{VERSION}} | Auditor {{AGENT_ROLE}} | Date {{DATE}}

| # | Check | Expected | Observed (evidence) | Pass / Fail |
|---|---|---|---|---|
| 1 | Audience rules | {{EXPECTED}} | {{EVIDENCE}} | {{RESULT}} |
| 2 | Permissions | network, camera only | {{EVIDENCE}} | {{RESULT}} |
| 3 | Data-safety declaration vs measured behavior | match | {{EVIDENCE}} | {{RESULT}} |
| 4 | Content rating | consistent | {{EVIDENCE}} | {{RESULT}} |
| 5 | Integrity (no ghostwriting language) | none | {{EVIDENCE}} | {{RESULT}} |
| 6 | Ads / analytics / vendor runtime on classpath | none | {{EVIDENCE}} | {{RESULT}} |
| 7 | Privacy policy live and consistent | yes | {{EVIDENCE}} | {{RESULT}} |
| 8 | App-data backup disabled | yes | {{EVIDENCE}} | {{RESULT}} |
| 9 | Delete-all leaves no residue | yes | {{EVIDENCE}} | {{RESULT}} |
| 10 | Release pair passed | yes | {{EVIDENCE}} | {{RESULT}} |

Overall: {{PASS_FAIL}}. Any FAIL blocks the release. Owner sign-off {{DATE}}.
