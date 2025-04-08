# Sets - Mengen
Ein Set ist eine Sammlung von Objekten. Diese 
Sammlung ist

* ungeordnet
* unveränderbar  
  Genauer: die einzelnen Objekte in einem Set 
  *sollten* nicht verändert werden. Es können aber
  neue Objekte hinzugefügt werden oder aber 
  bereits vorhandene Objekte gelöscht werden.
* nicht indiziert
* Die Objekte im Set müssen [hashable](./hashable.md)
  sein.

Sets werden genutzt, um mehrere Objekte ein einer
Variablen abzuspeichern. Dabei werden keine Duplikate
zu einem Set hinzugefügt.

## Anlegen eines Sets
Man kann entweder ein leeres Set anlegen

    myset = set()
    ## set()

oder das Set mit Inhalt anlegen

    myset = { "item1","item2", "item3" }
    ## {'item2', 'item1', 'item3'}

__Hinweis:__  
* Die Werte True und 1 werden in einem Set als ein
  Wert betrachtet. Kommen beide vor, wird ein Wert als
  Duplikat behandelt
* Die Werte False und 0 werden in einem Set als ein
  Wert betrachtet. Kommen beide vor, wird ein Wert als
  Duplikat behandelt

Beispiel

    myset = { 0, 1, 2, True, False }
    ## {0, 1, 2}

## Länge eines Sets

    len(myset)

    myset = { 1,2,3,4,5 }
    ## {1, 2, 3, 4, 5}
    
    len(myset)
    ## 5

## Zugriff auf ein Set

    myset = { 1,2,3,4,5 }
    ## {1, 2, 3, 4, 5}

### Zugriff auf alle Objekte in einem Set

    for elem in myset:
        print(elem)

### Zugriff auf alle Objekte in einem Set als Enumeration

    myset
    ## {1, 2, 3, 4, 5}
    
    for count, obj in enumerate(myset):
        print(f"count: {count} , obj: {obj}")
    
    Ausgabe:
    count: 0 , obj: 1
    count: 1 , obj: 2
    count: 2 , obj: 3
    count: 3 , obj: 4
    count: 4 , obj: 5

Sieh auch: [enumerate](https://docs.python.org/3/library/functions.html#enumerate) in der
Python Dokumentation.

## Objekt ist in einem Set

    object in myset

    if 1 in myset:
        print("in Set gefunden")

## Objekt ist nicht in einem Set

    object not in myset

    if 42 not in myset:
        print("nicht in Set gefunden")

## Objekt zu einem Set hinzufügen

    myset.add(6)
    myset
    ## {1, 2, 3, 4, 5, 6}

Ist ein Objekt bereits in einem Set vorhanden, wird
das Set nicht geändert

    myset.add(1)
    myset
    ## {1, 2, 3, 4, 5}

## Ein Set zu einem Set hinzufügen

    set1.update(set2)

Bereits vorhandene Objekte werden beim Update
ignoriert

    set1 = { 1,2,3,4,5 }
    set2 = { 3,4,5,6,7,8 }
    set1.update(set2)
    set1
    ## {1, 2, 3, 4, 5, 6, 7, 8}

## Ein Objekt aus einem Set löschen

    myset.remove(objekt)

    myset
    ## {1, 2, 3, 4, 5}
    myset.remove(3)
    myset
    ## {1, 2, 4, 5}

Wird beim Aufruf von remove ein Objekt angegeben,
das nicht im Set enthalten ist, wird ein KeyError
geworfen.

Alternativ kann man die Methode _discard_ nutzen.
Diese Methode wirft keinen KeyError, wenn das 
Objekt nicht im Set enthalten ist

    myset
    ## {1, 2, 3, 4, 5}
    myset.discard(42)
    myset
    ## {1, 2, 3, 4, 5}

Für Sets gibt es auch die Methode _pop_.

    objekt = myset.pop()

Da es auf Sets keinen Index gibt, wird mit dieser 
Methode ein zufälliges Objekt aus dem Set gelöscht. 
Die Methode gibt das gelöschte Objekt zurück.

## Set leeren

    myset.clear()

## Set löschen

    del myset

## Set Operationen
Für die Beispiele werden die folgenden Sets 
verwendet

    set1 = { 1,2,3,4,5 }
    ## {1, 2, 3, 4, 5} 
    set2 = { 3,4,5,6,7,8 }
    ## {3, 4, 5, 6, 7, 8}

### Vereinigung

    s1 | s2
    ## {1, 2, 3, 4, 5, 6, 7, 8}

    s3 = s1.union(s2)
    s3
    ## {1, 2, 3, 4, 5, 6, 7, 8}

Man kann mit _union_ auch mehrere Sets vereinigen

    myset = set1.union(set2, set3, set4)

### Schnitt

    s1 & s2
    ## {3, 4, 5}

## Differenz

In s1, nicht in s2

    s1 - s2
    ## {1, 2}
    
In s2, nicht in s1

    s2 -s1
    ## {8, 6, 7}

## frozenset
Set Objekte sind veränderbar. Mit Hilfe der
Funktion __frozenset__ werden Sets
"eingefroren" und somit unveränderbar.

    myset = { 1, 2, 3, 'A', 'B', 'C' }
    ## {'A', 1, 2, 3, 'B', 'C'}

    myset_frozen = frozenset(myset)
    ## frozenset({'A', 1, 2, 3, 'B', 'C'})

    type(myset_frozen)
    ## class 'frozenset'>

---

## Weiterführende Links

* [w3schools: Python Sets](https://www.w3schools.com/python/python_sets.asp)
* [Set Types - set, frozenset](https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset)
* [Hashable](https://docs.python.org/3/glossary.html#term-hashable)
* [dataclasses — Data Classes](https://docs.python.org/3/library/dataclasses.html#module-dataclasses)
* [w3schools: frozenset() Function](https://www.w3schools.com/python/ref_func_frozenset.asp)
* [Mengen managen über: set und frozenset](https://www.python-lernen.de/mengenlehre-set-frozenset.htm)
* [Python Set Comprehensions: How and When to Use Them](https://realpython.com/python-set-comprehension/)
 