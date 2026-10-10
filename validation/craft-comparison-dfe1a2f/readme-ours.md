# ColPick
Select the CSV columns you need, without changing row order.

For developers preparing an existing CSV for their next task. ColPick is a Python command-line tool: name the columns to keep; an unknown column produces an error.

## Try the supplied example
Requires Python 3.10+ and the supplied colpick.py and sample.csv in your working directory.
```sh
python colpick.py sample.csv order_id,total
```
Check that the result contains order_id and total in the requested order, with the input rows preserved. If a column is rejected, compare its name with the CSV header.

Internal: exact output encoding/destination are unspecified; verify against source before treating the example as run.
