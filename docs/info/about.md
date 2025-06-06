# Über diese Site
Auf dieser Site habe ich meine Daten zum 
[MVHS Workshop: Python für Automatisierungs- und Scripting-Aufgaben](https://www.mvhs.de/kurse/online-programm/it-digitales/workshop-python-fuer-automatisierungs-und-scripting-aufgaben/online-kurs-460-C-U486390) 
abgelegt.

Der gesamte Inhalt dieser Site ist in meinem
GitHub Repository
[maroph/mvhs_python_automatisierung_scripting](https://github.com/maroph/mvhs_python_automatisierung_scripting/)
abgelegt.

## Struktur des Repositories
Im Branch 
[main](https://github.com/maroph/mvhs_python_automatisierung_scripting/tree/main) 
des Repositories befinden sich die folgenden
Dateien und Verzeichnisse:

* .github/workflows/ci.yml  
  GitHub Actions Konfigurationsdatei.  
  Diese Konfigurationsdatei sorgt dafür, dass bei
  jedem commit im Branch main, der den Inhalt der
  Webseiten betrifft, die HTML Seiten neu erzeugt
  werden.
* docs  
  Markdown Sourcen dieser Site
* sources  
  Python Source Code
* LICENSE  
  Lizenz des Repositories ([CC-BY 4.0](https://creativecommons.org/licenses/by/4.0/))
* README.md  
  Readme Datei des Repositories
* build.bash  
  Linux build Skript.  
  Mit diesem Skript kann man lokal die HTML Seiten
  auf einem Linux System erzeugen.
* mkdocs.yml  
  [MkDocs](https://www.mkdocs.org/) 
  Konfigurationsdatei

Änderungen/Erweiterungen committe ich zuerst im 
Branch 
[develop](https://github.com/maroph/mvhs_python_automatisierung_scripting/tree/develop). Abschließend merge ich das Ergebnis
in den main Branch.

## Webseiten
Die Markdown Dateien für die Webseiten sind unter 
[docs](https://github.com/maroph/mvhs_python_automatisierung_scripting/tree/main/docs)
abgelegt.

Die Webseiten erzeuge ich aus den Markdown
Dateien mit dem  
[MkDocs](https://www.mkdocs.org/) 
Static Site Generator und dem darauf aufbauenden 
[Material for MkDocs](https://squidfunk.github.io/mkdocs-material/). Die erzeugten Webseiten
werden im Branch 
[gh-pages](https://github.com/maroph/mvhs_python_automatisierung_scripting/tree/gh-pages)
abgelegt.

Für den Aufruf der benötigten Python Module 
nutze ich ein Python Virtual Environment.

Auf die Webseiten kann man über die GitHub Page 
[maroph.github.io/mvhs_python_automatisierung_scripting](https://maroph.github.io/mvhs_python_automatisierung_scripting/)
zugreifen.

## Python
### Python Dateien
Die Python Dateien sind im Verzeichnis 
[sources](https://github.com/maroph/mvhs_python_automatisierung_scripting/tree/main/sources)
des Repositories abgelegt.

### Python Version und Betriebssysteme
Die Python Programme habe ich unter __Debian 12__
und __Windows 11__ getestet.  

Die jeweils verwendete Python Version kann man mit
dem Programm 
[version.py]{:target="blank"}
ausgeben.
[version.py]: https://raw.githubusercontent.com/maroph/mvhs_python_automatisierung_scripting/main/sources/version.py


#### Debian 12.11
```
$ python3 version.py
3.11.2 (main, Nov 30 2024, 21:22:50) [GCC 12.2.0]
sys.version_info(major=3, minor=11, micro=2, releaselevel='final', serial=0)
major        : 3
minor        : 11
micro        : 2
releaselevel : final
serial       : 0
```

#### Windows 11 24H2
```
> python.exe version.py
3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)]
sys.version_info(major=3, minor=13, micro=2, releaselevel='final', serial=0)
major        : 3
minor        : 13
micro        : 2
releaselevel : final
serial       : 0
```

### Python Virtual Environment
Zur Erzeugung der Webseiten verwende ich die 
folgenden Python Module

* [mkdocs-material](https://pypi.org/project/mkdocs-material/)  
  Das Modul [mkdocs](https://pypi.org/project/mkdocs/) wird dabei mitinstalliert.
* [mkdocs-git-revision-date-localized-plugin](https://pypi.org/project/mkdocs-git-revision-date-localized-plugin/)
* [mkdocs-rss-plugin](https://pypi.org/project/mkdocs-rss-plugin/)

Für die benötigten Python Module verwende ich das
folgende Virtual Environment:

```
python3 -m venv venv
source venv/bin/activate
python -m pip install --upgrade pip
python -m pip install --upgrade setuptools
python -m pip install --upgrade wheel
python -m pip install mkdocs-material
python -m pip install mkdocs-git-revision-date-localized-plugin
python -m pip install mkdocs-rss-plugin
```

### Python Virtual Environment (Ergänzung: Runtime)
Für die Beispiele werden zusätzlich die
folgenden Python Module benötigt:

* [beautifulsoup4](https://pypi.org/project/beautifulsoup4/)
* [lxml](https://pypi.org/project/lxml/)
* [python-dateutil](https://pypi.org/project/python-dateutil/)
* [requests](https://pypi.org/project/requests/)

```
python -m pip install beautifulsoup4
python -m pip install lxml
python -m pip install python-dateutil
python -m pip install requests
```


Für Testfälle benutze ich die 
[pytest](https://docs.pytest.org/en/stable/)
Module

* [pytest](https://pypi.org/project/pytest/)
* [pytest-order](https://pypi.org/project/pytest-order/)

```
python -m pip install pytest
python -m pip install pytest-order
```

Sollte das Modul pip und/oder venv nicht 
installiert sein, muss man das entsprechende 
Package installieren.

Auf einem Debian System geht das mit dem folgenden
Kommando

    sudo apt install python3-pip
    sudo apt install python3-venv
