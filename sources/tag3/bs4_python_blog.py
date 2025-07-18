# Beautiful Soup Dokumentation:
# https://www.crummy.com/software/BeautifulSoup/bs4/doc/
from bs4 import BeautifulSoup
import requests
import sys


url_blog = "https://www.python.org/blogs/"
try:
    response = requests.get(url_blog)
    soup = BeautifulSoup(response.text, "html.parser")
except Exception as e:
    print(e)
    sys.exit(1)

item_list = []
for item in soup.select(".list-recent-posts li"):
    item_list.append((item.find("h3").text.strip(), item.find("a").get("href")))

print('Inhalt der Seite')
print('----------------')
for title, link in item_list:
    print(f'Title : {title}')
    print(f'Link  : {link}')
    print('---')
