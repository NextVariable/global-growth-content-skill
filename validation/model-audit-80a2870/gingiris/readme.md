# Public README draft

# csvpeek

**Inspect CSV headers and row counts before integrating with Python.**

csvpeek is a small Python standard-library command-line tool that reads a local UTF-8 CSV and prints its header and data-row count as JSON. Use it for a quick inspection before writing your CSV integration. Files stay local: the tool does not upload or modify them.

## Get running

You need Python 3.10 or newer, `csvpeek.py`, and a UTF-8 CSV to inspect. There is no published installation package. Obtain the provided source file and sample through your project's source distribution, then open a terminal in the folder containing `csvpeek.py` and `sample.csv`. No package installation or third-party dependency is required.

```sh
python3 --version
python3 csvpeek.py sample.csv
```

For the included sample:

```csv
order_id,total
A001,12
A002,17
```

The command prints:

```json
{"header": ["order_id", "total"], "rows": 2}
```

The header is the first parsed CSV record. `rows` counts the remaining parsed records and excludes the header. Two data records are present in this sample.

## Inspect your file

Pass the file path as a positional argument:

```sh
python3 csvpeek.py path/to/file.csv
```

Quote paths containing spaces. There is no `--input` argument and no installed `csvpeek` console command. Run the script with Python directly.

## Understand the result

csvpeek uses Python's CSV reader to parse the file, reads the first record as the header and counts subsequent records. Its JSON output gives your integration code a basic view of the file's shape. It does not tell you that the header matches your expected schema, that every record has the same number of fields, or that the values are valid.

An empty file produces an empty header and zero rows. A header-only file has zero data rows. The tool reads the file to count its records; no performance benchmark or recommended size limit has been established.

## Troubleshooting

If the file cannot be opened, check its path and read permission. If decoding fails, obtain a UTF-8 file. File-access, Unicode and CSV errors handled by the script are reported on stderr with exit status 2. Do not treat a successful count as proof that a CSV is correctly formed for your application: parser acceptance is not comprehensive validation.

## Use it with a team

Keep a reviewed copy of the source alongside your team's integration workflow, document the Python requirement and use an approved sample to confirm the command and expected output. An automated job or coding assistant can invoke the same positional command and check the exit status before reading stdout as JSON. This is ordinary script execution; no Skill installation, MCP server or database connection is supplied.

csvpeek does not repair data, upload files or connect to databases. Confirm header names, identifiers, value types and business rules in your integration separately. Release and licence information have not been provided; verify applicable permission before redistribution or incorporating the source into your team project.

# Internal verification record

Loaded source: `./tests/fixtures/devtool/csvpeek.py`; loaded sample: same directory, `sample.csv`. The public instructions depend on source-file placement, not this test directory.

Actually executed command: `python3 csvpeek.py sample.csv`, working directory `./tests/fixtures/devtool`.

Environment: Python 3.14.3, Clang 16.0.0; executable `/Library/Frameworks/Python.framework/Versions/3.14/bin/python3`; macOS 26.3 arm64. stdout was `{"header": ["order_id", "total"], "rows": 2}` followed by a newline. stderr was empty. Exit code: 0. Exact captured evidence is in `readme-execution.json` alongside this draft.

Only the supplied sample was executed. Empty/header-only/error behaviour above is source-derived, not additional live test evidence. Python 3.10 compatibility, a fresh machine, arbitrary file sizes, distribution, licensing, published package and benchmarks were not independently verified. gr-readme informed first-screen clarity and quick start; unsupported badges, stars, URLs, installation packages and integrations were omitted rather than invented. No source changes or installation occurred.
