# Design Spec: Privacy and Compliance

## Audience
Age bands {{AGE_BANDS}}. Under-13 users possible: {{YES_NO}}.

## Posture
Offline-first, no accounts, no ads, no analytics SDKs, no contacts, no location, no advertising ID. App-data backup disabled.

## Data-minimization map
| Data | Created where | Stored where | Leaves device? | Why |
|---|---|---|---|---|
| Typed problem text | {{WHERE}} | local history | {{YES_NO}} | sent to explanation provider |
| Photo of problem | camera | not stored beyond {{PHOTO_RETENTION}} | {{YES_NO}} | transcription |
| Grade band hint | profile | preferences store | {{YES_NO}} | tune reading level |
| Meter counter | meter | preferences store | no | usage limit |

## Feature flags for pending decisions
crop_first_photo_intake: {{ON_OFF}} | send_coarse_grade_band: {{ON_OFF}}

## Parental consent
Required if under-13 data leaves the device. Mechanism: {{CONSENT_MECHANISM}}.

## Age screen
Neutral (no preset, no hint). Added only if a feature requires it.

## Retention and deletion
Learner can delete one item or all history; delete-all leaves no residue (test). Provider retention: {{PROVIDER_RETENTION}}.

## Store data-safety groundwork
Declarations derived from measured behavior: {{DECLARATIONS}}

## Open questions for owner and counsel
{{OPEN_QUESTIONS}}
