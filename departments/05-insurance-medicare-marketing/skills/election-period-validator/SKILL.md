---
name: election-period-validator
description: Determines which Medicare election periods apply to a client situation and date, with citation and confidence.
---
# Election-period validator

## When to use
Before advising that a client can enroll or change plans at a given time.

## Inputs
Client situation (age or eligibility date, current coverage, dual-eligible or low-income-subsidy status, move or institutional status, loss of coverage), and the date.

## Steps
1. List candidate periods: initial, initial coverage, annual enrollment (October 15 to December 7), Medicare Advantage open enrollment (January 1 to March 31), institutional, special election periods.
2. For each, state the window, the regulatory citation, and a confidence tag.
3. Check dual-eligible and low-income-subsidy special rules.
4. If the case is ambiguous, route to the carrier or the federal help line. Never guess.

## Outputs
Table: period, window, citation, confidence, next step.

## Gates
Re-verify rules yearly against the regulator. Do not market open enrollment as an extra enrollment opportunity; member-initiated inquiries and servicing are allowed.
