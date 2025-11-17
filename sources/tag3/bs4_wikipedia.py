# Beautiful Soup Dokumentation:
# https://www.crummy.com/software/BeautifulSoup/bs4/doc/
from bs4 import BeautifulSoup
import requests
import sys


# url = "https://de.wikipedia.org/wiki/Wikipedia:Hauptseite"
url = "https://de.wikipedia.org/"

try:
    # Ergänzung: 15.11.2025
    #
    # requests.get() Default HTTP Header Elemente:
    # headers = {
    #     "Accept": "*/*",
    #     "Accept-Encoding": "gzip, deflate",
    #     "Connection": "keep-alive",
    #     "Host": "de.wikipedia.org",
    #     "User-Agent": "python-requests/2.32.5"
    # }
    #
    # Der Header "User-Agent: python-requests/2.32.5" wird
    # von der Wikipedia nicht mehr akzeptiert und liefert
    # den HTTP Status Code 403 zurück.
    #
    # Minimaler HTTP Header, um auf die Wikipedia zugreifen
    # zu können:
    #
    # headers = {"User-Agent": ""}
    #
    headers = {
        "Host": "de.wikipedia.org",
        "User-Agent": "bs4_wikipedia/1.0",
        "Content-Type": "text/html;charset=utf-8",
        "Accept": "text/html",
        "Connection": "close"
    }

    # response = requests.get(url, headers={"User-Agent": "bs4_wikipedia/1.0"})
    response = requests.get(url, headers=headers)
    if response is None:
        print("Die Response/Antwort) ist None", file=sys.stderr)
        sys.exit(1)
    if response.ok:
        soup = BeautifulSoup(response.text, 'html.parser')
    else:
        try:
            response.raise_for_status()
        except Exception as ex:
            print(f"Fehler beim Zugriff auf die URL {url}", file=sys.stderr)
            print(str(ex), file=sys.stderr)
            sys.exit(1)
except Exception as e:
    print(e)
    sys.exit(1)

headlines = soup.find_all('h2')
if not headlines:
    print('Keine Headlines gefunden')
else:
    for idx, headline in enumerate(headlines):
        print(f'{idx:>2}: {headline.text.strip()}')
