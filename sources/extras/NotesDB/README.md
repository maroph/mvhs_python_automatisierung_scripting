# NotesDB
Die Datei notesdb.py enthält die Klasse NotesDB.

Die Klasse NotesDB implementiert eine sehr vereinfachte
Möglichkeit, Notizen zu verwalten. 

Mit diesem Beispiel wollte ich die folgenden Ding
ausprobieren:

* Datenbank  
  Zugriff aus Python auf eine Datenbank.
* Logging  
  Nutzung des Python logging Moduls.
* Docstring  
  Verwenden von Python Docstrings für die Code
  Documentation.
* pytest  
  Schreiben einfacher Tests mit pytest.

Hinweis:  
Ein einfaches Beispiel mit einer GUI findet man in dem
folgenden Artikel:  
[Build a Contact Book With Python, PyQt, and SQLite](https://realpython.com/python-contact-book/)

## Datenbank
Der 
[SQLite](https://www.sqlite.org/)
Treiber/Connnector ist Teil der Python Distribution. 
Darum habe ich diese Datenbank der Einfachheit halber
für mein Beispiel verwendet.

### Datenbankstruktur

#### Tabelle
Die Notizen werden in der Tabelle _notes_ gespeichert.

```
CREATE TABLE IF NOT EXISTS notes(
    note_id INTEGER PRIMARY KEY,
    title   TEXT NOT NULL,
    note    TEXT NOT NULL,
    cdt     TIMESTAMP NOT NULL,
    mdt     TIMESTAMP NOT NULL
)
```

Die Felder in der Tabelle haben die folgende Bedeutung:

* note_id  
  Jede Notiz erhält eine eindeutige Zahl (ID) beim Eintrag
  (INSERT) in die Tabelle.
* title  
  Der Titel der Notiz.
* note  
  Der Text der Notiz.
* cdt  
  Zeitpunkt der Erzeugung der Notiz als Datetime 
  (Datum, Uhrzeit).
* mdt  
  Zeitpunkt der letzten Änderung der Notiz als Datetime.

In der Methode
```
def note_add(self, title: str, note: str) -> int:
```

werden neue Notizen in die Datenbank eingetragen (INSERT)

```
INSERT INTO notes (title,note,cdt,mdt) VALUES(?,?,?,?)
```

Die Werte für _title_ und _note_ werden an die Methode
übergeben. Die Felder _cdt_ und _mdt_ werden mit dem
Wert _now_ versorgt, der vom Typ _datetime.datetime_
ist.

```
now = datetime.now()
```

Das Feld _note_id_ wird von der Datenbank automatisch
erzeugt. Im Code wird gezeigt, wie man nach dem _INSERT_
diesen Wert auslesen kann.

#### Indizes
Für den Zugriff auf die Daten verwende ich die folgenden
Indizes:

```
CREATE UNIQUE INDEX IF NOT EXISTS idx_unique ON notes(cdt,title)
CREATE INDEX IF NOT EXISTS idx_cdt ON notes(cdt)
CREATE INDEX IF NOT EXISTS idx_mdt ON notes(mdt)
CREATE INDEX IF NOT EXISTS idx_title ON notes(title)
```

In meinem Beispiel wird derzeit nur die Indizes
_idx_unique_ und _idx_mdt_ verwendet.

### Weiterführende Links
* [Python module sqlite3](https://docs.python.org/3/library/sqlite3.html)
* [SQLite Tutorial](https://www.sqlitetutorial.net/)
* [Python SQLite tutorial using sqlite3](https://pynative.com/python-sqlite/)

## Logging
Teil der Python Distribution ist das Modul 
[logging](https://docs.python.org/3/library/logging.html).
In meiner Klasse _NotesDB_ verwende ich die Log Level 
ERROR, INFO und DEBUG. Das Standardlevel ist ERROR.

## Docstring
Mit der Hilfe von Docstrings kann man seinen Python Code
dokumentieren. Die Verwendung von Docstrings ist in den
folgenden
[Python Enhancement Proposals](https://peps.python.org/)
beschrieben:

* [PEP 8 – Style Guide for Python Code](https://peps.python.org/pep-0008/)
* [PEP 257 – Docstring Conventions](https://peps.python.org/pep-0257/) 

Leider sind die Beschreibungen in den PEPs, für meine
Begriffe, relativ vage. Deshalb folge ich in meinen
Docstrings den Beispielen im Artikel
[Python Docstrings](https://www.geeksforgeeks.org/python-docstrings/).

In Python kann man alle Docstrings der Klasse _NotesDB_
folgendermaßen ausgeben:

```
help(NotesDB)
```

Einzelne Docstrings erhält man folgendermaßen:

```
print(NotesDB.__doc__)
print(NotesDB.__init__.__doc__)
print(NotesDB.note_add.__doc__)
...
```

## pytest
Für die Klasse habe ich einige sehr einfache pytest 
Testfälle geschrieben. Für den Ablauf werden die beiden
Module

* [pytest](https://pypi.org/project/pytest/)
* [pytest-order](https://pypi.org/project/pytest-order/)

benötigt. Den Test kann man folgendermaßen ablaufen lassen:

```
pytest notesdb_pytest.py -vv -s
```
