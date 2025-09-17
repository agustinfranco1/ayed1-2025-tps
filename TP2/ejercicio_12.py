"""
Ej 12: Resolver el siguiente problema, utilizando funciones:
Se desea llevar un registro de los socios que visitan un club cada día. Para ello, se 
ingresa el número de socio de cinco dígitos hasta ingresar un cero como fin de car
ga. Se solicita:
a. Informar para cada socio, cuántas veces ingresó al club. Cada socio debe 
aparecer una sola vez en el informe.
b. Solicitar un número de socio que se dio de baja del club y eliminar todos sus 
ingresos. Mostrar los registros de entrada al club antes y después de 
eliminarlo. Informar cuántos ingresos se eliminaron
"""
from typing import List

def cargar_socios() -> List[int]:
    """
    Permite cargar los socios que ingresaron por su numero de socio.

    Pre: No recibe parametros.

    Post: Devuelve una lista de enteros con los numeros de los socios cargados.
    """
    ingresos = []

    while True:
        nro = input("\nIngrese el numero de socio (5 digitos) o 0 para finalizar: ")
        if nro == "0":
            break
        if not nro.isdigit() or len(nro) != 5:
            print("Numero de socio invalido. Debe tener 5 digitos.")
            continue
        ingresos.append(int(nro))

    return ingresos


def mostrar_ingresos(ingresos: List[int]) -> None:
    """
    Muestra cuantas veces ingreso cada socio.

    Pre: Recibe una lista de enteros con los numeros de los socios que ingresaron.

    Post: No devuelve nada, imprime los socios que ingresaron y cuantas veces lo hicieron.
    """
    socios = []
    for socio in ingresos:
        if socio not in socios:
            veces = ingresos.count(socio)
            print(f"Socio {socio}: {veces} vez/veces")
            socios.append(socio)



def eliminar_socio(ingresos: List[int], baja: int) -> int:
    """
    Elimina todos los ingresos de un socio que se dio de baja.

    Pre: Recibe una lista de enteros correpondiente a los numeros de los socios que ingresaron
    y tambien recibe un numero entero correspondiente al numero de socio del socio que se haya dado de baja.

    Post: Devuelve un numero entero correspondiente al numero de ingresos del socio que se dio de baja.
    """
    cantidad = ingresos.count(baja)
    i = 0
    while i < len(ingresos):
        if ingresos[i] == baja:
            ingresos.pop(i)
        else:
            i += 1
    return cantidad


def main():
    ingresos = cargar_socios()
    print(f"\nRegistros de ingreso actuales: ")
    mostrar_ingresos(ingresos)

    while True:
        baja = input("\nIngrese el numero de socio que se dio de baja o 0 para finalizar: ")
        if baja == "0":
            break
        if not baja.isdigit() or len(baja) != 5:
            print("\nNumero invalido.")
            continue
        baja = int(baja)
        eliminados = eliminar_socio(ingresos, baja)
        print(f"\nSe eliminaron {eliminados} ingreso/s del socio {baja}.")
        print("\nRegistros despues de eliminar:")
        mostrar_ingresos(ingresos)

main()
