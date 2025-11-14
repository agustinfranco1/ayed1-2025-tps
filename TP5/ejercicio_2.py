"""
Ej 2: Realizar una función que reciba como parámetros dos cadenas de caracteres conteniendo 
números reales, sume ambos valores y devuelva el resultado como un 
número real. Devolver -1 si alguna de las cadenas no contiene un número válido, 
utilizando manejo de excepciones para detectar el error.
"""
def sumar_cadenas_numeros(str1: str, str2: str) -> float:
    """
    Transforma y calcula la suma entre dos numeros pertenecientes a los reales recibidos como cadenas.

    Pre: recibe dos strings correspondientes a numeros reales.

    Post: devuelve un numero flotante resultante de la suma como numero real, 
          o -1 si alguna cadena no contiene un numero valido.
    """
    try:
        num1 = float(str1)
        num2 = float(str2)
        return num1 + num2
    except ValueError:
        return -1.00


def main():
    cadena1 = input("Ingrese el primer numero real: ")
    cadena2 = input("Ingrese el segundo numero real: ")
    resultado = sumar_cadenas_numeros(cadena1, cadena2)

    if resultado == -1:
        print("Error: alguna de las cadenas no representa un numero valido.")
    else:
        print(f"El resultado de la suma es: {resultado}")


main()