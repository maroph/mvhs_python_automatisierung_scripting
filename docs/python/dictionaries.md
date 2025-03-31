# Dictionaries
Ein Dictionary speichert seinen Inhalt in Key/Value
(Schlüssel/Wert) Paaren ab. Der Datentyp der Werte
kann beliebig sein. Ähnliches gilt für die
Schlüssel, jedoch muss der Datentyp unveränderbar
sein (int, float, String, Tuple, ...). Der 
Zugriff auf die Values erfolgt dabei über den Key
und nicht, wie bei Listen, über einen Index.

* Die Datentypen für den Key müssen [hashable](./hashable.md) sein.


Bis einschließlich der Python Version 3.6 gab es 
für die Key/Value Paare eines Dictionaries keine
feste Reihenfolge. D.h.: hat man in einer for
Schleife (Beispiele siehe weiter unten) über die
Keys eines Dictionaries iteriert, hing die
Reihenfolge der Keys von der verwendeten Python
Implementierung ab. Seit der Python Version 3.7
sind Dictionaries ordered, d.h. die Key/Value Paare
werden in einer festen Reihenfolge ausgegeben. Die
Reihenfolge richtet sich nach dem Zeitpunkt, zu dem
sie in das Dictionary eingestellt wurden.

## Anlegen eines Dictionaries
Man kann entweder ein leeres Dictionary anlegen

    dict = {}
    ## {}
    
    oder

    d = dict()
    ## {}

oder das Dictionary mit Inhalt anlegen

    dict = {
        "key1": "val1",
        "key2": "val2"
    }
    ## {'key1': 'val1', 'key2': 'val2'}

## Zugriff auf einen Wert im Dictionary
Auf die Werte im Dictionary wird mit dem Schlüssel
zugegriffen:

    value = dict[key]

    value = dict["key1"]
    ## val1

Greift man auf einen Key zu, den es im Dictionary
nicht gibt, wird ein KeyError geworfen. 

### Zugriff auf einen Wert im Dictionary - auch wenn der Key nicht existiert

    value = dict.get(key)

Ist der Key nicht im Dictionary, wird _None_
zurückgegeben.

    value = dict.get(key, default_value)

Ist der Key nicht im Dictionary, wird der angegebene
Defaultwert zurückgegeben.

### Default Dictionary
Statt jedes Mal beim Aufruf von _get_ einen
Defaultwert mitzuübergeben, kann man auch die Klasse 
[defaultdict](https://docs.python.org/3/library/collections.html?highlight=defaultdict#collections.defaultdict)
verwenden.

    from collections import defaultdict

    def default_value():
        return 0

    dict = {}
    d = defaultdict(default_value, dict)
    value = d.get(key)

Wir jetzt beim Aufruf von _get_ ein Key verwendet,
der nicht im Dictionary abgelegt ist, wird der Wert,
den die Funktion _default_value_ zurückgibt (im
Beispiel __0__) zurückgegeben.

## Ein Key/Value Paar zum Dictionary hinzufügen:

    dict[key] = value

    dict["key3"] = "val3"
    dict
    ## {'key1': 'val1', 'key2': 'val2', 'key3': 'val3'}

## Ein Key/Value Paar auf einem Dictionary löschen

    del(dict[key])
    oder 
    del dict[key]
    
    del dict["key3"]
    dict
    ## {'key1': 'val1', 'key2': 'val2'}

Wird ein Key verwendet, des es im Dictionary nicht
gibt, wird ein KeyError geworfen.

### Löschen und lesen

    value = dict.pop(key)

    value = dict.pop("key2")
    ## val2
    dict
    ## {'key1': 'val1'}

Greift man auf einen Key zu, den es im Dictionary
nicht gibt, wird ein KeyError geworfen. 

Man kann abeim Auruf auch einen Defaultwert angeben,
der zurückgegeben wird, wenn der Key im Dictionary
nicht gefunden wird

    value = dict.pop(key, default_value)
    
    value = dict.pop("key42", "Don't Panic!")
    ## Don't Panic!


## Anzahl der Key/Value Paare in einem Dictionary

    len(dict)

    dict = { "key1": "val1", "key2": "val2" }
    ## {'key1': 'val1', 'key2': 'val2'}
    len(dict)
    ## 2 

## Abfragen ob ein Key in einem Dictionary enthalten ist

    key1 in dict

    if "key1" in dict:
        print("gefunden, Wert: ", dict["key1"])

## Abfragen ob ein Key nicht in einem Dictionary enthalten ist

    key1 not in dict

    if "key1" not in dict:
        print("nicht gefunden")

## Alle Keys aus einem Dictionary lesen

    for key in dict:
        print(key)

Oder

    for key in dict.keys():
        print(key)

## Alle Keys aus einem Dictionary als Enumeration lesen

    dict
    ## {'key1': 'val1', 'key2': 'val2', 'key3': 'val3'}
    
    list(enumerate(dict))
    ## [(0, 'key1'), (1, 'key2'), (2, 'key3')]  [(0, 'key1'), (1, 'key2'), (2, 'key3')]

    for count, key in enumerate(dict):
        print(f"count: {count} , key: {key}")
    
    Ausgabe:
    count: 0 , key: key1
    count: 1 , key: key2
    count: 2 , key: key3

Sieh auch: [enumerate](https://docs.python.org/3/library/functions.html#enumerate) in der
Python Dokumentation.

### Alle Keys in einer Liste speichern

    liste = list(dict.keys())

## Abfragen ob ein Wert in einem Dictionary enthalten ist

    value in dict.values()

    if "val1" in dict.values():
        print("gefunden")

## Abfragen ob ein Wert nicht in einem Dictionary enthalten ist

    value not in dict.values()

    if "val1" not in dict.values():
        print("nicht gefunden")

## Alle Values aus einem Dictionary lesen

    for key in dict:
        print(dict[key])

Oder 

    for value in dict.values():
        print(value)

### Alle Values in einer Liste speichern

    liste = list(dict.values())

## Alle Key/Value Paare aus einem Dictionary lesen

### Jedes Paar als Tuple

    for item in dict.items():
        print(item[0], item[1])

### Alles Paare in einer Liste speichern

    liste = list(dict.items())

### Jedes Paar als einzelne Werte: key, value

    for key, value in dict.items():
        print(key, value)

## Alle Key/Value Paare aus einem Dictionary als Enumeration lesen

    dict
    ## {'key1': 'val1', 'key2': 'val2', 'key3': 'val3'}
    
    for count, (key, value) in enumerate(dict.items()):
        print(f"count: {count} , key: {key} , value: {value}")


    Ausgabe:
    count: 0 , key: key1 , value: val1
    count: 1 , key: key2 , value: val2
    count: 2 , key: key3 , value: val3

Sieh auch: [enumerate](https://docs.python.org/3/library/functions.html#enumerate) in der
Python Dokumentation.

## Inhalt eines Dictionaries löschen

    dict.clear()

## Dictionary kopieren

    dict_copy = dict.copy()

**Achtung: es wird eine sogenannte _shallow copy_
erzeugt!**

D.h.: es werden die einzelnen Werte (Objekte)
kopiert - genauer gesagt: es werden die
Referenzen auf die Objekte kopiert. Ist ein Objekt
mutable (veränderbar - z.B. eine Liste), dann führt
eine Änderung an so einem Wert zu einer Änderungen
im Original und in der Kopie. Sind alle Werte im
Dictionary immutable (unveränderbar), dann reicht
diese Art der Kopie aus.

Eine vollständige Kopie kann man mit der Funktion
[deepcopy](https://docs.python.org/3/library/copy.html#copy.deepcopy) erzeugen
Aufruf

    import copy
    dict_copy = copy.deepcopy(dict)

## Einfügen eines Dictionaries

    dict.update(dict2)

Alle Key/Value Paare aus dem Dictionary dict2 werden
in das Dictionary dict eingefügt. Ist der Key
bereits in dict enthalten, wird der Wert durch den
Wert aus dem Dictionary dict2 ersetzt.

---

## Weiterführende Links

* [Python-Kurs: Dictionaries](https://www.python-kurs.eu/python3_dictionaries.php)
* [Dictionaries in Python](https://realpython.com/python-dicts/)
* [How to Iterate Through a Dictionary in Python](https://realpython.com/iterate-through-dictionary-python/)
* [Defaultdict in Python](https://www.geeksforgeeks.org/defaultdict-in-python/)
* [Python Dictionary Comprehensions: How and When to Use Them](https://realpython.com/python-dictionary-comprehension/)
