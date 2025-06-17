import pandas as pd
import os
import json


# Notes:
# 1) headers not included when using df.iloc[0,0]. To get headers, use df.columns

def compare_codes(lawrence_df, musab_df):
    if len(lawrence_df) != len(musab_df):
        raise ValueError("Rows of csv mismatch")
    if len(musab_df.columns) != len(lawrence_df.columns):
        raise ValueError("cols of csv mismatch")

    num_columns = len(lawrence_df.columns)
    num_rows = len(lawrence_df)

    myMap = {}
    for i in range(num_rows):
        errors = {
            "Lawrence": [],
            "Musab": []
        }
        response_id = lawrence_df.iloc[i, 0]
        for col in range(2, num_columns):  # loop stops at num_columns - 1
            val1 = lawrence_df.iloc[i, col]
            val2 = musab_df.iloc[i, col]
            # unclassified words (last column) append regardless
            if col == num_columns - 1 and (not is_blank(val1) or not is_blank(val2)):
                # 54 rows excluding the similar unclassified words. 70 otherwise
                # STIGMA1: 15
                # STIGMA2: 12
                if val1 == val2:
                    continue
                if not is_blank(val1):
                    errors["Lawrence"].append("Unclassified words: " + str(val1))
                if not is_blank(val2):
                    errors["Musab"].append("Unclassified words: " + str(val2))
            # if there is a mismatch (i.e. one has coded and the other has left blank)
            if is_blank(val1) != is_blank(val2) and col != num_columns - 1:
                if is_blank(val1):  # lawrence was blank but musab had a theme
                    errors["Musab"].append(musab_df.columns[col])
                else:
                    errors["Lawrence"].append(lawrence_df.columns[col])
        if errors["Musab"] or errors["Lawrence"]:
            myMap[f"ID {response_id}"] = errors
    print("num of rows to look at: ", len(myMap))
    return myMap


def extract_csv(xlsx_path, name):
    # Read the specific sheet
    df = pd.read_excel(xlsx_path, sheet_name=name)
    return df


def save_json(error_map, sheet_name):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    root_dir = os.path.abspath(os.path.join(base_dir, '..'))
    data_dir = os.path.join(root_dir, 'data')
    with open(os.path.join(data_dir, f"{sheet_name}.json"), 'w') as f:
        json.dump(error_map, f, indent=4)
    return


def is_blank(val):
    return pd.isna(val)
