"""
Ej 8: Desarrollar una función que devuelva una subcadena con los últimos N caracteres 
de una cadena dada. La cadena y el valor de N se pasan como parámetros.
"""
def ultimos_caracteres(cadena: str, n: int) -> str:
    """
    Genera una subcadena con los ultimos N caracteres de una cadena dada.

    Pre: recibe un string y un numero entero correspondiente a los 
         ultimos N caracteres que se desean extraer de la cadena dada.
    
    Post: devuelve un string con los ultimos N caracteres.
    """
    return cadena[-n:] if n <= len(cadena) else cadena


def main():
    cadena = input("Ingrese una frase: ")
    n = int(input("Ingrese la cantidad de caracteres a extraer desde el final: "))
    print(ultimos_caracteres(cadena, n))

    
main()