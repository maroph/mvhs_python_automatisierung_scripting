####################################################
# Copyright (c) 2025 by Manfred Rosenboom          #
# https://maroph.github.io/ (maroph@pm.me)         #
#                                                  #
# This work is licensed under a CC-BY 4.0 License. #
# https://creativecommons.org/licenses/by/4.0/     #
####################################################
#
from contextlib import closing
from datetime import datetime
from enum import Enum
import logging
from pathlib import Path
import sqlite3
from sys import version_info as sys_version_info


class NotesDBException(Exception):
    """
    Notes Database Exception Class.
    """
    def __init__(self, message: str):
        """
        Constructor: initializes a NotesDBException instance.

        Parameters:
            message (str) : exception error message text.
        """
        super().__init__()
        if not isinstance(message, str):
            raise TypeError("message is not a string")
        self.__message = message

    def __str__(self):
        """
        String representation of the NotesDBException instance.

        Returns:
            str: Exception class name and error message text.
        """
        return f"NotesDBException: {self.__message}"


class NotesDBLogLevel(Enum):
    """
    NotesDB Log Level Enum Class.

    The values are the same as the Python logging levels:
    https://docs.python.org/3/library/logging.html#logging-levels

    NotesDBLogLevel.CRITICAL (50)
    NotesDBLogLevel.ERROR    (40)
    NotesDBLogLevel.WARNING  (30)
    NotesDBLogLevel.INFO     (20)
    NotesDBLogLevel.DEBUG    (10)
    """
    CRITICAL = logging.CRITICAL
    ERROR = logging.ERROR
    WARNING = logging.WARNING
    INFO = logging.INFO
    DEBUG = logging.DEBUG

    @staticmethod
    def is_int_loglevel(int_level: int) -> bool:
        """
        Check whether a number represents a log level value.

        Parameters:
            int_level (int):

        Returns:
            bool: True if the number represents a log level value, False otherwise.
        """
        if not isinstance(int_level, int):
            return False
        try:
            NotesDBLogLevel(int_level)
            return True
        except:
            return False

    @staticmethod
    def is_string_loglevel(str_level: str) -> bool:
        """
        Check whether a string represents a log level value.

        Parameters:
            str_level (str):

        Returns:
            bool: True if the string represents a log level value, False otherwise.
        """
        if not isinstance(str_level, str):
            return False
        try:
            NotesDBLogLevel[str_level]
            return True
        except:
            return False


class NotesDB:
    """
    Notes Database Class.

    Sample class to manage a simple notes database.

    Attributes:
        dbfile (str)         : name of the database file (default: None, i.e.: use an in-memory database).
        remove_old_db (bool) : True: remove existing database file (default: False) - ignored if dbfile is None.
        loglevel (int|str)   : log level values: https://docs.python.org/3/library/logging.html#logging-levels.
                               Reading will always return an int.
        name (str)           : name of the database class ("NotesDB") - readonly attribute
        version(str)         : version of the database class - readonly attribute
        version_date(str)    : date of the version - readonly attribute
    """

    def __init__(self, dbfile: str = None, remove_old_db: bool = False, loglevel: int|str = NotesDBLogLevel.ERROR.value):
        """
        Constructor: initializes a NotesDB instance.

        Parameters:
            dbfile (str)         : name of the database file (default: None, i.e.: use an in-memory database).
            remove_old_db (bool) : True: remove existing database file (default: False).
            loglevel (int|str)   : log level values: https://docs.python.org/3/library/logging.html#logging-levels
                                   50, "CRITICAL"
                                   40, "ERROR"
                                   30, "WARNING"
                                   20, "INFO"
                                   10, "DEBUG"
        """
        self.__name = "NotesDB"
        self.__version = "0.1.0"
        self.__version_date = "12-MAY-2025"
        self.__dbfile = None
        self.__connection = None

        self.__loglevel = NotesDBLogLevel.ERROR.value
        self.__loglevel = self._checkLogLevel(loglevel)
        self.__logger = logging.getLogger(__name__)
        console_handler = logging.StreamHandler()
        # https://docs.python.org/3/library/logging.html#logrecord-attributes
        formatter = logging.Formatter("{asctime} {levelname} {module}#{filename}#{lineno}: {message}",
                                      style = "{",
                                      datefmt = "%Y-%m-%d %H:%M",
                                      )
        console_handler.setFormatter(formatter)
        if self.__logger.hasHandlers():
            self.__logger.handlers.clear()
        self.__logger.addHandler(console_handler)
        self.__logger.setLevel(self.__loglevel)

        self.__logger.info(f"{self.__name} {self.__version} ({self.__version_date})")
        self.__logger.info(f"{self.__name}: Python version     : {sys_version_info.major}.{sys_version_info.minor}.{sys_version_info.micro}")
        self.__logger.info(f"{self.__name}: SQLite version     : {sqlite3.sqlite_version}")
        self.__logger.info(f"{self.__name}: sqlite3 apilevel   : {sqlite3.apilevel}")
        self.__logger.info(f"{self.__name}: sqlite3 paramstyle : {sqlite3.paramstyle}")
        self.__logger.info(f"{self.__name}: thread safety      : {sqlite3.threadsafety}")

        if sys_version_info.major != 3:
            raise NotesDBException("Python 3 required")

        if dbfile:
            if not isinstance(dbfile, str):
                raise NotesDBException("dbfile is not a string")
            if len(dbfile.strip()) == 0:
                raise NotesDBException("dbfile is an empty string")
            self.__dbfile = dbfile
        elif isinstance(dbfile, str) and len(dbfile) == 0:
            raise NotesDBException("dbfile is an empty string")

        if not isinstance(remove_old_db, bool):
            raise NotesDBException("remove_old_db is not a boolean")
        if remove_old_db:
            if dbfile:
                path = Path(dbfile)
                if path.is_file():
                    path.unlink(True)
        try:
            if sys_version_info.minor > 11:
                self.__logger.info("register datetime adapter/converter")
                sqlite3.register_adapter(datetime, self.adapt_datetime_epoch)
                sqlite3.register_converter("timestamp", self.convert_timestamp)

            if dbfile:
                self.__connection = sqlite3.connect(self.__dbfile, detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
                Path(dbfile).chmod(0o600)
            else:
                self.__connection = sqlite3.connect(":memory:", detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
        except sqlite3.Error as error:
            self.__connection = None
            self.__logger.debug(f"can't open file {dbfile}: {error}", exc_info=True)
            raise NotesDBException(f"can't open file {dbfile}: {error}")

        try:
            self.__create_table()
        except sqlite3.Error as error:
            self.__logger.debug(f"sqlite3.error : {error}", exc_info=True)
            raise NotesDBException("can't create notes table and/or related indices")

    def __del__(self) -> None:
        """
        Destructor.
        """
        if self.__connection:
            try:
                self.__connection.close()
            except sqlite3.Error as error:
                self.__logger.debug(f"sqlite3.error : {error}", exc_info=True)
            finally:
                self.__connection = None

    def __str__(self) -> str:
        """
        String representation of the NotesDB instance.

        Returns:
            str:
        """
        _str = 'NotesDB("'
        if self.__dbfile:
            _str = _str + self.__dbfile
        else:
            _str = _str + ":memory:"
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
    def loglevel(self) -> int:
        return self.__loglevel

    @loglevel.setter
    def loglevel(self, loglevel: int|str):
        self.__loglevel = self._checkLogLevel(loglevel)
        self.__logger.setLevel(self.__loglevel)

    def _checkLogLevel(self, loglevel: int | str) -> int:
        """
        Check the given loglevel for a valid string or integer value and return the corresponding integer value.

        Parameters:
            loglevel (int|str):

        Returns:
            int: Python logging levels: 50, 40, 30, 20, 10
        """
        if isinstance(loglevel, str):
            if NotesDBLogLevel.is_string_loglevel(loglevel):
                return NotesDBLogLevel[loglevel].value
            else:
                self.__logger.debug(f"invalid log level string value: '{loglevel}' - log level not changed")
                return self.__loglevel
        elif isinstance(loglevel, int):
            if loglevel >= NotesDBLogLevel.CRITICAL.value:
                return NotesDBLogLevel.CRITICAL.value
            elif loglevel >= NotesDBLogLevel.ERROR.value:
                return NotesDBLogLevel.ERROR.value
            elif loglevel >= NotesDBLogLevel.WARNING.value:
                return NotesDBLogLevel.WARNING.value
            else:
                return NotesDBLogLevel.DEBUG.value
        else:
            raise NotesDBException(f"log level not an integer or a valid string: '{loglevel}'")

    # https://docs.python.org/3/library/sqlite3.html#sqlite3-adapter-converter-recipes
    # https://docs.python.org/3/library/sqlite3.html#how-to-adapt-custom-python-types-to-sqlite-values
    @staticmethod
    def adapt_datetime_epoch(dt: datetime) -> int:
        """
        Adapt datetime to Unix timestamp.

        Parameters:
            dt (datetime.datetime): The datetime object to be adapted

        Returns:
            float: Unix timestamp of the given datetime object
        """
        return int(dt.timestamp())

    # https://docs.python.org/3/library/sqlite3.html#sqlite3-adapter-converter-recipes
    # https://docs.python.org/3/library/sqlite3.html#how-to-convert-sqlite-values-to-custom-python-types
    @staticmethod
    def convert_timestamp(uts: int) -> datetime:
        """
        Convert Unix epoch timestamp to datetime object.

        Parameters:
            uts (float): Unix epoch timestamp

        Returns:
            datetime.datetime: The datetime object corresponding to the given Unix epoch timestamp.
        """
        return datetime.fromtimestamp(int(uts))

    @staticmethod
    def _dt_to_string(dt: datetime) -> str:
        """
        Converts a datetime object to a string formatted as 'YYYY-MM-DD HH:MM:SS'.

        Parameters:
            dt (datetime.datetime): The datetime object to be converted.

        Returns:
            str: A string representation of the given datetime in the format
                'YYYY-MM-DD HH:MM:SS'.
        """
        return dt.strftime("%Y-%m-%d %H:%M:%S")

    @staticmethod
    def date_begin(year: int, month: int, day: int) -> datetime:
        """
        Convert year, month and day ints to a datetime object with 00:00:00 as time.

        Parameters:
            year (int)  : year
            month (int) : month
            day (int)   : day in month

        Returns:
            datetime.datetime: datetime(year, month, day, 0, 0, 0, 0)
        """
        if not isinstance(year, int):
            raise NotesDBException("year is not an integer")
        if not isinstance(month, int):
            raise NotesDBException("month is not an integer")
        if not isinstance(day, int):
            raise NotesDBException("day is not an integer")

        return datetime(year, month, day, 0, 0, 0, 0)

    @staticmethod
    def date_end(year: int, month: int, day: int) -> datetime:
        """
        Convert year, month and day ints to a datetime object with 23:59:59 as time.

        Parameters:
            year (int)  : year
            month (int) : month
            day (int)   : day in month

        Returns:
            datetime.datetime: datetime(year, month, day, 23, 59, 59, 999999)
        """
        if not isinstance(year, int):
            raise NotesDBException("year is not an integer")
        if not isinstance(month, int):
            raise NotesDBException("month is not an integer")
        if not isinstance(day, int):
            raise NotesDBException("day is not an integer")

        return datetime(year, month, day, 23, 59, 59, 999999)

    def __create_table(self) -> None:
        """
        Create the NotesDB table notes and the related indices.
        """
        with closing(self.__connection.cursor()) as cursor:
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

    def note_add(self, title: str, note: str) -> int:
        """
        Add a new note.

        Parameters:
            title (str) : note title (non empty string)
            note (str)  : note text (non empty string)

        Returns:
            int: the note id in the database.
        """
        self.__logger.debug(f"note_add: title: {title}")
        self.__logger.debug(f"note_add: note : {note}")

        if not title:
            raise NotesDBException("title not set")
        if not isinstance(title, str):
            raise NotesDBException("title is not a string")
        if len(title.strip()) == 0:
            raise NotesDBException("title is an empty string")
        if not note:
            raise NotesDBException("note not set")
        if not isinstance(note, str):
            raise NotesDBException("note is not a string")
        if len(note.strip()) == 0:
            raise NotesDBException("note is an empty string")

        now = datetime.now()
        try:
            with closing(self.__connection.cursor()) as cursor:
                cursor.execute("INSERT INTO notes (title,note,cdt,mdt) VALUES(?,?,?,?)",
                               (title, note, now, now))
                self.__connection.commit()
                rowcount = cursor.rowcount
                note_id = cursor.lastrowid
            self.__logger.debug(f"note_add: INSERT: rowcount: {rowcount}")
            self.__logger.debug(f"note_add: INSERT: note_id : {note_id}")
        except sqlite3.Error as error:
            self.__logger.debug(f"note_add: sqlite3.error : {error}", exc_info=True)
            raise NotesDBException(f"{error}")

        if rowcount != 1:
            return -1
        return note_id

    def note_delete(self, note_id: int) -> bool:
        """
        Delete a new note.

        Parameters:
            note_id (int): id of note

        Returns:
            bool: True if successful, False otherwise
        """
        self.__logger.debug(f"note_delete: note_id: {note_id}")

        if not isinstance(note_id, int):
            raise NotesDBException("note_id is not an integer")
        if note_id < 1:
            raise NotesDBException("note_id is not an integer >= 1")

        try:
            with closing(self.__connection.cursor()) as cursor:
                cursor.execute("DELETE FROM notes WHERE note_id=?", (note_id,))
                self.__connection.commit()
                rowcount = cursor.rowcount
                note_id = cursor.lastrowid
            self.__logger.debug(f"note_delete: DELETE: rowcount : {rowcount}")
            self.__logger.debug(f"note_delete: DELETE: note_id  : {note_id}")
        except sqlite3.Error as error:
            self.__logger.debug(f"note_delete: sqlite3.error : {error}", exc_info=True)
            raise NotesDBException(f"{error}")

        if rowcount != 1:
            return False
        return True

    def note_update(self, note_id: int, title: str = None, note: str = None) -> bool:
        """
        Update a note.

        Parameters:
            note_id (int) : id of note
            title (str)   : title of note
            note (str)    : note text

        Returns:
            bool: True if successful, False otherwise
        """
        self.__logger.debug(f"note_update: note_id: {note_id}")
        self.__logger.debug(f"note_update: title  : {title}")
        self.__logger.debug(f"note_update: note   : {note}")

        if not title and not note:
            raise NotesDBException("Both title and note are not set")
        if not isinstance(note_id, int):
            raise NotesDBException("note_id is not an integer")

        if title:
            if not isinstance(title, str):
                raise NotesDBException("title is not a string")
            if len(title.strip()) == 0:
                raise NotesDBException("title is an empty string")
        if note:
            if not isinstance(note, str):
                raise NotesDBException("note is not a string")
            if len(note.strip()) == 0:
                raise NotesDBException("note is an empty string")

        now = datetime.now()
        try:
            with closing(self.__connection.cursor()) as cursor:
                if title and note:
                    if not isinstance(title, str):
                        raise NotesDBException("title is not a string")
                    if not isinstance(note, str):
                        raise NotesDBException("note is not a string")
                    cursor.execute("UPDATE notes SET mdt=?, title=?, note=? WHERE note_id=?",
                                   (now, title, note, note_id))
                elif note:
                    if not isinstance(note, str):
                        raise NotesDBException("note is not a string")
                    cursor.execute("UPDATE notes SET mdt=?, note=? WHERE note_id=?",
                                   (now, note, note_id))
                elif title:
                    if not isinstance(title, str):
                        raise NotesDBException("title is not a string")
                    cursor.execute("UPDATE notes SET mdt=?, title=? WHERE note_id=?",
                                   (now, title, note_id))
                else:
                    raise NotesDBException("both title and note are not set")
                self.__connection.commit()
                rowcount = cursor.rowcount
            self.__logger.debug(f"note_update: UPDATE: rowcount: {rowcount}")
        except sqlite3.Error as error:
            self.__logger.debug(f"note_update: sqlite3.error : {error}", exc_info=True)
            raise NotesDBException(f"{error}")

        if rowcount != 1:
            return False
        return True

    def note_get(self, note_id: int) -> list:
        """
        Get a note.

        Parameters:
            note_id (int):

        Returns:
            list: get note fields as list or an empty list if not found.
                  List elements:
                  0 : noted_id (int)
                  1 : title (str)
                  2 : note (str)
                  3 : cdt (datetime.datetime)
                  4 : mdt (datetime.datetime)
        """
        self.__logger.debug(f"note_get: note_id: {note_id}")

        if not isinstance(note_id, int):
            raise NotesDBException("note_id is not an integer")
        if note_id < 1:
            raise NotesDBException("note_id is not an integer >= 1")

        note_entry = None
        try:
            with closing(self.__connection.cursor()) as cursor:
                cursor.execute("SELECT note_id,title,note,cdt,mdt FROM notes WHERE note_id=?", (note_id,))
                note_entry = cursor.fetchone()

            if note_entry is None:
                return []

            if len(note_entry) != 5:
                return []

            if self.__logger.isEnabledFor(logging.INFO):
                self.__logger.info(f"note_get: SELECT: entry : {note_entry}")
                self.__logger.info(f"    SELECT: noted_id : {note_entry[0]}")
                self.__logger.info(f"    SELECT: title    : {note_entry[1]}")
                self.__logger.info(f"    SELECT: note     : {note_entry[2]}")
                self.__logger.info(f"    SELECT: cdt      : {self._dt_to_string(note_entry[3])}")
                self.__logger.info(f"    SELECT: mdt      : {self._dt_to_string(note_entry[4])}")

            return note_entry
        except sqlite3.Error as error:
            self.__logger.debug(f"note_get: sqlite3.error : {error}", exc_info=True)
            raise NotesDBException(f"{error}")

    def note_get_interval(self, first_date: datetime, last_date: datetime) ->list:
        """
        Get a list of notes in a certain datetime interval.

        Parameters:
            first_date (datetime.datetime):
            last_date  (datetime.datetime):

        Returns:
            list: the note data as a list or an empty list if no notes found.
        """
        self.__logger.debug(f"note_get_interval: first_date: {first_date}")
        self.__logger.debug(f"note_get_interval: last_date : {last_date}")

        if not isinstance(first_date, datetime):
            raise NotesDBException("first_date is not of type datetime.datetime")
        if not isinstance(last_date, datetime):
            raise NotesDBException("last_date is not of type datetime.datetime")
        if first_date > last_date:
            raise NotesDBException("first_date > last_date")

        try:
            with closing(self.__connection.cursor()) as cursor:
                cursor.execute("SELECT note_id,title,note,cdt,mdt FROM notes WHERE mdt >= ? AND mdt <= ? ORDER BY mdt desc",
                               (first_date, last_date))
                note_entries = cursor.fetchall()

            if len(note_entries) == 0:
                return []

            if self.__logger.isEnabledFor(logging.INFO):
                for note_entry in note_entries:
                    self.__logger.info(f"note_get_interval: SELECT: entry : {note_entry}")
                    self.__logger.info(f"    SELECT: noted_id : {note_entry[0]}")
                    self.__logger.info(f"    SELECT: title    : {note_entry[1]}")
                    self.__logger.info(f"    SELECT: note     : {note_entry[2]}")
                    self.__logger.info(f"    SELECT: cdt      : {self._dt_to_string(note_entry[3])}")
                    self.__logger.info(f"    SELECT: mdt      : {self._dt_to_string(note_entry[4])}")

            return note_entries
        except sqlite3.Error as error:
            self.__logger.debug(f"note_get_interval: sqlite3.error : {error}")

            raise NotesDBException(f"{error}")
