import pandas as pd

# Read the xlsx file
df = pd.read_excel("filename.xlsx", sheet_name=None)

# Split the sheets into different files
for sheet_name, sheet_data in df.items():
        sheet_data.to_excel(f"{sheet_name}.xlsx", index=False)