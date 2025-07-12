import json

with open("kontakte.json", mode="r", encoding="utf-8") as json_file:
    kontakte = json.load(json_file)

print(f'type(kontakte) : {type(kontakte)}')
print(kontakte)
print('---')
for kontakt in kontakte['kontakte']:
    print(f"Name    : {kontakt['name']['vorname']} {kontakt['name']['nachname']}")
    print(f"Adresse : {kontakt['adresse']['plz']} {kontakt['adresse']['ort']}, {kontakt['adresse']['strasse']}")
    print(f"Telefon : privat: {kontakt['telefon']['privat']} , mobil: {kontakt['telefon']['mobil']}")
    print(f"E-Mail  : {kontakt['email']}")
    print('---')
