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
    Password will be checked against Pwned Passwords database.
    Pwned Passwords Site: https://haveibeenpwned.com/Passwords

    The query API is described here
    https://www.troyhunt.com/ive-just-launched-pwned-passwords-version-2/#cloudflareprivacyandkanonymity

    Or also in this German article:
    Nach dem Passwort-Leak: Eigene Passwörter lokal checken
    https://www.heise.de/security/artikel/Nach-dem-Passwort-Leak-Eigene-Passwoerter-lokal-checken-4284756.html

    Parameters:
        password (str): the password to check

    Returns:
        count (int):
            0 : the password was not found in the Pwned Passwords database
          > 0 : number of times this password was found in the Pwned Passwords database
           -1 : error in request
           -2 : password is None
           -3 : password is not a string
           -4 : password is an empty string
    """

    if password is None:
        # print('password is None')
        return -2
    if not isinstance(password, str):
        # print('password is not a string')
        return -3
    if len (password) == 0:
        # print('password is an empty string')
        return -4

    digester = sha1()
    digester.update(password.encode('utf8'))
    hash = digester.hexdigest().upper()
    #
    lookup = hash[0:5]
    rest = hash[5:]
    #
    # print(f"password : {password}")
    # print(f"hash     : {hash}")
    # print(f"lookup   : {lookup}")
    # print(f"rest     : {rest}")
    # print(f"l+r      : {lookup}{rest}")

    url = f"https://api.pwnedpasswords.com/range/{lookup}"
    headers = {"Content-Type": "text/plain;charset=utf-8"}

    try:
        # TODO: Force TLS 1.2/1.3
        # Understanding TLS Versions: A Comprehensive Guide
        # https://master-spring-ter.medium.com/understanding-tls-versions-a-comprehensive-guide-791e599e181c
        res = requests.get(url, headers=headers)
        # print(res.text)
        # print('---')
        match = re.search(f"^{rest}.*$", res.text, re.VERBOSE | re.MULTILINE)
        if match is None:
            return 0
        (r, count) = match.group(0).split(':')
        # print(r, count)
        return int(count)
    except Exception as ex:
        # print('Error :', ex)
        return -1

if __name__ == '__main__':
    password = None
    print('password is None            :', check_password(password))
    #
    password = ('1', '2', '3')
    print('password is a list          :', check_password(password))
    #
    password = ''
    print('password is an empty string :', check_password(password))
    #
    password = '123456'
    print('password is too simple      :', check_password(password))
    #
    password = 'Agul2!-_7+QueLle'
    print('poassword is more complex   :', check_password(password))

