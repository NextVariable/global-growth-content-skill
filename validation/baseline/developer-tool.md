# csvpeek

Inspect a CSV header and count data rows before connecting it to your Python workflow.

csvpeek is a small local command-line tool for Python developers. It reads a UTF-8 CSV and prints JSON containing its header and number of remaining rows. It uses only the Python standard library and does not upload the file.

## Run the source

Requires Python 3.10 or newer. There is no published package to install. From the provided source directory, run:

```sh
python3 csvpeek.py sample.csv
```

Output:

```json
{"header": ["order_id", "total"], "rows": 2}
```

To inspect another file, use a positional file path:

```sh
python3 csvpeek.py path/to/file.csv
```

There is no `--input` option. The `rows` value counts CSV records after the first record, which is treated as the header. It is not necessarily the physical line count when a quoted field contains a newline.

## Limits and team adoption

The tool reads UTF-8 CSV files locally. It does not correct data, validate a schema, connect to a database, or provide an upload service. No performance benchmark, release package, community, or documentation site has been established. A successful parse is not proof that the CSV is suitable for your application.

For team adoption, keep the reviewed source with your workflow, specify Python 3.10 or newer, and agree whether each input file has a header and uses the expected CSV format. Try representative files and failure cases before depending on it in an automated ingestion process. Handle its nonzero exit status when a file cannot be read or parsed, and compare reported headers with your application’s required fields separately.

实际执行记录：工作目录为 `02-产品定位与增长内容/tests/fixtures/devtool`，执行 `python3 csvpeek.py sample.csv`，退出码为0，原始标准输出为 `{"header": ["order_id", "total"], "rows": 2}`。已读取指定源码验证使用位置参数与stdlib；没有运行性能、不同系统、非UTF-8输入或团队集成测试。
