# Hashable
Die Objekte in einem [Set](./sets.md) und die Keys
in einem [Dictionary](./dictionaries.md) müssen
_hashable_ sein. Deshalb die Frage: **Was bedeutet 
eigentlich _hashable_**? 

Im 
[Python Glossary: hashable](https://docs.python.org/3/glossary.html#term-hashable) 
findet man zum Thema Hashable den folgenden Eintrag:

>hashable  
>An object is hashable if it has a hash value which 
>never changes during its lifetime (it needs a 
>__hash__() method), and can be compared to other 
>objects (it needs an __eq__() method). Hashable 
>objects which compare equal must have the same hash 
>value.
>
>Hashability makes an object usable as a dictionary 
>key and a set member, because these data structures 
>use the hash value internally.
>
>Most of Python’s immutable built-in objects are 
>hashable; mutable containers (such as lists or 
>dictionaries) are not; immutable containers (such as 
>tuples and frozensets) are only hashable if their 
>elements are hashable. Objects which are instances 
>of user-defined classes are hashable by default.
>They all compare unequal (except with themselves),
>and their hash value is derived from their id().

Fazit: soll eine eigene Klasse _hashable_ sein, 
müssen die Methoden \_\_eq__ und \_\_hash__ 
geeignet implementiert werden.

Hier eine Tabelle die zeigt, welche Python Operation 
auf welche Methode einer Klasse delegiert werden:

| Operation | Dunder         | Rückgabewert              |
|-----------|----------------|---------------------------|
| a == b    | a.\_\_eq__(b)  | True/False/NotImplemented |  a.\_\_ne__(b)  | True/False/NotImplemented |
| hash(a)   | a.\_\_hash__() | int                       |

Die Methode \_\_eq__ gibt typischerweise einen von 
den Werten _True_, _False_ oder _NotImplemented_ 
(if objects can't be compared) zurück. Die 
Defaultimplementierung von \_\_eq__ basiert auf dem 
is Operator, der die Identity (Funktion _id_) 
vergleicht.

Die Defaultimplementierung von \_\_ne__ ruft 
\_\_eq__ auf und negiert den boolschen Rückgabewert. 
Hat \_\_eq__ den Rückgabewert _NotImplemented_, wird 
dieser auch von \_\_ne__ zurückgegeben.

Bei einer eigenen Implementierung der Methoden 
\_\_eq__ und \_\_hash__ ist folgendes zu beachten: 

    Ist a == b dann muss auch hash(a) == hash(b) sein
    Ist hash(a) == hash(b) dann kann a == b oder a != b sein
    Ist hash(a) != hash(b) dann muss auch a != b sein

---

## Weiterführende Links

* [Python Glossary: hashable](https://docs.python.org/3/glossary.html#term-hashable)
* [Every dunder method in Python](https://www.pythonmorsels.com/every-dunder-method/)
* [Hashing and Equality in Python](https://eng.lyft.com/hashing-and-equality-in-python-2ea8c738fb9d?gi=39d51031a25e)
* [What is "hashable" in Python?](https://www.pythonmorsels.com/what-are-hashable-objects/)
* [Overloading equality in Python](https://www.pythonmorsels.com/overloading-equality-in-python/)
* [Making hashable objects](https://www.pythonmorsels.com/making-hashable-objects/)
