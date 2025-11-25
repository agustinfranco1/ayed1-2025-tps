"""
Ej 1: Escribir una función que devuelva la cantidad de dígitos de un número entero, sin 
utilizar cadenas de caracteres.
"""
def cantidad_digitos(n: int) -> int:
    """
    Calcula la cantidad de digitos de un numero entero.

    Pre: recibe un numero entero a evaluar.

    Post: devuelve un numero entero correspondiente a la cantidad de digitos del numero recibido.
    """  
    # caso base
    if -10 < n < 10:
        return 1

    return 1 + cantidad_digitos(abs(n) // 10)


def main():
    try:
        numero = int(input("Ingrese un numero entero: "))
        resultado = cantidad_digitos(numero)
        if resultado == 1:
            print(f"El numero {numero} tiene un digito.")
        else:
            print(f"El numero {numero} tiene {resultado} digitos.")
    except ValueError:
        print("Debe ingresar un numero entero valido.")


main()