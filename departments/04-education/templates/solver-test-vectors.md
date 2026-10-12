# Solver Test Vectors (shared file format)

One vector file is run by every solver implementation. Format: one record per vector.

| Field | Meaning |
|---|---|
| id | unique vector id |
| kind | numeric / equation / simplification |
| expression or equation | text as the learner would type it |
| variable | unknown for equations |
| proposed | candidate answer to check |
| expect | verified / refuted / unverifiable |
| expect_overrides | per-engine expected result, if any |
| divergence_reason | required whenever an override exists; override may only be stricter |

## Required families
- Exact arithmetic (fractions, negatives, precedence, parentheses)
- Linear equations (one solution, none, infinite)
- Quadratics (two roots, repeated root, no real roots)
- Simplification (canonical polynomial equivalence)
- Malformed input (must be unverifiable, never verified)
- Out-of-domain input (must be unverifiable)
- Adversarial near-misses (almost-right answers must be refuted)

## Example row
{{VECTOR_ID}} | equation | {{EQUATION_TEXT}} | {{VARIABLE}} | {{PROPOSED}} | {{EXPECT}} | none | none
