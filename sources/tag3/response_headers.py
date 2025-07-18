import requests

res = requests.get('https://www.gutenberg.org/')
# print(f'HTTP Status : {res.status_code}')
print('Response Headers:')
for name, val in res.headers.items():
    print(f'{name:<20} : {val}')
