# Tabular-Cleanser 🧼

A lightweight CSV cleaning tool that helps you tidy up messy tabular data.

## Features

- Strips empty rows
- Removes duplicates
- Normalizes column names
- Outputs a cleaned version of the original file

## Usage

```bash
python clean_csv.py your_file.csv
```

It will create a new file: `your_file_cleaned.csv`

## Example

Original CSV:

| Name | Age |   |  
|------|-----|---|  
| Alice | 30 |   |  
| Bob   |  |   |  
| Alice | 30 |   |  

Cleaned CSV:

| name | age |  
|------|-----|  
| Alice | 30 |  
| Bob   |     |  
