# 04 Drawing Indexing

Owner: estimator-takeoff.

1. Split the merged PDF into one file per sheet at high resolution.
2. Extract the vector text layer per sheet. Flag sheets with no text layer (needs OCR; mark LOW).
3. Build the sheet-to-discipline classification index and the cross-reference matrix (detail callouts to sheets).
4. Count tagged items from vector text. State confidence. Never count from pixels.
5. Every record carries source sheet and reliability.
6. A human verifies LOW counts and every sheet marked unreadable.
7. Storage: a database plus connector for queries, or markdown drawing files; a hybrid is recommended. Keep sheet-to-record links either way.
8. Re-run on each new drawing revision and record the revision date.

GATE: takeoff does not start until the index is complete.
