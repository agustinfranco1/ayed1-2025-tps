"""
Ej 6: Escribir una función que reciba una lista de números enteros como parámetro y la 
normalice, es decir que todos sus elementos deben sumar 1.0, respetando las pro
porciones relativas que cada elemento tiene en la lista original. Desarrollar también 
un programa que permita verificar el comportamiento de la función. Por ejemplo, 
normalizar([1, 1, 2]) debe devolver [0.25, 0.25, 0.50].
"""
from typing import List

def normalizar(lista: List[int]) -> List[float]:
    """
    Normaliza una lista de numeros enteros.

    Pre: Recibe una lista de enteros que seran normalizados.

    Post: Devuelve una lista de flotantes ya normalizada.
    """
    total = sum(lista)
    if total == 0:
        return [0.0 for x in lista]
    return [i / total for i in lista]


assert sum(normalizar([1, 1, 2])) == 1.0
assert sum(normalizar([1, 1, 1])) == 1.0
assert sum(normalizar([2, 4, 8, 8])) == 1.0
assert sum(normalizar([17, 29, 34, 22, 33])) == 1.0
assert sum(normalizar([0, 0])) == 0.0
print("\nPruebas exitosas\n")



