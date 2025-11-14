"""
Ej 5: La raíz cuadrada de un número puede obtenerse mediante la función sqrt() del 
módulo math. Escribir un programa que utilice esta función para calcular la raíz 
cuadrada de un número cualquiera ingresado a través del teclado. El programa 
debe utilizar manejo de excepciones para evitar errores si se ingresa un número 
negativo
"""
from math import sqrt

def calcular_raiz(numero: float) -> float:
    """
    Calcula la raiz cuadrada de un numero dado.

    Pre: recibe un numero flotante a transformar.

    Post: devuelve la raiz cuadrada del numero ingresado, si el numero no es valido, devuelve -1.
    """
    try:
        if numero < 0:
            raise ValueError("El numero no puede ser negativo.")
        return sqrt(numero)
    except ValueError as e:
        print(f"Error: {e}")
        return -1.0


def main():
    try:
        valor = float(input("Ingrese un numero para calcular su raiz cuadrada: "))
        resultado = calcular_raiz(valor)
        if resultado != -1:
            print(f"La raiz cuadrada de {valor} es {resultado}")
    except ValueError:
        print("Error: Debe ingresar un numero valido.")


main()