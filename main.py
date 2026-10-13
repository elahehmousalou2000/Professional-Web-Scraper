import csv
import requests
from bs4 import BeautifulSoup

url = input("URL: ")
response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"}, timeout=10)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")
titles = [x.get_text(" ", strip=True) for x in soup.find_all(["h1", "h2", "h3"])]

with open("results.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["title"])
    for title in titles:
        writer.writerow([title])

print(f"Saved {len(titles)} titles.")
