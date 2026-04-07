Title:

    Inventory monitoring system

Description:

    This program reads inventory data from an Excel file and marks items below the minimum.

Input:

    Input file: 
        - data/inventory.xlsx
    Required columns:
        -Item number
        -Name
        -current_inventory
        -minimum_inventory

Output:

    - output/inventory_status.xlsx
    - Contains all items with calculated status
    - Highlights problematic items (Warning, Critical)

Status values:

    - OK
    - Warning
    - Critical
    
Run:

    pip install -r requirements.txt
    python main.py

Used technologies:

    -Python
    -pandas
    -openpyxl




