# Public copy

# How NorthLedger used two CSV files to start its month-end checks

*An illustrative case based on a frozen synthetic implementation record. NorthLedger is an authorised pseudonym, not evidence of a real customer outcome.*

For a Canadian bookkeeping service company, matching ecommerce orders with payments is part of the month-end checking work. In this illustrative case, NorthLedger previously used Excel formulas to compare an order CSV with a payment CSV. The bookkeeping task remained the same when it used ReconcilePad: identify entries that need attention, then return to the original records to understand them.

## Two files, an exact match and a list to investigate

The implementation record covers the August and September 2026 month ends, with 1,200 order rows in August and 1,250 in September. A bookkeeper used two UTF-8 CSV files, matching the order and payment records exactly by `order_id`.

ReconcilePad aligned the CSV records, flagged missing matches and exported a discrepancy list. The bookkeeper then returned to the original records and checked the listed entries individually. That manual investigation was the step that gave the list meaning: an unmatched order identifier alone did not establish that a payment had been lost.

The August list contained 12 unmatched order identifiers; September’s contained nine. Late-arriving payments or differences in export timing were present among these entries. The record did not measure the amount of any missing receipts. The lower September count therefore cannot be read as an improvement in collections or proof that ReconcilePad reduced payment errors.

## What changed in the recorded checks

The same bookkeeper took 90 minutes to check the list with the original template in August and 60 minutes for the first list check using ReconcilePad in September. These are observations from two different month ends. Order structure, familiarity and file coverage were not controlled, so the difference does not establish a product-caused time saving or predict another team’s results.

What the case does show is the role of the exported list in the workflow. It directs the bookkeeper to records that need investigation while leaving the accounting judgement with the person doing the check.

> “The list tells me where to start checking; it does not close the books for me.”

The quotation is reproduced from the authorised synthetic case record.

## What a peer bookkeeping team can learn from the workflow

For a team already working with order and payment CSV files, the workflow is concrete: supply the two UTF-8 files, align records by an exact `order_id` match, export the discrepancies and investigate them in the source records. The coverage and timing of those exports matter to how the discrepancy list should be interpreted.

ReconcilePad’s scope in this case is CSV alignment, missing-match flags and export. It does not handle bank records or refunds, and it does not complete the books. The useful question for another bookkeeping team is whether that list fits its checking process—not whether these two month ends prove a general saving.

**CTA: See the two-CSV workflow**

# Internal sources and authorisation

This is a synthetic frozen case, explicitly labelled in the public copy. R1 permits the pseudonym NorthLedger, the supplied data and the approved quotation. It does not authorise photographs. Do not add a portrait, logo, named employee or identity details, or present this as independently verified real-world customer success.

The supplied implementation record supports the August/September 2026 dates, 1,200/1,250 order rows, UTF-8 inputs, exact order_id matching, exported discrepancy list and manual investigation in original records. It supports 12/9 unmatched order identifiers and the presence of late payments or export timing differences. It supplies no lost-payment amount or recovery result.

L1 supports the single-bookkeeper 90-minute August baseline and 60-minute September first check, with uncontrolled order structure, familiarity and file coverage. We retain both observations and the limitations together. No causal or generalisable “save 33%” statement is authorised by this record. V1 supplies the exact short quotation; R1 authorises its use. Product scope is only CSV alignment, missing-match flagging and export, with no banking or refund handling.

The CTA has no supplied URL. Configure a destination showing the described two-CSV process and verify its accuracy before publication. No files were imported into ReconcilePad and no live customer check was executed here; this task generated the case text from the supplied frozen record.
