"""
Ej 10: Desarrollar una función para reemplazar todas las apariciones de una palabra por 
otra en una cadena de caracteres y devolver la cadena obtenida y un entero con la 
cantidad de reemplazos realizados. Tener en cuenta que sólo deben reemplazarse 
palabras completas, y no fragmentos de palabras. Escribir también un programa 
para verificar el comportamiento de la función.
"""
from typing import Tuple

def reemplazar_palabra(cadena: str, palabra_a_sustituir: str, palabra_nueva: str) -> Tuple[str, int]:
    """
    Reemplaza todas las apariciones de una palabra completa por otra en la cadena dada.

    Pre: recibe tres strings, uno correspondiente a la frase, el segundo correspondiente a la
         palabra que se busca reemplazar y por ultimo la palabra que se desea implementar a cambio.

    Post: retorna una tupla con el string con los cambios y 
          el numero de veces que se realizo el reemplazo.
    """
    palabras = cadena.split()
    contador = 0

    for i in range(len(palabras)):
        if palabras[i] == palabra_a_sustituir:
            palabras[i] = palabra_nueva
            contador += 1

    nueva_cadena = " ".join(palabras)
    return nueva_cadena, contador


def main():
    cadena = input("Ingrese una frase: ")
    palabra_a_sustituir = input("Ingrese la palabra que desea reemplazar: ")
    palabra_nueva = input("Ingrese la nueva palabra: ")

    resultado, cantidad = reemplazar_palabra(cadena, palabra_a_sustituir, palabra_nueva)

    print(f"Frase modificada: {resultado}")
    print(f"Cantidad de reemplazos realizados: {cantidad}")


main()