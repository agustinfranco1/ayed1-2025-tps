"""
Desarrollar cada una de las siguientes funciones y escribir un programa que permi
ta verificar su funcionamiento, imprimiendo la matriz luego de invocar a cada fun
ción:
a. Cargar números enteros en una matriz de N x N, ingresando los datos desde 
teclado. 
b. Ordenar en forma ascendente cada una de las filas de la matriz.
c. Intercambiar dos filas, cuyos números se reciben como parámetro.
d. Intercambiar dos columnas dadas, cuyos números se reciben como parámetro.
e. Trasponer la matriz sobre si misma. (intercambiar cada elemento Aij por Aji)
f.Calcular el promedio de los elementos de una fila, cuyo número se recibe como 
parámetro.
g. Calcular el porcentaje de elementos con valor impar en una columna, cuyo nú
mero se recibe como parámetro.
h. Determinar si la matriz es simétrica con respecto a su diagonal principal.
i.
Determinar si la matriz es simétrica con respecto a su diagonal secundaria.
j.
Determinar qué columnas de la matriz son palíndromos (capicúas), devolviendo 
una lista con los números de las mismas.
NOTA: El valor de N debe leerse por teclado. Las funciones deben servir cualquiera 
sea el valor ingresado
"""
from typing import List


def cargar_matriz(n: int) -> List[List[int]]:
    """
    Carga una matriz cuadrada de tamaño n x n con números enteros ingresados por teclado.

    Pre: n debe ser positivo  entero.

    Post: devuelve una matriz de enteros de tamaño n x n.
    """
    if n <= 0:
        raise ValueError("El tamaño N debe ser mayor que 0.")

    matriz: List[List[int]] = []

    for i in range(n):
        fila: List[int] = []
        for j in range(n):
            while True:
                try:
                    valor = int(input(f"Ingrese un entero para la posición ({i}, {j}): "))
                    fila.append(valor)
                    break
                except ValueError:
                    print("Error: Debe ingresar un numero entero.")
        matriz.append(fila)

    return matriz


def ordenar_filas(matriz: List[List[int]]) -> None:
    """
    Ordena cada fila de la matriz en forma ascendente.

    Pre: la matriz debe ser rectangular.

    Post: no devuelve nada, modifica cada fila de la matriz hasta que queda ordenada de menor a mayor.
    """
    for fila in matriz:
        fila.sort()


def intercambiar_filas(matriz: List[List[int]], f1: int, f2: int) -> None:
    """
    Intercambia las filas f1 y f2 de la matriz.

    Pre: 0 <= f1, f2 < len(matriz)

    Post: no devuelve nada, intercambia las filas correspondientes a f1 y f2.
    """
    n = len(matriz)
    if not (0 <= f1 < n and 0 <= f2 < n):
        raise ValueError("Indices de fila fuera de rango.")
    
    matriz[f1], matriz[f2] = matriz[f2], matriz[f1]


def intercambiar_columnas(matriz: List[List[int]], c1: int, c2: int) -> None:
    """
    Intercambia las columnas c1 y c2 de la matriz.

    Pre: 0 <= c1, c2 < len(matriz)

    Post: no devuelve nada, intercambia las columnas correspondientes a c1 y c2.
    """
    n = len(matriz)
    if not (0 <= c1 < n and 0 <= c2 < n):
        raise ValueError("Indices de columna fuera de rango.")

    for fila in matriz:
        fila[c1], fila[c2] = fila[c2], fila[c1]


def trasponer(matriz: List[List[int]]) -> None:
    """
    Transpone la matriz sobre si misma.

    Pre: matriz debe ser una lista de listas cuadrada.

    Post: no devuelve nada, modifica la matriz de modo que queda traspuesta.
    """
    n = len(matriz)
    for i in range(n):
        for j in range(i + 1, n):
            matriz[i][j], matriz[j][i] = matriz[j][i], matriz[i][j]


def promedio_fila(matriz: List[List[int]], fila: int) -> float:
    """
    Calcula el promedio de los elementos de una fila dada.

    Pre: 0 <= fila < len(matriz)

    Post: devuelve el promedio como float.
    """
    if not (0 <= fila < len(matriz)):
        raise ValueError("Indice de fila fuera de rango.")

    return sum(matriz[fila]) / len(matriz[fila])


def porcentaje_impares_columna(matriz: List[List[int]], col: int) -> float:
    """
    Calcula el porcentaje de valores impares en la columna indicada.

    Pre: 0 <= col < len(matriz)

    Post: devuelve un porcentaje entre 0 y 100.
    """
    n = len(matriz)
    if not (0 <= col < n):
        raise ValueError("Indice de columna fuera de rango.")

    total = n
    impares = sum(1 for i in range(n) if matriz[i][col] % 2 != 0)

    return (impares / total) * 100


def es_simetrica_principal(matriz: List[List[int]]) -> bool:
    """
    Determina si la matriz es simetrica respecto de la diagonal principal.

    Pre: matriz debe ser una lista de listas cuadrada.

    Post: Devuelve True si la matriz es simetrica respecto de su diagonal principal o False en caso contrario.
    """
    n = len(matriz)
    for i in range(n):
        for j in range(i + 1, n):
            if matriz[i][j] != matriz[j][i]:
                return False
    return True


def es_simetrica_secundaria(matriz: List[List[int]]) -> bool:
    """
    Determina si la matriz es simetrica respecto de la diagonal secundaria.

    Pre: matriz debe ser una lista de listas cuadrada.

    Post: devuelve True si la matriz es simetrica respecto de su diagonal secundaria o False en caso contrario.
    """
    n = len(matriz)
    for i in range(n):
        for j in range(n - 1 - i):
            if matriz[i][j] != matriz[n - 1 - j][n - 1 - i]:
                return False
    return True


def columnas_palindromas(matriz: List[List[int]]) -> List[int]:
    """
    Devuelve una lista con los indices de columnas que son palindromos.

    Pre: matriz debe ser una lista de listas cuadrada.

    Post: devuelve una lista con las columnas capicuas.
    """
    n = len(matriz)
    resultado: List[int] = []

    for col in range(n):
        columna = [matriz[f][col] for f in range(n)]
        if columna == columna[::-1]:
            resultado.append(col)

    return resultado


def main():
    try:
        n = int(input("Ingrese el valor de N para la matriz NxN: "))
        matriz = cargar_matriz(n)

        print("\nMatriz cargada:")
        for fila in matriz:
            print(fila)

        ordenar_filas(matriz)
        print("\nFilas ordenadas:")
        for fila in matriz:
            print(fila)

        intercambiar_filas(matriz, 0, n - 1)
        print("\nFilas intercambiadas:")
        for fila in matriz:
            print(fila)

        intercambiar_columnas(matriz, 0, n - 1)
        print("\nColumnas intercambiadas:")
        for fila in matriz:
            print(fila)

        trasponer(matriz)
        print("\nMatriz traspuesta:")
        for fila in matriz:
            print(fila)

        print("\nPromedio de la fila 0:", promedio_fila(matriz, 0))
        print("Porcentaje impares columna 0:", porcentaje_impares_columna(matriz, 0))

        print("\nSimetrica principal?:", es_simetrica_principal(matriz))
        print("\nSimetrica secundaria?:", es_simetrica_secundaria(matriz))

        print("\nColumnas palindromas:", columnas_palindromas(matriz))

    except ValueError as e:
        print(f"Error: {e}")

main()