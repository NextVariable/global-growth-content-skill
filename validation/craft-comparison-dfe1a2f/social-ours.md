## Professional post
Month-end reconciliation starts with a question: which order records need a closer look?

MatchRows aligns two CSV files by order ID and lists different statuses or records found on only one side. The list directs your review; it does not establish a missed payment. Return to the original records before deciding what happened. The tool does not write changes back.

See the accompanying workflow note.

## Technical thread
1. Two CSV files disagree. Start by checking whether order ID is a valid matching key for these inputs. MatchRows uses that key to align records.
2. Inspect different statuses and records present on only one side. One-sided in these inputs is not proof that an order is absent from the underlying system.
3. Verify against the original records before drawing a payment conclusion. MatchRows does not write back or decide missed payments. See the accompanying workflow note.
