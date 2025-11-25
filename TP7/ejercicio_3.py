"""
Ej 3: Escribir una función que devuelva la suma de los N primeros números naturales.
"""
def suma_n_naturales(n: int) -> int:
    """
    Calcula la suma de los N primeros numeros naturales.
    
    Pre: recibe un numero entero correspondiente a los N numeros que se sumaran.

    Post: devuelve un numero entero correspondiente a la suma de los primeros N numeros naturales.
    """
    try:
        if n < 0:
            raise ValueError("El numero debe ser no negativo.")
        
        # caso base
        if n == 0:
            return 0

        return n + suma_n_naturales(n - 1)
    
    except (TypeError, ValueError) as e:
        print(f"Error: {e}")
        return -1


def main():
    numero = int(input("\nIngrese un numero entero positivo: "))
    resultado = suma_n_naturales(numero)
    if resultado != -1:
        print(f"\nLa suma de los primeros {numero} numeros naturales es: {resultado}.\n")


main()