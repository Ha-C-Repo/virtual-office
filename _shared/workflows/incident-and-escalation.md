# Workflow: Incident and Escalation

Applies to: data exposure, a leaked internal number, a wrongly sent message, a compliance failure, a safety allegation, a failed gate that was bypassed, a security issue, a production outage.

## Severity
| Level | Meaning | Response |
|---|---|---|
| 1 | Harm to a person, safety allegation, legal threat, regulator contact, credential exposure | Owner role immediately; stop related work; counsel flag |
| 2 | Data exposure without known harm, wrong outward message, missed legal deadline | Owner role same day |
| 3 | Gate failure caught internally, near miss | Logged; fixed in the week |

## Steps
| # | Step | Who |
|---|---|---|
| 1 | Contain: stop the sending, publishing or processing. Do not delete evidence. | Whoever finds it |
| 2 | Escalation note (`../templates/escalation-note.md`), band WAIT. | Coordinator |
| 3 | Preserve: snapshot affected files and logs to a timestamped backup. | Records keeper |
| 4 | Record the exposure event: what, route, which archive implicated, solicited or not, containment, retention, who was told. | Records keeper |
| 5 | Owner decides on notices to affected parties and authorities. AI drafts only. | Owner role |
| 6 | Fix the cause. Use a verification step before declaring closed; prove the fix, do not assume it. | Lead department |
| 7 | Postmortem: facts, timeline, cause, lesson, process change. Blameless, factual. | Coordinator |
| 8 | Update the rule, SOP, skill or gate that failed. Add a regression case so it cannot recur. | QA editor |
| 9 | Close with evidence and a changelog line. | Records keeper |

## Rules
Never contact the affected party or a regulator without owner approval. Never reproduce a secret in any report; give its location only. Credentials involved are rotated by a human.
