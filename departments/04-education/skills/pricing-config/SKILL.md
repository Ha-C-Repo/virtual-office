---
name: pricing-config
description: Locked business-configuration workflow: all pricing values start zeroed, set only by the owner with a named source.
---
# Pricing Config

## When to use
Whenever tiers, prices, limits, trial length or cost ceilings are defined or changed.

## Inputs
Owner decision, `../../templates/business-config.md`.

## Steps
1. All values start at zero or TODO. The assistant never fills them.
2. The owner supplies each value with a named source and effective date.
3. Record approval line (who, when).
4. Run `../pricing-sanity-check/SKILL.md` before any value goes live.
5. The metering scaffold reads the config. Limit disabled sentinel means unlimited. Metering fails open (the opposite of the solver) because it is a business control, not a safety control.

## Outputs
Config file with every field set or explicitly TODO.

## Gates
No payment path exists until the owner approves one. Pricing in public copy must match the config.
