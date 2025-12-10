import pandas as pd
from pathlib import Path

EXCEL_PATH = Path("dummy_database.xlsx")

# Load and inspect the Excel file
df = pd.read_excel(EXCEL_PATH)

print("Column names in Excel file:")
print(df.columns.tolist())
print("\n" + "="*50 + "\n")

print("First few rows:")
print(df.head())
print("\n" + "="*50 + "\n")

print("Data types:")
print(df.dtypes)
print("\n" + "="*50 + "\n")

# Check if DOB column exists
if "DOB" in df.columns:
    print("DOB column found!")
    print("\nFirst 5 DOB values:")
    print(df["DOB"].head())
    print("\nAny null DOB values?")
    print(f"Null count: {df['DOB'].isna().sum()} out of {len(df)}")
else:
    print("DOB column NOT FOUND!")
    print("Available columns:", df.columns.tolist())