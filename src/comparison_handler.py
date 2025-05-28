import pandas as pd
import os
import json


def compare_codes(df1, df2):
    if len(df1) != len(df2):
        raise ValueError('The two csvs must have the same number of rows')

    num_columns = len(df1.columns)
    num_rows = len(df1)

    myMap = {}
    for i in range(num_rows):
        for col in range(2, num_columns):
            val1 = df1.iloc[i, col]
            val2 = df2.iloc[i, col]
            if (not val1 and val2) or (not val2 and val1) and val1 != val2:
                myMap[i] = myMap.get(i, 0) + 1
    print("Number of rows with at least one mismatch: ", len(myMap))
    return myMap


def extract_csv(xlsx_path,  name):
    # Read the specific sheet
    df = pd.read_excel(xlsx_path, sheet_name=name)
    return df


def save_json(error_map):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    root_dir = os.path.abspath(os.path.join(base_dir, '..'))
    data_dir = os.path.join(root_dir, 'data')
    with open(os.path.join(data_dir, 'error_map.json'), 'w') as f:
        json.dump(error_map, f, indent=4)
    return
