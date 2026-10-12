---
name: compliance-verification-before-completion
description: Gate order to run before reporting any work done, with honest reporting of what was observed.
---
## Order
1. Facts audit: every fact sourced.
2. VIN verify.
3. Sanity gates: price corridor, photo standard, buyer's guide, defects present and photographed.
4. Compliance check on all outward copy in marketing context.
5. Client and `-INT` pair validation.
6. Practice-run regression, if gate code or skills changed.
7. Skills audit, if a skill changed.

## Rules
- Report the exit code actually observed.
- Cross-check output against input; sample high-risk numbers more than once; tag confidence; route LOW to a human.
- The model never signs off its own number.
- Clean gates over LOW input is still a LOW deliverable.
