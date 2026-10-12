# Design Spec: Answer Verification

## Goal
No answer is shown as certified unless a deterministic solver agrees.

## Domain
Verified domain: {{VERIFIED_DOMAIN}} (for example numeric expressions, one equation in one unknown, simplification). Everything else is out-of-domain and labeled "not checked".

## Check plan
Built from the learner's own text. Never from the model output.

## Contract
| Input | Output |
|---|---|
| kind, expression or equation, variable, proposed answer | verdict (verified / refuted / unverifiable), detail, roots, audited flag |

## Fail-closed rules
Parse error, timeout, unsupported syntax, audit write failure: all map to unverifiable.

## Verdict routing
verified -> CERTIFIED | unverifiable -> UNCHECKED (LOW) | refuted -> one retry, then SOLVER_ONLY | provider offline -> SOLVER_ONLY or FAILED

## Audit record
timestamp, entry_point, inputs, status, detail, implementation

## Parity
Two independent implementations run one shared vector file. Divergence is allowed only toward stricter.

## Fact-base plan for non-math subjects
Source list {{FACT_SOURCES}}; citation required for every claim; claims without a source are unverifiable.

## Test plan
Vector families, wrong-answer-cannot-ship test, retry-bound test (call counting).

## Open questions
{{OPEN_QUESTIONS}}
