"""
Ej 1: Desarrollar una función para ingresar a través del teclado un número natural. La 
función rechazará cualquier ingreso inválido de datos utilizando excepciones y 
mostrará la razón exacta del error. Controlar que se ingrese un número, que ese 
número sea entero y que sea mayor que 0, mostrando un mensaje con la razón 
exacta del error en caso necesario. Devolver el valor ingresado cuando éste sea 
correcto. Escribir también un programa que permita probar el correcto funciona
miento de la misma.
"""
def validar_numero_natural(n: str) -> int | None:
    """
    Evalua si un numero pertenece al conjunto de los naturales.

    Pre: Recibe un string correspondiente al numero a evaluar.

    Post: Devuelve un numero entero correspondiente al recibido si pertenece a los naturales,
          de lo contrario no devuelve nada.
    """
    try:
        if n.strip() == "":
            raise ValueError("No se ingreso ningun valor.")

        try:
            numero = float(n)
        except ValueError:
            raise ValueError("No se ingreso un numero")

        if numero != int(numero):
            raise ValueError("El numero no es entero.")

        numero = int(numero)
        if numero <= 0:
            raise ValueError("El numero debe ser mayor que 0.")

        return numero

    except ValueError as e:
        print(f"Error: {e}")
        return None


def main():
    while True:
        entrada = input("Ingrese un numero natural: ")
        numero = validar_numero_natural(entrada)
        if numero is not None:
            print("Numero ingresado correctamente")
            break


main()