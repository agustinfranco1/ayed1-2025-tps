"""
Ej 14: Se solicita crear un programa para leer direcciones de correo electrónico y verificar 
si representan una dirección válida. Por ejemplo 
usuario@dominio.com.ar. Para que 
una dirección sea considerada válida el nombre de usuario debe poseer solamente 
caracteres alfanuméricos, la dirección contener un solo carácter @, el dominio debe 
tener al menos un carácter y tiene que finalizar con .com o .com.ar.  
Repetir el proceso de validación hasta ingresar una cadena vacía. Al finalizar mostrar 
un listado de todos los dominios, sin repetirlos y ordenados alfabéticamente, 
recordando que las direcciones de mail no distinguen mayúsculas ni minúsculas.
"""
def validar_correo(correo: str) -> bool:
    """
    Verifica si una direccion de correo electronico es valida.

    Pre: Recibe un string correspondiente al correo a evaluar.

    Post: retorna True si el correo es valido o False en caso contrario.
    """
    correo = correo.lower()

    # no debe haber mas de un @
    if correo.count("@") != 1:
        return False

    usuario, dominio = correo.split("@")

    # el usuario solo puede tener caracteres alfanumericos
    if not usuario.isalnum():
        return False

    # el dominio debe tener al menos un caracter
    if len(dominio) == 0:
        return False

    # valida si el dominio termina en .com o .com.ar
    if len(dominio) >= 4 and dominio[-4:] == ".com":
        return True
    if len(dominio) >= 7 and dominio[-7:] == ".com.ar":
        return True

    return False


def obtener_dominio(correo: str) -> str:
    """
    Extrae dominio de un correo.

    Pre: recibe un string correspondiente al correo a evaluar.

    Post: retorna un string correspondiente al dominio en minusculas.
    """
    return correo.lower().split("@")[1]


def main():
    dominios = []

    while True:
        correo = input("Ingrese un correo electronico (o enter para finalizar): ").strip()
        if correo == "":
            break

        if validar_correo(correo):
            dominio = obtener_dominio(correo)
            dominios.append(dominio)
        else:
            print("Correo invalido.")

    dominios.sort()
    print("\nDominios validos ingresados:")
    for d in dominios:
        print(d)


main()