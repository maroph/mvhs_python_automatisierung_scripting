import csv

with open('output.out.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Datum', 'Äpfel', 'Bananen', 'Kiwi'])
    writer.writerow(['2025-07-03', '2', '4', '0'])
    writer.writerow(['2025-07-07', '3', '2', '0'])

with open('output2.out.csv', 'w', encoding='utf-8', newline='') as f:
    fieldnames = ['Datum', 'Äpfel', 'Bananen', 'Kiwi']
    dict_writer = csv.DictWriter(f, fieldnames=fieldnames)
    # quoting: https://docs.python.org/3/library/csv.html#csv-constants
    # csv.QUOTE_ALL, csv.QUOTE_MINIMAL, csv.QUOTE_NONNUMERIC,
    # csv.QUOTE_NONE, csv.QUOTE_NOTNULL, csv.QUOTE_STRINGS
    # dict_writer = csv.DictWriter(f, fieldnames=fieldnames, quoting=csv.QUOTE_STRINGS)
    dict_writer.writeheader()
    dict_writer.writerow({'Datum': '2025-07-03', 'Äpfel': '2', 'Bananen': '4', 'Kiwi': '0'})
    dict_writer.writerow({'Datum': '2025-07-07', 'Äpfel': '3', 'Bananen': '2', 'Kiwi': '0'})

print('Inhalt der Datei output2.out.csv')
print('---')
with open('output2.out.csv', 'r', encoding='utf-8', newline='') as f:
    for line in f.readlines():
        print(line, end='')
