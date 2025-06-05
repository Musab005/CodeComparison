import argparse
from src.comparison_handler import compare_codes, extract_csv, save_json


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("xlsx1", help="xlsx path 1")
    parser.add_argument("xlsx2", help="xlsx path 2")
    parser.add_argument("name", help="sheet name to compare")

    args = parser.parse_args()

    lawrence_df = extract_csv(args.xlsx1, args.name)
    musab_df = extract_csv(args.xlsx2, args.name)
    error_map = compare_codes(lawrence_df, musab_df)

    save_json(error_map)


if __name__ == "__main__":
    main()
