# Beispiel: Funktionen als Werte in einem Dictionary
#
# Der Übersichtlichkeit halber wurde in diesem Beispiel auf
# eine Fehlerbehandlung (z.B.: Division durch 0) verzichtet.

def addieren(n1: int, n2: int, op_code: str = None) -> int:
    return n1 + n2

def subtrahieren(n1: int, n2: int, op_code: str = None) -> int:
    return n1 - n2

def multiplizieren(n1: int, n2: int, op_code: str = None) -> int:
    return n1 * n2

def dividieren(n1: int, n2: int, op_code: str = None) -> float:
    return float(n1) / float(n2)

def noop(n1 = None, n2 = None, op_code: str = None) -> str:
    if op_code:
        return f"Operation '{op_code}' nicht unterstützt"
    return "Operation nicht unterstützt"

op_dict = {
    '+': addieren,
    '-': subtrahieren,
    '*': multiplizieren,
    '/': dividieren
}

a = 3
b = 2
op_list = ['+', '-', '*', '/', '&' ]
for op in op_list:
    operation = op_dict.get(op, noop)
    print(f"{a} {op} {b} : {operation(a, b, op)}")
