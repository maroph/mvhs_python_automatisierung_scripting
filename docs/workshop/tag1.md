# Tag 1 (03.07.2025)
Das Thema des Tages war "Arbeiten mit Dateien/Verzeichnissen".
Eine gute Übersicht zu diesem Thema gibt der Artikel 
[Working With Files in Python](https://realpython.com/working-with-files-in-python/).


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
* [lesen_zeilenweise_verbessert.py](https://raw.githubusercontent.com/maroph/mvhs_python_automatisierung_scripting/main/sources/tag1/lesen_zeilenweise_verbessert.py)
* [lesen_n_zeilen.py](https://raw.githubusercontent.com/maroph/mvhs_python_automatisierung_scripting/main/sources/tag1/lesen_n_zeilen.py)
* [read_birthday_in_pi.py](https://raw.githubusercontent.com/maroph/mvhs_python_automatisierung_scripting/main/sources/tag1/read_birthday_in_pi.py)

Hinweis: im Beispiel 
[lesen_zeilenweise_verbessert.py](https://raw.githubusercontent.com/maroph/mvhs_python_automatisierung_scripting/main/sources/tag1/lesen_zeilenweise_verbessert.py)
wird der Walrus Operator verwendet. Dieser Operator wurde mit
Python 3.8 eingeführt. Eine Beschreibung zu diesem Operator 
findet man im Artikel 
[The Walrus Operator: Python's Assignment Expressions](http://realpython.com/python-walrus-operator/).

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

### Infos über Module ausgeben
Eine einfach eHilfeseite kann man sich in der Python Shell
ausgeben lassen:

```
python
>>> import os
>>> help(os)
Help on module os:

NAME
    os - OS routines for NT or Posix depending on what system we're on.

MODULE REFERENCE
    https://docs.python.org/3.13/library/os.html

    The following documentation is automatically generated from the Python
    source files.  It may be incomplete, incorrect or include features that
    are considered implementation detail and may vary between Python
    implementations.  When in doubt, consult the module reference at the
    location listed above.

DESCRIPTION
    This exports:
      - all functions from posix or nt, e.g. unlink, stat, etc.
      - os.path is either posixpath or ntpath
      - os.name is either 'posix' or 'nt'
      - os.curdir is a string representing the current directory (always '.')
      - os.pardir is a string representing the parent directory (always '..')
      - os.sep is the (or a most common) pathname separator ('/' or '\\')
      - os.extsep is the extension separator (always '.')
      - os.altsep is the alternate pathname separator (None or '/')
      - os.pathsep is the component separator used in $PATH etc
      - os.linesep is the line separator in text files ('\r' or '\n' or '\r\n')
      - os.defpath is the default search path for executables
      - os.devnull is the file path of the null device ('/dev/null', etc.)

    Programs that import and use 'os' stand a better chance of being
    portable between different platforms.  Of course, they must then
    only use functions that are defined by all platforms (e.g., unlink
    and opendir), and leave all pathname manipulation to os.path
:
```

Mit _dir_ kann man sich alle global definierten Namen (Konstanten,
Funktionen) un einem Modul ausgeben lassen.
```
import os
dir(os)
['DirEntry', 'EX_OK', 'F_OK', 'GenericAlias', 'Mapping', 'MutableMapping', 'O_APPEND', 'O_BINARY', 'O_CREAT', 'O_EXCL', 'O_NOINHERIT', 'O_RANDOM', 'O_RDONLY', 'O_RDWR', 'O_SEQUENTIAL', 'O_SHORT_LIVED', 'O_TEMPORARY', 'O_TEXT', 'O_TRUNC', 'O_WRONLY', 'P_DETACH', 'P_NOWAIT', 'P_NOWAITO', 'P_OVERLAY', 'P_WAIT', 'PathLike', 'R_OK', 'SEEK_CUR', 'SEEK_END', 'SEEK_SET', 'TMP_MAX', 'W_OK', 'X_OK', '_AddedDllDirectory', '_Environ', '__all__', '__builtins__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_check_methods', '_execvpe', '_exists', '_exit', '_fspath', '_get_exports_list', '_walk_symlinks_as_files', '_wrap_close', 'abc', 'abort', 'access', 'add_dll_directory', 'altsep', 'chdir', 'chmod', 'close', 'closerange', 'cpu_count', 'curdir', 'defpath', 'device_encoding', 'devnull', 'dup', 'dup2', 'environ', 'error', 'execl', 'execle', 'execlp', 'execlpe', 'execv', 'execve', 'execvp', 'execvpe', 'extsep', 'fchmod', 'fdopen', 'fsdecode', 'fsencode', 'fspath', 'fstat', 'fsync', 'ftruncate', 'get_blocking', 'get_exec_path', 'get_handle_inheritable', 'get_inheritable', 'get_terminal_size', 'getcwd', 'getcwdb', 'getenv', 'getlogin', 'getpid', 'getppid', 'isatty', 'kill', 'lchmod', 'linesep', 'link', 'listdir', 'listdrives', 'listmounts', 'listvolumes', 'lseek', 'lstat', 'makedirs', 'mkdir', 'name', 'open', 'pardir', 'path', 'pathsep', 'pipe', 'popen', 'process_cpu_count', 'putenv', 'read', 'readlink', 'remove', 'removedirs', 'rename', 'renames', 'replace', 'rmdir', 'scandir', 'sep', 'set_blocking', 'set_handle_inheritable', 'set_inheritable', 'spawnl', 'spawnle', 'spawnv', 'spawnve', 'st', 'startfile', 'stat', 'stat_result', 'statvfs_result', 'strerror', 'supports_bytes_environ', 'supports_dir_fd', 'supports_effective_ids', 'supports_fd', 'supports_follow_symlinks', 'symlink', 'sys', 'system', 'terminal_size', 'times', 'times_result', 'truncate', 'umask', 'uname_result', 'unlink', 'unsetenv', 'urandom', 'utime', 'waitpid', 'waitstatus_to_exitcode', 'walk', 'write']
```

Man kann sich auch den Hilfetext für eine einzelne Funktion
ausgeben lassen:

```
>>> print(os.listdir.__doc__)
Return a list containing the names of the files in the directory.

path can be specified as either str, bytes, or a path-like object.  If path is bytes,
  the filenames returned will also be bytes; in all other circumstances
  the filenames returned will be str.
If path is None, uses the path='.'.
On some platforms, path may also be specified as an open file descriptor;\
  the file descriptor must refer to a directory.
  If this functionality is unavailable, using it raises NotImplementedError.
  
The list is in arbitrary order.  It does not include the special
entries '.' and '..' even if they are present in the directory.
```


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
Das Modul
[pathlib](https://docs.python.org/3/library/pathlib.html)
erlaubt ein komfortables, betriebssystemübergreifendes Arbeiten
mit Datei- und Verzeichnisnamen - abstrahiert als Pfade (Path).

Der Artikel [Python's pathlib Module: Taming the File System](https://realpython.com/python-pathlib/)
enthält eine gute Einführung in die Nutzung des Moduls.

#### Beispiel open
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

#### Vergleich: os/pathlib Funktionen
In der Liste 
[Corresponding tools](https://docs.python.org/3/library/pathlib.html#corresponding-tools) 
findet man, welche Funktionen im Modul _os_ welchen Funktionen
im Modul _pathlib_ entsprechen.

#### Beispiel
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

Im Artikel 
[Shutil Module in Python](https://www.askpython.com/python-modules/shutil-module)
findet man eine Reihe von Beispielen zur Nutzung des
Moduls.

### Modul send2trash
Das Modul [send2trash](https://pypi.org/project/Send2Trash/) 
verschiebt zu löschende Daten (Dateien/Verzeichnisse) in den
Papierkorb.

Achtung: Dieses Modul muss mit _pip_ installiert werden.

```
from send2trash import send2trash
# Verschiebe eine Datei/Verzeichnis in den Papierkorb
send2trash('some_file')

# Verschiebe eine Liste von Dateien/Verzeichnissen in den Papierkorb
send2trash(['some_file1', 'some_file2'])
```

### Modul sys

* bietet Zugriff auf Systemfunktionen und Interpreter
  Informationen.
* verwenden für
    * mit dem Interpreter interagieren– Argumente aus der
      Kommandozeile lesen
    * das Skript vorzeitig beenden
    * Informationen zu Pfaden, Modulen und Versionen erhalten

| Funktion/Attribut                 | Beschreibung                      |
|:----------------------------------|:----------------------------------|
| sys.argv                          | Liste der Kommandozeilenargumente |
| sys.exit()                        | Skript/Programm beenden           |
| sys.version                       | Gibt die Python Version zurück    |
| sys.path                          | Liste der Modul Suchpfade         |
| sys.stdin, sys.stdout, sys.stderr | Zugriff auf die Ein-Ausgabestream |

Beispiel:

* [sys_beispiel.py](https://raw.githubusercontent.com/maroph/mvhs_python_automatisierung_scripting/main/sources/tag1/sys_beispiel.py)


### Modul arparse
CLI (Command Line Interface) Tools können eine Reihe von Optionen
und Argumenten haben. D.h. das Parsen von sys.argv kann sehr
aufwendig sein.

Diese Arbeit kann man sich vom Modul
[argparse](https://docs.python.org/3/library/argparse.html)
abnehmen lassen. In der Python Dokumentation gibt es das
[Argparse Tutorial](https://docs.python.org/3/howto/argparse.html),
das eine Reihe von Beispielen enthält.

Zusätzlich sind im Artikel
[Build Command-Line Interfaces With Python's argparse](https://realpython.com/command-line-interfaces-python-argparse/)
eine Reihe von Einsatzfällen beschrieben.

Beispiel:

* [script_argparse_template.py](https://raw.githubusercontent.com/maroph/mvhs_python_automatisierung_scripting/main/sources/extras/script_argparse_template.py)
