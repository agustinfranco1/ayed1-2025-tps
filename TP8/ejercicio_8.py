"""
Ej 8: Generar e imprimir un diccionario donde las claves sean números enteros entre 1 y 
20 (ambos incluidos) y los valores asociados sean el cuadrado de las claves.
"""
from typing import Dict

def cuadrados() -> Dict[int, int]:
    """
    Genera un diccionario con claves entre 1 y 20, y valores igual al cuadrado de las claves.

    Pre: no recibe parametros.

    Post: devuelve un diccionario de clave entera y valores por igual, correspondientes 
          a los numeros del 1 al 20 y sus cuadrados.
    """
    return {n: n ** 2 for n in range(1, 21)}


def main():
    diccionario = cuadrados()
    print("\nListado generado:")
    for clave, valor in diccionario.items():
        print(f"{clave}: {valor}")


main()