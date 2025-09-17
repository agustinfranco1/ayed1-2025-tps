"""
Ej 4: Eliminar de una lista de números enteros aquellos valores que se encuentren en 
una segunda lista. Imprimir la lista original, la lista de valores a eliminar y la lista 
resultante. La función debe modificar la lista original sin crear una copia modificada.
"""
from typing import List

def eliminar_valores(lista: List[int], eliminar: List[int]) -> None:
    """
    Elimina de la lista original todos los valores que esten en la segunda lista.

    Pre: Recibe dos listas de enteros, los elementos de la segunda se eliminaran de la primera.

    Post: No Devuelve nada, modifica la primera lista recibida.
    """
    i = 0
    while i < len(lista):
        if lista[i] in eliminar:
            lista.pop(i)
        else:
            i += 1


def main():
    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    lista2 = [1, 2, 3]

    print(f"\nLista original: {lista}")
    print(f"\nValores a eliminar: {lista2}")
    eliminar_valores(lista, lista2)
    print(f"\nLista resultante: {lista}")


main()
