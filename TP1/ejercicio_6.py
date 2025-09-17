"""
Ej 6: Desarrollar una función que reciba como parámetros dos números enteros positivos 
y devuelva como valor de retorno el número que resulte de concatenar ambos 
parámetros. Por ejemplo, si recibe 1234 y 567 debe devolver 1234567. No se per
mite utilizar facilidades de Python no vistas en clase.
"""

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
