---
name: {{SKILL_NAME_KEBAB_CASE}}
description: {{ONE_TO_TWO_SENTENCES_WHAT_IT_DOES_AND_WHEN_TO_LOAD_IT}}
---

# {{SKILL_TITLE}}

## When to use
{{TRIGGERS_AND_REQUEST_TYPES}}. Do not use for: {{EXCLUSIONS}}.

## Inputs
- {{INPUT_AND_WHERE_IT_COMES_FROM}}

## Steps
1. {{STEP}}
2. {{STEP}}
3. Tag confidence on every extracted fact; route LOW to a human.

## Outputs
- {{OUTPUT_AND_TEMPLATE_PATH}}

## Gates
- {{GATE_THAT_CAN_FAIL}}
- Human sign-off: {{WHO_AND_WHEN}}

## When data is missing
Return `NEEDS_INPUT: <what, from whom>`. Never fill a gap.

## Red flags and dealbreakers
- {{RED_FLAG}}

## Anti-patterns
- {{ANTI_PATTERN}}

## Related
Skills: {{SKILLS}}. Templates: {{TEMPLATES}}. Workflows: {{WORKFLOWS}}.

## Test record (for promotion)
Good case 1: {{RESULT}}. Good case 2: {{RESULT}}. Bad case (must fail correctly): {{RESULT}}.
