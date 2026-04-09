Project objective:

    The objective of the program is to create an inventory checking system that reads data from an Excel file and marks items that are below the minimum level.

Input:

    File: 
        -data/inventory.xlsx
    Columns:
        -Item number
        -Name
        -current_inventory
        -minimum_inventory

Output:

    - output/inventory_status.xlsx
    - contains all items with status column
    - separate list of problematic items (Warning + Critical)

Process stages:

    1. Excel file reading
    2. Required columns checking
    3. Data cleaning
        - Convert numeric columns to numbers
        - Handle missing values
        - Strip spaces from text fields
    4. Status calculation
    5. Problematic items filtering
    6. Result export
    7. Console summary
        - Total items count
        - OK items count
        - Warning items count
        - Critical items count

Validation rules:

    - If current_inventory > minimum_inventory --> OK
    - If current_inventory == minimum_inventory --> Warning
    - If current_inventory < minimum_inventory --> Critical

Final definition:

    Project is finished if:
        - the script runs without bugs or errors
        - output file is created
        - every row is given a status
        - the problematic items are listed.




