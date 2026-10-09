# Public draft

**Title: NorthLedger's two-CSV month-end review with ReconcilePad**

**Description:** See how NorthLedger aligned order and payment exports, reviewed unmatched IDs and checked original records across two month-end reviews.

# NorthLedger's two-CSV month-end review with ReconcilePad

At the August and September 2026 month-ends, NorthLedger used ReconcilePad to align ecommerce order and payment CSVs, export unmatched order IDs and investigate the original records. NorthLedger is an authorised customer pseudonym in this synthetic case. The list directed the bookkeeper's checks; it did not complete the accounts or establish missing revenue.

## The task: review the exports before closing the month

NorthLedger's month-end task was to align an order CSV with a payment CSV. The earlier routine used Excel formulas. The bookkeeper needed to identify records that did not match, then determine what those differences meant by checking the originals.

For the two recorded month-ends, the order exports contained 1,200 rows in August and 1,250 in September. The workflow still depended on the coverage and timing of the files being compared. An unmatched ID was a starting point for investigation rather than a payment verdict.

## The implementation: exact matching, then human review

The bookkeeper supplied two UTF-8 files and matched their `order_id` values as exactly equal strings. ReconcilePad flagged order rows with no payment match and exported a difference list. The bookkeeper then checked the listed entries one by one in the original records.

ReconcilePad's role was limited to CSV alignment, missing-match identification and export. It did not process bank records or refunds. The investigative work stayed with the bookkeeper, who used the list to decide where to start.

> “The list tells me where to start checking; it does not close the books for me.”

## What the records show

August's comparison found 12 unmatched order IDs; September's found 9. Investigation found late arrivals or differences in export timing among those entries. The records did not measure the value of missed payments, and the unmatched counts cannot be presented as unpaid orders recovered.

The same bookkeeper's first review of the list took 90 minutes with the earlier template in August and 60 minutes with ReconcilePad in September. Those are observations from two different month-end reviews. Order structure, familiarity with the task and file coverage were not controlled, so the difference does not establish a product-caused saving or predict another firm's review time.

## What a peer firm can take from the workflow

The transferable mechanism is explicit: align the two exports by exact order ID, export the unmatched orders, and check each item against the source records. Before applying it to your month-end work, verify file coverage and identifier consistency. Keep responsibility for payment interpretation and account completion with the bookkeeper.

**CTA: See the two-CSV workflow**

# Internal sources and authorisation

This case uses only its R1 authorisation, the August/September implementation record, L1 timing observations and V1 approved quote. R1 allows the pseudonym, listed data and quotation. Photographs are not authorised and no photo asset is included. Dates, order counts, unmatched counts and 90/60-minute observations are synthetic frozen records, not independently observed customer research. The public copy labels the synthetic case and does not use a 33% saving headline, causal assertion or monetary recovery claim. gr-blog-post and content SOP supply narrative framing, but they cannot supply new first-person experiences, credentials, research or publication permission. No customer result was validated externally and no page was published.
