from bs4 import BeautifulSoup
import requests
import sys

url = "https://curl.se/docs/caextract.html"

try:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
except Exception as e:
    print(e)
    sys.exit(1)

table = soup.find("table")
row = table.find_all('tr')[1]
td = row.find("td")
a = td.find("a")
print(f"{a.text} : https://curl.se{a.get('href')}")
