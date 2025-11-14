"""
Ej 6: El método index permite buscar un elemento dentro de una lista, devolviendo la 
posición que éste ocupa. Sin embargo, si el elemento no pertenece a la lista se 
produce una excepción de tipo ValueError. Desarrollar un programa que cargue 
una lista con números enteros ingresados a través del teclado (terminando con -1) 
y permita que el usuario ingrese el valor de algunos elementos para visualizar la 
posición que ocupan, utilizando el método index. Si el número no pertenece a la 
lista se imprimirá un mensaje de error y se solicitará otro para buscar. Abortar el 
proceso al tercer error detectado. No utilizar el operador in durante la búsqueda.
"""
from typing import List

def buscar_posicion(lista: List[int], numero: int) -> int:
    """
    Busca la ubicacion de un numero entero dentro de una lista de estos.

    Pre: recibe una lista de enteros y el numero entero que se desea buscar dentro de la lista.

    Post: Devuelve la posicion que ocupa el numero ingresado en la lista.
    """
    return lista.index(numero) + 1


def main():
    lista = []

    while True:
        try:
            valor = int(input("Ingrese numeros enteros (-1 para finalizar): "))
            if valor == -1:
                break
            lista.append(valor)
        except ValueError:
            print("Error: Debe ingresar un numero entero valido.")

    print(f"\nLista cargada: {lista}")

    errores = 0
    while errores < 3:
        try:
            buscado = int(input("\nIngrese el numero a buscar: "))
            posicion = buscar_posicion(lista, buscado)
            print(f"El numero {buscado} se encuentra en la posicion {posicion}.")
        except ValueError:
            errores += 1
            print(f"Error: el numero no se encuentra en la lista. Intentos fallidos: {errores}/3")

    print("\nSe ha alcanzado el limite de 3 errores, programa finalizado.")


main()