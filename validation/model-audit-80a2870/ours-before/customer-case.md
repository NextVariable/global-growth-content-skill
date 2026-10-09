# Public customer case

# How NorthLedger used two CSVs to start its month-end checks

For NorthLedger, a bookkeeping firm represented here by an authorised pseudonym, month-end review meant comparing ecommerce orders with payment exports and returning to the original records when an order ID did not match. The firm previously used Excel formulas for that task.

In August and September 2026, a bookkeeper used ReconcilePad as part of this review. The workflow stayed focused on a specific question: which order rows have no matching order ID in the payment CSV? It did not treat that question as proof that money was missing.

## From an Excel comparison to a review list

The bookkeeper selected two UTF-8 CSV files and compared their `order_id` values as exact strings. ReconcilePad marked order rows without a matching payment ID and exported a discrepancy list. The bookkeeper then checked the listed items individually against the original records.

The August input contained 1,200 order rows, with 12 unmatched order IDs. The September input contained 1,250 order rows, with nine unmatched order IDs. The follow-up checks found late-arriving payments or differences in export timing among those unmatched items. No amount of missed payment was measured.

The useful output of the tool in this workflow was a list of places to begin investigating. Deciding what each difference meant remained the bookkeeper’s job.

## What the two reviews recorded

The implementation record reports 90 minutes for one bookkeeper’s August review of the list using the original template, and 60 minutes for that bookkeeper’s first September review of the list using ReconcilePad. These are observations from two different month-end reviews, not a controlled performance comparison.

Order structure, familiarity with the process and file coverage were not held constant. The records therefore do not establish that ReconcilePad caused the difference, or that other firms should expect the same result. They also do not measure the time needed to close the books.

As the bookkeeper put it:

> “The list tells me where to start checking; it does not close the books for me.”

## Where the workflow ends

ReconcilePad supports CSV alignment, marking missing matches and exporting the review list. It does not handle bank connections or refunds. The original records and human follow-up remain necessary for interpreting discrepancies and completing the bookkeeping work.

For another small Canadian bookkeeping firm, this case offers a process to examine: prepare order and payment CSVs, compare exact order IDs, export the unmatched rows and investigate the originals. It is evidence of a bounded implementation, rather than a promise of a particular saving or recovery amount.

**CTA: See the two-CSV workflow.**

Understand how an order export and a payment export become a list for manual review.

# Internal source and authorisation note

This is a synthetic frozen case for peer bookkeepers at the awareness stage. R1 authorises the NorthLedger pseudonym, the supplied data and the exact V1 quote; photographs are not authorised and no photo asset is included. The August and September implementation observations support the file counts, unmatched-ID counts and manual-check mechanism. L1 supports the stated 90/60-minute observations only, with uncontrolled conditions preserved. V1 is quoted exactly within its permission. Neither implementation evidence nor L1 establishes product-caused time savings, missed-payment recovery or results generalisable to other clients.

The CTA points conceptually to a workflow explanation; no destination, publication or customer identity verification is claimed. Do not use a “saves 33%” headline, customer photos, fabricated ledger automation or bank/refund features. Public clearance here means the supplied synthetic authorisation covers the included statements, not that a real customer approval or live publication was verified.
