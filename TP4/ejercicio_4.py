"""
Ej 4: Escribir una función que reciba como parámetro un número entero entre 0 y 3999 y 
lo convierta en un número romano, devolviéndolo en una cadena de caracteres.
"""

def entero_a_romano(numero: int) -> str:
    """
    Convierte un numero entero entre 0 y 3999 en su equivalente en numeros romanos.

    Pre: recibe un numero entero entre 0 y 3999.

    Post: devuelve un string con el numero romano correspondiente a numero.
    """
    valores = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    simbolos = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

    resultado = ""
    i = 0

    while numero > 0:
        if numero >= valores[i]:
            resultado += simbolos[i]
            numero -= valores[i]
        else:
            i += 1

    return resultado


def main():
    numero = int(input("Ingrese un numero entero entre 0 y 3999: "))
    romano = entero_a_romano(numero)
    print(f"Numero romano: {romano}")


main()