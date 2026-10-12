# 03 Tender Ingest to Reconciliation (three-phase, human owns the thinking)

## Phase 1: understand scope
1. Estimator reads the tender package by hand and writes the clarification register (`../templates/clarification-register.md`) and the returnable pricing schedule (`../templates/returnable-pricing-schedule.md`).
2. `../skills/tender-ingest/SKILL.md` classifies and indexes documents.
3. `../skills/requirement-register/SKILL.md` extracts four buckets and cross-checks the human's registers. It lists what the human missed.
4. `../skills/contract-risk-review/SKILL.md` scores eleven risk types.

## Phase 2: direct costs
5. Assemblies are customized from the base library to the project. Takeoffs are exported and mapped to the estimate workbook.
6. Estimate lines with rate basis; unknown rates emit TBD placeholders and trigger supplier quotes.
7. The workbook carries an AI-instructions tab for any embedded assistant.

## Phase 3: indirects, offer and reconciliation
8. Duration-driven indirects.
9. `../skills/inclusions-exclusions/SKILL.md` writes the client-facing inclusions and exclusions.
10. Every tender requirement is either priced or explicitly excluded.
11. **Fresh-session reconciliation** (`../skills/bid-reconciliation/SKILL.md`) against the requirement register. GATE: verdict READY.
12. Hand to the bid pipeline for documents and sign-off (`01-bid-pipeline.md` step 10).
