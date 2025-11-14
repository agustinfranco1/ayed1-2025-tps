"""
Ej 3: Desarrollar un programa que utilice una función que reciba como parámetro una 
cadena de caracteres conteniendo una dirección de correo electrónico y devuelva 
una tupla con las distintas partes que componen dicha dirección. Ejemplo: 
alguien@uade.edu.ar -> (alguien, uade, edu, ar). La función debe detectar 
formatos de fecha inválidos y devolver una tupla vacía.
"""
from typing import Tuple

def desarmar_correo(correo: str) -> Tuple[str]:
    """
    Desarma una direccion de correo electronico en partes.

    Pre: recibe un string correspondiente a un correo electronico.

    Post: devuelve una tupla de strings con las partes del correo, 
          o la devuelve vacia si el correo recibido es invalido.
    """
    try:
        if "@" not in correo:
            raise ValueError("La direccion debe contener un '@'.")
        if correo.count("@") > 1:
            raise ValueError("La dirección no puede tener mas de un '@'.")

        usuario, dominio = correo.split("@")

        if not usuario or not dominio:
            raise ValueError("El correo debe tener usuario y dominio validos.")

        partes = [usuario] + dominio.split(".")

        return tuple(partes)

    except ValueError as e:
        print(f"Error: {e}")
        return ()


def main():
    correo = input("\nIngrese una direccion de correo electronico: ").strip()
    partes = desarmar_correo(correo)

    if partes:
            print(f"Partes del correo: {partes}")


main()