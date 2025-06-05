# Simple Python program to compare open coding between two csv files (coded by different coders)
I developed this project to help me with the survey analysis in my internship

The program ignores the first 2 columns of the csv (ID, textual responses). It compares the coded values in the remaining columns.
Any non blank cell is considered to be coded under the theme represented by the column name.
Output file `error_map.json` is saved in the data directory. The keys are the ID's where the mismatch is present. 
The values are the extra themes coded by Lawrence and Musab (i.e. all the mismatches).

### To run:
1) Save the two `.xlsx` files in the data directory
2) Run from project root `python -m scripts.compare_codes {path_to_xlsx1} {path_to_xlsx2} {sheet_name}` where `{sheet_name}` is the specific csv file to compare
