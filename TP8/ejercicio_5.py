"""
Ej 5: En geometría un vector es un segmento de recta orientado que va desde un punto 
A hasta un punto B. Los vectores en el plano se representan mediante un par orde
nado de números reales (x, y) llamados componentes. Para representarlos basta 
con unir el origen de coordenadas con el punto indicado en sus componentes.
Escribir una función que reciba dos vectores en forma de tuplas y devuelva un valor 
de verdad indicando si son ortogonales o no. Desarrollar también un programa que 
permita verificar el comportamiento de la función.
"""
from typing import Tuple

def son_ortogonales(vector1: Tuple[int], vector2: Tuple[int]) -> bool:
    """
    Determina si dos vectores son ortogonales.

    Pre: recibe dos tuplas de enteros correspondientes a dos vectores.

    Post: devuelve True si los vectores son ortogonales, o False en caso contrario.
    """
    try:
        if len(vector1) != 2 or len(vector2) != 2:
            raise ValueError("Cada vector debe tener exactamente dos componentes.")

        producto_escalar = vector1[0] * vector2[0] + vector1[1] * vector2[1]
        return producto_escalar == 0
    except Exception as e:
        print(f"Error: {e}")
        return None


def main():
    try:
        vector1 = input("\nIngrese el primer vector (dos numeros separados por espacio): ")
        vector2 = input("\nIngrese el segundo vector (dos numeros separados por espacio): ")

        vector_1 = tuple(int(valor) for valor in vector1.split())
        vector_2 = tuple(int(valor) for valor in vector2.split())

        resultado = son_ortogonales(vector_1, vector_2)

        if resultado is None:
            pass 
        elif resultado:
            print(f"\nLos vectores {vector_1} y {vector_2} son ortogonales.")
        else:
            print(f"\nLos vectores {vector_1} y {vector_2} no son ortogonales.")
    except ValueError:
        print("Error: debe ingresar solo numeros validos.")


main()