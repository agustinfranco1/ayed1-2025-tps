def diadelasemana(dia: int, mes: int, anio: int) -> int:
    """
    Calcula el dia de la semana de una fecha determinada.

    Pre: Reciibe 3 numeros enteros, el dia, el mes y el anio.

    Post: Retorna un numero entero correspondiente al dia de la semana numericamente,
          considerando que dom = 0, lun = 1, etc.
    """
    if mes < 3:
        mes = mes + 10
        anio = anio - 1
    else:
        mes = mes - 2
    siglo = anio // 100
    anio2 = anio % 100
    diasem = (((26*mes-2)//10)+dia+anio2+(anio2//4)+(siglo//4)-(2*siglo)) % 7
    if diasem < 0:
        diasem = diasem + 7
    return diasem  


def dias_del_mes(mes: int, anio: int) -> int:
    """
    Calcula los dias del mes segun el mes introducido.

    Pre: Recibe 2 numeros enteros, el mes y el anio.

    Post: Devuelve un numero entero correspondiente al numero de dias del mes ingresado.
    """
    if mes in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif mes in [4, 6, 9, 11]:
        return 30
    elif mes == 2:
        if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
            return 29
        else:
            return 28

def fecha_valida(mes: int, anio: int) -> bool:
    """
    Evalúa si la fecha ingresada es válida.

    Pre: Recibe 2 números enteros, mes y anio.

    Post: Retorna True si la fecha es válida o False si no lo es.
    """
    if anio < 1:
        return False
    if mes < 1 or mes > 12:
        return False
    return True

def imprimir_calendario(mes: int, anio: int) -> None:
    """
    Imprime el calendario de un mes en un anio especifico.

    Pre: Recibe 2 numeros enteros, el mes y el anio.

    Post: No retorna nada, imprime el calendario del mes segun los parametros dados.
    """
    print(f"\nCalendario de {mes}/{anio}\n")
    print("Do Lu Ma Mi Ju Vi Sá")

    inicio = diadelasemana(1, mes, anio)
    print("   " * inicio, end="")

    for dia in range(1, dias_del_mes(mes, anio) + 1):
        print(f"{dia:2}", end=" ")
        if (inicio + dia) % 7 == 0:
            print()
    print()



def main():
    """
    Solicita al usuario el mes y el anio e invoca otras funciones 
    para validar, calcular e imprimir el calendario del mes indicado.

    Pre: No recibe parametros.

    Post: No retorna nada, imrprime mensaje de error en caso de ingresar fecha invalida.
    """
    mes = int(input("Ingrese el número de mes (1-12): "))
    anio = int(input("Ingrese el año: "))

    if fecha_valida(mes, anio):
        imprimir_calendario(mes, anio)
    else:
        print("La fecha ingresada no es válida.")


main()
