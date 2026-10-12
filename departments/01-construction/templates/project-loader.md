# Project Loader ({{PROJECT_NAME}})

Small file read first by any session working on this job.

## Read in this order
1. Department rules: `knowledge/rules.md`
2. Project snapshot (dated {{SNAPSHOT_DATE}}): `{{SNAPSHOT_PATH}}`
3. Drawing index: `{{DRAWING_INDEX_PATH}}`
4. Memory file (append-only): `{{MEMORY_PATH}}`

## LIVE DOCUMENTS (always read the source, never a copy)
- Obligations register: `{{OBLIGATIONS_REGISTER_PATH}}`
- Correspondence register: `{{CORRESPONDENCE_REGISTER_PATH}}`
- Budget workbook: `{{BUDGET_WORKBOOK_PATH}}`
- Contract risk register: `{{RISK_REGISTER_PATH}}`
- Change order register: `{{CHANGE_ORDER_REGISTER_PATH}}`

## Current status
Phase: {{PROJECT_PHASE}}. Open items: {{OPEN_ITEMS}}.
