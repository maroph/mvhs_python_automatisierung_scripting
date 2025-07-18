import requests

res = requests.get('https://www.gutenberg.org/cache/epub/11/pg11.txt')
print(f'HTTP Status : {res.status_code}')
print('---')
print(res.text[:950])
print('---')
