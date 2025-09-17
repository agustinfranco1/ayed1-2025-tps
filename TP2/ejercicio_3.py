"""
Ej 3: Crear una lista con los cuadrados de los números entre 1 y N (ambos incluidos), 
donde N se ingresa desde el teclado. Luego se solicita imprimir los últimos 10 valo
res de la lista. 
"""
from typing import List

def calcular_cuadrados(N: int) -> List[int]:
    """
    Genera una lista con los cuadrados de los números de 1 a N.

    Pre: Recibe un numero entero correspondiente al numero hasta el que llegara la lista.

    Post: Retorna una lista de enteros correspondientes al cuadrado de los numeros del 1 al N.
    """
    return [i**2 for i in range(1, N + 1)]


def ultimos_diez(lista: List[int]) -> List[int]:
    """
    Busca los ultimos diez elementos de la lista recibida.

    Pre: Recibe una lista de enteros.

    Post: Devuelve la lista de enteros ingresada pero con los ultimos 10 elementos de la misma unicamente.
    """
    return lista[-10:]


def main():
    #Solicita y valida el numero al usuario
    while True:
        N = input("Ingrese un numero entero positivo: ")

        if N.isdigit() and int(N) > 0:
            N = int(N)
            break
        
        else:
            print("Error: debe ingresar un numero entero mayor a 0.")

    lista_cuadrados = calcular_cuadrados(N)

    #Mostrar últimos 10
    print(f"\nUltimos 10 valores de la lista: \n{(ultimos_diez(lista_cuadrados))}")
    


main()
