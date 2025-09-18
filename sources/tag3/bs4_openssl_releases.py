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

# each <section> describes a version
div_releases = soup.select("div[data-hpc] section")
# print(f"div_releases: {div_releases}")

count = 0
for rel in div_releases:
    # <h2>: version name
    # <relative-time datetime="...">: release datetime
    # https://github.com/github/relative-time-element
    print(f"{rel.find("h2").text.strip():<20} - {rel.find("relative-time").get("datetime")}")
    count += 1
    if count > 10:
        break
