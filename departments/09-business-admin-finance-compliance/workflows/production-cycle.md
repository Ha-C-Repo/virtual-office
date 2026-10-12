# Three-Phase Production Cycle

## Phase 1: Assess the batch by hand
Human does this; the AI prepares the checklist only.
1. Precondition checks on environment readings (within targets and freshness window).
2. Readiness percentage against the work plan.
3. Lineage pull from the lineage record.
4. PPE and SOP check (`../skills/sop-repository/SKILL.md`).
5. {{OPERATOR_ROLE}} hand-writes the work plan.
GATE: no execution without a written work plan.

## Phase 2: Execute and log output
1. Staff perform the work.
2. Records keeper logs the session: asset tags, hold-until dates, grid positions (`../skills/inventory-reconciler/SKILL.md`).
3. Readings and incidents logged to their registers.

## Phase 3: Commercial release and reconciliation
1. Hold clock runs; only the clock releases it.
2. Listing built after release, with photo and confirmed identification.
3. Pricing follows the lifecycle schedule: release, markdown, liquidation flag.
4. Count verified; register, physical and sales reconciled (`weekly-yield-audit.md`).

## Sign-off
{{OWNER_ROLE}} approves the work plan and any exception to the lifecycle schedule.

## Standard AI task pattern
Narrow task, background context, process to follow, output template.
