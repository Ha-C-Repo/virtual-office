# Life Story (Memoir) Pipeline (16 steps, 11 gates)

Subject = author of record. Humans lead interviews and sign gates. See `../agents/memoir-archivist-editor.md`.

| # | Step | Skill | Gate |
|---|---|---|---|
| 1 | Intake and decline screens | `../skills/memoir-intake-and-scope/SKILL.md` | G1 |
| 2 | Consent pack executed | `../skills/memoir-consent-pack/SKILL.md` | G2 |
| 3 | Subject requests their own data exports | consent pack | |
| 4 | Raw-intake manifest with hashes and provenance; raw sealed read-only | `../skills/memoir-ingest-and-privacy/SKILL.md` | G3 |
| 5 | Deterministic parse (no model) | ingest | |
| 6 | Dedup, cluster, place resolution (no model) | ingest | |
| 7 | Sensitivity tiering and deny-list. No model call before this passes | ingest | G4 |
| 8 | Timeline v1 with provenance and confidence | ingest | |
| 9 | Voice profile stratified by register; Stage 0 calibration PASS or CORPUS-INADEQUATE | `../skills/memoir-voice-profile/SKILL.md` | G5a |
| 10 | Gap analysis (domain by era matrix) | `../skills/memoir-interview-protocol/SKILL.md` | |
| 11 | Human-led clarification interviews | interview protocol | G5b |
| 12 | Architecture: timeline v2, outline, one-sentence subject of the book | `../skills/memoir-drafting-and-assertion-audit/SKILL.md` | |
| 13 | Draft one chapter at a time with passage authorship ledger | drafting; loop in `memoir-drafting-loop.md` | |
| 14 | Verify: voice-fidelity report and assertion audit | drafting and anti-slop | G5c |
| 15 | Clearance: persons register, permissions, outside legal read | `../skills/persons-and-clearance/SKILL.md` | G6, G7, G8 |
| 16 | Deliver or publish: consents still current, copyright review, disclosure per format | `release-and-disclosure.md` | G9, G10, G11 |

## Human sign-offs
{{OWNER}} signs G1, G2, G8 and G11. The subject signs consent, reviews interview notes and approves each chapter. A qualified outside reviewer performs the legal read.

## Deliverable tiers
T0 timeline, T1 story map, T2 drafted manuscript, T3 private family edition, T4 public release. Stop at the tier the subject chose. T3 and T4 require full clearance.

## Stop conditions
Consent withdrawn, exposure event, Stage 0 inadequate with no fallback accepted, unresolved counsel-required item. Stop, seal, and escalate.
