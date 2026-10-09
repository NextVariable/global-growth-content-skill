# Public replacement draft for A1

**Title: How to find orders missing from a payment CSV**

**Description:** Compare order and payment CSVs by exact order ID in ReconcilePad, export unmatched orders and check the source records before drawing payment conclusions.

**Existing slug retained:** /guides/missing-payment-rows

# How to find orders missing from a payment CSV

An order missing from a payment CSV is an order with no matching order ID in that file. It is a record to investigate, not proof that the order is unpaid. ReconcilePad aligns two UTF-8 CSV files by exact order-ID strings and exports the unmatched order rows for review.

## Prepare exports with matching coverage

Choose the Orders and Payments exports for the period you are checking. Check that both files cover the intended month, and note whether their export times or inclusion rules differ. A payment recorded later or omitted from an export can leave an order unmatched even when money has arrived. Keep the original files so you can trace the review back to the source records.

Check the order-ID columns before importing. ReconcilePad matches strings exactly: `001` and `1` differ, and extra spaces change the string. It does not trim spaces or restore leading zeroes. If an export has changed IDs, correct the export through your source workflow before relying on the comparison; ReconcilePad does not repair IDs automatically.

## Select both files and their order-ID columns

Select the two UTF-8 CSVs in ReconcilePad and specify the order-ID column in each file. Compare the files using exact string matching. ReconcilePad marks rows from the Orders file that have no matching ID in the Payments file; it does not modify either source file.

For this minimal synthetic example, the inputs are:

orders.csv
```csv
order_id
001
002
003
```

payments.csv
```csv
order_id
001
003
```

Choose `order_id` in both files. The expected unmatched order is `002`. Export the review CSV. Its expected unmatched order-ID content is:

```csv
order_id
002
```

This illustrates the review's contents, not a guarantee of exact UI labels, export filename or extra metadata columns. No live application run was supplied for this tutorial.

## Investigate the exported review list

Check `002` in the original order records and payment records. Confirm whether the payment is absent, late, outside the export's time range or recorded with a different identifier. The comparison locates unmatched records; the original records determine their meaning. Refunds are outside this tool's processing scope, and there is no bank API to establish whether cash has been received.

## Handle problematic files before relying on the result

If an order ID is blank, fix it in the source export and produce a corrected file for comparison. A blank identifier cannot provide a reliable order-level match. If IDs are duplicated, return to the original records and determine what each row represents; the tool does not guarantee automatic duplicate resolution. An ID appearing in the payment export does not prove that every order row with that ID has been correctly paid.

If the files are not UTF-8, obtain UTF-8 exports before selecting them. If expected matches appear in the review, inspect exact strings, spaces, leading zeroes and export coverage first. After correcting the source export, repeat the comparison and recheck the result. Do not edit the accounting ledger solely because an ID appears in a review list.

Keep original exports. A review list is a starting point for checking the original records, not your accounting ledger.

**CTA: See the two-CSV review workflow**

# Internal editorial decision and evidence

Update A1 at its existing slug because the intended reader and missing-payment-row question are unchanged. Do not create a competing “Fix missing payment CSV entries” article: “fix” would also imply repair capability that F1 does not have. Replace “Missing rows are unpaid orders” and “it fixes IDs automatically”; preserve the final unaffected paragraph verbatim. Inputs, example and expected `002` all come exclusively from this case. The sample output represents logical review content, with no invented export schema. No keyword volume, search ranking, live run, deployment or indexing was verified. gr-blog-post and SEO content SOP informed direct-answer and usable tutorial structure; invented first-person experience, unrelated source links, publication commands and keyword-tool requirements were excluded under the frozen-source constraint.
