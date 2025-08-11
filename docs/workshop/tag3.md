# Tag 3 (17.07.2025)

## Requests
Das Modul _Requests_ erlaubt das einfache Senden und
empfangen vom HTTP/1.1 Requests/Responses.

Beispiel:  

```
import requests

res = requests.get('https://www.gutenberg.org/cache/epub/11/pg11.txt')
print(res.status_code)
print(res.text[:950]
```

Diese Anfrage gibt die ersten 950 Zeichen einer Textversion
des Buches "Alice's Adventures in Wonderland" aus.

Beispiel: Response Header auslesen  

```
import requests

res = requests.get('https://www.gutenberg.org/')
print('Response Headers:')
for name, val in res.headers.items():
    print(f'{name:<20} : {val}')
```

### Links
* [PyPi: requests](https://pypi.org/project/requests/)
* [Requests](https://requests.readthedocs.io/en/latest/)
* [Python's Requests Library (Guide)](https://realpython.com/python-requests/)

### Code Beispiele

* [request_anfrage.py](https://raw.githubusercontent.com/maroph/mvhs_python_automatisierung_scripting/main/sources/tag3/request_anfrage.py)
* [response_headers.py](https://raw.githubusercontent.com/maroph/mvhs_python_automatisierung_scripting/main/sources/tag3/response_headers.py)

## Beautiful Soup
Beautiful Soup bietet dem Anwender die Möglichkeit, auf 
einfach Weise HTML Seiten und XML Dateien zu parsen.

**Achtung**: das Parsen funktioniert nicht bei per
JavaScript erzeugten Inhalten!

Vorgehensweise: Website-Inhalte mit requests laden und
den Text mit BeautifulSoup verarbeiten.

```
import requests
from bs4 import BeautifulSoup

res = requests.get('https://example.com')
soup = BeautifulSoup(res.text, 'html.parser')
```

| Funktion                 | Beschreibung                                                                |
|:-------------------------|:----------------------------------------------------------------------------|
| soup.select('.klasse')   | findet alle Elemente mit dieser Klasse – auch andere CSS-Selektoren möglich |
| soup.find('element')     | findet erstes Element mit bestimmtem Elementnamen                           |
| soup.find_all('element') | findet alle Elemente mit bestimmtem Elementnamen                            |
| element.get('attribut')  | z. B. Link extrahieren von Attribut                                         |
| element.text             | den Text aus einem Element erhalten                                         |
| element.text.strip()     | reinen Text bereinigt auslesen                                              |

### Links
* 
* [PyPi: beautifulsoup4](https://pypi.org/project/beautifulsoup4/)
* [Beautiful Soup: Homepage](https://www.crummy.com/software/BeautifulSoup/)
* [PyPi: lxml](https://pypi.org/project/lxml/)
* [lxml: Homepage](https://lxml.de/)

### Code Beispiele

* [bs4_python_blog.py](https://raw.githubusercontent.com/maroph/mvhs_python_automatisierung_scripting/main/sources/tag3/bs4_python_blog.py)
* [bs4_sample.py](https://raw.githubusercontent.com/maroph/mvhs_python_automatisierung_scripting/main/sources/tag3/bs4_sample.py)
* [bs4_wikipedia.py](https://raw.githubusercontent.com/maroph/mvhs_python_automatisierung_scripting/main/sources/tag3/bs4_wikipedia.py)
* [bs_rss_bund_sample.py](https://raw.githubusercontent.com/maroph/mvhs_python_automatisierung_scripting/main/sources/tag3/bs_rss_bund_sample.py)
* [bs_rss_read_sample.py](https://raw.githubusercontent.com/maroph/mvhs_python_automatisierung_scripting/main/sources/tag3/bs_rss_read_sample.py)
