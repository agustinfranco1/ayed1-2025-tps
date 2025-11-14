"""
Ej 13: Escribir una función buscarclave() que reciba como parámetros un diccionario y un 
valor, y devuelva una lista de claves que apunten ("mapeen") a ese valor en el dic
cionario. Comprobar el comportamiento de la función mediante un programa apropiado.
"""
from typing import Dict, List

def buscarclave(diccionario: Dict[str, str], valor_buscado: str) -> List[str]:
    """
    Devuelve una lista de claves que apuntan al valor especificado.

    Pre: recibe un diccionario de claves strings asociadas a un valor asignado por el usuario 
         y el valor que se va a buscar que debe pertenecer al valor a alguno de los elementos 
         del diccionario.

    Post: devuelve una lista con las claves asociadas al valor recibido.
    """
    try:
        if not diccionario:
            raise ValueError("El diccionario esta vacio.")
        
        claves_encontradas = [clave for clave, valor in diccionario.items() if valor == valor_buscado]
        return claves_encontradas
    except Exception as e:
        print(f"Error: {e}")
        return []


def main():
    try:
        cantidad = int(input("\nCuantos elementos desea ingresar en el diccionario?: "))
        if cantidad <= 0:
            raise ValueError("Debe ingresar al menos un elemento.")

        diccionario = {}
        for i in range(cantidad):
            clave = input(f"\nIngrese la clave {i + 1}: ").strip()
            valor = input(f"Ingrese el valor asociado a '{clave}': ").strip()
            diccionario[clave] = valor

        valor_buscado = input("\nIngrese el valor que desea buscar: ").strip()
        claves = buscarclave(diccionario, valor_buscado)

        print("\nDiccionario ingresado:")
        for k, v in diccionario.items():
            print(f"{k}: {v}")

        if claves:
            print(f"\nLas claves que apuntan al valor '{valor_buscado}' son: {claves}")
        else:
            print(f"\nNo se encontraron claves que apunten al valor '{valor_buscado}'.")

    except ValueError as e:
        print(f"Error: {e}")


main()