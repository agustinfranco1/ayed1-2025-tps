"""
Ej 9: Generar e imprimir una lista por comprensión entre A y B con los múltiplos de 7 
que no sean múltiplos de 5. A y B se ingresar desde el teclado. 
"""
from typing import List

def multiplos_7_no_5(a: int, b: int) -> List[int]:
    """
    Genera una lista de multiplos de 7 menos los divisibles por 5 en un rango de a hasta b.

    Pre: Recibe dos numeros enteros, entre los cuales se buscaran aquellos que cumplan la condicion.

    Post: Devuelve una lista de enteros divisibles por 7 pero no por 5 entre los rangos ingresados.
    """
    return [n for n in range(a, b + 1) if n % 7 == 0 and n % 5 != 0]


def main():
    while True:
        a = input("\nIngrese el valor de inicio: ")
        if a.isdigit() and int(a) > 0:
            a = int(a)
            break
        else:
            print("\nError: debe ingresar un numero entero mayor a 0.")
    
    while True:
        b = input("\nIngrese el valor de finalizacion: ")
        if b.isdigit() and int(b) > a:
            b = int(b)
            break
        else:
            print("\nError: debe ingresar un numero entero mayor al de inicio.")


    lista = multiplos_7_no_5(a, b)

    print(f"\nMultiplos de 7 que no son múltiplos de 5 entre {a} y {b}: \n{lista}")


main()
