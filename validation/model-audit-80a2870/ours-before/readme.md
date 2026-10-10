# Public README

# csvpeek

Check a CSV’s header and data-row count before connecting it to your Python workflow. csvpeek reads a local UTF-8 CSV and prints a JSON summary. It uses the Python standard library, requires Python 3.10 or later, and does not upload your file.

## Run your first check

Obtain `csvpeek.py` from the source distribution you have been given and save it in a working directory. There is no published installation package in the supplied release information. You do not need to install third-party Python dependencies.

Check your Python version:

```sh
python3 --version
```

Use Python 3.10 or later. Place a CSV beside the script, or pass a path to another local file. For this minimal example, save the following UTF-8 text as `sample.csv`:

```csv
order_id,total
A001,12
A002,17
```

From the directory containing the script and sample, run:

```sh
python3 csvpeek.py sample.csv
```

Expected output:

```json
{"header": ["order_id", "total"], "rows": 2}
```

The header is the first CSV row. The count is the number of rows after that header, so this sample contains two data rows. To inspect another file, pass its path as the positional argument:

```sh
python3 csvpeek.py path/to/file.csv
```

There is no `--input` option. The supported first-run route is running the Python file directly, rather than `pip install csvpeek` or an installed `csvpeek` command.

## What the summary means

csvpeek uses Python’s CSV reader to read the first row as the header and count the remaining rows. It prints the column names and count as JSON to standard output. That makes it a small preliminary check when you need to know whether an export has the expected columns and number of rows before wiring it into another workflow.

An empty file produces an empty header and a count of zero. A file with only a header produces a count of zero. The program reads through the file to obtain the count; no speed or file-size benchmark is available.

## Limits and errors

The input must be a readable local UTF-8 CSV. csvpeek does not correct data, verify business meaning, inspect column types, connect to a database or upload files. A header and row count alone do not establish that an import is safe or the data is complete. The script does not modify your CSV.

Pass a file path you can read. Missing or unreadable files, decoding errors and CSV-reading errors caught by the script produce an error on standard error and exit status 2. If the command fails, check the supplied path, local permissions and encoding. Correct or re-export the input through your existing process; csvpeek will not repair it for you.

## Using it with a team

Keep the script version you evaluated with your team’s agreed tooling. Record which files are inspected, what column names and counts are expected, and how exceptions are handled before a downstream import. Each operator needs local access to the input file; there is no database integration or shared service to configure in this script.

The sample command has been run locally against the supplied sample with Python 3.14.3 and returned the output above. Other Python versions and your team’s files still need checks in the environments where you plan to use it. Release packaging, licence terms and maintenance arrangements were not supplied; confirm those before adopting or redistributing it as part of a team process.

Start with the sample, then inspect one of your own authorised CSVs and compare the summary with the import’s requirements.

# Internal verification record

The source and sample were read before execution. Source inspection found local file reading with the standard library, positional `file` argument, JSON stdout, caught file/encoding/CSV errors and no network or file-write operations. The source was not changed.

The working directory was `./tests/fixtures/devtool/`. Actual commands were `python3 --version` and `python3 csvpeek.py sample.csv`. The first returned stdout `Python 3.14.3` with a trailing newline; the second returned stdout `{"header": ["order_id", "total"], "rows": 2}` with a trailing newline. Both had empty stderr and exit status 0. The environment was macOS 26.3 arm64; the exact runtime details, commands, cwd and captured streams are in `readme-execution.json` alongside this draft.

No installation, package publication, Python 3.10 compatibility run, error-path execution, performance benchmark, database integration or team rollout was performed. Error-path and empty-file statements are source-derived. No repository, documentation, community or licence URL was invented. The absolute fixture location appears only in this internal record and is not a product installation dependency.
