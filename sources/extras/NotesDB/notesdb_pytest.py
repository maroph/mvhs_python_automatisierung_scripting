####################################################
# Copyright (c) 2025 by Manfred Rosenboom          #
# https://maroph.github.io/ (maroph@pm.me)         #
#                                                  #
# This work is licensed under a CC-BY 4.0 License. #
# https://creativecommons.org/licenses/by/4.0/     #
####################################################
#
import pytest
from notesdb import NotesDB
import datetime
import logging

notesdb  = None
logger  = logging.getLogger(__name__)

@pytest.mark.order(1)
def test_set_logger():
    global logger

    console_handler = logging.StreamHandler()
    # https://docs.python.org/3/library/logging.html#logrecord-attributes
    formatter = logging.Formatter("{asctime} {levelname} {module}#{filename}#{lineno}: {message}",
                                  style="{",
                                  datefmt="%Y-%m-%d %H:%M",
                                  )
    console_handler.setFormatter(formatter)

    if logger.hasHandlers():
        logger.handlers.clear()

    logger.addHandler(console_handler)
    logger.setLevel(logging.ERROR)
    # logger.setLevel(logging.INFO)

@pytest.mark.order(2)
def test_create_notesdb():
    global notesdb
    notesdb = NotesDB()
    # notesdb = NotesDB(dbfile="test.db")
    # https://docs.python.org/3/library/logging.html#logging-levels
    # notesdb = NotesDB(loglevel="INFO")
    # notesdb = NotesDB(loglevel="DEBUG")

@pytest.mark.order(3)
def test_setup():
    nid = notesdb.note_add('First Note', 'This is a first test note')
    assert nid == 1

    nid = notesdb.note_add('Title Note 2', 'Note 2')
    assert nid == 2

    nid = notesdb.note_add('Title Note 3', 'Note 3')
    assert nid == 3

    nid = notesdb.note_add('Title Note 4', 'Note 4')
    assert nid == 4

    nid = notesdb.note_add('Title Note 5', 'Note 5')
    assert nid == 5

    nid = notesdb.note_add('Title Note 6', 'Note 6')
    assert nid == 6

    nid = notesdb.note_add('Title Note 7', 'Note 7')
    assert nid == 7

    nid = notesdb.note_add('Title Note 8', 'Note 8')
    assert nid == 8

    nid = notesdb.note_add('Title Note 9', 'Note 9')
    assert nid == 9

    nid = notesdb.note_add('Title Note 10', 'Note 10')
    assert nid == 10

@pytest.mark.order(4)
def test_update_note():
    global notesdb
    global logger

    resp = notesdb.note_update(1, note='Note 1 - updated')
    assert resp == True
    node_entry = notesdb.note_get(1)
    assert node_entry != None
    assert len(node_entry) == 5

    id, t, n, ct, mt = notesdb.note_get(1)
    if logger.isEnabledFor(logging.INFO):
        logger.info(f"note id          : {id}")
        logger.info(f"title            : {t}")
        logger.info(f"note             : {n}")
        logger.info(f"creation time    : {ct}")
        logger.info(f"modifiction time : {mt}")

@pytest.mark.order(5)
def test_interval():
    global notesdb
    global logger

    dt_last = datetime.datetime.now()
    dt_first = dt_last.replace(month=1, day=1, hour=0, minute=0, second=0, microsecond=0)
    logger.info(f">>>>>dt_first : {dt_first}")
    logger.info(f">>>>>dt_last  : {dt_last}")
    note_entries = notesdb.note_get_interval(dt_first, dt_last)
    assert note_entries != None
    logger.info(f"number of hits: {len(note_entries)}")
    if logger.isEnabledFor(logging.INFO):
        for note_entry in note_entries:
            logger.info(f"    {note_entry}")

@pytest.mark.order(6)
def test_delete_note():
    global notesdb
    resp = notesdb.note_delete(5)
    assert resp == True
    node_entry = notesdb.note_get(5)
    assert node_entry != None
    assert len(node_entry) == 0
