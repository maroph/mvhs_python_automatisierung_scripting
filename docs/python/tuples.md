# Tuples - Unveränderliche Listen
Tuple verhalten sich genau wie Listen, aber ihr Inhalt kann nicht verändert werden.

## Anlegen eines Tuple
    tuple = ("val1", "val2")

### Leeres Tuple

    tuple = ()

### Tuple mit einem Element

    tuple = ("val1",)

## Zugriff auf einen Wert in einem Tuple
Auf die Werte in einem Tuple wird mit dem Index zugegriffen:

    value1 = tuple[0]
    value2 = tuple[1]

__Achtung__: der Index einer Liste fängt immer mit dem Wert 0 an.

## Zugriff auf das letzte/vorletzte Element eines Tuple:

    value = tuple[-1] # letztes Element
    value = tuple[-2] # vorletztes Element
    ...

## Anzahl der Werte in einem Tuple

    len(tuple)

## Abfragen ob ein Wert in einem Tuple enthalten ist

    if "val1" in tuple:
        print("gefunden")

## Abfragen ob ein Wert nicht in einem Tuple enthalten ist

    if "val1" not in tuple:
        print("nicht gefunden")

## Alle Werte aus einem Tuple lesen

    for value in tuple:
        print(value)

---

Ein Tutorial zum Thema Tuple findet man hier: 
[Python's tuple Data Type: A Deep Dive With Examples](https://realpython.com/python-tuple/)
