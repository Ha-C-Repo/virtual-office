# Unit Record: {{STOCK_NUMBER}}

The spine. Nothing else works until this record is correct. Every fact carries a source and a confidence tag: HIGH (title, odometer statement, independent inspection), MED (auction condition report, service record, recall, warranty paperwork), LOW (seller statement, photo inference). Never classify hearsay as an inspection. Decode failure is a recorded gap, not a guess.

## Identity
Stock number (unique): {{STOCK_NUMBER}}
VIN: {{VIN}}   VIN reconciled against documents and photos: {{YES_NO}}
Year / make / model / trim: {{YEAR}} {{MAKE}} {{MODEL}} {{TRIM}}   (source: public VIN decode, HIGH)
Acquired from (permitted channel): {{ACQUISITION_CHANNEL}}   Date: {{DATE}}

## Facts
| Field | Value | Confidence | Source (file path) | Recorded |
|---|---|---|---|---|
| Odometer | {{MILEAGE}} | {{HIGH_MED_LOW}} | {{SOURCE_PATH}} | {{DATE}} |
| Title status | {{TITLE_STATUS}} | {{HIGH_MED_LOW}} | {{SOURCE_PATH}} | {{DATE}} |
| Owners / history | {{HISTORY}} | {{HIGH_MED_LOW}} | {{SOURCE_PATH}} | {{DATE}} |
| Equipment list | {{EQUIPMENT}} | {{HIGH_MED_LOW}} | {{SOURCE_PATH}} | {{DATE}} |
| Open recalls checked | {{RECALL_RESULT}} | {{HIGH_MED_LOW}} | {{SOURCE_PATH}} | {{DATE}} |

## Documents on file
Allowed types: title, odometer_statement, inspection_sheet, auction_condition_report, service_record, recall_notice, buyers_guide_prior, warranty_paperwork, seller_statement, photo.
| Type | Confidence | Path | Hash | Notes |
|---|---|---|---|---|
| {{DOC_TYPE}} | {{HIGH_MED_LOW}} | {{FILE_PATH}} | {{FILE_HASH}} | {{NOTES}} |

## Defects (ranked)
| Id | Category (structural / mechanical / cosmetic / wear) | Severity (critical / major / minor) | Description | Disclosed | Photographed | Recon closed |
|---|---|---|---|---|---|---|
| {{DEFECT_ID}} | {{CATEGORY}} | {{SEVERITY}} | {{DESCRIPTION}} | {{YES_NO}} | {{YES_NO}} | {{YES_NO}} |

## Grade and status
Grade: {{A_INSPECTED / B_DECLARED / C_AS_IS_UNVERIFIED}} (from evidence on file; any open recon item downgrades an otherwise-A unit; conflicting evidence is resolved, never averaged)
Status: {{INTAKE / RECON / FRONT_LINE_READY / LISTED / SOLD / DELIVERED}}
Recommended price: {{RECOMMENDED_PRICE}}   Floor: {{FLOOR_PRICE}}   (from `inventory-comp-grid.md`; owner sets the price: {{OWNER_PRICE}})
Next action and owner: {{NEXT_ACTION}} / {{ROLE}}
