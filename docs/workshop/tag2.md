# Tag 2 (10.07.2025)

## CSV Dateien
[Wikipedia: CSV (Dateiformat)](https://de.wikipedia.org/wiki/CSV_(Dateiformat)):
Das Dateiformat CSV steht für englisch "Comma-separated values" 
und beschreibt den Aufbau einer Textdatei zur Speicherung oder 
zum Austausch einfach strukturierter Daten.

Jede Zeile in einer CSV-Datei entspricht einer Zeile in einer
Tabelle. Die einzelnen Spalten werden durch ein Komma (',')
voneinander getrennt.

Beispiel:
```
Name,Vorname,Straße,PLZ,Ort
Maier,Anne,Dorfstraße,12345,Dorf
Müller,David,Ortstraße,54321,Ort
Muster,Mila,Stadtstraße,13524,Stadt
```

Für das Lesen/Schreiben von CSV-Dateien kann man das Modul 
[csv](https://docs.python.org/3/library/csv.html)
verwenden.

### CSV Lesen

Beispiel:

```
import csv

with open (csv_file, encoding='utf-8', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
```

Das obige Programm erzeugt die folgende Ausgabe: 

```
['Name', 'Vorname', 'Straße', 'PLZ', 'Ort']
['Maier', 'Anne', 'Dorfstraße', '12345', 'Dorf']
['Müller', 'David', 'Ortstraße', '54321', 'Ort']
['Muster', 'Mila', 'Stadtstraße', '13524', 'Stadt']
```

**Hinweis**:  
Das _open_ Argument

```
newline=''
```

sollte man beim Arbeiten mit CSV-Dateien immer angeben, da sowohl
_open_ als auch _csv.writer_ versuchen, Zeilenumbrüche zu 
handhaben.

Beispiel: Ausgabe einzelner Felder/Spalten

```
with open (csv_file, encoding='utf-8', newline='') as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        print(f'{row[1]:<5} {row[0]}')
```

Ausgabe

```
Anne  Maier
David Müller
Mila  Muster
```

Mit dem Attribut _line_num_ erhält man die jeweilige
Zeilennummer in der CSV-Datei.

Beispiel: 
```
with open (csv_file, encoding='utf-8', newline='') as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        print(f'{reader.line_num} : {row[1]:<5} {row[0]}')
```

Ausgabe

```
2 : Anne  Maier
3 : David Müller
4 : Mila  Muster
```

Neben dem 
[reader](https://docs.python.org/3/library/csv.html#csv.reader) 
kann man auch einen
[DictReader](https://docs.python.org/3/library/csv.html#csv.DictReader)
verwenden.

Der _DictReader_ liest die erste Zeile als Header Zeile ein und 
erzeugt für jede weitere Zeile ein Dictionary mit dem Spaltennamen
als Key und dem Inhalt als Value.

Zusätzlich zum Attribut _line_num_ hat ein _DictReader_ das
Attribut _fieldNames_. Dieses Attribut gibt die Namen der
Spalten/Felder als Liste zurück.

Beispiel: 

```
with open (csv_file, encoding='utf-8', newline='') as f:
    reader = csv.DictReader(f)
    print('Fieldnames:', reader.fieldnames)
    for row in reader:
        print(f'{reader.line_num} : {row['Vorname']:5} {row['Name']}')
```

Ausgabe:

```
Fieldnames: ['Name', 'Vorname', 'Straße', 'PLZ', 'Ort']
2 : Anne  Maier
3 : David Müller
4 : Mila  Muster
```

Enthät die CSV-Datei keine Headerzeile, kann man die Namen
als Liste übergeben.

Beispiel:

```
with open (csv_file, encoding='utf-8', newline='') as f:
    reader = csv.DictReader(f, fieldnames=('COL1', 'COL2', 'COL3', 'COL4', 'COL5'))
    print('Fieldnames:', reader.fieldnames)
    for row in reader:
        print(f'{reader.line_num} : {row['COL2']:5} {row['COL1']}')
```

Ausgabe:

```
Fieldnames: ('COL1', 'COL2', 'COL3', 'COL4', 'COL5')
1 : Vorname Name
2 : Anne  Maier
3 : David Müller
4 : Mila  Muster
```

Da der _DictReader_ in diesem Fall keine Headerzeile erwartet,
wird im obigen Beispiel diese Zeile mit ausgegeben. Mit dem Aufruf
_next(reader)_ vor der _for_ Schleife kann man diese Zeile
überspringen.

#### Code Beispiele

* [csv_lesen.py](https://raw.githubusercontent.com/maroph/mvhs_python_automatisierung_scripting/main/sources/tag2/csv_lesen.py)
* [regional_averages_tm_year.py](https://raw.githubusercontent.com/maroph/mvhs_python_automatisierung_scripting/main/sources/tag2/regional_averages_tm_year.py)
* [csv_import_to_sqlite.py](https://raw.githubusercontent.com/maroph/mvhs_python_automatisierung_scripting/main/sources/tag2/csv_import_to_sqlite.py)

### CSV Schreiben
Zum Schreiben einer CSV-Datei kann man einen 
[writer](https://docs.python.org/3/library/csv.html#csv.writer) 
oder auch einen
[DictWriter](https://docs.python.org/3/library/csv.html#csv.DictWriter)
verwenden.

```
with open('output.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Datum', 'Äpfel', 'Bananen', 'Kiwi'])
    writer.writerow(['2025-07-03', '2', '4', '0'])
    writer.writerow(['2025-07-07', '3', '2', '0'])
```

```
with open('output.csv', 'w', encoding='utf-8', newline='') as f:
    fieldnames = ['Datum', 'Äpfel', 'Bananen', 'Kiwi']
    dict_writer = csv.DictWriter(f, fieldnames=fieldnames)
    dict_writer.writeheader()
    dict_writer.writerow({'Datum': '2025-07-03', 'Äpfel': '2', 'Bananen': '4', 'Kiwi': '0'})
    dict_writer.writerow({'Datum': '2025-07-07', 'Äpfel': '3', 'Bananen': '2', 'Kiwi': '0'})
```

#### Code Beispiel
* [csv_schreiben.py](https://raw.githubusercontent.com/maroph/mvhs_python_automatisierung_scripting/main/sources/tag2/csv_schreiben.py)


## JSON Dateien
[Wikipedia: JSON](https://de.wikipedia.org/wiki/JSON): 
Die JavaScript Object Notation (JSON) ist ein kompaktes
Datenformat in einer einfach lesbaren Textform für den
Datenaustausch zwischen Anwendungen. JSON ist von
Programmiersprachen unabhängig. Parser und Generatoren
existieren in den meisten verbreiteten Sprachen.

Es wird eine Schlüssel-Wert-Struktur (ähnlich wie in Python
Dictionaries) verwendet.

Die folgenden beiden Quellen geben eine gute Übersicht zur
JSON Syntax:

* [Introducing JSON](https://www.json.org/json-en.html)
* [ECMA-404: The JSON Data
Interchange Syntax](https://ecma-international.org/publications-and-standards/standards/ecma-404/)
    * [ECMA-404: lokale Kopie](./ECMA-404_2nd_edition_december_2017.pdf)

**JSON Beispiel**

```
{
  "name": "Anna",
  "alter": 25,
  "hobbys": ["lesen", "reisen"]
}
```

**JSON Datentypen**  

| JSON Datentyp | Beschreibung                                                                |
|:--------------|:----------------------------------------------------------------------------|
| object        | Eine Sammlung von Key-Value Paren innerhalb von geschwungenen Klammern ({}) |
| array         | Eine Liste von Werten, innerhalb eckiger Klammern ([])                      |
| string        | Text innerhalb vcn Anführungszeichen ("")                                   |
| number        | Ganze Zahlen oder Dezimalzahlen                                             |
| boolean       | Entweder true oder false - ohne Anführungszeichen                           |
| null          | Repräsentiert einen Null Wert. Wird null geschrieben                        |


**Python vs JSON**  

| Python       | JSON   |
|:-------------|:-------|
| dict | object |
| list | array  |
| tuple | array  |
| str | string |
| int | number |
| float | number |
| True | true |
| False | false |
| None | null |

Zur Bearbeitung von JSON Daten kann das Modul
[json](https://docs.python.org/3/library/json.html)
verwendet werden.

Eine gute Übersicht zur Verwendung von JSON in Python 
findet man im Artikel 
[Working With JSON Data in Python](https://realpython.com/python-json/).
