"""
Ej 5: Escribir una función filtrar_palabras() que reciba una cadena de caracteres 
conteniendo una frase y un entero N, y devuelva otra cadena con las palabras 
que tengan N o más caracteres de la cadena original. 
Escribir también un programa para verificar el comportamiento de la misma. 
Hacer tres versiones de la función, para cada uno de los siguientes casos: 
a. Utilizando sólo ciclos normales 
b. Utilizando listas por comprensión 
c. Utilizando la función filter
"""
def filtrar_palabras_a(frase: str, n: int) -> str:
    """
    Filtra las palabras que tienen N o mas caracteres de un string utilizando ciclos normales.

    Pre: recibe un string y un numero entero correspondinetes a la frase y cantidad de caracteres.

    Post: devuelve un string formado por las palabras que tienen N o mas caracteres.
    """
    palabras = frase.split()
    resultado = []

    for palabra in palabras:
        if len(palabra) >= n:
            resultado.append(palabra)

    return " ".join(resultado)


def filtrar_palabras_b(frase: str, n: int) -> str:
    """
    Version b: utilizando listas por comprensión.

    Pre: recibe un string y un numero entero correspondinetes a la frase y cantidad de caracteres.

    Post: devuelve un string formado por las palabras que tienen N o mas caracteres.
    """
    return " ".join([palabra for palabra in frase.split() if len(palabra) >= n])


def filtrar_palabras_c(frase: str, n: int) -> str:
    """
    Version c: utilizando la funcion filter.

    Pre: recibe un string y un numero entero correspondinetes a la frase y cantidad de caracteres.

    Post: devuelve un string formado por las palabras que tienen N o mas caracteres.
    """
    return " ".join(filter(lambda palabra: len(palabra) >= n, frase.split()))


def main():
    frase = input("Ingrese una frase: ")
    n = int(input("Ingrese un numero entero correspondiente al minimo de caracteres: "))

    print("\nVersion a:")
    print(filtrar_palabras_a(frase, n))

    print("\nVersion b:")
    print(filtrar_palabras_b(frase, n))

    print("\nVersion c:")
    print(filtrar_palabras_c(frase, n))


main()