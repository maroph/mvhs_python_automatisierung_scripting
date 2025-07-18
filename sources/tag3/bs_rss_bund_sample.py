import requests
from bs4 import BeautifulSoup

url = "https://www.nabu.de/rssfeed.php"
response = requests.get(url)
soup = BeautifulSoup(response.content, features="xml") # Beachte: XML-Parser

# Alle Artikel-Elemente
items = soup.find_all("item")
lng = len(items)
if lng > 5:
    lng = 5

for item in items[:lng]: # Nur die ersten 5
    title = item.find("title").text
    link = item.find("link").text
    pub_date = item.find("pubDate").text
    print(f"{title} ({pub_date})\n{link}\n")
