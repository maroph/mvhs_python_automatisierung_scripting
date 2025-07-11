import csv

csv_file = 'adressen.csv'

with open (csv_file, encoding='utf-8', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        # print(row)
        print(f'{reader.line_num} : {row}')

print()

with open (csv_file, encoding='utf-8', newline='') as f:
    reader = csv.reader(f)
    next(reader)
    # header = next(reader)
    # print(f'header : {header}')
    for row in reader:
        # print(f'{row[1]:<5} {row[0]}')
        print(f'{reader.line_num} : {row[1]:<5} {row[0]}')

print()

with open (csv_file, encoding='utf-8', newline='') as f:
    reader = csv.DictReader(f)
    # reader = csv.DictReader(f, fieldnames=('COL1', 'COL2', 'COL3', 'COL4', 'COL5'))
    # next(reader)
    print('Fieldnames:', reader.fieldnames)
    for row in reader:
        print(f'{reader.line_num} : {row['Vorname']:5} {row['Name']}')
        # print(f'{reader.line_num} : {row['COL2']:5} {row['COL1']}')
