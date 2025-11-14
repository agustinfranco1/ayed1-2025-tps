"""
Ej 3: Desarrollar una función que devuelva una cadena de caracteres con el nombre del 
mes cuyo número se recibe como parámetro. Los nombres de los meses deberán 
obtenerse de una lista de cadenas de caracteres inicializada dentro de la función. 
Devolver una cadena vacía si el número de mes es inválido. La detección de meses 
inválidos deberá realizarse a través de excepciones.
"""
def nombre_mes(mes: int) -> str:
    """
    Convierte un numero en su equivalente en meses del año.

    Pre: recibe un numero entero correspondiente a un mes.

    Post: devuelve un string con el nombre del mes correspondiente, o vacio si el numero no es valido.
    """
    try:
        meses = [
            "enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", 
            "noviembre", "diciembre"
        ]

        if mes < 1 or mes > 12:
            raise IndexError

        return meses[mes - 1]

    except (TypeError, IndexError):
        return ""


def main():
    try:
        numero = int(input("Ingrese el numero de mes (1-12): "))
        nombre_mes = nombre_mes(numero)

        if nombre_mes == "":
            print("Error: numero de mes invalido.")
        else:
            print(f"El mes correspondiente es: {nombre_mes}")
    except ValueError:
        print("Error: debe ingresar un numero entero.")


main()