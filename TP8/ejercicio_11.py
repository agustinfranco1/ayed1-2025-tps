"""
Ej 11: Crear una función contarvocales(), que reciba una palabra y cuente cuántas vocales 
contiene, identificando la cantidad de cada una. Devolver un diccionario con los 
resultados. Luego desarrollar un programa para leer una frase e invocar a la 
función por cada palabra que contenga la misma. Imprimir las palabras y la 
cantidad de vocales hallada.
"""
from typing import Dict

def contar_vocales(frase: str) -> Dict[str, int]:
    """
    Cuenta cuantas vocales contiene una palabra, identificando la cantidad de cada una en la misma.

    Pre: recibe un string con una o mas palabras.

    Post: devuelve un diccionario de clave string y valores enteros 
          correspondientes a las vocales encontradas y su cantidad.
    """
    vocales = "aeiou"
    conteo = {v: 0 for v in vocales}

    for letra in frase.lower():
        if letra in conteo:
            conteo[letra] += 1

    # se eliminan las vocales que no se ppresentaron
    return {v: c for v, c in conteo.items() if c > 0}


def main():
    frase = input("\nIngrese una frase: ").strip()
    palabras = frase.split()

    for palabra in palabras:
        resultado = contar_vocales(palabra)
        total_vocales = sum(resultado.values())
        print(f"\nPalabra: {palabra}")
        print(f"Total de vocales: {total_vocales}")
        print("Cantidad de cada vocal:", resultado)


main()