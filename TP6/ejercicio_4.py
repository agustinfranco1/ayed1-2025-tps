"""
Ej 4: Desarrollar un programa para eliminar todos los comentarios de un programa  escrito 
en lenguaje Python. Tener en cuenta que los comentarios comienzan con el 
signo # (siempre que éste no se encuentre encerrado entre comillas simples o do
bles) y que también se considera comentario a las cadenas de documentación 
(docstrings).
"""
import os


def limpiar_linea_de_comentarios(linea: str) -> str:
    """
    Elimina comentarios de una linea de codigo python.

    Pre: recibe una cadena de codigo en lenguaje python a analizar.

    Post: devuelve la cadena de codigo sin comentarios en esta.
    """

    nueva_linea = ""
    comillas_simples = False
    comillas_dobles = False
    i = 0

    while i < len(linea):
        char = linea[i]

        if char == "'" and not comillas_dobles:
            comillas_simples = not comillas_simples
            nueva_linea += char
            i += 1
            continue

        if char == '"' and not comillas_simples:
            comillas_dobles = not comillas_dobles
            nueva_linea += char
            i += 1
            continue

        if char == "#" and not comillas_simples and not comillas_dobles:
            break

        nueva_linea += char
        i += 1

    return nueva_linea.rstrip()  


def eliminar_comentarios(archivo: str) -> None:
    """
    Elimina comentarios y docstrings de un archivo python y genera uno nuevo con sufijo.

    Pre: recibe una cadena con el nombre del archivo a modificar.

    Post: no devuelve nada, crea una copia del archivo pero sin comentarios en el.
    """

    if not os.path.exists(archivo):
        raise FileNotFoundError("El archivo ingresado no existe.")

    if not archivo.endswith(".py"):
        raise ValueError("El archivo debe tener extension .py")

    salida = archivo.replace(".py", "_sin_comentarios.py")

    dentro_docstring = False
    delimitador_doc = ""

    with open(archivo, "rt", encoding="utf-8") as entrada, \
         open(salida, "wt", encoding="utf-8") as salida_archivo:

        for linea in entrada:
            if not dentro_docstring:
                if linea.strip().startswith(("'''", '"""')):
                    dentro_docstring = True
                    delimitador_doc = linea.strip()[:3]
                    continue 
            else:
                if delimitador_doc in linea:
                    dentro_docstring = False
                continue  

            linea_limpia = limpiar_linea_de_comentarios(linea)

            if linea_limpia.strip() != "":
                salida_archivo.write(linea_limpia + "\n")

    print(f"Archivo generado correctamente: {salida}")


def main():
    try:
        archivo = input("\nIngrese el nombre del archivo python a limpiar: ").strip()

        if archivo == "":
            raise ValueError("Debe ingresar un nombre de archivo.")

        eliminar_comentarios(archivo)

    except Exception as e:
        print(f"Error: {e}")


main()