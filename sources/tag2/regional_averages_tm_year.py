import csv

# https://www.dwd.de/opendata
# https://www.dwd.de/opendatahelp
# https://www.dwd.de/DE/leistungen/_functions/Suche/Suche_Formular.html
# https://dwd-geoportal.de/
#
# Quelle der Datei regional_averages_tm_year.csv:
# https://opendata.dwd.de/climate_environment/CDC/regional_averages_DE/annual/air_temperature_mean/regional_averages_tm_year.txt
csv_file = 'regional_averages_tm_year.csv'

with open (csv_file, encoding='utf-8', newline='') as f:
    reader = csv.reader(f, delimiter=';')
    next(reader)
    next(reader)
    print('---')
    for row in reader:
        print(f'Deutschland : {row[0]}: {row[-2].strip():>5}')
        print(f'Bayern      : {row[0]}: {row[5].strip():>5}')
        print('---')

print()
print('='*50)
print()

with open (csv_file, encoding='utf-8', newline='') as f:
    reader = csv.DictReader(f, delimiter=';', fieldnames=('Jahr','Platzhalter',',Brandenburg/Berlin','Brandenburg','Baden-Wuerttemberg','Bayern','Hessen','Mecklenburg-Vorpommern','Niedersachsen','Niedersachsen/Hamburg/Bremen','Nordrhein-Westfalen','Rheinland-Pfalz','Schleswig-Holstein','Saarland','Sachsen','Sachsen-Anhalt','Thueringen/Sachsen-Anhalt','Thueringen','Deutschland','EMPTY'))
    next(reader)
    next(reader)
    print('---')
    for row in reader:
        print(f'Deutschland : {row['Jahr']}: {row['Deutschland'].strip():>5}')
        print(f'Bayern      : {row['Jahr']}: {row['Bayern'].strip():>5}')
        print('---')
