import requests
from bs4 import BeautifulSoup
import csv

# Wikipedia page URL
url = "https://en.wikipedia.org/wiki/Machine_learning"

# Send a request to the webpage and parse the HTML
soup = BeautifulSoup(
    requests.get(url, headers={"User-Agent": "Mozilla/5.0"}).text,
    "html.parser"
)

# Find the main content section of the page
content = soup.find("div", id="mw-content-text")

# Find the first table with at least 3 data rows (ignore navigation tables)
for table in content.find_all("table"):
    if table.get("role") == "navigation":
        continue  # skip navigation tables

    rows = table.find_all("tr")
    data_rows = [r for r in rows if r.find_all("td")]  # rows with actual data

    if len(data_rows) >= 3:
        break  # stop once we find a suitable table

# Get all rows from the selected table
rows = table.find_all("tr")

# Extract column headers from the first row
headers = [th.get_text(strip=True) for th in rows[0].find_all("th")]

# If no headers exist, create default column names
if not headers:
    headers = [f"col{i + 1}" for i in range(len(rows[0].find_all(['td', 'th'])))]

# Extract table data
data_wiki_table = []
for row in rows[1:]:  # skip header row
    cells = [c.get_text(strip=True) for c in row.find_all(["td", "th"])]

    # Add empty strings if a row has fewer cells than headers
    cells += [""] * (len(headers) - len(cells))

    data_wiki_table.append(cells)

# Save the table data to a CSV file
with open("wiki_table.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(headers)  # write header row
    writer.writerows(data_wiki_table)  # write data rows

print("Table saved.")

