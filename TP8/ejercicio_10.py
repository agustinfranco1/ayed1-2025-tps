"""
Ej 10: Desarrollar una función eliminarclaves() que reciba como parámetros un diccionario 
y una lista de claves. La función debe eliminar del diccionario todas las claves 
contenidas en la lista, devolviendo el diccionario modificado y un número entero 
que represente la cantidad de claves eliminadas. Desarrollar también un programa 
para verificar su comportamiento.
"""
from typing import Dict, List, Tuple

def eliminar_claves(diccionario_base: Dict[str, int], claves_a_eliminar: List[str]) -> Tuple[Dict[str, int], int]:
    """
    Elimina del diccionario todas las claves contenidas en la lista recibida.

    Pre: recibe un diccionario de clave string y valor entero y una lista de strings 
         correspondientes a las claves que se desean eliminar del diccionario.

    Post: devuelve una tupla con el diccionario de clave string y valor entero modificado 
          y un entero correspondiente a la cantidad de claves elmiminadas.
    """
    eliminadas = 0
    for clave in claves_a_eliminar:
        if clave in diccionario_base:
            del diccionario_base[clave]
            eliminadas += 1
    return diccionario_base, eliminadas


def main():
    diccionario = {
        "uno": 1,
        "dos": 2,
        "tres": 3,
        "cuatro": 4,
        "cinco": 5,
        "seis": 6,
        "siete": 7,
        "ocho": 8,
        "nueve": 9
    }

    print("\nDiccionario original:")
    print(diccionario)

    claves_a_eliminar = input("\nIngrese las claves a eliminar separadas por comas: ").split(",")
    claves_a_eliminar = [clave.strip() for clave in claves_a_eliminar]

    diccionario_modificado, cantidad = eliminar_claves(diccionario, claves_a_eliminar)

    print("\nDiccionario modificado:")
    print(diccionario_modificado)
    print(f"\nCantidad de claves eliminadas: {cantidad}")


main()