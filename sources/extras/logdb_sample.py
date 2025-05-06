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
# logdb_sample: ein einfaches Beispiel zur Nutzung
# eines Datetime Feldes in in einer SQLite Tabelle.
#
# Der Python Typ datetime wird automatisch auf das
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
# einen Zeitstempel (log_dt) und eine Lognachricht (log_msg).
#
# Zusätzlich wird beim Eintrag in die Tabelle
# jedem Satz eine log_id zugewiesen.
#
import datetime
from enum import Enum
import sqlite3
import sys

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

# https://docs.python.org/3/library/sqlite3.html#sqlite3-adapter-converter-recipes
# https://docs.python.org/3/library/sqlite3.html#how-to-adapt-custom-python-types-to-sqlite-values
def adapt_date_iso(val: datetime.date) -> str :
    """Adapt datetime.date to ISO 8601 date."""
    print(f"adapt_date_iso(val) : {val} : type(val) : {type(val)}")
    return val.isoformat()

def adapt_datetime_iso(val: datetime.datetime) -> str :
    """Adapt datetime.datetime to timezone-naive ISO 8601 date."""
    print(f"adapt_datetime_iso(val) : {val} : type(val) : {type(val)}")
    return val.isoformat()

def adapt_datetime_epoch(val: datetime.datetime) -> float:
    """Adapt datetime.datetime to Unix timestamp."""
    print(f"adapt_datetime_epoch(val) : {val} : type(val) : {type(val)}")
    return int(val.timestamp())


# https://docs.python.org/3/library/sqlite3.html#sqlite3-adapter-converter-recipes
# https://docs.python.org/3/library/sqlite3.html#how-to-convert-sqlite-values-to-custom-python-types
def convert_date(val: str) -> datetime.date:
    """Convert ISO 8601 date to datetime.date object."""
    print(f"convert_date(val) : {val} : type(val) : {type(val)}")
    return datetime.date.fromisoformat(val.decode())

def convert_datetime(val: str) -> datetime.datetime:
    """Convert ISO 8601 datetime to datetime.datetime object."""
    print(f"convert_datetime(val) : {val} : type(val) : {type(val)}")
    return datetime.datetime.fromisoformat(val.decode())

def convert_timestamp(val: float) -> datetime.datetime:
    """Convert Unix epoch timestamp to datetime.datetime object."""
    print(f"convert_timestamp(val) : {val} : type(val) : {type(val)}")
    return datetime.datetime.fromtimestamp(int(val))


print("logdb_sample")
print(f"Python version : {sys.version}")
print(f"SQLite version : {sqlite3.sqlite_version}")

if sys.version_info.major != 3:
    print("Python 3 is required")
    sys.exit(1)

con = None
cur = None

try:
    if sys.version_info.minor > 11:
        print("register needed adapters/converters")
        sqlite3.register_adapter(datetime.date, adapt_date_iso)
        sqlite3.register_adapter(datetime.datetime, adapt_datetime_iso)
        sqlite3.register_adapter(datetime.datetime, adapt_datetime_epoch)

        sqlite3.register_converter("date", convert_date)
        sqlite3.register_converter("datetime", convert_datetime)
        sqlite3.register_converter("timestamp", convert_timestamp)

    con = sqlite3.connect(':memory:', detect_types=sqlite3.PARSE_DECLTYPES)
    # from pathlib import Path
    # path = Path('logdb_sample.db')
    # if path.is_file():
    #     path.unlink(True)
    # con = sqlite3.connect('logdb_sample.db', detect_types=sqlite3.PARSE_DECLTYPES)
    con.autocommit = True
except sqlite3.Error as error:
    print(f"sqlite3 error (connect) : {error}")
    sys.exit(1)

try:
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS logrecords
                      (
                       log_id    INTEGER PRIMARY KEY AUTOINCREMENT,
                       log_level INTEGER NOT NULL,
                       log_dt    TIMESTAMP NOT NULL,
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
    now = datetime.datetime.now()
    cur.execute("INSERT INTO logrecords (log_level,log_dt,log_msg) VALUES(?,?,?)",
      (LogLevel.ERROR.value, now, "ERROR message"))
    rowcount = cur.rowcount
    log_id = cur.lastrowid
    print(f"INSERT: rowcount : {rowcount}")
    print(f"INSERT: log_id   : {log_id}")

    print("INSERT #2")
    now = datetime.datetime.now()
    cur.execute("INSERT INTO logrecords (log_level,log_dt,log_msg) VALUES(?,?,?)",
                (LogLevel.DEBUG.value, now, "DEBUG message"))
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
        print(f"    log_msg   : {log_entry[3]}, {type(log_entry[3])}")
        print('---')
    cur.close()
except sqlite3.Error as error:
    print(f"sqlite3.error (SELECT) : {error}")
    sys.exit(1)

con.close()
