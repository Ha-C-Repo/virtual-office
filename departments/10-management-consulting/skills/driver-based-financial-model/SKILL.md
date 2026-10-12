---
name: driver-based-financial-model
description: Build a financial model from operational drivers with three scenarios and a two-variable sensitivity table.
---
# Driver-Based Financial Model

## Steps
1. Choose the five to ten drivers that explain results (volume, price, mix, utilization, headcount, payment terms).
2. Tie each driver to a client data source; tag assumptions.
3. Build revenue, cost and cash flow from the drivers, month by month for {{MODEL_MONTHS}} months.
4. Scenarios: downside, base, upside, each defined by driver values.
5. Sensitivity: a two-variable table on the two drivers that matter most.
6. Reconcile the base year to the client's actual statements.
7. Write a one-page reading guide in plain language.

## Gates
Reconciliation difference above {{TOLERANCE}} blocks release. Models are not valuations or forecasts of guaranteed outcomes.
