# Workflow: Outward Deliverable Chain

Applies to anything that leaves the office: documents, emails, listings, posts, replies, proposals, reports, filings.

## Chain
| # | Step | Who | Gate / sign-off |
|---|---|---|---|
| 1 | Draft from an approved template using verified facts only. | Author agent | `../skills/verify-dont-generate/SKILL.md` |
| 2 | Create the internal twin (-INT). | Author agent | `../skills/two-document-rule/SKILL.md` |
| 3 | Voice check. | Voice firewall | BLOCK stops the chain |
| 4 | Four-pass review: calculation cross-check, completeness and sourcing, leak scan, layout. | QA editor | PASS / FIX-AND-RERUN / BLOCK |
| 5 | Compliance review: Tier 1 rules, advertising, consent, privacy, disclosures. | Compliance reviewer | PASS / FIX-AND-RERUN / BLOCK; route to third party if needed |
| 6 | Anonymization scrub on the outward piece. | Scrubber | PASS / AUTO-FIX / BLOCK |
| 7 | Pair check: outward and twin exist and match. | QA editor | Missing twin = BLOCK |
| 8 | Approval package (`../templates/approval-request.md`). | Coordinator | |
| 9 | HUMAN SIGN-OFF. | Owner role | Explicit, version-specific, logged |
| 10 | Export in the final format and send or publish at human pace. | Human | Silence is not approval |
| 11 | Log: register row, correspondence log, permalink or reference. | Records keeper | |
| 12 | One-line delivery summary: what shipped, headline number, confidence tier, open flags. | QA editor | |

## Rules
- A template pass never pre-clears a filled copy. Every filled copy goes through the chain.
- Any edit after step 9 voids approval and returns to step 3.
- A gate that is SKIP is a hole; resolve it before release.
- Refusals are logged, not hidden.
- If any step is repeated three or more times by hand, nominate it for promotion (`../skills/skill-promotion-pipeline/SKILL.md`).
