"""
Ej 4: Una fábrica de bicicletas guarda en una matriz la cantidad de unidades producidas 
en cada una de sus plantas durante una semana. De este modo, cada columna re
presenta el día de la semana y cada fila a una de sus fábricas. 
Se solicita:
a. Crear una matriz con datos generados al azar para N fábricas durante una 
semana, considerando que la capacidad máxima de fabricación es de 150 
unidades por día y puede suceder que en ciertos días no se fabrique nin
guna. 
b. Mostrar la cantidad total de bicicletas fabricadas por cada fábrica. 
c. Cuál es la fábrica que más produjo en un solo día (detallar día y fábrica).
d. Cuál es el día más productivo, considerando todas las fábricas combinadas.
e. Crear una lista por comprensión que contenga la menor cantidad fabricada 
por cada fábrica
"""
from typing import List, Tuple
import random


def generar_produccion(n: int) -> List[List[int]]:
    """
    Genera una matriz de produccion de tamaño n x 7, Cada fabrica produce entre 0 y 150 bicicletas por dia.

    Pre: n debe ser un entero positivo.

    Post: devuelve una matriz de tamaño n x 7 con valores entre 0 y 150.
    """
    if n <= 0:
        raise ValueError("La cantidad de fabricas debe ser mayor que cero.")

    matriz: List[List[int]] = []
    for _ in range(n):
        fila = [random.randint(0, 150) for _ in range(7)]
        matriz.append(fila)

    return matriz


def total_por_fabrica(matriz: List[List[int]]) -> List[int]:
    """
    Calcula la cantidad total de bicicletas fabricadas por cada fabrica.

    Pre: matriz debe ser una lista de listas valida (Nx7).

    Postcondición:
        - Retorna una lista de totales por fila.
    """
    return [sum(fila) for fila in matriz]


def mayor_produccion_un_dia(matriz: List[List[int]]) -> Tuple[int]:
    """
    Determina que fabrica produjo mas en un solo dia.

    Pre: matriz debe ser una lista de listas valida (Nx7).

    Post: devuelve una tupla con fabrica, dia y produccion.
    """
    max_prod = -1
    fab_max = -1
    dia_max = -1

    for f in range(len(matriz)):
        for d in range(7):
            if matriz[f][d] > max_prod:
                max_prod = matriz[f][d]
                fab_max = f
                dia_max = d

    return fab_max, dia_max, max_prod


def dia_mas_productivo(matriz: List[List[int]]) -> int:
    """
    Determina el dia con mayor produccion total considerando todas las fabricas.

    Pre: matriz debe ser una lista de listas valida (Nx7).

    Post: devuelve el indice de dia con mayor produccion total.
    """
    totales_por_dia = [0] * 7

    for fila in matriz:
        for d in range(7):
            totales_por_dia[d] += fila[d]

    return totales_por_dia.index(max(totales_por_dia))


def minimos_por_fabrica(matriz: List[List[int]]) -> List[int]:
    """
    Obtiene la minima produccion registrada por cada fabrica.

    Pre: matriz debe ser una lista de listas valida (Nx7).

    Post: devuelve una lista de minimos por fila.
    """
    return [min(fila) for fila in matriz]


def mostrar_matriz(matriz: List[List[int]]) -> None:
    """
    Muestra la matriz de forma clara.

    Pre: recibe una matriz valida.

    Post: no devuelve nada, imprime la matriz en pantalla
    """
    for fila in matriz:
        print(fila)


def main():
    try:
        n = int(input("\nIngrese la cantidad de fabricas: "))
        matriz = generar_produccion(n)

        print("\nProduccion")
        mostrar_matriz(matriz)

        totales = total_por_fabrica(matriz)
        print("\nTotal fabricado por cada fabrica:")
        for i, t in enumerate(totales):
            print(f"Fabrica {i + 1}: {t} unidades")

        f, d, prod = mayor_produccion_un_dia(matriz)
        print(f"\nMayor produccion en un solo dia:")
        print(f"Fabrica {f + 1}, dia {d + 1}, produccion: {prod} unidades")

        dia_max = dia_mas_productivo(matriz)
        print(f"\nDia mas productivo: dia {dia_max + 1}")

        minimos = minimos_por_fabrica(matriz)
        print("\nMinima produccion por fabrica:")
        print(minimos)

    except ValueError as e:
        print(f"Error: {e}")

main()