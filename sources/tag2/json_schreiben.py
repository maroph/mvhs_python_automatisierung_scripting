import json

kontakte = {
    "kontakte" : []
}
# print(kontakte)

kontakt = {
    'name': {
      'vorname': 'Anne',
      'nachname': 'Maier'
    },
    'adresse': {
        'strasse': 'Dorfstraße 1',
        'plz': '12345',
        'ort': 'Dorf'
    },
    'telefon':
        {
            'privat': '0123-456789',
            'mobil': '0700-1234567'},
    'email': 'anne.maier@example.com'
}
kontakte['kontakte'].append(kontakt)
# print(kontakte)

kontakt = {
    'name': {
      'vorname': 'David',
      'nachname': 'Müller'
    },
    'adresse': {
        'strasse': 'Ortstraße 12',
        'plz': '54321',
        'ort': 'Ort'
    },
    'telefon': {
        'privat': None,
        'mobil': '0700-7654321'
    },
    'email': 'david.mueller@example.com'
}
kontakte['kontakte'].append(kontakt)
# print(kontakte)

kontakt = {
    'name': {
      'vorname': 'Mila',
      'nachname': 'Muster',
    },
    'adresse': {
        'strasse': 'Stadtstrasse 123',
        'plz': '13524',
        'ort': 'Stadt'
    },
    'telefon': {
        'privat': None,
        'mobil': '0700-1237654'
    },
    'email': 'mila.muster@example.com'
}
kontakte['kontakte'].append(kontakt)
# print(kontakte)
# print()

print('Python : ')
print(kontakte)
print('---')
print('JSON - unformatiert : ')
print(json.dumps(kontakte, ensure_ascii=False))
print('---')
print('JSON - formatiert   : ')
print(json.dumps(kontakte, indent=2, ensure_ascii=False))

# schreiben der JSON-Datei kontakte.out.json
with open("kontakte.out.json", mode="w", encoding="utf-8") as json_file:
    json.dump(kontakte, json_file, indent=2, ensure_ascii=False)
