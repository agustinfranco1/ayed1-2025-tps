"""
Ej 7: Escribir un programa que juegue con el usuario a adivinar un número. El programa 
debe generar un número al azar entre 1 y 500 y el usuario debe adivinarlo. Para 
eso, cada vez que se introduce un valor se muestra un mensaje indicando si el nú
mero que tiene que adivinar es mayor o menor que el ingresado. Cuando consiga 
adivinarlo, se debe imprimir en pantalla la cantidad de intentos que le tomó hallar 
el número. Si el usuario introduce algo que no sea un número se mostrará un 
mensaje en pantalla y se lo contará como un intento más.
"""
from random import randint, seed
seed(1)

def adivinar_numero(numero_aleatorio: int) -> None:
    """
    Solicita numeros al usuario hasta que ingrese el numero aleatorio seleccionado entre 1 y 500, 
    dando pistas en el proceso.

    Pre: Recibe un numero entero que el usuario debera adivinar.

    Post: No retorna nada pero solicita al usuario numeros al usuario numeros hasta que adivine el numero dado,
          dandole pistas en el proceso de si el numero es mayor o menor que el que ingreso e indicando cuando no
          se ingreso un numero valido.
    """
    intentos = 0
    print("Debes adivinar un numero entre 1 y 500")

    while True:
        try:
            entrada = int(input("Ingresa tu intento: "))
            intentos += 1

            if entrada < numero_aleatorio:
                print("El numero es mayor.")
            elif entrada > numero_aleatorio:
                print("El numero es menor.")
            else:
                print(f"Adivinaste el numero en {intentos} intentos.")
                break

        except ValueError:
            intentos += 1
            print("Error: debes ingresar un numero entero valido.")


def main():
    numero_aleatorio = randint(1, 500)
    adivinar_numero(numero_aleatorio)

main()