import re

birthday = input('Enter birthday (DDMMYY): ')

with open('pi_million_digits.txt', 'r', encoding='utf-8') as f:
    content = f.read()

match = re.search(f"{birthday}", content, re.MULTILINE)
if match:
    print('gefunden')
else:
    print('nicht gefunden')

print()
print('---')
print()

# Alternative Lösung
matches = re.findall(f"{birthday}", content, re.MULTILINE)
print(f'Anzahl Treffer: {len(matches)}')
