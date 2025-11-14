"""
Ej 11: Escribir un programa que cuente cuántas veces se encuentra una subcadena dentro 
de otra cadena, sin diferenciar mayúsculas y minúsculas. Tener en cuenta que los 
caracteres de la subcadena no necesariamente deben estar en forma consecutiva 
dentro de la cadena, pero sí respetando el orden de los mismos.
"""
def contar_subcadena(cadena: str, subcadena: str) -> int:
    """
    Cuenta cuantas veces se encuentra una subcadena dentro de otra cadena, 
    sin diferenciar mayusculas ni minusculas y de manera no necesariamente consecutiva

    Pre: recibe dos strings, la frase a analizar y la subcadena a buscar dentro de la misma.

    Post: devuelve un numero entero correspondiente a la cantidad de ocurrencias de la subcadena 
          dentro de la cadena principal.
    """
    cadena = cadena.lower()
    subcadena = subcadena.lower()
    contador = 0
    indice_sub = 0

    for caracter in cadena:
        if caracter == subcadena[indice_sub]:
            indice_sub += 1
            if indice_sub == len(subcadena):
                contador += 1
                indice_sub = 0  # reinicia para buscar mas ocurrencias

    return contador


def main():
    cadena = input("Ingrese una frase: ")
    subcadena = input("Ingrese la palabra a buscar: ")

    cantidad = contar_subcadena(cadena, subcadena)

    print(f"Ocurrencias: {cantidad}")


main()