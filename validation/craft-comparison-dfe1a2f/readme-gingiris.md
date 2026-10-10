# ColPick
A CSV column selector for developers.

Keep the columns your next task needs while preserving input row order. Requires Python 3.10+.

## Quick start
With the supplied colpick.py and sample.csv in the working directory:
```sh
python colpick.py sample.csv order_id,total
```
Inspect the result for order_id and total. Unknown column names raise an error: check the input header and run again.

Internal: use a real terminal recording as the hero asset once the example is executed. No asset or execution result is supplied here.
