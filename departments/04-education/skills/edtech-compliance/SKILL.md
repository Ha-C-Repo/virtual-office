---
name: edtech-compliance
description: Children's-privacy decision tree for any feature that touches learner data.
---
# EdTech Compliance Decision Tree

## When to use
Whenever a feature, SDK, permission or analytics event might collect, store or transmit learner data.

## Inputs
Feature description, data elements involved, the audience (age bands), data-minimization map (`../../templates/design-spec-privacy.md`).

## Steps
1. Do we need to collect this at all? If not, do not.
2. Can it stay on the device? If yes, keep it there and record it in the map.
3. Must it leave the device? State why, where it goes, retention, deletion path.
4. Could the user be under 13? Off-device collection then needs verifiable parental consent (COPPA). Prefer designs that avoid it.
5. School context? Raise education-records questions (FERPA) for the owner and counsel.
6. Audience rules: if the app is for children, no behavioral advertising and no third-party analytics SDKs.
7. Age screen: neutral (no preset, no hint) and only if a feature needs it.
8. Update the map: data, where created, where stored, whether it leaves the device, why.

## Outputs
Decision record per feature and an updated data-minimization map.

## Gates
Any unresolved children's-data question blocks the feature. Owner and counsel decide.
