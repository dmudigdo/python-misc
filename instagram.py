# Extracts Instagram follower/following data from ...
# Reads in the HTML, spits out the data as CSV

from bs4 import BeautifulSoup
import csv

def extract_two_level_divs_to_csv(html_file, csv_file):
    with open(html_file, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")

    # Find all outer divs with class "_a6-p"
    outer_divs = soup.find_all("div", class_="_a6-p")

    rows = []
    for outer in outer_divs:
        # Step 1: go one level down (first nested div)
        level1 = outer.find("div")
        if not level1:
            continue

        # Step 2: get ALL direct child divs at level 2
        level2_divs = level1.find_all("div", recursive=False)

        # Collect their text
        texts = [div.get_text(strip=True) for div in level2_divs]

        # Add to rows (pad with empty strings if less than 2 divs)
        while len(texts) < 2:
            texts.append("")
        rows.append(texts[:2])  # keep only first two in case of extras

    # Write results to CSV
    with open(csv_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Handle", "Date"])  # header
        writer.writerows(rows)

# Example usage
html_file = "followers.html"   # your HTML file
csv_file = "output.csv"      # desired output CSV
extract_two_level_divs_to_csv(html_file, csv_file)
