# Lesen der Datei adressen.csv und die Daten in eine
# SQLite Tabelle eintragen.
from contextlib import closing
import csv
from pathlib import Path
import sqlite3

try:
    # Erzeuge die SQLite Datenbank ind er Datei sqlite.db
    path = Path('sqlite.db')
    # Lösche die Datei, falls bereits voirganden
    path.unlink(missing_ok=True)

    # Öffne eine Verbindung zur SQLite Datenbank.
    with sqlite3.connect(path.name) as sqlite_connection:
        # Erzeuge einen Cursor für die Datenbankzugriffe
        with closing(sqlite_connection.cursor()) as cursor:
            cursor.execute("""CREATE TABLE IF NOT EXISTS adressen
                              (
                               name    TEXT,
                               vorname TEXT,
                               plz     INTEGER,
                               ort     TEXT,
                               strasse TEXT
                               )""")

            with open('adressen.csv', encoding='utf-8', newline='') as f:
                # Erzeuge eine DictReader für die CSV-Datei
                dr = csv.DictReader(f)
                for csv_row in dr:
                    # Lese die CSV-Datei zeilenweise
                    print(f'{csv_row['Name']}|{csv_row['Vorname']}|{csv_row['PLZ']}|{csv_row['Ort']}|{csv_row['Straße']}')
                    # Füge die Daten der Zeile in die Tabelle der Datenbank ein
                    cursor.execute("INSERT INTO adressen (name,vorname,plz,ort,strasse) VALUES(?,?,?,?,?)",
                                   (csv_row['Name'], csv_row['Vorname'], csv_row['PLZ'], csv_row['Ort'], csv_row['Straße']))
            # Schließe die Transaktion. Die Daten sind danach
            # für alle in der Datenbank sichtbar
            sqlite_connection.commit()

        print()
        print('---')
        print()

        with closing(sqlite_connection.cursor()) as cursor:
            # Lese die Tabelle aus der Datenbank aus
            cursor.execute('SELECT * FROM adressen')
            while (sql_row := cursor.fetchone()):
                # Ausgabe der einzelnen Datensätze
                print(sql_row)
except FileNotFoundError as e:
    print(f'CSV-Datei: nicht gefunden: {e}')
except PermissionError as e:
    print(f'CSV-Datei: kein Lesezugriff: {e}')
except OSError as e:
    print(f'OSError: {e}')
except csv.Error as e:
    print(f'CSV-Fehler: {e}')
except sqlite3.Error as e:
    print(f'SQLite Fehler: {e}')
