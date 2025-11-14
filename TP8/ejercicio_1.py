"""
Ej 1: Desarrollar las siguientes funciones utilizando tuplas para representar fechas y ho
rarios, y luego escribir un programa que las vincule:
 a. Ingresar una fecha desde el teclado, verificando que corresponda a una fecha 
válida.
 b. Sumar N días a una fecha.
 c. Ingresar un horario desde teclado, verificando que sea correcto.
 d. Calcular la diferencia entre dos horarios. Si el primer horario fuera mayor al 
segundo se considerará que el primero corresponde al día anterior. En ningún 
caso la diferencia en horas puede superar las 24 horas.
"""
from typing import Tuple

def fecha_valida(dia: int, mes: int, anio: int) -> bool:
    """
    Verifica si una fecha es valida.

    Pre: recibe 3 numeros enteros correspondientes al dia, mes y año.

    Post: devuelve True si la fecha es valida o False si no lo es.
    """
    if mes < 1 or mes > 12 or dia < 1:
        return False

    dias_por_mes = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    # Año bisiesto
    if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
        dias_por_mes = (31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

    return dia <= dias_por_mes[mes - 1]


def ingresar_fecha() -> Tuple[int]:
    """
    Solicita y evalua una fecha.

    Pre: no recibe parametros.

    Post: devuelve una tupla cargada con los numeros enteros correspondienes a una fecha validada.
    """
    while True:
        try:
            dia = int(input("Ingrese el dia: "))
            mes = int(input("Ingrese el mes: "))
            anio = int(input("Ingrese el año: "))

            if not fecha_valida(dia, mes, anio):
                raise ValueError("La fecha ingresada no es valida")
            return (dia, mes, anio)
        except ValueError as e:
            print(f"Error: {e}. Intente nuevamente.\n")


def sumar_dias(fecha: Tuple[int], n: int) -> Tuple[int]:
    """
    Suma N dias a una fecha.

    Pre: recibe una tupla de enteros correspondientes a una fecha y 
         el entero que se desea sumar a la misma.

    Post: devuelve una tupla de enteros con la nueva fecha resultante de la suma.
    """
    dia, mes, anio = fecha
    dias_por_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    while n > 0:
        # Año bisiesto
        if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
            dias_por_mes[1] = 29
        else:
            dias_por_mes[1] = 28

        dia += 1
        if dia > dias_por_mes[mes - 1]:
            dia = 1
            mes += 1
            if mes > 12:
                mes = 1
                anio += 1
        n -= 1

    return (dia, mes, anio)


def ingresar_horario() -> Tuple[int]:
    """
    Solicita y evalua una horario.

    Pre: no recibe parametros.

    Post: devuelve una tupla de enteros correspondientes a un horario validado.
    """
    while True:
        try:
            hora = int(input("Ingrese la hora (0-23): "))
            minutos = int(input("Ingrese los minutos (0-59): "))

            if not (0 <= hora < 24 and 0 <= minutos < 60):
                raise ValueError("Horario invalido")
            return (hora, minutos)
        except ValueError as e:
            print(f"Error: {e}. Intente nuevamente.\n")


def diferencia_horarios(h1: Tuple[int], h2: Tuple[int]) -> Tuple[int]:
    """
    Calcula la diferencia entre dos horarios.

    Pre: recibe dos tuplas de enteros correspondientes a dos horarios validos.

    Post: devuelve una tupla de enteros con el horario que separa los horarios recibidos.
    """
    h1_min = h1[0] * 60 + h1[1]
    h2_min = h2[0] * 60 + h2[1]

    if h1_min > h2_min:
        h2_min += 24 * 60

    dif_min = h2_min - h1_min
    horas = dif_min // 60
    minutos = dif_min % 60
    return (horas, minutos)


def main():
    while True:
        print("\n1. Ingresar y validar una fecha")
        print("2. Sumar N dias a una fecha valida")
        print("3. Ingresar y validar un horario")
        print("4. Calcular la diferencia entre dos horarios")
        print("5. Salir\n")

        opcion = input("Seleccione una opcion: ")

        try:
            if opcion == "1":
                fecha = ingresar_fecha()
                print(f"\nFecha valida: {fecha[0]:02d}/{fecha[1]:02d}/{fecha[2]}\n")

            elif opcion == "2":
                fecha = ingresar_fecha()
                n = int(input("Ingrese la cantidad de dias a sumar: "))
                nueva_fecha = sumar_dias(fecha, n)
                print(f"\nFecha resultante: {nueva_fecha[0]:02d}/{nueva_fecha[1]:02d}/{nueva_fecha[2]}")

            elif opcion == "3":
                horario = ingresar_horario()
                print(f"\nHorario valido: {horario[0]:02d}:{horario[1]:02d}")

            elif opcion == "4":
                print("Ingrese el primer horario:")
                h1 = ingresar_horario()
                print("Ingrese el segundo horario:")
                h2 = ingresar_horario()
                diferencia = diferencia_horarios(h1, h2)
                print(f"\nDiferencia: {diferencia[0]} horas y {diferencia[1]} minutos")

            elif opcion == "5":
                print("Programa finalizado.")
                break

            else:
                print("Opcion no valida. Intente nuevamente.\n")

        except ValueError as e:
            print(f"Error: {e}. Intente nuevamente.\n")


main()