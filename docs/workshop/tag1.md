# Tag 1 (03.07.2025)

## Lesen und Schreiben von Dateien

### Datei öffnen
Dateien werden mit der Funktion 
[open](https://docs.python.org/3/library/functions.html#open)
geöffnet.

```
open(<datei>, <modus>) – liefert Dateiobjekt zurück

Datei: Name der Datei
Im selben Verzeichnis reicht der Name der Datei.
Ansonsten muss ein relativer/absoluter Pfadname
verwendet werden.

Modus:
r  – lesen (Standard), Fehler falls Datei nicht da
a  – anhängen, Datei wird erstellt, falls nicht da
w  – schreiben, Datei wird erstellt, falls nicht da
x  – erstellen, Fehler, wenn Datei existiert
a+ - anhängen, schreiben und lesen, Datei wird erstellt falls nicht da
r+ - lesen und update, Fehler, wenn Datei nicht da
w+ – schreiben und update, Datei erstellt, falls nicht da
Für binary b ergänzen
```

#### Beispiel: Absolute Pfadangabe
Befindet sich die Datei im selben Verzeichnis wie das
Skript, aber Python wird aus einem anderen Verzeichnis
aufgerufen, muss ein Pfadname verwendet werden, da die
Datei sonst nicht gefunden wird. Diesen Pfad kann
man folgendermaßen erzeugen:

```
import os

# Ordner ermitteln
skript_ordner = os.path.dirname(__file__)

# Ordner mit dem Dateinamen verbinden
dateipfad = os.path.join(skript_ordner, 
'datei.txt'
```

### Datei lesen

```
f = open('text.txt', 'r', encoding='utf-8')
content = f.read()
print(content)
f.close()
```

#### Kompakter mit with

```
with open('text.txt', 'r', encoding='utf-8') as f:
    content = f.read()
print(content)
```
Beispiele:  

* [lesen.py](https://raw.githubusercontent.com/maroph/mvhs_python_automatisierung_scripting/main/sources/tag1/lesen.py)
* [lesen_zeilenweise](https://raw.githubusercontent.com/maroph/mvhs_python_automatisierung_scripting/main/sources/tag1/lesen_zeilenweise.py)
* [lesen_n_zeilen.py](https://raw.githubusercontent.com/maroph/mvhs_python_automatisierung_scripting/main/sources/tag1/lesen_n_zeilen.py)
* [read_birthday_in_pi.py](https://raw.githubusercontent.com/maroph/mvhs_python_automatisierung_scripting/main/sources/tag1/read_birthday_in_pi.py)

### Datei schreiben

```
with open('data.txt', 'w') as f:
    # Datei wird erstellt, falls nicht vorhanden
    f.write('Hello, world!')
```

Beispiel: [schreiben.py](https://raw.githubusercontent.com/maroph/mvhs_python_automatisierung_scripting/main/sources/tag1/schreiben.py)

## Module für die Automatisierung
Ein Modul ist eine Datei, die Python Definitionen und
Befehle enthält (z.B. Funktionen, Methoden, Konstanten,
Klassen etc.).

Die folgenden Module werden in der Automatisierung
häufig verwendet:

* [os](https://docs.python.org/3/library/os.html): Arbeiten mit dem Betriebssystem (Dateien, 
Verzeichnisse).
* [shutil](https://docs.python.org/3/library/shutil.html): Höhere Dateimanipulation (Kopieren, Verschieben).
* [pathlib](https://docs.python.org/3/library/pathlib.html): Komfortables Arbeiten mit Pfaden
* [send2trash](https://pypi.org/project/Send2Trash/): Sicheres Löschen  
* [datetime](https://docs.python.org/3/library/datetime.html), [dateutil](https://dateutil.readthedocs.io/en/stable/) für Operationen mit Datumsangaben

Das Modul send2trash muss mit pip extra installiert
werden. Die anderen Module gehören zur Stand Python
Laufzeitumgebung.

### Packages installieren
Die meisten Module werden als Packages auf der Seite
[PyPi](https://pypi.org/) zur Verfügung gestellt. Diese
Packages kann man folgendermaßen auf seinem System
installieren:

```
python -m pip install package_name
```

Beispiel send2trash:

```
python -m pip install send2trash
```

### Module importieren
Module müssen vor der Nutzung mit der Anweisung
_import_ in das Skript importiert werden.

Beispiel:
```
import os
print(os.getcwd()) # aktuelles Arbeitsverzeichni
 from os import getcwd
 print(getcwd())  # aktuelles Arbeitsverzeichnis
```

Alternativ:
```
from os import getcwd
print(getcwd())  # aktuelles Arbeitsverzeichnis
```

Bei der _import_ Anweisung kann auch ein Alias 
angegeben werden:

```
import modul as alias

oder

from module import name as alias
```

Beim Zugriff wird dann der Aliasnamen verwendet.

### Modul os

* [os.getcwd()](https://docs.python.org/3/library/os.html#os.getcwd)  
  Gibt das aktuelle Arbeitsverzeichnis zurück.
* [os.mkdir(name)](https://docs.python.org/3/library/os.html#os.mkdir)  
  Ordner erstellen über relative|absolute Pfadangabe, falls
  vorhanden wird ein FileExistsError geworfen.
* [os.makedirs(name1/name2)](https://docs.python.org/3/library/os.html#os.makedirs)  
  Ordner mit Unterordner(n) erzeugen.
* [os.listdir(name)](https://docs.python.org/3/library/os.html#os.listdir)  
  Gibt eine Liste vom Verzeichnisinhalt zurück, aber
  ohne die Verzeichnisse . und ..
* [os.walk(top)](https://docs.python.org/3/library/os.html#os.walk)  
  Git das Tuple (dirpath, dirnames, filenames) zurück.
    * dirpath  
      Ist der Pfad zum Verzeichnis
    * dirnames  
      Liste mit allen Verzeichnisnamen
    * filenames  
      Liste mit allen Dateinamen

#### Submodul os.path
* [os.path](https://docs.python.org/3/library/os.path.html)  
  Arbeiten an Pfadnamen
* [os.path.exists(datei)](https://docs.python.org/3/library/os.path.html#os.path.exists)  
  Prüft, ob die Datei vorhanden ist
* [os.path.dirname(datei)](https://docs.python.org/3/library/os.path.html#os.path.dirname)  
  Gibt von einem Pfad den Ordnernamen zurück
* [os.path.basename(datei)](https://docs.python.org/3/library/os.path.html#os.path.basename)  
  Gibt von einem Pfad den Dateinamen zurück  
* file_name, file_extension = [os.path.splitext(datei)](https://docs.python.org/3/library/os.path.html#os.path.splitext)  
  Spaltet den Pfadnamen in (root, ext) auf. 
* [os.path.join(verzeichnis, datei)](https://docs.python.org/3/library/os.path.html#os.path.join)  
  Einen Pfad zusammensetzen 
* [os.path.isdir()]()  
  Prüft, ob der Pfad ein Verzeichnis ist.
* [os.path.isfile()]()  
  Prüft, ob der Pfad eine Datei ist.
* [os.path.exists()]()  
  Prüft, ob es den Pfad gibt
* [os.path.expanduser('~')]()  
  Expandiert ~ zum Namen des Benutzerverzeichnisses

#### Beispiele
##### Absoluten Pfad ermitteln

```
import os
# Holt den Ordner, in dem das Skript liegt
# Die Dunder-Variable __file__ enthält Pfad 
# zu der aktuellen Datei.
skript_ordner = os.path.dirname(__file__)

# Verbindet ihn mit dem Dateinamen
dateipfad = os.path.join(skript_ordner, 'adressen.csv')
```

##### os.path.join()
Dateipfade betriebssystemgerecht zusammenzusetzen 
(/ oder \\, je nach System)

```
import os
pfad = os.path.join("Ordner", "unterordner", "datei.txt")
print(pfad)
# Windows: "Ordner\unterordner\datei.txt"
# macOS/Linux: "Ordner/unterordner/datei.txt"
```

##### Alle Dateien aus Ordner auflisten

```
import os
for file in os.listdir('beispielordner'):
    print(file)
```

##### Weitere Beispiele

* [dateien_auflisten1.py](https://raw.githubusercontent.com/maroph/mvhs_python_automatisierung_scripting/main/sources/tag1/dateien_auflisten1.py)
* [dateien_auflisten2.py](https://raw.githubusercontent.com/maroph/mvhs_python_automatisierung_scripting/main/sources/tag1/dateien_auflisten2.py)
* [verschachtelte_verzeichnisse.py](https://raw.githubusercontent.com/maroph/mvhs_python_automatisierung_scripting/main/sources/tag1/verschachtelte_verzeichnisse.py)
* [ordner_erstellen.py](https://raw.githubusercontent.com/maroph/mvhs_python_automatisierung_scripting/main/sources/tag1/ordner_erstellen.py)
* [groesste_datei.py](https://raw.githubusercontent.com/maroph/mvhs_python_automatisierung_scripting/main/sources/tag1/groesste_datei.py)

### Modul pathlib
Eine Alternative zu 
[open](https://docs.python.org/3/library/functions.html#open)
ist
[Path.open](https://docs.python.org/3/library/pathlib.html#pathlib.Path.open).

```
from pathlib import Path
path = Path('uebersicht_dateien.txt')
with path.open(mode = 'r', encoding="utf-8") as f:
    content = f.read()
print(content)
```

Oder kürzer:

```
from pathlib import Path
path = Path('uebersicht_dateien.txt')
content = path.read_text(encoding="utf-8")
print(content)
```

_read_text_ kümmert sich um das Öffnen und Schließen der 
Datei, genau wie auch _write_text_.

In der Liste 
[Corresponding tools](https://docs.python.org/3/library/pathlib.html#corresponding-tools) 
findet man, welche Funktionen im Modul _os_ welchen Funktionen
im Modul _pathlib_ entsprechen.

Hier ein Beispiel, in dem der Inhalt eines Verzeichnisses
mit der Funktion _iterdir_ aufgelistet werden:

* [pathlib_dateien_auflisten.py](https://raw.githubusercontent.com/maroph/mvhs_python_automatisierung_scripting/main/sources/tag1/pathlib_dateien_auflisten.py)

### Modul shutil
Das Modul 
[shutil](https://docs.python.org/3/library/shutil.html)
stelle eine Reihe von Highlevel Operationen zur Verfügung um
Dateien und Verzeichnisse zu kopieren, zu verschieben oder zu
löschen.

* [shutil.copy(urspr,ziel)](https://docs.python.org/3/library/shutil.html#shutil.copy)  
  Datei kopieren
* [shutil.copytree(ursprOrdner,zielOrdner)](https://docs.python.org/3/library/shutil.html#shutil.copytree)  
  Ordner kopieren
* [shutil.move(urspr,ziel)](https://docs.python.org/3/library/shutil.html#shutil.move)  
  Datei/Ordner verschieben (Achtung kann überschreiben!)
* [shutil.rmtree(path)](https://docs.python.org/3/library/shutil.html#shutil.rmtree)  
  Löscht ein Verzeichnis samt allen Unterverzeichnissen
