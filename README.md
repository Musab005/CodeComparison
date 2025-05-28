# Simple Python program to compare open coding between two csv files (coded by different coders)
The program ignores the first 2 columns of the csv (ID, responses). It compares the coded values (for example 1's and 0's) in remaining columns.
Output file `error_map.json` is saved in the data directory. The keys are the row index where the mismatch is present. 
The values are the total number of mismatches in that row.

### To run:
1) Save the two `.xlsx` files in the data directory
2) Run from project root `python -m scripts.compare_codes {path_to_xlsx1} {path_to_xlsx2} {sheet_name}` where `{sheet_name}` is the specific csv file to compare

### Note:
I developed this project to help me with the survey analysis in my internship