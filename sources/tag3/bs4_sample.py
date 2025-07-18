
# Beautiful Soup Dokumentation:
# https://www.crummy.com/software/BeautifulSoup/bs4/doc/
from bs4 import BeautifulSoup
import os
import sys

use_local_file = True
# use_local_file = False

url_site = "https://maurice-web.de"
url_training = "https://maurice-web.de/tr/2507_vhs_python_automatisierung/"

if use_local_file:
    try:
        with open('Automatisierung_mit_Python_Juli_2025_VHS-maurice-web.html', mode='r', encoding='utf-8') as fp:
            soup = BeautifulSoup(fp, 'html.parser')
    except Exception as e:
        print(e)
        sys.exit(1)
else:
    try:
        import requests
        response = requests.get(url_training)
        soup = BeautifulSoup(response.content, "html.parser")
    except Exception as e:
        print(e)
        sys.exit(1)

# soup:
# <!DOCTYPE html>
# <html>
# ...
# </html>
# print(soup.prettify())

main = soup.find("main") # <main> ... </main>

# main:
# <main>
# ...
# </main>
# print(main.prettify())


print(f'Webseite: {main.find('h2').text}')
print(f'URL: {url_training}')
print('Verfügbare Trainingsdateien')
print('---')
# for a_tag in main.find_all("a", {'target':'_blank'}):
for a_tag in main.find_all("a"):
    href = a_tag.get('href')
    if href == '#':
        continue
    print(os.path.basename(href))
    print(f'    ({url_site}{href})')
print('---')
