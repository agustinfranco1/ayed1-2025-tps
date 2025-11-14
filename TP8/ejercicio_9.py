"""
Ej 9: Escribir un programa que permita ingresar un número entero N y genere un 
diccionario por comprensión con la tabla de multiplicar de N del 1 al 12. Mostrar la 
tabla de multiplicar con el formato apropiado.
"""
from typing import Dict

def generar_tabla_multiplicar(n: int) -> Dict[int, int]:
    """
    Genera un diccionario con la tabla de multiplicar del numero N del 1 al 12.

    Pre: recibe un numero entero correspondiente al numero del cual se generara la tabla.

    Post: devuelve un diccionario de clave y valor enteros por igual, 
          correspondientes a los valores del 1 al 12 adjuntos a dichos numeros multiplicados por N.
    """
    return {i: n * i for i in range(1, 13)}

def main():
    try:
        n = int(input("\nIngrese un numero entero para generar su tabla de multiplicar: "))
        tabla = generar_tabla_multiplicar(n)
        print("\nTabla generada:")
        for clave, valor in tabla.items():
            print(f"{clave}: {valor}")

    except ValueError:
        print("Error: Debe ingresar un numero entero valido.")


main()