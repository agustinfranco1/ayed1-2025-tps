"""
Ej 5: Desarrollar un programa que permita realizar reservas en una sala de cine de N 
filas con M butacas por cada fila. Desarrollar  las siguientes funciones y utilizarlas 
en un mismo programa:
mostrar_butacas: Mostrará por pantalla el estado de cada una de las butacas 
del cine. Esta función deberá ser invocada antes de que se realice la reserva, y 
se volverá a invocar luego de la misma con los estados actualizados.
reservar: Deberá recibir una matriz y la butaca seleccionada, y actualizará la 
sala en caso de estar disponible dicha butaca. La función devolverá True/False 
si logró o no reservar la butaca.
cargar_sala: Recibirá una matriz como parámetro y la cargará con valores 
aleatorios para simular una sala con butacas ya reservadas.
butacas_libres: Recibirá como parámetro la matriz y retornará cuántas buta
cas desocupadas hay en la sala.
butacas_contiguas: Buscará la secuencia más larga de butacas libres conti
guas en una misma fila y devolverá las coordenadas de inicio de la misma. 
"""
import random
from typing import List, Tuple, Optional


def cargar_sala(sala: List[List[str]]) -> None:
    """
    Carga la sala con valores aleatorios ('L' para libre, 'X' para ocupada).

    Pre: sala debe ser una matriz rectangular.

    Post: no devuelve nada, modifica la matriz, asignando aleatoriamente 'L' o 'X' en cada posición.
    """
    for i in range(len(sala)):
        for j in range(len(sala[i])):
            sala[i][j] = random.choice(["L", "X"])


def mostrar_butacas(sala: List[List[str]]) -> None:
    """
    Muestra por pantalla el estado actual de la sala.

    Pre: sala debe ser una matriz rectangular de strings 'L' o 'X'.

    Post: no devuelve nada, imprime por pantalla la matriz.
    """
    print("\nEstado de la sala:")
    print("   " + " ".join(f"{j:2d}" for j in range(len(sala[0]))))
    print("  " + "---" * len(sala[0]))

    for i, fila in enumerate(sala):
        print(f"{i:2d}| " + " ".join(fila))
    print()


def reservar(sala: List[List[str]], fila: int, butaca: int) -> bool:
    """
    Intenta reservar una butaca en caso de estar libre.

    Pre: fila y butaca deben ser indices validos y sala debe ser una matriz rectangular.

    Post: devuelve True si la butaca estaba libre y se reservo, o False en caso de que ya estuviese ocupada
    """
    if sala[fila][butaca] == "L":
        sala[fila][butaca] = "X"
        return True
    return False


def butacas_libres(sala: List[List[str]]) -> int:
    """
    Cuenta cuantas butacas libres hay en la sala.

    Pre: sala debe ser una matriz rectangular.

    Post: devuelve un entero correspondiente a la cantidad total de butacas marcadas como 'L'.
    """
    return sum(fila.count("L") for fila in sala)


def butacas_contiguas(sala: List[List[str]]) -> Optional[Tuple[int]]:
    """
    Busca la mayor cantidad de butacas contiguas libres en una misma fila.

    Pre: sala debe ser una matriz rectangular.

    Post: devuelve una tupla (fila, inicio_columna, longitud_maxima), de no haber butacas libres 
          contiguas devuelve None.
    """
    mejor_fila = -1
    mejor_inicio = -1
    mejor_longitud = 0

    for i, fila in enumerate(sala):
        inicio = 0
        longitud = 0

        for j, asiento in enumerate(fila):
            if asiento == "L":
                longitud += 1

                if longitud == 1:
                    inicio = j

                if longitud > mejor_longitud:
                    mejor_longitud = longitud
                    mejor_fila = i
                    mejor_inicio = inicio
            else:
                longitud = 0

    if mejor_longitud == 0:
        return None

    return mejor_fila, mejor_inicio, mejor_longitud


def main():
    try:
        n = int(input("Ingrese la cantidad de filas del cine: "))
        m = int(input("Ingrese la cantidad de butacas por fila: "))

        if n <= 0 or m <= 0:
            raise ValueError("Las dimensiones deben ser enteros positivos.")

        sala = [["L" for _ in range(m)] for _ in range(n)]

        cargar_sala(sala)

        mostrar_butacas(sala)

        fila = int(input("Ingrese la fila que desea reservar: "))
        butaca = int(input("Ingrese la butaca que desea reservar: "))

        if fila < 0 or fila >= n or butaca < 0 or butaca >= m:
            raise IndexError("La fila o la butaca están fuera del rango válido.")

        if reservar(sala, fila, butaca):
            print("Reserva realizada con éxito.")
        else:
            print("La butaca ya está ocupada.")

        mostrar_butacas(sala)

        print(f"Total de butacas libres: {butacas_libres(sala)}")

        contiguas = butacas_contiguas(sala)
        if contiguas is not None:
            fila_max, col_inicio, longitud = contiguas
            print(
                f"Mayor secuencia de butacas contiguas libres: {longitud} "
                f"(Fila {fila_max}, desde columna {col_inicio})"
            )
        else:
            print("No hay secuencias de butacas contiguas libres.")

    except ValueError as e:
        print(f"Error: {e}")
    except IndexError as e:
        print(f"Error: {e}")


main()