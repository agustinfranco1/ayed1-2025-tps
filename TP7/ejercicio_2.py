"""
Ej 2: Desarrollar una función que reciba un número binario y lo devuelva convertido a 
base decimal. 
"""
def binario_a_decimal(binario: str) -> int:
    """
    Convierte un numero binario a decimal.

    Pre: recibe un string correspondiente a un numero binario.

    Post: devuelve un numero entero correspondiente al numero binario recibido 
          convertido en decimal.
    """
    try:
        if not binario:
            raise ValueError("La cadena no puede estar vacia.")
        if any(c not in "01" for c in binario):
            raise ValueError("El numero binario solo puede contener '0' y '1'.")

        # caso base
        if len(binario) == 1:
            return int(binario)

        return int(binario[0]) * (2 ** (len(binario) - 1)) + binario_a_decimal(binario[1:])

    except ValueError as e:
        print(f"Error: {e}")
        return -1


def main():
    binario = input("\nIngrese un numero binario: ").strip()
    resultado = binario_a_decimal(binario)
    if resultado != -1:
        print(f"\nEl numero binario {binario} equivale a {resultado} en base decimal.\n")


main()