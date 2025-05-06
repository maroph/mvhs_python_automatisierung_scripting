import pytest
from notesdb import NotesDB, NotesDBException
import datetime

notesdb  = None

@pytest.mark.order(1)
def test_create_notesdb():
    global notesdb
    notesdb = NotesDB()
    # notesdb = NotesDB(verbose=True, debug=True)

@pytest.mark.order(2)
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

@pytest.mark.order(3)
def test_update_note():
    global notesdb
    resp = notesdb.note_update(1, note='Note 1 - updated')
    assert resp == True
    node_entry = notesdb.note_get(1)
    assert node_entry != None
    assert len(node_entry) == 5

    id, t, n, ct, mt = notesdb.note_get(1)
    print(f"note id          : {id}")
    print(f"title            : {t}")
    print(f"note             : {n}")
    print(f"creation time    : {ct}")
    print(f"modifiction time : {mt}")

@pytest.mark.order(4)
def test_interval():
    global notesdb
    dt_last = datetime.datetime.now()
    dt_first = dt_last.replace(month=1, day=1, hour=0, minute=0, second=0, microsecond=0)
    print(f">>>>>dt_first : {dt_first}")
    print(f">>>>>dt_last  : {dt_last}")
    note_entries = notesdb.note_get_intervall(dt_first, dt_last)
    assert note_entries != None
    print(f"number of hits: {len(note_entries)}")
    for note_entry in note_entries:
        print(f"    {note_entry}")

@pytest.mark.order(5)
def test_delete_note():
    global notesdb
    resp = notesdb.note_delete(5)
    assert resp == True
    node_entry = notesdb.note_get(5)
    assert node_entry != None
    assert len(node_entry) == 0
