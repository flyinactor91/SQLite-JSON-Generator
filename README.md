# SQLite-JSON-Generator
Generate an SQLite database from a JSON config file  
Michael duPont - [mdupont.com](https://mdupont.com)

---

## Configure

This simple script uses Python3 code to generate an SQLite database according to a compatible JSON file. This JSON file follows the following structure:

```json
{
    "<Table_Name>": {
        "columns": ["<col_1>", "<col_2>"],
        "rows": [
            ["<val_1>", "<val_2>"],
            ["<val_1>", "<val_2>"],
            ["<val_1>", "<val_2>"],
        ]
    }
}
```

The only two required values are "columns" and "rows" while the rest can be renamed. You can add as many tables, columns and rows as you want.

In addition to the given columns, the script prepends an "id" column to each table and assigns an "id" value for each row starting at zero.

## Running

```python3 dbgen.py [source.json] [output.sqlite]```

Ex:

```python3 dbgen.py example.json example.sqlite```