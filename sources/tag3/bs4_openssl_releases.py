# List the 10 most recent OpenSSL release versions
from bs4 import BeautifulSoup
import requests
import sys

url_release_page = "https://github.com/openssl/openssl/releases"
try:
    response = requests.get(url_release_page)
    soup = BeautifulSoup(response.text, "html.parser")
except Exception as e:
    print(e)
    sys.exit(1)

div_h2_releases = soup.select("div[data-hpc] h2")
# print(f"div_releases: {div_releases}")

count = 0
for rel in div_h2_releases:
    print(rel.text.strip())
    count += 1
    if count > 10:
        break
