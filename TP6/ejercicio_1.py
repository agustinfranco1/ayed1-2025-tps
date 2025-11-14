"""
Ej 1: Escribir un programa que lea un archivo de texto conteniendo un conjunto de ape
llidos y nombres en formato "Apellido, Nombre" y guarde en el archivo 
ARMENIA.TXT los registros de aquellas personas cuyo apellido termina con la cade
na "IAN", en el archivo ITALIA.TXT los terminados en "INI" y en ESPAÑA.TXT los 
terminados en "EZ". Descartar el resto.
"""
import os

def terminacion_nombres(archivo_entrada: str) -> None:
    """
    Lee un archivo de texto con nombres y apellidos y los clasifica segun su terminacion.

    Pre: recibe un string con el nombre del archivo a evaluar, este debe tener al menos un 
         nombre completo valido en formato "Apellido, Nombre".

    Post: no devuelve nada, crea tres archivos (ARMENIA.TXT, ITALIA.TXT, ESPAÑA.TXT) 
          con los nombres completos correspondientes.
    """
    try:
        ruta_base = os.path.dirname(__file__)
        archivo_path = os.path.join(ruta_base, archivo_entrada)

        with open(archivo_path, "rt", encoding="utf-8") as f:
            lineas = f.readlines()

        archivos = {
            "IAN": open(os.path.join(ruta_base, "ARMENIA.TXT"), "wt", encoding="utf-8"),
            "INI": open(os.path.join(ruta_base, "ITALIA.TXT"), "wt", encoding="utf-8"),
            "EZ": open(os.path.join(ruta_base, "ESPAÑA.TXT"), "wt", encoding="utf-8")
        }

        for linea in lineas:
            linea = linea.strip()
            if not linea:
                continue
            apellido = linea.split(",")[0].strip().upper()

            if apellido.endswith("IAN"):
                archivos["IAN"].write(linea + "\n")
            elif apellido.endswith("INI"):
                archivos["INI"].write(linea + "\n")
            elif apellido.endswith("EZ"):
                archivos["EZ"].write(linea + "\n")

        print("Clasificacion completada correctamente.")

    except FileNotFoundError:
        print(f"Error: el archivo '{archivo_entrada}' no existe.")


def main():
    archivo_entrada = input("\nIngrese el nombre del archivo de texto: ").strip()
    terminacion_nombres(archivo_entrada)


main()