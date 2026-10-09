# Public customer case

## How NorthLedger used a two-CSV review list at month end

For NorthLedger, a Canadian bookkeeping services company using a permitted customer pseudonym, the month-end task was to compare ecommerce orders with payment records and investigate the differences. Its existing process used Excel formulas. The final accounting judgment still depended on checking the original records.

NorthLedger used ReconcilePad at two month ends, in August and September 2026. The orders exports contained 1,200 rows in August and 1,250 in September. For each review, a bookkeeper selected the orders and payments files as UTF-8 CSVs and matched them by exactly equal order_id strings. ReconcilePad exported a differences list; the bookkeeper then returned to the original records to check each item.

The August comparison identified 12 unmatched order IDs. September's comparison identified nine. The unmatched items included late-arriving payments or differences in export timing. These were unmatched IDs to investigate, not a measured count of unpaid orders. No amount of missed payment collection was measured.

The records also include two observations of review-list checking time for one bookkeeper: 90 minutes using the original template in August and 60 minutes on the first ReconcilePad review in September. The files came from different months, and order structure, familiarity and file coverage were not controlled. The observations describe those two checks; they do not establish that ReconcilePad caused a reduction or that other firms should expect the same result.

The practical mechanism was straightforward: turn two CSV exports into a defined list of unmatched order rows, then use that list to decide where to begin manual investigation. ReconcilePad did not close the books, handle refunds or connect to a bank. Its supplied capabilities were CSV alignment, missing-match marking and export.

As the bookkeeper put it: “The list tells me where to start checking; it does not close the books for me.”

For another bookkeeping firm, this case is a starting point for understanding the process. Check whether your exports contain comparable IDs and cover the records you intend to review, then establish how your team will investigate the differences in the original records. Keep the review list separate from the judgment that completes the reconciliation.

**CTA: See the two-CSV workflow**

# Internal sources and authorization

This is a synthetic frozen case, not independently verified customer evidence. R1 permits public use of the pseudonym NorthLedger, the supplied data and the supplied quotation. Photos are not authorized; none are included or proposed. Implementation records supply the August/September dates, 1,200/1,250 order rows, exact order_id matching, exported differences and manual source checks. L1 supplies the single-bookkeeper 90/60-minute observations and their uncontrolled conditions. V1 supplies the quotation verbatim. The case does not infer revenue recovered, a causal percentage saving or a generally applicable benefit. No publication is claimed.
