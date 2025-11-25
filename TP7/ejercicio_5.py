"""
Ej 5: Realizar una función que devuelva el resto de dos números enteros, utilizando restas sucesivas.
"""
def resto_por_restas(dividendo: int, divisor: int) -> int:
    """
    Calcula el resto entre dos numeros enteros utilizando restas sucesivas.

    Pre: recibe dos numeros enteros cuya division se va a calcular.

    Post: devuelve un numero entero correspondiente a la division de los numeros recibidos.
    """
    try:
        if divisor == 0:
            raise ZeroDivisionError("El divisor no puede ser cero.")

        signo = -1 if dividendo < 0 else 1
        dividendo, divisor = abs(dividendo), abs(divisor)

        # caso base
        if dividendo < divisor:
            return signo * dividendo

        return signo * resto_por_restas(dividendo - divisor, divisor)

    except ZeroDivisionError as e:
        print(f"Error: {e}")
        return -1


def main():
    try:
        dividendo = int(input("\nIngrese el dividendo entero: "))
        divisor = int(input("\nIngrese el divisor entero: "))

        resultado = resto_por_restas(dividendo, divisor)
        if resultado != -1:
            print(f"\nEl resto de dividir {dividendo} entre {divisor} es: {resultado}")

    except ValueError:
        print("Error: Debe ingresar valores enteros validos.")


main()