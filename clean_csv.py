import pandas as pd
import sys
import os

def normalize_column_names(columns):
    return [col.strip().lower().replace(" ", "_") for col in columns]

def clean_csv(file_path, output_path=None):
    if not os.path.exists(file_path):
        print("❌ File not found.")
        return

    df = pd.read_csv(file_path)

    print(f"📊 Loaded {len(df)} rows and {len(df.columns)} columns")

    df.columns = normalize_column_names(df.columns)
    df.dropna(how="all", inplace=True)
    df.drop_duplicates(inplace=True)

    if not output_path:
        output_path = file_path.replace(".csv", "_cleaned.csv")

    df.to_csv(output_path, index=False)
    print(f"✅ Cleaned CSV saved to: {output_path}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python clean_csv.py data.csv")
    else:
        clean_csv(sys.argv[1])
