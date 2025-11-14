"""
Ej 2: Escribir un programa que permita dividir un archivo de texto cualquiera en partes 
que se puedan enviar por correo electrónico. El tamaño máximo de las partes se 
ingresa por teclado. Los nombres de los archivos generados deben respetar el 
nombre original con el agregado de un sufijo que indique de qué parte se trata. 
Tener en cuenta que ningún registro puede ser dividido; la partición debe efectuarse 
después del delimitador del mismo. Mostrar un mensaje de error si el proceso no 
pudiera llevarse a cabo. Recordar que no se permite cargar el archivo completo en 
memoria.
"""
import os

def dividir_por_palabras(nombre_archivo: str, max_palabras: int) -> None:
    """
    Divide un archivo de texto en partes, cada una con una cantidad maxima de palabras.

    Pre: recibe un string con el nombre del archivo a evaluar y un numero entero correspondiente 
         al limite de palabras maximas por parte.

    Post: no devuelve nada, crea archivos con el mismo nombre del archivo base y un sufijo.
    """
    try:
        ruta_base = os.path.dirname(__file__)
        archivo_path = os.path.join(ruta_base, nombre_archivo)

        if not os.path.exists(archivo_path):
            print(f"Error: el archivo '{nombre_archivo}' no existe.")
            return

        if max_palabras <= 0:
            print("Error: la cantidad maxima de palabras debe ser mayor que cero.")
            return

        base, ext = os.path.splitext(nombre_archivo)
        parte_num = 1
        contador_palabras = 0

        with open(archivo_path, "rt", encoding="utf-8") as entrada:
            salida_path = os.path.join(ruta_base, f"{base}_parte{parte_num}{ext}")
            salida = open(salida_path, "wt", encoding="utf-8")

            for linea in entrada:
                palabras = linea.split()
                for palabra in palabras:
                    if contador_palabras >= max_palabras:
                        salida.close()
                        parte_num += 1
                        salida_path = os.path.join(ruta_base, f"{base}_parte{parte_num}{ext}")
                        salida = open(salida_path, "wt", encoding="utf-8")
                        contador_palabras = 0

                    salida.write(palabra + " ")
                    contador_palabras += 1

            salida.close()

        print(f"Archivo dividido correctamente en {parte_num} parte/s.")

    except FileNotFoundError:
        print(f"Error: el archivo '{nombre_archivo}' no fue encontrado.")
    except ValueError:
        print("Error: el numero maximo de palabras debe ser un entero valido.")


def main():
    nombre = input("\nIngrese el nombre del archivo de texto: ")
    try:
        max_palabras = int(input("\nIngrese la cantidad maxima de palabras por archivo: "))
        dividir_por_palabras(nombre, max_palabras)
    except ValueError:
        print("Error: debe ingresar un numero entero para la cantidad maxima de palabras.")

main()