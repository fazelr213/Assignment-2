import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Data_science"

# Get webpage
response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
soup = BeautifulSoup(response.text, "html.parser")

# Find main content
content = soup.find("div", id="mw-content-text")

# Words to exclude
exclude = ["References", "External links", "See also", "Notes"]

headings_list = []

# Find all h2 headings
for h2 in content.find_all("h2"):
    heading = h2.get_text().replace("[edit]", "").strip()

    # Skip unwanted headings
    if not any(word in heading for word in exclude):
        headings_list.append(heading)

# Save to file
with open("headings.txt", "w") as f:
    for h in headings_list:
        f.write(h + "\n")

print("Headings saved to headings.txt")
