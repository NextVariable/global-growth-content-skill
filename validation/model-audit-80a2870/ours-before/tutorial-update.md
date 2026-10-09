# Updated article draft

**Existing asset:** A1, `/guides/missing-payment-rows`

**Title:** How to find orders missing from a payment CSV

**Description:** Compare two UTF-8 CSV exports by an exact order ID match, export unmatched order rows and check the original records before drawing payment conclusions.

# How to find orders missing from a payment CSV

An order row without a matching order ID in your payment CSV needs investigation. It does not, by itself, mean the order is unpaid. ReconcilePad can compare two UTF-8 CSV files using the order ID columns you specify and export the order rows that have no exact match in the payment file. You then check those rows against the original records.

This workflow is for bookkeepers at small Canadian ecommerce bookkeeping firms who need a review list from order and payment exports. ReconcilePad does not change the source files or repair IDs automatically.

## Prepare exports that can be compared

Keep the original Orders and Payments exports. Choose files for the period you intend to review, and check their coverage and export times before matching them. A difference between files can reflect what the exports contain rather than whether a payment exists.

Both files must be UTF-8 CSVs. Identify the order ID column in each file. ReconcilePad matches strings exactly: `001` matches `001`, but it does not automatically match `1`, `001 ` or another altered form. It does not remove spaces or change leading zeros. Avoid letting a spreadsheet convert the IDs before you compare them.

For a small demonstration, use these files:

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

The IDs are strings. The zeros in `001`, `002` and `003` are part of their values.

## Compare the files in ReconcilePad

Select the order and payment CSV files. Specify the order ID column for each file; in this example, both columns are named `order_id`. Run the comparison and inspect the order rows marked as having no payment-file match. Export the review CSV.

In this demonstration, the expected unmatched order ID is `002`: the payments file contains `001` and `003`, but no exact `002`. The expected content of the review list is:

```csv
order_id
002
```

This shows the expected unmatched data, not a claim about an unprovided UI button name or a fixed export filename. With the demonstration files, neither `001` nor `003` should be an unmatched order.

## Investigate the review list

For each unmatched row, return to the original order and payment records. Check whether the ID is written the same way, whether the exports cover the same information and whether a payment falls outside the exported period. Record your finding in your bookkeeping process. Do not label every unmatched row as an unpaid order based solely on the comparison.

ReconcilePad finds exact ID matches and marks missing matches. It does not determine whether a refund has been processed, connect to a bank API or correct an accounting ledger.

## Handle a comparison that does not look right

If order IDs are blank, repair the missing identifiers through your source-record process and produce a corrected export before relying on the comparison. A blank value is not a usable basis for deciding which order to investigate.

If an ID appears more than once, check the original records to understand the duplication. ReconcilePad does not guarantee automatic resolution of duplicate IDs. An ID match alone does not establish that duplicated rows or their amounts have been reconciled.

If you expected a match but see an unmatched row, compare the exact ID strings, including spaces and leading zeros. Correct the relevant source information or export through your normal process, preserving the original files, then compare again. ReconcilePad will not silently normalise those differences for you.

If the files have the wrong coverage, obtain exports appropriate to your intended review. If a file is not UTF-8 CSV, obtain a suitable export before using this workflow. These corrections happen outside ReconcilePad’s matching function.

Keep original exports. A review list is a starting point for checking the original records, not your accounting ledger.

**CTA: Try the two-CSV review workflow with the sample above.**

Compare the three order IDs against the two payment IDs, confirm that `002` is the unmatched row, then use the same checks when reviewing your own exports.

# Internal editorial decision and verification

Update A1 in place: the proposed “Fix missing payment CSV entries” title serves the same reader and problem, so it does not justify a new page. Keep the supplied slug as an asset identifier; no live URL or deployment is claimed. The revised title retains A1’s accurate task framing. The old unpaid-order conclusion and automatic-ID-fixing claim are replaced throughout, while the supplied final paragraph is retained verbatim.

The input F1 supports selection of two UTF-8 files, user-selected ID columns, exact string alignment, marking unmatched order rows, review export and no source-file modification. The example is reasoned from the supplied fixture values; no executable ReconcilePad implementation was provided or run. UI wording, actual export format beyond the expected data, indexing and ranking remain unverified. There is no keyword-tool evidence, so this is a task-based article update without search-volume or traffic claims. The reader can complete a comparison and investigate exceptions; the CTA needs no invented URL.
