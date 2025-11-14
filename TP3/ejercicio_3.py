"""
Ej 3: Desarrollar un programa para rellenar una matriz de N x N con números enteros al 
azar comprendidos en el intervalo [0,N2), de tal forma que ningún número se repita. 
Imprimir la matriz por pantalla.
"""
import random
from typing import List


def generar_matriz(n: int) -> List[List[int]]:
    """
    Genera una matriz de N x N con numeros enteros aleatorios unicos en el rango [0, N2).

    Pre: n debe ser un entero mayor que cero.

    Post: devuelve una matriz de tamaño NxN con numeros aleatorios sin repetirse.
    """
    if n <= 0:
        raise ValueError("El valor de N debe ser un entero mayor que cero.")

    numeros = list(range(n * n))

    random.shuffle(numeros)

    matriz = []
    indice = 0

    for _ in range(n):
        fila = numeros[indice:indice + n]
        matriz.append(fila)
        indice += n

    return matriz


def imprimir_matriz(matriz: List[List[int]]) -> None:
    """
    Imprime una matriz formateada por pantalla.

    Pre: matriz debe ser una lista de listas.

    Post: no devuelve nada, imprime la matriz por pantalla.
    """
    for fila in matriz:
        print(" ".join(f"{elem:3d}" for elem in fila))


def main():
    try:
        n = int(input("Ingrese el tamaño N de la matriz: "))

        matriz = generar_matriz(n)
        print("\nMatriz generada:")
        imprimir_matriz(matriz)

    except ValueError as e:
        print(f"Error: {e}")


main()