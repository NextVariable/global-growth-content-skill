# Update decision — internal

Update existing asset A1 at /guides/missing-payment-rows. The intended reader and task are the same, so a second article would duplicate the existing answer. The new draft replaces the incorrect unpaid-order and automatic-ID-fix claims, keeps the unaffected closing paragraph verbatim, and does not claim a deployed site update. No keyword-tool evidence is available.

# Complete public article

**Title:** How to find orders missing from a payment CSV

**Description:** Match two UTF-8 CSV exports by order ID in ReconcilePad, export unmatched order rows, and check the original records before interpreting a missing match.

## Find the order rows that need a closer look

At month end, an order may appear in your orders export without a matching entry in the payment export you are checking. That is a reason to investigate the original records. It is not proof that the order is unpaid.

ReconcilePad helps small Canadian ecommerce bookkeeping firms identify those rows. You select two UTF-8 CSV files, specify the order-number column in each, and match the IDs as exactly equal strings. The tool marks rows in the orders file with no payment match and exports a CSV for review. It does not modify your source files.

## Prepare the two exports

Choose the orders and payments exports that cover the period and records you intend to compare. Check the export coverage before interpreting a difference: a payment file that covers a different period may fail to match an order for reasons unrelated to whether payment was collected.

Inspect the order-number columns in both files. Keep IDs as text so that a value such as 001 remains 001. ReconcilePad does not remove spaces or repair leading zeros. A value of 001 will not equal 1, and an ID with an added space will not equal the same ID without it.

If an order ID is blank, repair the missing ID manually in the originating records and create a corrected export before relying on the match. If an ID appears more than once, return to the source records to determine why. The tool does not guarantee that it resolves duplicate IDs automatically.

## Match and export the review list

Select your orders CSV and payments CSV in ReconcilePad. Specify the column containing the order number in each file. Run the comparison, review the order rows with no matching payment ID, and export the review CSV. The UI's exact control names are not specified here.

For a minimal example, use these two files:

**orders.csv**

```csv
order_id
001
002
003
```

**payments.csv**

```csv
order_id
001
003
```

The expected review result contains order 002 because no payment row has an exactly equal order_id. The following illustrates the expected unmatched data; it does not claim a particular product-generated filename or additional output columns:

```csv
order_id
002
```

## Investigate the differences

For each exported row, check the original order and payment records and the coverage of the exports. Establish whether a timing difference, missing source entry or inconsistent ID explains the missing match. Do not mark the order unpaid solely because it appears in this list.

If an expected match is absent, inspect both IDs for spaces, changed leading zeros or other string differences. Correct the source data as appropriate and re-export it; ReconcilePad does not fix IDs automatically. If you cannot establish the correct ID, leave the item unresolved for manual review.

If a file cannot be used, check that it is a UTF-8 CSV and that you selected the correct order-number column. A comparison with the wrong column or incomplete export is not a trustworthy reconciliation. Duplicate or blank IDs require source-level investigation before you rely on the result.

ReconcilePad provides CSV alignment, missing-match marking and a review export. It does not handle refunds or connect to a bank API. Resolve those questions using the original records and your bookkeeping process.

**CTA: Try the two-CSV review workflow with the sample IDs above**

Keep original exports. A review list is a starting point for checking the original records, not your accounting ledger.
