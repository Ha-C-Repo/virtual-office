---
name: reserve-sweep
description: Prepares the Friday capital-reserve sweep instruction: a set percentage of gross revenue moved to reserve until a cap is reached.
---
# Reserve sweep

## When to use
Every Friday.

## Steps
1. Read gross revenue for the week from the sales register (cite the audit week).
2. Apply the configured sweep percentage ({{SWEEP_PERCENT}}).
3. Check the current reserve balance against the cap ({{RESERVE_CAP}}). If the cap is reached, the sweep is zero and the log says so.
4. Write the sweep instruction and the log line (week, gross, percent, amount, balance after, status).
5. Present to {{OWNER_ROLE}}.

## Outputs
Sweep instruction and log row (`../../templates/reserve-sweep-log.md`).

## Gates
The skill never moves money. Missing revenue data returns a flag. Stale sales data (older than the freshness window) is refused.
