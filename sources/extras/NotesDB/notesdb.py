####################################################
# Copyright (c) 2025 by Manfred Rosenboom          #
# https://maroph.github.io/ (maroph@pm.me)         #
#                                                  #
# This work is licensed under a CC-BY 4.0 License. #
# https://creativecommons.org/licenses/by/4.0/     #
####################################################
#
import datetime
from pathlib import Path
import sqlite3
import sys


class NotesDBException(Exception):
    """Notes Database Exception Class."""
    def __init__(self, message):
        super().__init__()
        self.__message = message

    def __str__(self):
        return self.__message


class NotesDB:
    """
    Notes Database Class.

    Attributes:
        dbfile (str): name of the database file (default: None, i.e.: use an in-memory database).
        remove_old_db (bool): True: remove existing database file (default: False).
        verbose (bool): True: enable verbose mode (default: False).
        debug (bool): True: enable debug mode (default: False).
    """
    def __init__(self, dbfile: str = None, remove_old_db: bool = False, verbose: bool = False, debug: bool = False):
        """
        Constructor: initializes a NotesDB object.

        Parameters:
            dbfile (str): name of the database file (default: None, i.e.: use an in-memory database).
            remove_old_db (bool): True: remove existing database file (default: False).
            verbose (bool): True: enable verbose mode (default: False).
            debug (bool): True: enable debug mode (default: False).

        """
        self.__name = "NotesDB"
        self.__version = '0.1.0'
        self.__version_date = "04-MAY-2025"
        self.__dbfile = None
        self.__connection = None
        if verbose:
            self.__verbose = True
        else:
            self.__verbose = False
        if debug:
            self.__debug = True
        else:
            self.__debug = False

        if self.__verbose:
            print(f"{self.__name} {self.__version} ({self.__version_date})")
            print(f"{self.__name}: Python version     : {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}")
            print(f"{self.__name}: SQLite version     : {sqlite3.sqlite_version}")
            print(f"{self.__name}: sqlite3 apilevel   : {sqlite3.apilevel}")
            print(f"{self.__name}: sqlite3 paramstyle : {sqlite3.paramstyle}")
            print(f"{self.__name}: thread safety      : {sqlite3.threadsafety}")

        if sys.version_info.major != 3:
            raise NotesDBException('Python 3 required')

        if dbfile:
            if not isinstance(dbfile, str):
                raise NotesDBException('dbfile is not a string')
            self.__dbfile = dbfile
        elif isinstance(dbfile, str) and len(dbfile) == 0:
            raise NotesDBException('dbfile is an empty string')

        if remove_old_db:
            if dbfile:
                path = Path(dbfile)
                if path.is_file():
                    path.unlink(True)
        try:
            if sys.version_info.minor > 11:
                if self.__verbose:
                    print("register datetime adapter/converter")
                sqlite3.register_adapter(datetime.datetime, self.adapt_datetime_epoch)
                sqlite3.register_converter("timestamp", self.convert_timestamp)

            if dbfile:
                self.__connection = sqlite3.connect(self.__dbfile, detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
            else:
                self.__connection = sqlite3.connect(':memory:', detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
        except sqlite3.Error as error:
            self.__connection = None
            if self.__debug:
                print(f"{self.__name}: DEBUG: __init__: sqlite3.error : {error}")
            raise NotesDBException(f"can't open file {dbfile}: {error}")
        try:
            self.__create_table()
        except sqlite3.Error as error:
            if self.__debug:
                print(f"{self.__name}: DEBUG: __init__: sqlite3.error : {error}")
            raise NotesDBException("can't create notes table and/or related indices")

    def __del__(self):
        """Destructor."""
        if self.__connection:
            self.__connection.close()
            self.__connection = None

    def __str__(self):
        _str = 'NotesDB("'
        if self.__dbfile:
            _str = _str + self.__dbfile
        else:
            _str = _str + ':memory:'
        _str = _str + '")'
        return _str

    @property
    def name(self) -> str:
        return self.__name

    @property
    def version(self) -> str:
        return self.__version

    @property
    def version_date(self) -> str:
        return self.__version_date

    @property
    def verbose(self) -> bool:
        return self.__verbose

    @verbose.setter
    def verbose(self, verbose: bool):
        if verbose:
            self.__verbose = True
        else:
            self.__verbose = False

    @property
    def debug(self) -> bool:
        return self.__debug

    @debug.setter
    def debug(self, debug: bool):
        if debug:
            self.__debug = True
        else:
            self.__debug = False

    # https://docs.python.org/3/library/sqlite3.html#sqlite3-adapter-converter-recipes
    # https://docs.python.org/3/library/sqlite3.html#how-to-adapt-custom-python-types-to-sqlite-values
    @staticmethod
    def adapt_datetime_epoch(val: datetime.datetime) -> float:
        """Adapt datetime.datetime to Unix timestamp."""
        return int(val.timestamp())

    # https://docs.python.org/3/library/sqlite3.html#sqlite3-adapter-converter-recipes
    # https://docs.python.org/3/library/sqlite3.html#how-to-convert-sqlite-values-to-custom-python-types
    @staticmethod
    def convert_timestamp(val: float) -> datetime.datetime:
        """Convert Unix epoch timestamp to datetime.datetime object."""
        return datetime.datetime.fromtimestamp(int(val))

    @staticmethod
    def dt_to_string(dt: datetime.datetime) -> str:
        return dt.strftime('%Y-%m-%d %H:%M:%S')

    @staticmethod
    def date_begin(year: int, month: int, day: int) -> datetime.datetime:
        if not isinstance(year, int):
            raise NotesDBException('year is not an integer')
        if not isinstance(month, int):
            raise NotesDBException('month is not an integer')
        if not isinstance(day, int):
            raise NotesDBException('day is not an integer')

        return datetime.datetime(year, month, day)

    @staticmethod
    def date_end(year: int, month: int, day: int) -> datetime.datetime:
        if not isinstance(year, int):
            raise NotesDBException('year is not an integer')
        if not isinstance(month, int):
            raise NotesDBException('month is not an integer')
        if not isinstance(day, int):
            raise NotesDBException('day is not an integer')

        return datetime.datetime(year, month, day, 23, 59, 59, 999999)

    def __create_table(self) -> None:
        """Create the NotesDB table notes and the related indices."""
        cursor = self.__connection.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS notes(
                              note_id INTEGER PRIMARY KEY,
                              title   TEXT NOT NULL,
                              note    TEXT NOT NULL,
                              cdt     TIMESTAMP NOT NULL,
                              mdt     TIMESTAMP NOT NULL
                          )""")
        cursor.execute("CREATE UNIQUE INDEX IF NOT EXISTS idx_unique ON notes(cdt,title)")
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_cdt ON notes(cdt)")
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_mdt ON notes(mdt)")
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_title ON notes(title)")
        self.__connection.commit()
        cursor.close()

    def note_add(self, title: str, note: str) -> int:
        """
        Add a new note.

        Args:
            title (str): note title.
            note  (str): note text.
            Both title and note must be a non-empty string.

        Returns:
            int: the note id in the database.
        """
        if self.__debug:
            print(f"{self.__name}: DEBUG: note_add: title: {title}")
            print(f"{self.__name}: DEBUG: note_add: note : {note}")

        if not title:
            raise NotesDBException("title not set")
        if not isinstance(title, str):
            raise NotesDBException('title is not a string')
        if not note:
            raise NotesDBException("note not set")
        if not isinstance(note, str):
            raise NotesDBException('note is not a string')

        now = datetime.datetime.now()
        cursor = None
        try:
            cursor = self.__connection.cursor()
            cursor.execute("INSERT INTO notes (title,note,cdt,mdt) VALUES(?,?,?,?)",
                           (title, note, now, now))
            self.__connection.commit()
            rowcount = cursor.rowcount
            note_id = cursor.lastrowid
            if self.__debug:
                print(f"{self.__name}: DEBUG: note_add: INSERT: rowcount: {rowcount}")
                print(f"{self.__name}: DEBUG: note_add: INSERT: note_id : {note_id}")
            cursor.close()
        except sqlite3.Error as error:
            if self.__debug:
                print(f"{self.__name}: DEBUG: noze_add: sqlite3.error : {error}")
            raise NotesDBException(f"{error}")
        finally:
            if cursor:
                cursor.close()

        if rowcount != 1:
            return -1
        return note_id

    def note_delete(self, note_id: int) -> bool:
        """ delete a note """
        if self.__debug:
            print(f"{self.__name}: DEBUG: note_delete: note_id: {note_id}")

        if not isinstance(note_id, int):
            raise NotesDBException('note_id is not an integer')
        if note_id < 1:
            raise NotesDBException('note_id is not an integer >= 1')

        cursor = None
        try:
            cursor = self.__connection.cursor()
            cursor.execute("DELETE FROM notes WHERE note_id=?", (note_id,))
            self.__connection.commit()
            rowcount = cursor.rowcount
            note_id = cursor.lastrowid
            if self.__debug:
                print(f"{self.__name}: DEBUG: note_delete: DELETE: rowcount : {rowcount}")
                print(f"{self.__name}: DEBUG: note_delete: DELETE: note_id  : {note_id}")
            cursor.close()
        except sqlite3.Error as error:
            if self.__debug:
                print(f"{self.__name}: DEBUG: note_delete: sqlite3.error : {error}")
            raise NotesDBException(f"{error}")
        finally:
            if cursor:
                cursor.close()

        if rowcount != 1:
            return False
        return True

    def note_update(self, note_id: int, title: str = None, note: str = None) -> bool:
        """ update a note """
        if self.__debug:
            print(f"{self.__name}: DEBUG: note_update: note_id: {note_id}")
            print(f"{self.__name}: DEBUG: note_update: title  : {title}")
            print(f"{self.__name}: DEBUG: note_update: note   : {note}")

        if not title and not note:
            raise NotesDBException("Both title and note are not set")
        if not isinstance(note_id, int):
            raise NotesDBException("node_id is not an integer")

        now = datetime.datetime.now()
        cursor = None
        try:
            cursor = self.__connection.cursor()
            if title and note:
                if not isinstance(title, str):
                    raise ValueError("title is not a string")
                if not isinstance(note, str):
                    raise ValueError("note is not a string")
                cursor.execute("UPDATE notes SET mdt=?, title=?, note=? WHERE note_id=?",
                               (now, title, note, note_id))
            elif note:
                if not isinstance(note, str):
                    raise ValueError("note is not a string")
                cursor.execute("UPDATE notes SET mdt=?, note=? WHERE note_id=?",
                               (now, note, note_id))
            elif title:
                if not isinstance(title, str):
                    raise ValueError("title is not a string")
                cursor.execute("UPDATE notes SET mdt=?, title=? WHERE note_id=?",
                               (now, title, note_id))
            else:
                raise ValueError("both title and note are not set")
            self.__connection.commit()
            rowcount = cursor.rowcount
            if self.__debug:
                print(f"{self.__name}: DEBUG: note_update: UPDATE: rowcount: {rowcount}")
            cursor.close()
        except sqlite3.Error as error:
            if self.__debug:
                print(f"{self.__name}: DEBUG: note_update: sqlite3.error : {error}")
            raise NotesDBException(f"{error}")
        finally:
            if cursor:
                cursor.close()

        if rowcount != 1:
            return False
        return True

    def note_get(self, note_id: int) -> list:
        """ get a note """
        if self.__debug:
            print(f"{self.__name}: DEBUG: note_get: note_id: {note_id}")

        if not isinstance(note_id, int):
            raise ValueError('note_id is not an integer')
        if note_id < 1:
            raise ValueError('note_id is not an integer >= 1')

        cursor = None
        note_entry = None
        try:
            cursor = self.__connection.cursor()
            cursor.execute("SELECT note_id,title,note,cdt,mdt FROM notes WHERE note_id=?", (note_id,))
            note_entry = cursor.fetchone()

            if note_entry is None:
                return []

            if len(note_entry) != 5:
                return []

            if self.__verbose:
                print(f"{self.__name}: note_get: SELECT: entry : {note_entry}")
                print(f"{self.__name}:     SELECT: noted_id : {note_entry[0]}")
                print(f"{self.__name}:     SELECT: title    : {note_entry[1]}")
                print(f"{self.__name}:     SELECT: note     : {note_entry[2]}")
                print(f"{self.__name}:     SELECT: cdt      : {self.dt_to_string(note_entry[3])}")
                print(f"{self.__name}:     SELECT: mdt      : {self.dt_to_string(note_entry[4])}")
        except sqlite3.Error as error:
            if self.__debug:
                print(f"{self.__name}: DEBUG: note_get: sqlite3.error : {error}")
            raise NotesDBException(f"{error}")
        finally:
            if cursor:
                cursor.close()

        return note_entry

    def note_get_intervall(self, first_date: datetime.datetime, last_date: datetime.datetime) ->list:
        """ get a list of notes """
        if self.__debug:
            print(f"{self.__name}: DEBUG: note_get_intervall: first_date: {first_date}")
            print(f"{self.__name}: DEBUG: note_get_intervall: last_date : {last_date}")

        if not isinstance(first_date, datetime.datetime):
            raise ValueError('first_date is not of type datetime.datetime')
        if not isinstance(last_date, datetime.datetime):
            raise ValueError('last_date is not of type datetime.datetime')

        cursor = None
        try:
            cursor = self.__connection.cursor()
            cursor.execute("SELECT note_id,title,note,cdt,mdt FROM notes WHERE mdt >= ? AND mdt <= ? ORDER BY mdt desc",
                           (first_date, last_date))
            note_entries = cursor.fetchall()

            if len(note_entries) == 0:
                return []

            if self.__verbose:
                for note_entry in note_entries:
                    print(f"{self.__name}: note_get_intervall: SELECT: entry : {note_entry}")
                    print(f"{self.__name}:     SELECT: noted_id : {note_entry[0]}")
                    print(f"{self.__name}:     SELECT: title    : {note_entry[1]}")
                    print(f"{self.__name}:     SELECT: note     : {note_entry[2]}")
                    print(f"{self.__name}:     SELECT: cdt      : {self.dt_to_string(note_entry[3])}")
                    print(f"{self.__name}:     SELECT: mdt      : {self.dt_to_string(note_entry[4])}")
        except sqlite3.Error as error:
            if self.__debug:
                print(f"{self.__name}: DEBUG: note_get_intervall: sqlite3.error : {error}")
            raise NotesDBException(f"{error}")
        finally:
            if cursor:
                cursor.close()

        return note_entries
