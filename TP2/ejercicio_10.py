"""
Ej 10: Generar una lista con números al azar entre 1 y 100 y crear una nueva lista con los 
elementos de la primera que sean impares. El proceso deberá realizarse utilizando 
la función filter(). Imprimir las dos listas por pantalla.
"""
import random as rn
from typing import List

def generar_lista(n: int) -> List[int]:
    """
    Genera una lista de N numeros entre 1 y 100 aleatoriamente.

    Pre: Recibe un numero entero, la cantidad elementos que tendra la lista.

    Post: Devuelve una lista de enteros con N cantidad de elementos entre 1 y 100.
    """
    return [rn.randint(1, 100) for x in range(n)]

def filtrar_impares(lista: List[int]) -> List[int]:
    """
    Filtra los elementos impares de otra lista.

    Pre: Recibe una lista de enteros.

    Post: Devuelve una lista de enteros correspondientes a los elementos impares de la lista recibida.
    """
    return list(filter(lambda x: x % 2 != 0, lista))

def main():
    while True:
        n = input("Ingrese la cantidad de numeros a generar: ")
        if n.isdigit() and int(n) > 0:
            n = int(n)
            break
        else:
            print("Error: debe ingresar un numero entero mayor a 0.")

    lista_1_100 = generar_lista(n)
    lista_impares = filtrar_impares(lista_1_100)

    print(f"\nLista original: \n{lista_1_100}")
    print(f"\nLista de impares: \n{lista_impares}")

main()
