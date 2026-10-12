# Run State: {{PROJECT_NAME}}

- Wave: {{WAVE_NUMBER}}
- Started: {{START_TIME}}
- Approved batch: {{BATCH_SCOPE}}

## Pending
{{PENDING_NODES}}

## Running
| Node | Started | Expected finish (mean + 1 stddev) |
|---|---|---|
| {{NODE_ID}} | {{START_TIME}} | {{EXPECTED_FINISH}} |

## Completed
{{COMPLETED_NODES}}

## Failures
| Node | Time | Error | Retries | Action |
|---|---|---|---|---|
| {{NODE_ID}} | {{TIME}} | {{ERROR_TEXT}} | {{RETRY_COUNT}} | {{ACTION}} |

## Timing memory (seconds per node type)
| Node type | Samples | Mean | Stddev | Last updated |
|---|---|---|---|---|
| {{NODE_TYPE}} | {{SAMPLES}} | {{MEAN}} | {{STDDEV}} | {{DATE}} |

Circuit breaker: stop after {{MAX_ERRORS}} consecutive errors and ask a human.
