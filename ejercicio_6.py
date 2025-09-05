def concatenar_numeros(a: int, b: int) -> int:
    """
    Concatena dos números enteros.

    Pre: Recibe 2 numeros enteros.

    Post: Devuelve ambos numeros concatenados en un entero.
    """
    return int(str(a) + str(b))


def main():
    """
    Solicita dos numeros al usuario e invoca a otra funcion para concatenarlos.

    Pre: No recibe parametros.

    Post: Imprime el numero entero concatenado o un mensaje de error en caso de ingresar un numero invalido.
    """
    num_1 = int(input("Ingrese el primer número: "))
    num_2 = int(input("Ingrese el segundo número: "))

    if num_1 > 0 and num_2 > 0:
        resultado = concatenar_numeros(num_1, num_2)
        print("El número concatenado es:", resultado)
    else:
        print("Error: Ambos números deben ser positivos.")


main()
