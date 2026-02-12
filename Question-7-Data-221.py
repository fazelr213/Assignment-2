import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Data_science"

response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
soup = BeautifulSoup(response.text, "html.parser")

# Print page title
print("Title:", soup.title.text)

# Find first paragraph with at least 50 characters
for character in soup.find("div", id="mw-content-text").find_all("p"):
    text = character.get_text(strip=True)
    if len(text) >= 50:
        print("First Paragraph:")
        print(text)
        break
