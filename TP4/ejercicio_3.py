"""
Ej 3: Los números de claves de dos cajas fuertes están intercalados dentro de un número 
entero llamado "clave maestra", cuya longitud no se conoce. Realizar un programa 
para obtener ambas claves, donde la primera se construye con los dígitos ubicados 
en posiciones impares de la clave maestra y la segunda con los dígitos ubicados en 
posiciones pares. Los dígitos se numeran desde la izquierda. Ejemplo: Si clave 
maestra fuera 18293, la clave 1 sería 123 y la clave 2 sería 89.
"""
from typing import Tuple

def dividir_claves(clave_maestra: str) -> Tuple[str]:
    """
    Separa una clave maestra en dos claves intercaladas.
    
    Pre: recibe un string que debera ser la clave maestra.

    Post: devuelve una tupla de strings con las dos claves resultantes.
    """
    clave1 = ""
    clave2 = ""

    for i in range(len(clave_maestra)):
        if (i + 1) % 2 != 0:  # posición impar 
            clave1 += clave_maestra[i]
        else:  # posición par
            clave2 += clave_maestra[i]

    return clave1, clave2


def main():
    clave_maestra = input("Ingrese la clave maestra: ")
    clave1, clave2 = dividir_claves(clave_maestra)
    print(f"Clave 1: {clave1}")
    print(f"Clave 2: {clave2}")


main()