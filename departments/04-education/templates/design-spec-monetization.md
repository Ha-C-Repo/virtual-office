# Design Spec: Monetization (decision pending)

Status: undecided. No payment path exists in the app. Owner decides.

## Options
| Option | Description | For | Against |
|---|---|---|---|
| A | {{OPTION_A}} | {{FOR}} | {{AGAINST}} |
| B | {{OPTION_B}} | {{FOR}} | {{AGAINST}} |
| C | {{OPTION_C}} | {{FOR}} | {{AGAINST}} |
| D | {{OPTION_D}} | {{FOR}} | {{AGAINST}} |

## Metering scaffold
Local counter plus config-driven limit. No payment path. Fails open. Meter increments on successful outcomes only; retries never count.

## Unit economics inputs
| Input | Value | Source | Status (MEASURED / UNMEASURED) |
|---|---|---|---|
| Photo share of problems | {{VALUE}} | {{SOURCE}} | {{STATUS}} |
| Vision cost per call | {{VALUE}} | {{SOURCE}} | {{STATUS}} |
| Explain cost per call | {{VALUE}} | {{SOURCE}} | {{STATUS}} |
| Retry share | {{VALUE}} | {{SOURCE}} | {{STATUS}} |
| Free allowance | {{VALUE}} | {{SOURCE}} | {{STATUS}} |
| Store fee share | {{VALUE}} | {{SOURCE}} | {{STATUS}} |

## Formulas
Cost per problem = photo share x vision cost + explain cost x (1 + retry share)
Free exposure = free users x allowance x cost per problem
Paid margin = price x (1 - store fee share) - usage x cost per problem

## Decision record
Chosen option {{CHOSEN}} | Approved by {{OWNER}} on {{DATE}} | Sanity check result {{RESULT}}
