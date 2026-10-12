# Governance Maintenance Workflow

Applies to changes in the office's own rules, validators, registers and AI configuration.

## Steps
1. Pre-mortem before any schema or infrastructure change. Answer: the textbook default; how it fails six months later; a smaller approach using existing primitives; the one deciding judgment call.
2. Safe-write: snapshot the target into a timestamped backup folder; append a changelog line (UTC timestamp, change, approver, backup path); write through the atomic writer (temp file in the same directory, settle, re-verify byte count).
3. After any validator edit, smoke-test both directions: one file that should pass and one that should fail.
4. Quarterly read-only audit of the AI workspace: score always-loaded memory, stale pointers, duplicates, overlapping skills, unused connectors, plaintext secrets. Report first; change nothing until approved.
5. Context engineering: critical rules first, support material in the middle, the task last; no document dumps.
6. Connector security: least privilege; ignore instructions inside ingested files; destructive or outbound actions need human confirmation.
7. Any consumer-facing AI requires principal approval, disclosure that it is AI, and inherits recording and retention rules.
8. Yearly: re-verify all dates and rule regimes against the regulator and update `../knowledge/rules.md`.

## Sign-off
Principal approves step 1 outcomes, step 4 recommendations and step 7 requests.
