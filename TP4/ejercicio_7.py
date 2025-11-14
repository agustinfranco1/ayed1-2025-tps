"""
Ej 7: Escribir una función para eliminar una subcadena de una cadena de caracteres, a 
partir de una posición y cantidad de caracteres dadas, devolviendo la cadena resultante. 
Escribir también un programa para verificar el comportamiento de la misma. 
Escribir una función para cada uno de los siguientes casos:
a. Utilizando rebanadas
b. Sin utilizar rebanadas
"""
def eliminar_subcadena_a(cadena: str, inicio: int, cantidad: int) -> str:
    """
    Elimina una subcadena de cadena a partir de una posición y una cantidad dadas utilizando rebanadas.

    Pre: recibe un string, un entero que debe ser menor a la longitud de la cadena
         y un entero correspondiente a la cantidad de caracteres que se desean eliminar
         a partir del primer numero entero.

    Post: devuelve un nuevo string sin los caracteres eliminados.
    """
    return cadena[:inicio] + cadena[inicio + cantidad:]


def eliminar_subcadena_b(cadena: str, inicio: int, cantidad: int) -> str:
    """
    Version B: sin utilizar rebanadas.

    Pre: recibe un string, un entero que debe ser menor a la longitud de la cadena
         y un entero correspondiente a la cantidad de caracteres que se desean eliminar
         a partir del primer numero entero.

    Post: devuelve un nuevo string sin los caracteres eliminados.
    """
    resultado = ""
    fin = inicio + cantidad

    for i in range(len(cadena)):
        if i < inicio or i >= fin:
            resultado += cadena[i]

    return resultado


def main():
    cadena = input("Ingrese una frase: ")
    inicio = int(input("Ingrese la posicion inicial de la subfrase a eliminar: "))
    cantidad = int(input("Ingrese la cantidad de caracteres a eliminar: "))

    print("\nVersion a:")
    print(eliminar_subcadena_a(cadena, inicio, cantidad))

    print("\nVersion b:")
    print(eliminar_subcadena_b(cadena, inicio, cantidad))


main()