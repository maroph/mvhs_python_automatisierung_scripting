import requests
from bs4 import BeautifulSoup

# RSS Feed: Blog on OpenSSL Library
url = "https://openssl-library.org/post/index.xml"

response = requests.get(url)

soup = BeautifulSoup(response.content, "xml")

# print(soup.prettify())

channel = soup.find('channel')
print(f'channel.titel         : {channel.title.text}')
print(f'channel.link          : {channel.link.text}')
print(f'channel.lastBuildDate : {channel.lastBuildDate.text}')
print(f'channel.generator     : {channel.generator.text}')
print(f'channel.language      : {channel.language.text}')

# <atom:link href="https://openssl-library.org/post/index.xml" rel="self" type="application/rss+xml"/>
atom_link = channel.find("atom:link")
if atom_link:
    print(f'channel atom:link     : {atom_link.get("href")}')
    print(f'        rel           : {atom_link.get("rel")}')
    print(f'        type          : {atom_link.get("type")}')
else:
    print('channel atom:link     : None}')

print('---')

item_list = soup.find_all("item")
lng = len(item_list)
if lng > 5:
    lng = 5
for item in item_list[:lng]:
    print(f'title   : {item.title.text}')
    print(f'pubDate : {item.pubDate.text}')
    print(f'link    : {item.link.text}')
    # print(f'guid    : {item.guid.text}')
    # print(f'Description\n{item.description.text}')
    print('---')
