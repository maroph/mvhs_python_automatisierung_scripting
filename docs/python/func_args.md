# Funktionsargumente
Oft werden in einer Funktionsdefinition
alle Parameter angegeben, z.B.:

```
def func_sample(arg1, arg2, arg3):
```

Es gibt aber auch die Möglichkeit, eine nicht
festgelegte Anzahl von Parametern zu verwenden.

```
def func_sample(*args):
```
Hier werden die Argumente als Tupel an die Funktion
übergeben.

```
def func_sample(**kwargs):
```
In diesem Fall werden die Argumente als Dictonary
an die Funktion übergeben.

Ein Beispiel hierzu ist in der Source 
[func_arg_args_kwargs.py]{:target="blank"}
[func_arg_args_kwargs.py]: https://raw.githubusercontent.com/maroph/mvhs_python_automatisierung_scripting/main/sources/extras/func_arg_args_kwargs.py
abgelegt.

---

## Weiterführende Links

* [Python-Kurs: Funktionen](https://www.python-kurs.eu/python3_funktionen.php)
* [Python Tips: *args and **kwargs](https://book.pythontips.com/en/latest/args_and_kwargs.html)
