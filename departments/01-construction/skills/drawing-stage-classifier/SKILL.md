---
name: drawing-stage-classifier
description: Classifies a drawing set as issued-for-construction, construction documents, design development or schematic/budget and maps it to the locked risk adder and contingency.
---
## When to use
Immediately after drawing-reading and before pricing.

## Inputs
Sheet index, title blocks, revision clouds, issue notes, presence of schedules and details.

## Steps
1. Read title block issue labels and revision history on every structural sheet.
2. Check indicators: member schedules present, connection details present, foundation and anchor plans present, general notes complete.
3. Assign one stage: IFC (issued for construction), CD (construction documents), DD (design development), SD (schematic / budget).
4. Look up the stage adder and contingency in the locked rate table. Do not choose them yourself.
5. If indicators conflict (for example IFC label but no schedules), classify at the lower stage and record why.

## Outputs
`drawing_stage`, `stage_adder_pct`, `contingency_pct`, reasoning line.

## Gates
Stage and adder appear on the internal margin report cover and never on the client document. A stage change on revision triggers a re-price.
