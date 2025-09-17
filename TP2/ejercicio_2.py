"""
Ej 2: Escribir funciones para:
a. Generar una lista de N números aleatorios del 1 al 100. El valor de N se ingresa 
a través del teclado.
b. Recibir una lista como parámetro y devolver True si la misma contiene algún 
elemento repetido. La función no debe modificar la lista.
c. Recibir una lista como parámetro y devolver una nueva lista con los elementos 
únicos de la lista original, sin importar el orden. 
Combinar estas tres funciones en un mismo programa.
"""
import random as rn
from typing import List

def generar_lista(num: int) -> List[int]:
    """
    Genera una lista de N numeros aleatorios entre 1 y 100.

    Pre: Recibe un entero correspondiente a N.

    Post: Retorna una lista cargada con N cantidad de elementos aleatorios entre 1 y 100.
    """
    return [rn.randint(1, 100) for x in range(num)]

def repetidos(lista: List[int]) -> bool:
    """
    Evalua si una lista tiene un elemento repetido.

    Pre: Recibe una lista de enteros a evaluar.

    Post: Devuelve True si hay algun elemento repetido en la lista o False en caso contrario.
    """
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] == lista[j]:
                return True
    return False

def elementos_unicos(lista: List[int]) -> List[int]:
    """
    Genera una nueva lista con los elementos unicos de otra ya cargada.

    Pre: Recibe una lista de enteros, de la cual se van a extraer los elementos unicos.

    Post: Devuelve una lista cargada con los elementos unicos de la lista recibida.
    """
    unicos = []
    for elem in lista:
        if elem not in unicos:
            unicos.append(elem)
    return unicos

def main():
    while True:
        n = input("Ingrese la cantidad de numeros a generar: ")
        if n.isdigit() and int(n) > 0:
            n = int(n)
            break
        else:
            print("Error: debe ingresar un numero entero mayor a 0.")

    numeros = generar_lista(n)
    print("\nLista generada:", numeros)

    if repetidos(numeros):
        lista_unicos = elementos_unicos(numeros)
        print("\nLista con elementos unicos:", lista_unicos)

    else:
        print("\nLa lista no tiene elementos repetidos.")

    
main()