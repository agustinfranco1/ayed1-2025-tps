"""
Ej 7: Escribir una función diasiguiente(dia, mes año) que reciba como parámetro una 
fecha cualquiera expresada por tres enteros y calcule y devuelva otros tres enteros 
correspondientes el día siguiente al dado. Utilizando esta función sin modificaciones 
ni agregados, desarrollar programas que permitan:
a. Sumar N días a una fecha.
b. Calcular la cantidad de días existentes entre dos fechas cualesquiera.
"""
def es_bisiesto(anio: int) -> bool:
    """
    Evalua si un anio es bisiesto.

    Pre: 1 numero entero, el anio.

    Post: Devuelve True si el anio es bisiesto o False si no lo es.
    """
    return (anio % 400 == 0) or (anio % 4 == 0 and anio % 100 != 0)


def dias_en_mes(mes: int, anio: int) -> int:
    """
    Calcula los dias que tiene el mes ingresado.

    Pre: Recibe 2 numeros enteros, el mes y el anio.

    Post: Retorna un numero entero, los dias que tiene el mes ingresado.
    """
    if mes in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif mes in [4, 6, 9, 11]:
        return 30
    elif mes == 2:
        return 29 if es_bisiesto(anio) else 28
    return 0


def fecha_valida(dia: int, mes: int, anio: int) -> bool:
    """
    Evalua si la fecha ingresada es valida

    Pre: 3 numeros enteros, dia, mes y anio.

    Post: Retorna True si la fecha es valida o False si no lo es.
    """
    if anio < 1:
        return False
    if mes < 1 or mes > 12:
        return False
    if dia < 1 or dia > dias_en_mes(mes, anio):
        return False
    return True


def leer_fecha(mensaje: str) -> tuple[int, int, int]:
    """
    Solicita la fecha al usuario y usa otra funcion para validar la misma.

    Pre: Recibe un string, el mensaje a comunicar previo a solicitar las fechas.

    Post: Retorna una tupla con tres numeros enteros, el dia, el mes y el anio una vez sean validos.
    """
    while True:
        print(mensaje)
        dia = int(input("Día: "))
        mes = int(input("Mes: "))
        anio = int(input("Año: "))
        if fecha_valida(dia, mes, anio):
            return (dia, mes, anio)
        else:
            print("Fecha inválida, intente de nuevo.\n")


def diasiguiente(dia: int, mes: int, anio: int) -> tuple[int, int, int]:
    """
    Calcula el dia siguiente a la fecha recibida.

    Pre: Recibe 3 numeros enteros, el dia, el mes y el anio.

    Post: Retorna una tupla cragada con 3 enteros, el dia, el mes y el anio,
          correspondientes a la fecha siguiente a la recibida
    """
    if dia < dias_en_mes(mes, anio):
        return dia + 1, mes, anio
    else:
        if mes == 12:
            return 1, 1, anio + 1
        else:
            return 1, mes + 1, anio


def sumar_dias(dia: int, mes: int, anio: int, dias_sumados: int) -> tuple[int, int, int]:
    """
    Calcula la fecha resultada de la suma de una fecha ingresada con los dias deseados.

    Pre: Recibe 4 numeros enteros, el dia, el mes y el anio correspondientes a la fecha que se desea sumar
         y por ultimo la cantidad de dias a sumar.

    Post: Retorna una tupla con tres numeros enteros, 
          correspondientes al dia, mes y anio resultantes de la suma.
    """
    for x in range(dias_sumados):
        dia, mes, anio = diasiguiente(dia, mes, anio)
    return (dia, mes, anio)


def dias_entre(dia_1: int, mes_1: int, anio_1: int, dia_2: int, mes_2: int, anio_2: int) -> int:
    """
    Calcula la cantidad de dias entre dos fechas diferentes.

    Pre: Recibe 6 numeros enteros correspondientes a los dias, meses y anios de dos fechas diferentes.

    Post: Retorna un numero entero equivalente a la cantidad de dias de diferencia entre ambas fechas.
    """
    if (anio_1, mes_1, dia_1) > (anio_2, mes_2, dia_2):
        dia_1, mes_1, anio_1, dia_2, mes_2, anio_2 = dia_2, mes_2, anio_2, dia_1, mes_1, anio_1

    contador = 0
    while (dia_1, mes_1, anio_1) != (dia_2, mes_2, anio_2):
        dia_1, mes_1, anio_1 = diasiguiente(dia_1, mes_1, anio_1)
        contador += 1
    return contador


def main():
    """
    Junta las funciones correspondientes para solicitar fechas al usuario y calcular el dia siguiente a una fecha, 
    sumar N dias a una fecha y calcular los dias entre dos fechas diferentes.

    Pre: No recibe parametros.

    Post: Imprime los resultados de las diferentes funciones una vez ejecutadas.
    """
    print("Calcular día siguiente:")
    dia, mes, anio = leer_fecha("Ingrese una fecha:")
    siguiente = diasiguiente(dia, mes, anio)
    print(f"El día siguiente es: {siguiente[0]}/{siguiente[1]}/{siguiente[2]}")

    print("\nSumar N días:")
    d, m, a = leer_fecha("Ingrese una fecha:")
    dias_a_sumar = int(input("¿Cuántos días desea sumar?: "))
    nueva_fecha = sumar_dias(d, m, a, dias_a_sumar)
    print(f"La fecha luego de sumar {dias_a_sumar} días es: {nueva_fecha[0]}/{nueva_fecha[1]}/{nueva_fecha[2]}")

    print("\nCalcular días entre dos fechas:")
    dia_1, mes_1, anio_1 = leer_fecha("Ingrese la primera fecha:")
    dia_2, mes_2, anio_2 = leer_fecha("Ingrese la segunda fecha:")
    cantidad = dias_entre(dia_1, mes_1, anio_1, dia_2, mes_2, anio_2)
    print(f"La cantidad de días entre ambas fechas es: {cantidad}")


main()
