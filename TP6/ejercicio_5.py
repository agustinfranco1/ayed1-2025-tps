"""
Ej 5: Se dispone de dos formatos diferentes de archivos de texto en los que se almacenan 
datos de empleados, detallados más abajo. Desarrollar un programa para con
vertir cada uno de los formatos suministrados, grabando los datos obtenidos en 
otro archivo con formato CSV. Los archivos de entrada pueden generarse con Block 
de Notas o cualquier otro editor, copiando y pegando los ejemplos proporcionados. 
Ambos archivos tienen tres campos por registro: Apellido y Nombre, Fecha de alta 
y Domicilio
"""
import os
from typing import List

def detectar_formato(linea: str) -> int:
    """
    Determina el formato del archivo segun la estructura de la primera linea.

    Pre: recibe una cadena correspondiente a una linea del archivo.

    Post: devuelve 1 si es formato de campos fijos, o 2 si es formato con prefijos de longitud.
    """
    linea = linea.rstrip("\n")

    if len(linea) >= 2 and linea[:2].isdigit():
        return 2

    return 1


def procesar_formato_1(linea: str) -> List[str]:
    """
    Procesa una linea del formato 1 cuyos campos son de longitud fija con un espacio entre ellos.

    Pre: recibe una cadena correspondiente a una linea con: Apellido y Nombre | Fecha de alta | Domicilio.

    Post: devuelve una lista de cadenas con los 3 campos limpios de espacios vacios.
    """
    # Apellido y Nombre: posiciones 0-19 (20 chars)
    # Fecha: 21-28 (8 chars)
    # Domicilio: desde 30 en adelante
    apellido_nombre = linea[0:20].strip()
    fecha = linea[21:29].strip()
    domicilio = linea[30:].strip()

    return [apellido_nombre, fecha, domicilio]


def procesar_formato_2(linea: str) -> List[str]:
    """
    Procesa una linea del formato 2, donde cada campo esta precedido por un numero de dos digitos que indica 
    la longitud del siguiente campo.

    Pre: recibe una linea que debe tener prefijos de longitud validos.

    Post: devuelve una lista de cadenas con todos los campos encontrados.
    """
    idx = 0
    campos = []

    while idx < len(linea):
        if not linea[idx: idx + 2].isdigit():
            raise ValueError("Formato 2 invalido: prefijo no numerico encontrado.")

        longitud = int(linea[idx: idx + 2])
        idx += 2

        campo = linea[idx: idx + longitud]
        campos.append(campo.strip())

        idx += longitud

    return campos


def convertir_a_csv(nombre_archivo: str) -> None:
    """
    Convierte un archivo de datos de empleados (formato 1 o formato 2) a CSV.

    Pre: recibe una cadena con el nombre del archivo a evaluar, debe cumplir con alguno de los 
         formatos su contenido.

    Post: no devuelve nada, crea un archivo CSV con el nombre del archivo base.
    """
    try:
        ruta_base = os.path.dirname(__file__)
        archivo_path = os.path.join(ruta_base, nombre_archivo)

        if not os.path.exists(archivo_path):
            print(f"Error: el archivo '{nombre_archivo}' no existe.")
            return

        with open(archivo_path, "rt", encoding="utf-8") as f:
            primeras_lineas = f.readlines()

        if not primeras_lineas:
            print("Error: el archivo esta vacio.")
            return

        primera_linea_util = next((l for l in primeras_lineas if l.strip()), "")
        formato = detectar_formato(primera_linea_util)

        base, _ = os.path.splitext(nombre_archivo)
        csv_path = os.path.join(ruta_base, f"{base}.csv")

        with open(csv_path, "wt", encoding="utf-8") as salida:
            salida.write("Apellido y Nombre,Fecha,Domicilio\n") 

            for linea in primeras_lineas:
                linea = linea.rstrip("\n")
                if not linea.strip():
                    continue  

                if formato == 1:
                    campos = procesar_formato_1(linea)
                else:
                    campos = procesar_formato_2(linea)

                salida.write(",".join(campos) + "\n")

        print(f"Conversion exitosa. Archivo generado: {csv_path}")

    except ValueError as e:
        print(f"Error en el formato del archivo")


def main():
    nombre = input("Ingrese el nombre del archivo a convertir: ").strip()

    convertir_a_csv(nombre)


main()