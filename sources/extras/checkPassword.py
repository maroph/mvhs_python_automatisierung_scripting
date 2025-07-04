#!/usr/bin/env python3
#
####################################################
# Copyright (c) 2025 by Manfred Rosenboom          #
# https://maroph.github.io/ (maroph@pm.me)         #
#                                                  #
# This work is licensed under a CC-BY 4.0 License. #
# https://creativecommons.org/licenses/by/4.0/     #
####################################################
#
from hashlib import sha1
import re
import requests


def check_password(password: str) -> int:
    """
    Das Passwort wird in der Pwned Passwords Datenbank gesucht.
    Pwned Passwords Site: https://haveibeenpwned.com/Passwords

    Parameters:
        password (str): das zu überprüfende Passwort.

    Returns:
        Es wird zurückgegeben, wie oft das Passwort in der Datenbank gefunden wurde.
        count (int):
            0 : Das Passwort wurde in der Pwned Passwords Datenbank nicht gefunden
          > 0 : Anzahl der Treffer in der Pwned Passwords Datenbank
           -1 : Fehler beim GET Request
           -2 : password ist None
           -3 : password ist kein String
           -4 : password ist ein leerer String

    Beschreibung des Query APIs:
    https://www.troyhunt.com/ive-just-launched-pwned-passwords-version-2/

    Eine deutsche Beschreibung findet man in dem folgenden Artikel:
    Nach dem Passwort-Leak: Eigene Passwörter lokal checken
    https://www.heise.de/security/artikel/Nach-dem-Passwort-Leak-Eigene-Passwoerter-lokal-checken-4284756.html

    Beispiel
    --------
    password : 123456
    sha1     : 7C4A8D09CA3762AF61E59520943DC26494F8941B

    lookup   : 7C4A8
    rest     : D09CA3762AF61E59520943DC26494F8941B

    Der Wert von lookup wird mit einem GET Request geschickt:

    https://api.pwnedpasswords.com/range/7C4A8

    Zurück bekommt man eine Liste von allen Hashwerten, die mit diesem
    Lookup String ("7C4A8") beginnen. Jeder Hashwert steht in einer
    extra Zeile und hat das Format

    <rest>:<count>

    Beispiel:
    001CE884342580D934A29D94060B3796C30:6
    00AD0FC3FA522D0474F9A28FD478C06669D:1
    00D7955EF1FFF374F6759D8AE026C09EEA0:4
    ...
    D09CA3762AF61E59520943DC26494F8941B:130075037
    ...
    FF849C5DE93593756DDF7AECBBE40B9A947:9
    FF90FEE99C8E2961AD1077ADEE4C6FEFF30:1
    FFA7B0AD1884D08B5AE2644C8D9D76BD4B5:1

    Aus dieser Liste muss man die Zeile heraussuchen, die den eigenen Rest enthält.

    Für das obige Beispiel erhält man das folgende Ergebnis:

    D09CA3762AF61E59520943DC26494F8941B:130075037

    D.h.: das Passwort "123456" wurde 130075037 Mal in der Datenbank gefunden.

    Wird der eigene Rest nicht gefunden, ist das Passwort in der Datenbank
    nicht bekannt.
    """

    if password is None:
        # print('password ist None')
        return -2
    if not isinstance(password, str):
        # print('password ist kein String')
        return -3
    if len (password) == 0:
        # print('password ist ein leerer String')
        return -4

    digester = sha1()
    digester.update(password.encode('utf8'))
    hash = digester.hexdigest().upper()

    lookup = hash[0:5]
    rest = hash[5:]

    # print(f"password : {password}")
    # print(f"hash     : {hash}")
    # print(f"lookup   : {lookup}")
    # print(f"rest     : {rest}")
    # print(f"l+r      : {lookup}{rest}")

    url = f"https://api.pwnedpasswords.com/range/{lookup}"
    headers = { "Content-Type": "text/plain;charset=utf-8" }

    try:
        res = requests.get(url, headers=headers)
        # print(res.text)
        # print('---')
        match = re.search(f"^{rest}.*$", res.text, re.MULTILINE)
        if match is None:
            return 0
        # print(match.group(0))
        # print('---')
        r, count = match.group(0).split(':')
        # print(f"rest: {r} - count: {count}")
        return int(count)
    except Exception as ex:
        # print('Error :', ex)
        return -1

if __name__ == '__main__':
    print('password is None            :', check_password(None))
    print('password is a list          :', check_password(('1', '2', '3')))
    print('password is an empty string :', check_password(''))
    print('password is too simple      :', check_password('123456'))
    print('password is more complex    :', check_password('Agul2!-_7+QueLle'))
