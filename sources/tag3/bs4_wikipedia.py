# Beautiful Soup Dokumentation:
# https://www.crummy.com/software/BeautifulSoup/bs4/doc/
from bs4 import BeautifulSoup
import requests
import sys


url = 'https://de.wikipedia.org/wiki/Wikipedia:Hauptseite'

try:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
except Exception as e:
    print(e)
    sys.exit(1)

headlines = soup.find_all('h2')
if not headlines:
    print('Keine Headlines gefunden')
else:
    for idx, headline in enumerate(headlines):
        print(f'{idx:>2}: {headline.text.strip()}')
