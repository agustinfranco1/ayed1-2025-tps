from typing import List


def imprimir_matriz(m: List[List[int]]) -> None:
    """
    Imprime la matriz de forma formateada.

    Pre: m debe ser una matriz valida.

    Post: no devuelve nada, imprime la matriz con un nuevo formato.
    """
    for fila in m:
        print(" ".join(f"{x:3d}" for x in fila))
    print()


def matriz_a(n: int) -> List[List[int]]:
    """
    Matriz A: Valores impares sobre la diagonal principal, el resto en 0.
    
    Pre: n debe ser un entero positivo.

    Post: Devuelve una matriz con valores positivos en la diagonal.
    """
    m = [[0 for _ in range(n)] for _ in range(n)]
    valor = 1
    for i in range(n):
        m[i][i] = valor
        valor += 2
    return m


def matriz_b(n: int) -> List[List[int]]:
    """
    Matriz B: Ceros excepto la diagonal opuesta a la de la matriz A que contiene valores decrecientes.
    
    Pre: n debe ser positivo.

    Post: Devuelve una matriz con valores en la diagonal correspondiente.
    """
    m = [[0 for _ in range(n)] for _ in range(n)]
    valor = n ** 3  
    for i in range(n):
        m[i][n - 1 - i] = valor
        valor -= (n - 1) 
    return m


def matriz_c(n: int) -> List[List[int]]:
    """
    Matriz C: Se rellenan filas con valores decrecientes empezando desde n.

    Pre: n debe ser positivo.

    Post: Devuelve una matriz con filas de valores repetidos decrecientes.
    """
    m = []
    valor = n
    for _ in range(n):
        m.append([valor] * n)
        valor -= 1
    return m


def matriz_d(n: int) -> List[List[int]]:
    """
    Matriz D: Rellena filas segun el patron: fila 0 = n*2, fila 1 = 2*n - 4 ...

    Pre: n debe ser positivo.
    
    Post: Devuelve la matriz segun el patron correspondiente.
    """
    m = []
    valor = n * 2
    for _ in range(n):
        m.append([valor] * n)
        valor -= 2
    return m


def matriz_e(n: int) -> List[List[int]]:
    """
    Matriz E: Valores simetricos en filas y columnas, patron cruzado.

    Pre: n debe ser positivo.

    Post: Devuelve la matriz según el patron correspondiente.
    """
    m = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if (i + j) % 2 == 1:
                m[i][j] = i + j
    return m


def matriz_f(n: int) -> List[List[int]]:
    """
    Matriz F: Ceros arriba y numeros consecutivos abajo formando una tabla creciente.

    Pre: n debe ser positivo.

    Post: Devuelve la matriz con el patron observado.
    """
    m = [[0 for _ in range(n)] for _ in range(n)]
    valor = 1
    for i in range(n):
        for j in range(n - 1, -1, -1):
            if i + j >= n - 1:
                m[i][j] = valor
                valor += 1
    return m


def matriz_g(n: int) -> List[List[int]]:
    """
    Matriz G: Relleno en espiral.

    Pre: n debe ser positivo.
    
    Post: Devuelve una matriz con valores consecutivos siguiendo un camino espiralado.
    """
    m = [[0 for _ in range(n)] for _ in range(n)]
    valor = 1
    for i in range(n):
        if i % 2 == 0:
            for j in range(n):
                m[i][j] = valor
                valor += 1
        else:
            for j in range(n - 1, -1, -1):
                m[i][j] = valor
                valor += 1
    return m


def matriz_h(n: int) -> List[List[int]]:
    """
    Matriz H: valores consecutivos en columnas, zigzag vertical.

    Pre: n debe ser positivo.

    Post: Devuelve la matriz con patron correspondiente.
    """
    m = [[0 for _ in range(n)] for _ in range(n)]
    valor = 1
    for j in range(n):
        if j % 2 == 0:
            for i in range(n):
                m[i][j] = valor
                valor += 1
        else:
            for i in range(n - 1, -1, -1):
                m[i][j] = valor
                valor += 1
    return m


def matriz_i(n: int) -> List[List[int]]:
    """
    Matriz I: Se rellena por diagonales ascendentes.

    Pre: n debe ser positivo.

    Post: Devuelve una matriz donde se rellenan valores por diagonales.
    """
    m = [[0 for _ in range(n)] for _ in range(n)]
    valor = 1
    for suma in range(2 * n - 1):
        for i in range(n):
            j = suma - i
            if 0 <= j < n:
                m[i][j] = valor
                valor += 1
    return m


def main():
    try:
        n = int(input("Ingrese N para la matriz N x N: "))
        if n <= 0:
            raise ValueError("N debe ser un entero positivo.")

        opciones = {
            "a": matriz_a,
            "b": matriz_b,
            "c": matriz_c,
            "d": matriz_d,
            "e": matriz_e,
            "f": matriz_f,
            "g": matriz_g,
            "h": matriz_h,
            "i": matriz_i
        }

        print("Matrices disponibles: a b c d e f g h i")
        eleccion = input("¿Qué matriz desea generar?: ").lower()

        if eleccion not in opciones:
            raise ValueError("Opción invalida.")

        matriz = opciones[eleccion](n)
        imprimir_matriz(matriz)

    except ValueError as e:
        print(f"Error: {e}")


main()