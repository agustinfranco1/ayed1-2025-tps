def es_bisiesto(anio: int) -> bool:
    """
    Evalua si el año es bisiesto.

    Pre: Recibe un numero entero correspondiente al año.

    Post: Retorna True si el año ingresado es bisiesto o False en caso contrario.
    """
    return (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)


def fecha_valida(dia: int, mes: int, anio: int) -> bool:
    """
    Verifica si los números proporcionados corresponden a una fecha válida.

    Pre: Recibe 3 numeros enteros correspondientes a al dia, mes y año.

    Post: Devuelve True si todos los valores son validos o False en caso contrario.
    """
    if dia <= 0 or mes <= 0 or anio <= 0:
        return False
    
    if mes > 12:
        return False
    
    dias_por_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    if mes == 2 and es_bisiesto(anio):
        max_dia = 29
    else:
        max_dia = dias_por_mes[mes - 1]
    
    return dia <= max_dia


def main():
    """
    Solicita la fecha a evaluar al usuario e invoca otras funciones para evaluar su validez.

    Pre: No recibe parametros.

    Post: Muestra en pantalla si la fecha ingresada es valida o invalida.
    """
    dia = int(input("Ingrese el dia: "))
    mes = int(input("Ingrese el mes: "))
    anio = int(input("Ingrese el año: "))

    if fecha_valida(dia, mes, anio):
        print(f"La fecha {dia}/{mes}/{anio} es válida.")
    else:
        print(f"La fecha {dia}/{mes}/{anio} es inválida.")

main()
