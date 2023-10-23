import csv, argparse, re
default_csv_file = "Mobile_Food_Facility_Permit.csv"

def parse_arguments():
    """
    Return Arguments provided by the CLI
    """
    parser = argparse.ArgumentParser(
        description="CLI for getting places that matches our item search"
    )
    parser.add_argument("--csv", default=default_csv_file, const=default_csv_file, nargs="?")
    parser.add_argument("--food", nargs="+", required=True)
    return parser


def search_by_food_items(file, match_words):
    """
    Function to get the match using regexp of the words that we have passed through the CLI
    """
    matched_locations = []
    with open(file, "r") as csv_file:
        csv_content = csv.DictReader(csv_file)
        for row in csv_content:
            if re.search("|".join(match_words), row["FoodItems"], re.IGNORECASE):
                matched_locations.append({
                    "address": row["Address"],
                    "applicant": row["Applicant"]
                })
    return matched_locations


if __name__ == '__main__':
    args = parse_arguments()
    args = args.parse_args()
    locations = search_by_food_items(args.csv, args.food)
    if not locations:
        print(f"There is not a location where they provide {args.food}")
    else:
        for location in locations:
            print(f"Address: {location['address']}, Applicant: {location['applicant']}")

