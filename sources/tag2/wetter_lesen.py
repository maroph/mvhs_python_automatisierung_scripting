import json

with open("wetter.json", mode="r", encoding="utf-8") as json_file:
    wetter = json.load(json_file)
print(wetter)

print(f'Wetter in {wetter["stadt"]}')
print(f'  Aktuell: {wetter["temperatur"]["aktuell"]}\u00B0 Grad')
print(f'  Zustand: {wetter["wetter"]}')
