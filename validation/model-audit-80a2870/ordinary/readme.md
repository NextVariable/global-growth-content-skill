# csvpeek

Inspect a local CSV's header and data-row count before you connect it to your Python workflow.

csvpeek reads a UTF-8 CSV on your computer and prints a JSON summary. It uses Python's standard library, uploads nothing and does not change your file.

## First run

You need Python 3.10 or later and a copy of `csvpeek.py`. There is no released installable package in the supplied project information, so there is no `pip install csvpeek` step. Place the script in a working directory and run it directly with Python:

```sh
python3 --version
python3 csvpeek.py path/to/file.csv
```

Pass the file path as a positional argument. There is no `--input` option.

For a minimal first check, save this data as `sample.csv` beside the script:

```csv
order_id,total
A001,12
A002,17
```

From that directory, run:

```sh
python3 csvpeek.py sample.csv
```

Expected output:

```json
{"header": ["order_id", "total"], "rows": 2}
```

The first CSV record becomes the header. The `rows` value counts the subsequent CSV records. Use the summary to check whether the field names and record count match what your next processing step expects.

## What the result means

csvpeek uses the standard-library CSV reader. It does not validate your business schema, inspect values, repair malformed data, connect to a database or upload files. It assumes the first record is a header; a headerless file will have its first record reported as the header and excluded from the data-row count. An empty file returns an empty header and zero rows. Counting requires reading through the file; no performance benchmarks are available.

If a file cannot be opened or decoded as UTF-8, or the CSV reader reports a CSV error, the script prints an error beginning with `csvpeek:` to standard error and exits with status 2. Check the path, read permissions and encoding before rerunning. Other CSV quality problems may still parse successfully; a successful count is not a data-quality certification.

## Using it with a team

Start with a representative local export and compare the reported header and count with the producing system's expectations. Agree which headers and counts warrant further review before integrating the CSV. Keep those acceptance rules outside csvpeek: it reports the file structure and count but does not enforce your team's rules.

The script uses only the Python standard library. There is no supplied release package, benchmark, community link or documentation site to rely on here. Licensing information has not been provided; establish the project's license before adopting or redistributing it in your organization.

## Verified example

The sample command above was run against the supplied script and sample file using Python 3.14.3. It returned the displayed JSON, with no standard-error output and exit status 0. This verifies that sample run, not every Python version or file type.

---

# Internal execution record

Actual directory: `/Users/francis/Desktop/海外增长 skill/02-产品定位与增长内容/tests/fixtures/devtool/`.

Command: `python3 csvpeek.py sample.csv`.

Environment: Python 3.14.3; platform and raw command records are retained in `readme-run.json` beside this draft. Actual stdout: `{"header": ["order_id", "total"], "rows": 2}` followed by a newline. Actual stderr: empty. Exit status: 0. `python3 --version` also exited 0 with stdout `Python 3.14.3` followed by a newline and empty stderr. No installation, network access or source modification was performed. Runtime versions other than the observed environment and error-path executions have not been tested.
