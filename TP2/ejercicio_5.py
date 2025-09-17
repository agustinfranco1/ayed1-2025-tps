"""
Ej 5: Escribir una función que reciba una lista como parámetro y devuelva True si la lista 
está ordenada en forma ascendente o False en caso contrario. Por ejemplo, 
ordenada([1, 2, 3]) retorna True y ordenada(['b', 'a']) retorna False. Desarrollar 
además un programa para verificar el comportamiento de la función.
"""
from typing import List

def ordenada(lista: List[int]) -> bool:
    """
    Evalua si la lista esta ordenada de forma ascendente.

    Pre: Recibe una lista que en realidad puede ser tanto de enteros como de strings.

    Post: Devuelve True si la lista se encuentra ordenada de forma ascendente o False en caso contrario.
    """
    for i in range(len(lista) - 1):
        if lista[i] > lista[i + 1]:
            return False
    return True



assert ordenada([1, 2, 3]) == True
assert ordenada([3, 2, 1]) == False
assert ordenada(['a', 'b', 'c']) == True
assert ordenada(['b', 'a']) == False
print("\nPruebas exitosas\n")