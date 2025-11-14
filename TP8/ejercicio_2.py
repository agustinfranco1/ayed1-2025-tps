"""
Ej 2: Escribir una función que reciba como parámetro una tupla conteniendo una fecha 
(día,mes,año) y devuelva una cadena de caracteres con la misma fecha expresada 
en formato extendido. La función debe contemplarse que el año se ingrese en dos 
dígitos, los que serán interpretados según un año de corte definido dentro del 
programa. Cualquier año mayor que éste se considerará del siglo pasado. Por 
ejemplo, si el año de corte fuera 30, la función devuelve "12 de Octubre de 2030" 
para (12,10,30). Pero si la tupla fuera (25, 12, 31) devolverá "25 de Diciembre de 
1931". Si el año se ingresa en cuatro dígitos el año de corte no será tenido en 
cuenta. Escribir también un programa para ingresar los datos, invocar a la función y 
mostrar el resultado.
"""
from typing import Tuple

def transformar_fecha(fecha: Tuple[int], anio_corte: int = 30) -> str:
    """
    Convierte una fecha a formato extendido, si el año se ingresa con 2 digitos, 
    sera interpretado segun el año de corte establecido.
    
    Pre: recibe una tupla de enteros correspondientes a una fecha y un entero 
         correspondiente al año de corte.
    
    Post: devuelve un string con la fecha recibida en formato extendido.
    """
    try:
        dia, mes, anio = fecha
        meses = (
            "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
            "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
        )

        if not (1 <= mes <= 12):
            raise ValueError("El mes debe estar entre 1 y 12")
        if not (1 <= dia <= 31):
            raise ValueError("El dia debe estar entre 1 y 31")

        if anio < 100:  
            if anio > anio_corte:
                anio += 1900
            else:
                anio += 2000
        elif anio < 1000 or anio > 9999:
            raise ValueError("El año debe tener 2 o 4 digitos")

        return f"{dia} de {meses[mes - 1]} de {anio}"

    except ValueError as e:
        return f"Error: {e}."


def main():
    while True:
        try:
            dia = int(input("\nIngrese el dia: "))
            mes = int(input("\nIngrese el mes: "))
            anio = int(input("\nIngrese el año: "))

            fecha = (dia, mes, anio)
            resultado = transformar_fecha(fecha)
            print(f"\nResultado: {resultado}")

            continuar = input("\nDesea ingresar otra fecha? (s/n): ")
            if continuar != "s":
                print("Programa finalizado.")
                break

        except ValueError:
            print("Error: Ingrese solo numeros enteros validos.\n")


main()