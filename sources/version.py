#!/usr/bin/env python3
# Ausgabe der verwendeten Python Version
# und Daten zum verwendeten Rechner.
#
# https://docs.python.org/3/library/platform.html
import platform

print('Python Version :', platform.python_version())
print('---')
print('Name      :', platform.node())
print('System    :', platform.system())
print('Release   :', platform.release())
print('Version   :', platform.version())
print('Machine   :', platform.machine())
print('Processor :', platform.processor())
