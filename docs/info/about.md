# Über diese Site
Auf dieser Site habe ich meine Daten zum Kurs 
[MVHS Workshop: Python für Automatisierungs- und Scripting-Aufgaben](https://www.mvhs.de/kurse/online-programm/it-digitales/workshop-python-fuer-automatisierungs-und-scripting-aufgaben/online-kurs-460-C-U486390) 
abgelegt.

Der gesamte Inhalt dieser Site (HTML und Python
Source Code) ist abgelegt in meinem GitHub
Repository
[maroph/mvhs_python_automatisierung_scripting](https://github.com/maroph/mvhs_python_automatisierung_scripting/).

Auf die Webseiten kann man über die GitHub Page 
[maroph.github.io/mvhs_python_automatisierung_scripting](https://maroph.github.io/mvhs_python_automatisierung_scripting/)
zugreifen.

Die Python Dateien sind im Verzeichnis 
[sources](https://github.com/maroph/mvhs_python_automatisierung_scripting/tree/main/sources)
des Repositories abgelegt.

__Die Python Programme habe ich unter Debian 12
und Windows 11 getestet.__  

Die verwendete Python Version kann man mit dem Programm 
[version.py](https://raw.githubusercontent.com/maroph/mvhs_python_automatisierung_scripting/main/sources/version.py) 
ausgeben.

**Debian 12.10**
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

**Windows 11 24H2**
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

## Struktur des Repositories
Im Branch 
__[main](https://github.com/maroph/mvhs_python_automatisierung_scripting/tree/main)__ 
des Repositories befinden sich die folgenden
Dateien und Verzeichnisse:

* .github/workflows/ci.yml  
  GitHub Actions Konfigurationsdatei.  
  Diese Konfigurationsdatei sorgt dafür, dass bei
  jedem commit im Branch main die HTML Seiten
  neu erzeugt werden.
* docs  
  Markdown Sourcen dieser Site
* sources  
  Python Source Code
* LICENSE  
  Lizenz des Repositories (CC-BY 4.0)
* README.md  
  Readme Datei des Repositories
* build.bash  
  Linux build Skript.  
  Mit diesem Skript kann man lokal die HTML Seiten
  erzeugen.
* mkdocs.yml  
  [MkDocs](https://www.mkdocs.org/) Konfigurationsdatei

Die Webseiten aus den Markdown Dateien erzeuge
ich mit dem  
[MkDocs](https://www.mkdocs.org/) 
Static Site Generator. Die erzeugten Webseiten 
werden im Branch 
__[gh-pages](https://github.com/maroph/mvhs_python_automatisierung_scripting/tree/gh-pages)__
abgelegt.

## Mein Python Virtual Environment
Zur Erzeugung der Webseiten verwende ich die 
folgenden Python Module

* [mkdocs-material](https://pypi.org/project/mkdocs-material/)  
  Das Modul [mkdocs](https://pypi.org/project/mkdocs/) wird dabei mitinstalliert.
* [mkdocs-git-revision-date-localized-plugin](https://pypi.org/project/mkdocs-git-revision-date-localized-plugin/)

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
```

Für die Kursbeispiele werden zusätzlich die
folgenden Python Module benötigt:

* [beautifulsoup4](https://pypi.org/project/beautifulsoup4/)
* [requests](https://pypi.org/project/requests/)

```
python -m pip install beautifulsoup4
python -m pip install requests 
```

Sollte das Modul pip und/oder venv nicht 
installiert sein, muss man das entsprechende 
Package installieren.

Auf einem Debian System geht das mit dem folgenden
Kommando

    sudo apt install python3-pip
    sudo apt install python3-venv

---

* Das [Python favicon](https://www.favicon.cc/?action=icon&file_id=831343) im Verzeichnis 
assets ist von der Site [favicon.cc](https://www.favicon.cc/)
* Die [Python Logo](../assets/python-logo-only2.png) Datei ist eine verkleinerte Version der Datei 
[python-logo-only.png](https://s3.dualstack.us-east-2.amazonaws.com/pythondotorg-assets/media/community/logos/python-logo-only.png).
