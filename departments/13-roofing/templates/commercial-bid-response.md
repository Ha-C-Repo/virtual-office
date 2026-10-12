# Commercial Bid Response

Bid {{BID_ID}} | Owner / building {{BUILDING_REF}} | Due {{BID_DUE}} | Pre-bid walk {{PREWALK_DATE}} | Addenda acknowledged {{ADDENDA_LIST}}
Prepared by {{BID_MANAGER}} | Owner decision to bid {{OWNER}} {{DATE}}

## Requirements matrix
| Requirement | Required | We meet (y/n) | Evidence |
|---|---|---|---|
| Years of experience | {{REQ_YEARS}} | {{YES_NO}} | {{EVIDENCE}} |
| Manufacturer-approved applicator / certifications | {{REQ_CERTS}} | {{YES_NO}} | {{EVIDENCE}} |
| Insurance limits / bonding | {{REQ_INSURANCE}} | {{YES_NO}} | {{EVIDENCE}} |
| Substitution controls | {{REQ_SUBS}} | {{YES_NO}} | {{EVIDENCE}} |
| Warranty term and type (NDL / prorated / material only) | {{REQ_WARRANTY}} | {{YES_NO}} | {{EVIDENCE}} |
| Safety submittals | {{REQ_SAFETY}} | {{YES_NO}} | {{EVIDENCE}} |
| Schedule | {{REQ_SCHEDULE}} | {{YES_NO}} | {{EVIDENCE}} |

## Site conditions
Existing system {{EXISTING_SYSTEM}} | Layers {{LAYERS}} | Drains, scuppers, curbs, parapets, penetrations {{DETAILS}} | Moisture survey {{SURVEY_REF}} (verified by probes or cores {{YES_NO}}) | Access and edges {{ACCESS}}

## Proposed system
{{SYSTEM}} (TPO / PVC / EPDM / mod-bit / coating) with insulation {{INSULATION}}, cover board {{COVER_BOARD}}, attachment {{ATTACHMENT}}. Manufacturer constraints checked {{YES_NO}} (VERIFY).

## Quantities and price
Roof area {{AREA}} | Basis {{TAKEOFF_REF}} | Base bid {{BASE_BID}} | Alternates {{ALTERNATES}} | Unit price for wet insulation replacement {{WET_INSULATION_UNIT_PRICE}} | Margin check {{MARGIN_PCT}} (`python ../harnesses/job_cost.py price --cost {{COST}} --margin {{MARGIN_PCT}}`)

## Exclusions and clarifications
{{EXCLUSIONS}}

## Safety
Fall protection plan outline {{FALL_PLAN_REF}} | Hot work controls {{HOT_WORK}} | Drone survey pilot certified {{YES_NO}}

Signed by {{OWNER}} ____ date ____ | Submitted {{SUBMITTED_AT}} | Result {{RESULT}}
