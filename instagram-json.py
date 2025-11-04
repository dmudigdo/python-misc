import json
import csv
from datetime import datetime

def extract_values_and_dates(json_file):
    """Extracts (value, date_str) pairs from the given JSON file."""
    with open(json_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    results = {}
    for item in data.get("relationships_following", []):
        for entry in item.get("string_list_data", []):
            # Extract the username from the URL
            # (Note fwers/fwing have different URL formats)
            href = entry.get("href", "")
            href = href.replace("/_u","")
            href = href[26:]

            ts = entry.get("timestamp", None)
            # Convert timestamp to readable date (if present)
            if ts is not None:
                date_str = datetime.fromtimestamp(ts).strftime("%Y-%m-%d %H:%M:%S")
            else:
                date_str = ""

            results[href] = date_str
    return results


def excluding_join(dict1, dict2, join_type="left"):
    """
    Left excluding join = items in dict1 not in dict2
    Right excluding join = items in dict2 not in dict1
    """
    join_result = []

    if join_type == "left":
        for key in dict1.keys() - dict2.keys():
            join_result.append((key, dict1[key]))
    elif join_type == "right":
        for key in dict2.keys() - dict1.keys():
            join_result.append((key, dict2[key]))
    else:
        raise ValueError("join_type must be 'left' or 'right'")

    return join_result


def write_to_csv(filename, records, header=("Href", "Date")):
    """Writes records (list of tuples) to a CSV file."""
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(records)

# Example usage
fwing_data = extract_values_and_dates("following.json")
fwers_data = extract_values_and_dates("followers.json")

# Left excluding join: in old but not in new
left_excluding = excluding_join(fwing_data, fwers_data, join_type="left")
write_to_csv("fwing-not-fwers.csv", left_excluding)

# Right excluding join: in new but not in old
right_excluding = excluding_join(fwing_data, fwers_data, join_type="right")
write_to_csv("fwers-not-fwing.csv", right_excluding)

print("✅ Results written to left_excluding.csv and right_excluding.csv")

