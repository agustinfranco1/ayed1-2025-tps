"""
Ej 6: Desarrollar una función que extraiga una subcadena de una cadena de caracteres, 
indicando la posición y la cantidad de caracteres deseada. Devolver la subcadena 
como valor de retorno. Escribir también un programa para verificar el comporta
miento de la misma. Ejemplo, dada la cadena "El número de teléfono es 4356
7890" extraer la subcadena que comienza en la posición 25 y tiene 9 caracteres, 
resultando la subcadena "4356-7890". Escribir una función para cada uno de los siguientes casos:
a. Utilizando rebanadas
b. Sin utilizar rebanadas
"""
def extraer_subcadena_a(cadena: str, inicio: int, cantidad: int) -> str:
    """
    Extrae una subcadena de un string a partir de una posición y cantidad dadas utilizando rebanadas.

    Pre: recibe un string, un entero que debe ser menor a la longitud de la cadena
         y un entero correspondiente a los caracteres que se desean extraer.

    Post: devuelve la subcadena de longitud 'cantidad' comenzando en 'inicio'.
    """
    return cadena[inicio:inicio + cantidad]


def extraer_subcadena_b(cadena: str, inicio: int, cantidad: int) -> str:
    """
    Version b: sin utilizar rebanadas.

    Pre: recibe un string, un entero que debe ser menor a la longitud de la cadena
         y un entero correspondiente a los caracteres que se desean extraer.
         
    Post: devuelve la subcadena de longitud 'cantidad' comenzando en 'inicio'.
    """
    subcadena = ""
    fin = inicio + cantidad

    for i in range(inicio, fin):
        if i < len(cadena):
            subcadena += cadena[i]

    return subcadena


def main():
    cadena = input("Ingrese una cadena: ")
    inicio = int(input("Ingrese la posicion inicial: "))
    cantidad = int(input("Ingrese la cantidad de caracteres: "))

    print("\nVersion a:")
    print(extraer_subcadena_a(cadena, inicio, cantidad))

    print("\nVersion b:")
    print(extraer_subcadena_b(cadena, inicio, cantidad))


main()