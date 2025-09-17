"""
Ej 1: Desarrollar cada una de las siguientes funciones y escribir un programa que per
mita verificar su funcionamiento imprimiendo la lista luego de invocar a cada fun
ción:
a. Cargar una lista con números al azar de cuatro dígitos. La cantidad de elemen
tos también será un número al azar de dos dígitos.
b. Calcular y devolver el producto de todos los elementos de la lista anterior.
c. Eliminar todas las apariciones de un valor en la lista anterior. El valor a eliminar 
se ingresa desde el teclado y la función lo recibe como parámetro. No utilizar 
listas auxiliares.
d. Determinar si el contenido de una lista cualquiera es capicúa, sin usar listas 
auxiliares. Un ejemplo de lista capicúa es [50, 17, 91, 17, 50].
"""
import random as rn
from typing import List

def cargar_lista() -> List[int]:
    """
    Genera una lista de numeros aleatorios de 4 digitos y la cantidad generada,
    un numero aleatorio de 2 digitos tambien.

    Pre: No recibe parametros.

    Post: Retorna una lista cargada con los numeros enteros generados de forma aleatoria
    """
    cantidad = rn.randint(10, 99)
    return [rn.randint(1000, 9999) for x in range(cantidad)]

def producto(nums: List[int]) -> int:
    """
    Calcula el producto de todos los elementos de la lista.

    Pre: Recibe una lista de enteros.

    Post: Retorna un entero correspondiente al producto de todos los enteros cargados en la lista.
    """
    resultado = 1
    for n in nums:
        resultado *= n
    return resultado

def eliminar_valor(nums: List[int], valor: int) -> None:
    """
    Elimina todas las apariciones de un valor en la lista.

    Pre: Recibe una lista de enteros y un entero correspondiente al numero que se quiere extraer de la lista.

    Post: Modifica la lista proporcionada pero no retorna nada.
    """
    i = 0
    while i < len(nums):
        if nums[i] == valor:
            nums.pop(i)
        else:
            i += 1

def es_capicua(nums: List[int]) -> bool:
    """
    Verifica si una lista es capicua.

    Pre: Recibe una lista de numeros enteros.

    Post: Retorna un booleano correspondiente a True si la lista es capicua o False si no lo es.
    """
    izquierda = 0
    derecha = len(nums) - 1
    while izquierda < derecha:
        if nums[izquierda] != nums[derecha]:
            return False
        izquierda += 1
        derecha -= 1
    return True

def main():
    numeros = cargar_lista()
    print(f"\nLista cargada: {numeros}")

    print(f"\nProducto de todos los elementos: {producto(numeros)}\n")

    valor = int(input("\nIngrese un valor a eliminar de la lista: "))
    eliminar_valor(numeros, valor)
    print(f"Lista después de eliminar {valor}: {numeros}\n")

    print(f"¿La lista es capicúa?: {es_capicua(numeros)}")

main()
