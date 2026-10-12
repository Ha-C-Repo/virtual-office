---
name: spreadsheet-formula-auditor
description: Diagnoses broken formulas in finance workbooks and proposes fixes only; the owner approves changes.
---
# Spreadsheet formula auditor

## When to use
When a yield, cost or invoice workbook shows wrong totals or errors.

## Checks
Reference errors; circular references; SUM ranges that stop short of the data; hardcoded rates inside formulas; mismatched ranges between numerator and denominator; mixed units; hidden rows included or excluded unexpectedly.

## Steps
1. Read the workbook structure and list formulas by sheet.
2. Run the checks. Record cell, problem, suggested fix.
3. Recompute the suspect total by an independent path.
4. Present proposed fixes; do not edit.

## Outputs
Audit table: cell, issue, evidence, proposed fix.

## Gates
Proposes only. {{OWNER_ROLE}} approves and a backup is taken before any change.
