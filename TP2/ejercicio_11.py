"""
Ej 11: Una clínica necesita un programa para atender a sus pacientes. Cada paciente que 
ingresa se anuncia en la recepción indicando su número de afiliado (número entero 
de 4 dígitos) y además indica si viene por una urgencia (ingresando un 0) o con 
turno (ingresando un 1). Para finalizar se ingresa -1 como número de socio. Luego 
se solicita:
a. Mostrar un listado de los pacientes atendidos por urgencia y un listado de 
los pacientes atendidos por turno en el orden que llegaron a la clínica.
b. Realizar la búsqueda de un número de afiliado e informar cuántas veces fue 
atendido por turno y cuántas por urgencia. Repetir esta búsqueda hasta 
que se ingrese -1 como número de afiliado. 
"""
from typing import List

def cargar_pacientes() -> List[int]:
    """
    Permite cargar el ingreso de pacientes y si vinieron por urgencia o con turno.

    Pre: No recibe parametros.

    Post: Devuelve dos listas, una de pacientes llegados por urgencias y otra de pacientes con turno previo.
    """
    urgencias = []
    turnos = []

    while True:
        nro = input("\nIngrese número de afiliado (4 dígitos) o -1 para finalizar: ")
        if nro == "-1":
            break
        if not nro.isdigit() or len(nro) != 4:
            print("\nNúmero de afiliado inválido. Debe tener 4 dígitos.")
            continue
        nro = int(nro)

        tipo = input("\nIngrese 0 para urgencia o 1 para turno: ")
        if tipo not in ["0", "1"]:
            print("\nOpción inválida. Debe ingresar 0 o 1.")
            continue

        if tipo == "0":
            urgencias.append(nro)
        else:
            turnos.append(nro)

    return urgencias, turnos
    

def buscar_afiliado(urgencias: List[int], turnos: List[int]) -> None:
    """
    Permite buscar cuantas veces un afiliado fue atendido por urgencia y/o por turno.

    Pre: Recibe dos listas de enteros, una correspondiente a los numeros de afiliados de los pacientes 
    llegados por urgencias y la otra a los numeros de afiliados de los pacientes llegados por turno.

    Post: No devuelve nada, imprime las veces que un paciente fue atendido por urgencia y/o turno.
    """
    while True:
        nro = input("\nIngrese número de afiliado para buscar (-1 para salir): ")
        if nro == "-1":
            break
        if not nro.isdigit() or len(nro) != 4:
            print("\nNumero de afiliado invalido. Debe tener 4 dígitos.")
            continue
        nro = int(nro)

        urg = urgencias.count(nro)
        turno = turnos.count(nro)

        if not urg and turno:
            print(f"\nEl afiliado {nro} fue atendido {turno} vez/veces por turno.")
        elif urg and not turno:
            print(f"\nEl afiliado {nro} fue atendido {urg} vez/veces por urgencia.")
        else:
            print(f"\nEl afiliado {nro} fue atendido {urg} vez/veces por urgencia y {turno} vez/veces por turno.")


def main():
    urgencias, turnos = cargar_pacientes()
    print(f"\nPacientes atendidos por urgencia: \n{urgencias}")
    print(f"\nPacientes atendidos por turno: \n{turnos}")
    buscar_afiliado(urgencias, turnos)


main()
