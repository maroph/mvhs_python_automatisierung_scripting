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
# 07-JUN-2025
import requests
from bs4 import BeautifulSoup


def fetch_openssl_newslog(max_newslog_items: int = 10) -> None:
    """
    Hole die neuesten Einträge aus dem OpenSSL Newslog.
    OpenSSL Newslog Seite: https://openssl-library.org/news/newslog/index.html

    Parameters:
        max_newslog_items (int): Anzahl der gewünschten Einträge, oder -1: alle Einträge

    Returns: None

    Die Einträge werden in der Form 'Datum | Meldung' auf stdout ausgegeben.
    """
    NEWSLOG_URL = "https://openssl-library.org/news/newslog/index.html"

    if max_newslog_items == 0:
        return

    if max_newslog_items < 0:
        max_newslog_items = 0

    try:
        response = requests.get(NEWSLOG_URL)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Fehler beim Lesen der OpenSSL Newslog-Seite: {e}")
        return

    soup = BeautifulSoup(response.content, "html.parser")

    table = soup.find("table")
    if table is None:
        print("Kein HTML Element table auf der Seite gefunden")
        return

    for row in table.tbody.find_all('tr'):
        max_newslog_items -= 1
        columns = row.find_all('td')
        if columns is None:
            continue
        if len(columns) < 2:
            continue
        print(f"{columns[0].text} | {columns[1].text}")
        if max_newslog_items == 0:
            break


if __name__ == "__main__":
    # Hole alle Einträge
    # fetch_openssl_newslog(-1)

    # Hole die letzen 5 Einträge
    # fetch_openssl_newslog(5)

    # Hole die Standardanzahl an Einträgen
    fetch_openssl_newslog()
