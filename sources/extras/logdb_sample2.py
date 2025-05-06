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
# logdb_sample2: ein einfaches Beispiel zur Nutzung
# eines Datetime Feldes in in einer SQLite Tabelle.
#
# Der Python Typ datetime wird manuell auf das
# Zeitstempelformat der SQLite Datenbank konvertiert.
#
# Beispieldatenbank
# -----------------
# In der Tabelle logrecords werden Logsätze gespeichert.
# Jeder Satz enthält ein LogLevel (log_level)
#
# FATAL = 6
# ERROR = 5
# WARN = 4
# INFO = 3
# DEBUG = 2
# TRACE = 1
#
# und eine Lognachricht (log_msg).
#
# Zusätzlich wird beim Eintrag in die Tabelle
# jedem Satz eine log_id zugewiesen und der
# Zeitstempel (Datetime) der Eintrags wird
# hinzugefügt.
#
# --------------------------------------------------
#
# Getestet mit Python 3.13.2 unter Windows 11 24H2
#
import datetime
from dateutil import tz
from enum import Enum
import sqlite3
import sys

use_utc: bool = True
# use_utc: bool = False


class LogLevel(Enum):
    FATAL = 6
    ERROR = 5
    WARN = 4
    INFO = 3
    DEBUG = 2
    TRACE = 1

    @staticmethod
    def is_int_loglevel(int_level: int) -> bool:
        try:
            LogLevel(int_level)
            return True
        except:
            return False


def dt_string_to_dt(dt_string: str) -> datetime.datetime:
    if not use_utc:
        dt = datetime.datetime.strptime(dt_string, '%Y-%m-%d %H:%M:%S.%f localtime')
        # dt = datetime.datetime.strptime(dt_string, '%Y-%m-%d %H:%M:%S.%f')
        return dt.astimezone(tz.tzlocal())
    dt = datetime.datetime.strptime(dt_string, '%Y-%m-%d %H:%M:%S')
    dt = dt.replace(tzinfo=tz.tzutc())
    return dt.astimezone(tz.tzlocal())

def dt_to_dt_string(dt: datetime.datetime) -> str:
    dt = dt.replace(tzinfo=tz.tzlocal())
    if not use_utc:
        return dt.strftime('%Y-%m-%d %H:%M:%S.%f localtime')
    utc = dt.astimezone(tz.tzutc())
    return utc.strftime('%Y-%m-%d %H:%M:%S')

def dt_to_string(dt: datetime.datetime) -> str:
    if not use_utc:
        return dt.strftime('%Y-%m-%d %H:%M:%S.%f')
    return dt.strftime('%Y-%m-%d %H:%M:%S')

print("logdb_sample2")
print(f"Python version : {sys.version}")
print(f"SQLite version : {sqlite3.sqlite_version}")

if sys.version_info.major != 3:
    print("Python 3 is required")
    sys.exit(1)

con = None
cur = None

try:
    con = sqlite3.connect(':memory:')
    # from pathlib import Path
    # path = Path('logdb_sample2.db')
    # if path.is_file():
    #     path.unlink(True)
    # con = sqlite3.connect('logdb_sample2.db')
    con.autocommit = True
except sqlite3.Error as error:
    print(f"sqlite3 error (connect) : {error}")
    sys.exit(1)

try:
    cur = con.cursor()
    if use_utc:
        cur.execute("""CREATE TABLE IF NOT EXISTS logrecords
                          (
                           log_id    INTEGER PRIMARY KEY AUTOINCREMENT,
                           log_level INTEGER NOT NULL,
                           log_dt    TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
                           log_msg   TEXT NOT NULL
                          ) """)
    else:
        cur.execute("""CREATE TABLE IF NOT EXISTS logrecords
                          (
                           log_id    INTEGER PRIMARY KEY AUTOINCREMENT,
                           log_level INTEGER NOT NULL,
                           log_dt    TEXT NOT NULL,
                           log_msg   TEXT NOT NULL
                          ) """)
    cur.execute("CREATE INDEX IF NOT EXISTS idx_level ON logrecords(log_level)")
    cur.execute("CREATE INDEX IF NOT EXISTS idx_dt ON logrecords(log_dt)")
    cur.close()
except sqlite3.Error as error:
    print(f"sqlite3 error (CREATE TABLE/INDEX) : {error}")
    sys.exit(1)

try:
    cur = con.cursor()
    print("INSERT #1")
    if use_utc:
        cur.execute("INSERT INTO logrecords (log_level,log_msg) VALUES(?,?)",
          (LogLevel.ERROR.value, "ERROR message"))
    else:
        dt_now_local = datetime.datetime.now()
        cur.execute("INSERT INTO logrecords (log_level,log_dt,log_msg) VALUES(?,?,?)",
          (LogLevel.ERROR.value, dt_to_dt_string(dt_now_local), "ERROR message"))
    rowcount = cur.rowcount
    log_id = cur.lastrowid
    print(f"INSERT: rowcount : {rowcount}")
    print(f"INSERT: log_id   : {log_id}")

    print("INSERT #2")
    dt_now_local = datetime.datetime.now()
    cur.execute("INSERT INTO logrecords (log_level,log_dt,log_msg) VALUES(?,?,?)",
                (LogLevel.DEBUG.value, dt_to_dt_string(dt_now_local), "DEBUG message"))
    rowcount = cur.rowcount
    log_id = cur.lastrowid
    print(f"INSERT: rowcount : {rowcount}")
    print(f"INSERT: log_id   : {log_id}")

    cur.close()
except sqlite3.Error as error:
    print(f"sqlite3.error (INSERT) : {error}")
    sys.exit(1)

try:
    cur = con.cursor()
    cur.execute("SELECT log_id,log_level,log_dt,log_msg FROM logrecords WHERE log_id=?", (1,))
    log_entry = cur.fetchone()

    print(f"SELECT: entry : {log_entry}")
    print(f"    log_id    : {log_entry[0]}, {type(log_entry[0])}")
    print(f"    log_level : {log_entry[1]}, {type(log_entry[1])}")
    print(f"                {LogLevel(int(log_entry[1]))}, {type(LogLevel(int(log_entry[1])))}")
    print(f"    log_dt    : {log_entry[2]}, {type(log_entry[2])}")
    dt_local = dt_string_to_dt(log_entry[2])
    print(f"                {dt_to_string(dt_local)}, {type(dt_local)}")
    print(f"    log_msg   : {log_entry[3]}, {type(log_entry[3])}")
    print()

    cur.execute("SELECT log_id,log_level,log_dt,log_msg FROM logrecords ORDER BY log_id ASC")
    log_entries = cur.fetchall()
    for log_entry in log_entries:
        print(f"SELECT: entry : {log_entry}")
        print(f"    log_id    : {log_entry[0]}, {type(log_entry[0])}")
        print(f"    log_level : {log_entry[1]}, {type(log_entry[1])}")
        print(f"                {LogLevel(int(log_entry[1]))}, {type(LogLevel(int(log_entry[1])))}")
        print(f"    log_dt    : {log_entry[2]}, {type(log_entry[2])}")
        dt_local = dt_string_to_dt(log_entry[2])
        print(f"                {dt_to_string(dt_local)}, {type(dt_local)}")
        print(f"    log_msg   : {log_entry[3]}, {type(log_entry[3])}")
        print('---')
except sqlite3.Error as error:
    print(f"sqlite3.error (SELECT) : {error}")
    sys.exit(1)

con.close()
