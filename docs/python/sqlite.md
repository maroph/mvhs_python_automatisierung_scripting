# SQLite
[SQLite](https://www.sqlite.org/) ist eine 
[public-domain](https://www.sqlite.org/copyright.html)
SQL Datenbankimplementierung. Die Software ist in der
Programmiersprache C geschrieben. Zur Python 
Laufzeitumgebung gehört das Modul 
[sqlite3](https://docs.python.org/3/library/sqlite3.html),
das die Nutzung dieser Datenbank ermöglicht.

Beispiele für die Nutzung der Datenbank findet man im 
[SQLite Tutorial](https://www.sqlitetutorial.net/). 
Dort ist auch das 
[Python Binding](https://www.sqlitetutorial.net/sqlite-python/)
für die SQL Aufrufe beschrieben.

Eine Übersicht zur Funktionalität von SQLite findet man
in dem folgenden Artikel: 
[Wikipedia:SQLite](https://de.wikipedia.org/wiki/SQLite).

## Database GUI
Als GUI für eine SQLite Datenbank kann man den 
[DB Browser for SQLite](https://sqlitebrowser.org/)
verwenden.

## Zeitstempel (Datetime)
Zeitstempel (Datum und Uhrzeit) werden in einer SQLite
Datenbank als String (Typ TEXT) oder Zahl (Typ
INTEGER) in der Datenbank abgelegt. Dabei werden die
folgenden Formate verwendet:

**Zeitstempel als String**  
```
YYYY-MM-DD HH:mm:ss[.SSS]
```

Beispiel:  
```
2025-04-28 16:36:42 oder auch 2025-04-28 16:36:42:123
```

**Zeitstempel als Zahl**
```
<zahl: Zeit in Sekunden seit dem 01.01.1970>
```

Beispiel:  
```
1745933801  - 2025-04-29 15:36:41
```

Mehr Details zu den unterstützen Formaten findet man
in den Kapiteln
[Datatypes In SQLite](https://www.sqlite.org/datatype3.html) und 
[Date And Time Functions](https://www.sqlite.org/lang_datefunc.html) der
[SQLite Dokumentation](https://www.sqlite.org/docs.html).

In Python werden Zeitstempel in einem datetime Objekt
abgelegt.

Es bleibt die Frage, wie man diese verschiedenen
Formate (SQLite und Python) zusammenbringt.

Hierfür gibt es zwei Lösungen. Für beide Lösungen
habe ich ein kleines Python Programm geschrieben,
um das jeweilige Verhalten zu demonstrieren

- [logdb_sample.py]{:target="blank"}  
  In diesem Beispiel nutze ich die automatische
  Konvertierung zwischen Zeitstempel in der Datenbank
  und datetime Objekt im Python Programm.
- [logdb_sample2.py]{:target="blank"}  
  In diesem Beispiel führe ich eine manuelle 
  Konvertierung zwischen Zeitstempel in der Datenbank
  und datetime Objekt im Python Programm aus.

[logdb_sample.py]: https://raw.githubusercontent.com/maroph/mvhs_python_automatisierung_scripting/main/sources/extras/logdb_sample.py

[logdb_sample2.py]: https://raw.githubusercontent.com/maroph/mvhs_python_automatisierung_scripting/main/sources/extras/logdb_sample2.py

In den Beispielen wird eine Tabelle _logrecords_ verwendet,
in der Logsätze gesammelt werden. Die Tabelle enthält
die folgenden Felder:

- log_id  
  Eine eindeutige ID (Integer).
- log_level  
  LogLevel
    - 6 : FATAL
    - 5 : ERROR
    - 4 : WARN
    - 3 : INFO
    - 2 : DEBUG
    - 1 : TRACE
- log_dt  
  Zeitstempel der Erzeugung des Logsatzes.
- log_msg  
  Logging Message (String).

### Python: automatische Konvertierung
[logdb_sample.py]{:target="blank"}

[logdb_sample.py]: https://raw.githubusercontent.com/maroph/mvhs_python_automatisierung_scripting/main/sources/extras/logdb_sample.py

Beim Aufruf der Funktion 
[sqlite3.connect()](https://docs.python.org/3/library/sqlite3.html#sqlite3.connect)

kann man zusätzlich das Argument

```
detect_types=sqlite3.PARSE_DECLTYPES
```

angeben. Für die Konvertierung der Datentypen werden
dann Adapter- und Konverterfunktionen verwendet.

Eine Beschreibung hierzu findet man hier: 
[Adapter and converter recipes](https://docs.python.org/3/library/sqlite3.html#adapter-and-converter-recipes).

**Adapterfunktionen**  
```
def adapt_date_iso(val: datetime.date) -> str :
    """Adapt datetime.date to ISO 8601 date."""
    return val.isoformat()

def adapt_datetime_iso(val: datetime.datetime) -> str :
    """Adapt datetime.datetime to timezone-naive ISO 8601 date."""
    return val.isoformat()

def adapt_datetime_epoch(val: datetime.datetime) -> float:
    """Adapt datetime.datetime to Unix timestamp."""
    print(f"adapt_datetime_epoch(val) : {val} : type(val) : {type(val)}")
    return int(val.timestamp())
```

**Zugehörige Register Funktionen**  
```
sqlite3.register_adapter(datetime.date, adapt_date_iso)
sqlite3.register_adapter(datetime.datetime, adapt_datetime_iso)
sqlite3.register_adapter(datetime.datetime, adapt_datetime_epoch)
```

**Konverterfunktionen**
```
def convert_date(val: str) -> datetime.date:
    """Convert ISO 8601 date to datetime.date object."""
    return datetime.date.fromisoformat(val.decode())

def convert_datetime(val: str) -> datetime.datetime:
    """Convert ISO 8601 datetime to datetime.datetime object."""
    return datetime.datetime.fromisoformat(val.decode())

def convert_timestamp(val: float) -> datetime.datetime:
    """Convert Unix epoch timestamp to datetime.datetime object."""
    return datetime.datetime.fromtimestamp(int(val))
```

**Zugehörige Register Funktionen**  
```
sqlite3.register_converter("date", convert_date)
sqlite3.register_converter("datetime", convert_datetime)
sqlite3.register_converter("timestamp", convert_timestamp)
```

Die jeweiligen Funktionsnamen können frei gewählt werden
und müssen dann beim Aufruf der jeweiligen _register_XXX_
Funktion angegeben werden.

Bis Python 3.11 gab es Standardkonverter, die man - 
ohne eigene Implementierung - nutzen konnte. Ab 
Python 3.12 sind die Standardkonverter deprecated und
sollten nicht mehr genutzt werden.

Damit die Konverter aufgerufen werden, gibt man bei der
Deklaration eines Zeitstempel Feldes in einer Tabelle
den Typ `TIMESTAMP` statt `TEXT` oder `INTEGER` an.

```
CREATE TABLE IF NOT EXISTS logrecords (
    log_id    INTEGER PRIMARY KEY AUTOINCREMENT,
    log_level INTEGER NOT NULL,
    log_dt    TIMESTAMP NOT NULL,
    log_msg   TEXT NOT NULL
)
```

### Python: manuelle Konvertierung
[logdb_sample2.py]{:target="blank"}

[logdb_sample2.py]: https://raw.githubusercontent.com/maroph/mvhs_python_automatisierung_scripting/main/sources/extras/logdb_sample2.py

Für die Zeitstempel in der Datenbank nutze ich in diesem
Fall die Formate

```
YYYY-MM-DD HH:mm:ss
```

und

```
YYYY-MM-DD HH:mm:ss.mmmmmm localtime
```

Für die Umwandlung zwischen datetime und Zeitstempel
habe ich die folgenden Funktionen geschrieben:

```
def dt_string_to_dt(dt_string: str) -> datetime

def dt_to_dt_string(dt: datetime.datetime) -> str:
```

In diesem Beispiel sind 2 Fälle programmiert:

1. Verwendung der lokalen Zeit im Python Programm
   und in der Datenbank.
2. Verwendung der lokalen Zeit im Python Programm
   und UTC Zeit in der Datenbank.

```
use_utc: bool = False
```

Die Tabelle in der Datenbank ist folgendermaßen deklariert:

```
CREATE TABLE IF NOT EXISTS logrecords (
    log_id    INTEGER PRIMARY KEY AUTOINCREMENT,
    log_level INTEGER NOT NULL,
    log_dt    TEXT NOT NULL,
    log_msg   TEXT NOT NULL
)
```


```
use_utc: bool = True
```

Die Tabelle in der Datenbank ist in diesem Fall 
folgendermaßen deklariert:

```
CREATE TABLE IF NOT EXISTS logrecords (
    log_id    INTEGER PRIMARY KEY AUTOINCREMENT,
    log_level INTEGER NOT NULL,
    log_dt    TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    log_msg   TEXT NOT NULL
)
```

Die Deklaration

```
log_dt TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
```

hat den **Vorteil**, das man beim _SQL INSERT_ das Feld
_log_dt_ nicht mit angeben muss und es von der Datenbank
dann automatisch belegt wird. Der **Nachteil** dieser
Deklaration ist, das der Zeitstempel als UTC Zeit und nicht
als lokale Zeit abgelegt wird.

Gibt man den Zeitstempel beim _SQL INSERT_ mal an und mal
nicht, enthält der Zeitstempel die Zeit mal als UTC Zeit
und mal als lokale Zeit. Da aber alle Zeitstempel das
Format 

```
YYYY-MM-DD HH:mm:ss
```

haben, wäre nicht mehr klar, wann der Eintrag erzeugt
wurde.

Um dieses Problem zu umgehen, verwende ich in diesem Fall
für die Zeitstempel generell die UTC Zeit.

---

## Weiterführende Links

* [SQLite](https://www.sqlite.org/)
    * [Documentation](https://www.sqlite.org/docs.html) 
* [DB Browser for SQLite](https://sqlitebrowser.org/)
* [Python module sqlite3](https://docs.python.org/3/library/sqlite3.html)
    * [Tutorial](https://docs.python.org/3/library/sqlite3.html#tutorial) 
* [SQLite Tutorial](https://www.sqlitetutorial.net/)
    * [Python Binding](https://www.sqlitetutorial.net/sqlite-python/)
* [Python SQLite tutorial using sqlite3](https://pynative.com/python-sqlite/)
