"""
Ej 1: Desarrollar una función que determine si una cadena de caracteres es capicúa, sin 
utilizar cadenas auxiliares ni rebanadas. Escribir además un programa que permita 
verificar su funcionamiento.
"""
def es_capicua(texto: str) -> bool:
    """
    Determina si un string es capicua.

    Pre: recibe un string a analizar.

    Post: devuelve True si es capicua, False en caso contrario.
    """
    inicio = 0
    fin = len(texto) - 1
    
    while inicio < fin:
        if texto[inicio] != texto[fin]:
            return False
        inicio += 1
        fin -= 1
    
    return True


def main():
    texto = input("Ingrese una cadena: ")
    if es_capicua(texto):
        print("La cadena es capicua.")
    else:
        print("La cadena no es capicua.")


main()