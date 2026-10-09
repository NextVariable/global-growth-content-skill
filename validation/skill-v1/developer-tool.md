## README draft

# csvpeek

Inspect the header and row count of a local UTF-8 CSV before writing your import code. csvpeek is a Python standard-library script that reads a file on your machine and prints JSON. It does not upload data, correct CSVs or connect to a database.

## Requirements and setup

Use Python 3.10 or later. There is no published package and no dependency installation step. Obtain `csvpeek.py` from the supplied source; do not use a guessed pip package.

From this repository’s `tests/fixtures/devtool` directory, run:

```sh
python3 --version
python3 csvpeek.py sample.csv
```

Expected output for the included sample:

```json
{"header": ["order_id", "total"], "rows": 2}
```

For your own input:

```sh
python3 csvpeek.py path/to/file.csv
```

The file path is positional; `--input` is not a supported option. The first record is treated as the header. `rows` counts the records after it, not physical lines in the file.

## Limits and failure points

The input must be a readable local UTF-8 CSV. A missing file, permission failure, decoding error or reported CSV parsing error causes an error and a nonzero exit. Counting requires reading through the file; there are no verified throughput benchmarks. The script does not validate row lengths, repair malformed data, infer column types or prove that a CSV is safe to import. An empty file returns an empty header and zero rows by the source logic; that edge case was read but not run in this check.

## Team adoption

For individual use, inspect the output before writing an importer. For a team, agree on encoding and export format, pin the reviewed source revision and decide how this JSON output fits your checks. The supplied script reads the input and prints output; it performs no network operations or file writes. License, long-term maintenance and integration compatibility need review before team adoption because the fixture provides no licensing or service terms. No documentation site, community or commercial-service links are available in the supplied material.

## Execution evidence

Working directory: `/Users/francis/Desktop/海外增长 skill/02-产品定位与增长内容/tests/fixtures/devtool`.

Commands actually run:

```sh
python3 --version
python3 csvpeek.py sample.csv
```

Observed output:

```text
Python 3.14.3
{"header": ["order_id", "total"], "rows": 2}
```

Both commands completed with exit status 0 in one execution. Source inspection confirmed use of argparse, csv, json and pathlib, one positional file argument and no writes/network. Only the included sample was run; Python 3.10 compatibility, other systems, failure cases and real team pipelines remain untested. The demonstration above is textual and reproducible, not a supplied screenshot. This README aims at developers evaluating the tool and leads to running the sample, with no purchase or star CTA.
