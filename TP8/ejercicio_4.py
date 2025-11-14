"""
Ej 4: Escribir una función que indique si dos fichas de dominó encajan o no. Las fichas 
son recibidas en dos tuplas, por ejemplo: (3, 4) y (5, 4). La función devuelve True 
o False. Escribir también un programa para verificar su comportamiento. Considerar 
el uso de conjuntos para resolver este ejercicio.
"""
from typing import Tuple

def dominos_encajan(ficha1: Tuple[int], ficha2: Tuple[int]) -> bool:
    """
    Determina si dos fichas de domino encajan.

    Pre: recibe dos tuplas de enteros con los valores de los dominos.

    Post: devuelve True si las fichas encajan, o False en caso contrario.
    """
    try:
        if len(ficha1) != 2 or len(ficha2) != 2:
            raise ValueError("\nCada ficha debe tener exactamente dos valores")
        if not all(0 <= valor <= 6 for valor in ficha1 + ficha2):
            raise ValueError("\nLos valores de las fichas deben estar entre 0 y 6")

        return not set(ficha1).isdisjoint(ficha2)
    except Exception as e:
        print(f"Error: {e}.")
        return None 


def main():
    try:
        ficha1 = input("\nIngrese la primera ficha (dos numeros del 0 al 6 separados por espacio): ")
        ficha2 = input("\nIngrese la segunda ficha (dos numeros del 0 al 6 separados por espacio): ")

        ficha_1 = tuple(int(valor) for valor in ficha1.split())
        ficha_2 = tuple(int(valor) for valor in ficha2.split())

        resultado = dominos_encajan(ficha_1, ficha_2)

        if resultado is None:
            pass
        elif resultado:
            print(f"Las fichas {ficha_1} y {ficha_2} encajan.")
        else:
            print(f"Las fichas {ficha_1} y {ficha_2} no encajan.")
    except ValueError:
        print("\nError: debe ingresar solo numeros enteros validos.")


main()