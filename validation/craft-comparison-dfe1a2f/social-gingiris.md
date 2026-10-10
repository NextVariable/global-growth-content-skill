## Professional post
A reconciliation list is a starting point, not a payment verdict.

MatchRows compares two CSV files by order ID and lists status differences and one-sided records. Use those records to focus the next manual check against the original data. It does not write back or determine whether a payment was missed.

See the accompanying workflow note.

## Technical thread
1. What can two CSV files tell you about a reconciliation problem? MatchRows aligns them by order ID and surfaces status differences or one-sided records.
2. Read each result as a reason to check, not a conclusion. A record missing from one input may still exist in the underlying system.
3. Return to the original records for the payment decision. MatchRows does not write changes back. See the accompanying workflow note.
