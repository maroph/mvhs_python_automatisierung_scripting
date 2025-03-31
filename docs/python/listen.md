# Listen
Eine Liste ist eine Sammlung von Elementen, die in einer festen Reihenfolge
abgelegt werden. Der Datentyp der Elemente kann beliebig sein. Der Zugriff erfolgt 
über den Index, der die Position des Elements in der Liste bestimmt. Indizes 
beginnen mit 0 und nicht mit 1!

## Anlegen einer Liste
Man kann entweder ein leere Liste anlegen

    liste = []
    ## []
    
    oder

    l = list()
    ## []

oder eine Liste mit Inhalt anlegen

    liste = [ "val1", "val2" ]
    liste = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]
    liste = [i for i in range(1, 11)]
    liste = [ "Don't Panic!", 42, [ 3, 1, 4] ]

## Anzahl der Werte in einer Liste

    len(liste)

    liste = [i for i in range(1, 11)]
    ## [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    len(liste)
    ## 10

## Index-Zugriff auf einen Wert in einer Liste
Auf die Werte in einer Liste kann mit dem Index zugegriffen werden

    liste = [ "val1", "val2" ]

    value1 = liste[0] # erstes Element
    ## val1
    value2 = liste[1] # zweites Element
    ## val2

### Zugriff auf das letzte/vorletzte/... Element einer Liste

    liste = [i for i in range(1, 11)]
    ## [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    value = liste[-1] # letztes Element
    ## 10
    value = liste[-2] # vorletztes Element
    ## 9
    ...

### Slicing
Man kann auch eine Liste mit einem zusammenhängenden
Teil einer Liste erzeugen:

    liste = [i for i in range(1, 11)]
    ## [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    liste[0:5] # Elemente 0 bis 4 der Liste
    ## [1, 2, 3, 4, 5]

    liste[6:] # Elemente 6 bis Ende
    ## [7, 8, 9, 10]

### Weiter Beispiele
    liste = [i for i in range(1, 11)]
    ## [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    liste[0]
    ## 1

    liste[6]
    ## 7

    liste[-1]
    ## 10

    liste[-2]
    ## 9

    liste[0:5]
    ## [1, 2, 3, 4, 5]

    liste[6:]
    ## [7, 8, 9, 10]

    liste[6:8]
    ## [7, 8]

    liste[:2]
    ## [1, 2]

    liste[3:-1]
    ## [4, 5, 6, 7, 8, 9]

    liste[:-1]
    ## [1, 2, 3, 4, 5, 6, 7, 8, 9]

## Ein Wert am Ende der Liste hinzufügen

    liste.append(value)

    liste = [i for i in range(1, 11)]
    ## [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    liste.append(11)
    ## [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

## Einen Wert in eine Liste einfügen:

    liste.insert(idx, value)

    liste = [i for i in range(1, 11)]
    ## [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    liste.insert(3, 42)
    ## [1, 2, 3, 42, 4, 5, 6, 7, 8, 9, 10]

## Erstes Auftreten eines Wertes aus einer Liste löschen

    liste.remove(value)
         
    liste
    ## [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 3]
    liste.remove(3)
    ## [1, 2, 4, 5, 6, 7, 8, 9, 10, 3]


## Ein Wert aus einer Liste löschen

    del(liste[idx])
    oder 
    del liste[idx]
    
    liste
    ## [1, 2, 3, 3, 4, 5, 6, 7, 8, 9, 10]
    del(liste[3])
    liste
    ## [1, 2, 3, 5, 6, 7, 8, 9, 10]

## Letzten Wert lesen und aus der Liste löschen

    value = liste.pop()
    
    liste
    ## [1, 2, 3, 3, 4, 5, 6, 7, 8, 9, 10]
    value = liste.pop()
    ## [1, 2, 3, 4, 5, 6, 7, 8, 9]
    value
    ## 10

## Einen Wert lesen und aus der Liste löschen

    value = liste.pop(idx)

    liste
    ## [1, 2, 3, 3, 4, 5, 6, 7, 8, 9, 10]
    value = liste.pop(4)
    ## [1, 2, 3, 4, 6, 7, 8, 9, 10]
    value
    ## 5

## Listenelemente an eine Liste anhängen

    liste.extend(liste2)
    
    liste1
    ## [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    liste2
    ## [11, 12, 13, 14, 15]
    liste.extend(liste2)
    ## [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    liste3 = liste1 + liste2
    ## [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

## Wie oft ist ein Wert in einer Liste enthalten

    liste.count(wert)
    
    liste
    ## [1, 2, 3, 3, 4, 5, 6, 7, 8, 9, 10]
    liste.count(3)
    ## 2
    liste.count(42)
    ## 0

## Erstes Auftreten eines Wertes in einer Liste
Sieh auch: [Python List Index() Tutorial](https://www.datacamp.com/tutorial/python-list-index)

    idx = liste.index(value)
    idx = liste.index(value, start)
    idx = liste.index(value, start, stop)
    
    start : Index, ab dem gesucht wird
    stop  : Es wird gesucht bis vor diesem Index 

    liste
    ## [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 3]
    idx = liste.index(3)
    ## 2

__Vorsicht: Wurde der Wert nicht in der Liste
gefunden, wird ein ValueError geworfen__

    idx = liste.index(42)
          ^^^^^^^^^^^^^^^
    ValueError: 42 is not in list

## Abfragen, ob ein Wert in einer Liste enthalten ist

    value in liste

    liste
    ## [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    if 3 in liste:
        print("gefunden")

## Abfragen, ob ein Wert nicht in einer Liste enthalten ist

    value not in liste

    liste
    ## [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    if 42 not in liste:
        print("nicht gefunden")

## Alle Werte aus einer Liste lesen

    for value in liste:
        print(value)

## Alle Werte aus einer Liste als Enumeration lesen

    liste
    ## ['a', 'b', 'c']

    list(enumerate(liste))
    ## [(0, 'a'), (1, 'b'), (2, 'c')]

    for count, obj in enumerate(liste):
        print(f"count: {count} , obj: {obj}")
    
    Ausgabe:
    count: 0 , obj: a
    count: 1 , obj: b
    count: 2 , obj: c

    for count, obj in enumerate(liste, start=42):
        print(f"count: {count} , obj: {obj}")
    
    Ausgabe:
    count: 42 , obj: a
    count: 43 , obj: b
    count: 44 , obj: c

Sieh auch: [enumerate](https://docs.python.org/3/library/functions.html#enumerate) in der
Python Dokumentation.

## Inhalt einer Liste löschen

    liste.clear()
    oder
    del liste[:]

## Umkehr der Reihenfolge in einer Liste

    liste.reverse()

## Werte in einer Liste sortieren

    liste.sort()

Beim Aufruf von sort ist darauf zu achten, dass für
alle Objekte (Werte) in der Liste das gleiche
Sortierverfahren verwendet werden kann.

Beispiel: die Liste enthält nur Zahlen oder nur
Strings. Andernfalls wird ein TypeError
geworfen:

    ## TypeError: ’<’ not supported between instances of ’str’ and ’int’

### Sortierreihenfolge umkehren

    liste.sort(reverse=True)

## Liste kopieren

    liste2 = liste.copy()
    oder
    liste2 = liste[:]

**Achtung: es wird eine sogenannte _shallow copy_
erzeugt!**

D.h.: es werden die einzelnen Einträge (Objekte)
kopiert - genauer gesagt: es werden die
Referenzen auf die Objekte kopiert. Ist ein Objekt
mutable (veränderbar - z.B. eine Liste), dann führt
eine Änderung an so einem Wert zu einer Änderungen
im Original und in der Kopie. Sind alle Werte in der
Liste immutable (unveränderbar), dann reicht diese
Art der Kopie aus.

Eine vollständige Kopie kann man mit der Funktion
[deepcopy](https://docs.python.org/3/library/copy.html#copy.deepcopy) erzeugen
Aufruf

    import copy
    liste2 = copy.deepcopy(liste)

## Prüfen, ob alle Listenelemente vom gleichen Datentyp sind.

Im Beispiel wird geprüft, ob alle Elemente in der
Liste vom Datentyp str sind.

    def is_list_of_strings(lst):
        return lst and isinstance(lst, list) and all(isinstance(item, str) for item in lst)

## Alle Werte aus einer Liste lesen und löschen
Mit dieser naheliegenden for Schleife lässt sich das Problem leider nicht lösen :-(

    for value in liste:
        print(value)
        liste.pop(0)

Denn: es wird einerseits implizit ein Iterator benutzt, um alle Elemente der Liste 
nacheinander zu bekommen und zum anderen wird direkt auf der Liste operiert.

Man kann hierzu eine while Schleife verwenden:

    while (len(liste) > 0):
        print(liste.pop(0))

Alternativ kann man auch die folgende for Schleife verwenden:

    for _ in range(len(liste)):
        print(liste.pop(0))

---

## Weiterführende Links

* [Python Documentation: More on Lists](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)
* [Python Documentation: Built-in Function sorted](https://docs.python.org/3/library/functions.html#sorted)
* [Python Documentation: Sorting Techniques](https://docs.python.org/3/howto/sorting.html)
* [Python-Kurs: Listen](https://www.python-kurs.eu/python3_listen.php)
* [Python's list Data Type: A Deep Dive With Examples](https://realpython.com/python-list/)
