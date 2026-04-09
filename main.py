import pandas as pd
from pathlib import Path

df = pd.read_excel("data/inventory.xlsx")

def validate_inventory(df):
    errors = []

    required_columns = [
        "Item number",
        "Name",
        "Inventory",
        "Minimum"
    ]

    for col in required_columns:
        if col not in df.columns:
            errors.append(f"Missing column: {col}")

    if errors:
        return errors

    if (df["Inventory"] < 0).any():
        errors.append("Negative values in Inventory column")

    if (df["Minimum"] < 0).any():
        errors.append("Negative values in Minimum column")

    if ((df["Item number"] >= 10000) & (df["Item number"] <= 99999)).all():
        errors.append("Item number must be a 5-digit number")

    cols = ["Item number", "Inventory", "Minimum"]

    converted = pd.to_numeric(df[cols].stack(), errors = "coerce")

    if converted.isna().any():
        errors.append("All values must be numeric in selected columns")

    


    

