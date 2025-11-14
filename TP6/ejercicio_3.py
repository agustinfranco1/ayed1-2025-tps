"""
Ej 3: Una institución deportiva necesita clasificar a sus atletas para inscribirlos en los 
próximos Juegos Panamericanos. Para eso encargó la realización de un programa 
que incluya las siguientes funciones:
GrabarRangoAlturas(): Graba en un archivo las alturas de los atletas de distintas 
disciplinas, los que se ingresan desde el teclado. Cada dato se debe grabar en una 
línea distinta. Ejemplo:
 <Deporte 1>
 <altura del atleta 1>
 <altura del atleta 2>
 < . . . >
 <Deporte 2>
 <altura del atleta 1>
 <altura del atleta 2>
 < . . . >
 GrabarPromedio(): Graba en un archivo los promedios de las alturas de los atle
tas, leyendo los datos del archivo generado en el paso anterior. La disciplina y el 
promedio deben grabarse en líneas diferentes. Ejemplo:
 <Deporte 1>
 <Promedio de alturas deporte 1>
 <Deporte 2>
 <Promedio de alturas deporte 2>
 < . . . >
 MostrarMasAltos() Muestra por pantalla las disciplinas deportivas cuyos atletas 
superan la estatura promedio general. Obtener los datos del segundo archivo.
"""
import os
from typing import Optional, List, Tuple


def GrabarRangoAlturas(nombre_archivo: str) -> None:
    """
    Graba en un archivo las alturas de atletas por disciplina.

    Pre: recibe el nombre del archivo donde se guardaran los datos.

    Post: no devuelve nada. Crea un archivo con deportes y las alturas de los atletas correspondientes.
    """
    ruta_base = os.path.dirname(__file__)
    archivo_path = os.path.join(ruta_base, nombre_archivo)

    print("\nCarga de alturas de atletas")

    with open(archivo_path, "wt", encoding="utf-8") as f:
        while True:
            deporte = input("\nNombre del deporte: ").strip()
            if deporte == "":
                break
            f.write(deporte + "\n")

            while True:
                entrada = input(f"Ingrese altura de un atleta de '{deporte}' (Enter para terminar este deporte): ").strip()
                if entrada == "":
                    break
                try:
                    altura = float(entrada)
                    if altura <= 0:
                        print("Error: la altura debe ser un numero positivo. Reintente.")
                        continue
                    f.write(str(altura) + "\n")
                except ValueError:
                    print("Error: valor invalido. Ingrese un numero valido para la altura.")
    print(f"\nCarga finalizada. Archivo guardado como: {nombre_archivo}\n")


def GrabarPromedio(nombre_archivo_alturas: str, nombre_archivo_promedios: str) -> None:
    """
    Lee el archivo de alturas y graba los promedios por disciplina en otro archivo.

    Pre: recibe el nombre del archivo de alturas y el nombre del archivo de salida de promedios.

    Post: no devuelve nada, crea el archivo de promedios con pares de deporte y el 
          promedio de altura de sus atletas.
    """
    ruta_base = os.path.dirname(__file__)
    path_alturas = os.path.join(ruta_base, nombre_archivo_alturas)
    path_promedios = os.path.join(ruta_base, nombre_archivo_promedios)

    if not os.path.exists(path_alturas):
        print(f"Error: no existe '{nombre_archivo_alturas}'.")
        return

    with open(path_alturas, "rt", encoding="utf-8") as fin, \
        open(path_promedios, "wt", encoding="utf-8") as prom:

        deporte_actual: Optional[str] = None
        suma = 0.0
        contador = 0

        for linea in fin:
            linea = linea.strip()
            if linea == "":
                continue

            try:
                altura = float(linea)
                suma += altura
                contador += 1
            except ValueError:
                if deporte_actual is not None and contador > 0:
                    promedio = suma / contador
                    prom.write(deporte_actual + "\n")
                    prom.write(f"{promedio:.2f}\n")
                deporte_actual = linea
                suma = 0.0
                contador = 0

        if deporte_actual is not None and contador > 0:
            promedio = suma / contador
            prom.write(deporte_actual + "\n")
            prom.write(f"{promedio:.2f}\n")

    print(f"\nArchivo de promedios generado: {nombre_archivo_promedios}\n")


def MostrarMasAltos(nombre_archivo_promedios: str) -> None:
    """
    Muestra las disciplinas con promedio superior al promedio general.

    Pre: recibe el nombre del archivo de promedios.

    Post: no devuelve nada, imprime por pantalla las disciplinas cuyo promedio es mayor que el promedio general.
    """
    ruta_base = os.path.dirname(__file__)
    path_promedios = os.path.join(ruta_base, nombre_archivo_promedios)

    if not os.path.exists(path_promedios):
        print(f"Error: no existe '{nombre_archivo_promedios}'. Ejecute primero la generación de promedios.")
        return


    disciplinas: List[Tuple[str, float]] = []
    with open(path_promedios, "rt", encoding="utf-8") as f:
        while True:
            deporte = f.readline()
            if not deporte:
                break
            deporte = deporte.strip()
            promedio_line = f.readline()
            if not promedio_line:
                print(f"Advertencia: formato invalido en '{nombre_archivo_promedios}'.")
                break
            try:
                promedio = float(promedio_line.strip())
            except ValueError:
                print(f"Advertencia: valor numarico invalido para el promedio de {deporte}. Se omite.")
                continue
            disciplinas.append((deporte, promedio))

    if not disciplinas:
        print("El archivo de promedios esta vacio o no contiene datos validos.")
        return

    promedio_general = sum(p for _, p in disciplinas) / len(disciplinas)

    print("\nDisciplinas con promedio superior al general")
    print(f"Promedio general de alturas: {promedio_general:.2f}\n")
    encontradas = False
    for deporte, prom in disciplinas:
        if prom > promedio_general:
            print(f"{deporte}: {prom:.2f}")
            encontradas = True
    if not encontradas:
        print("Ninguna disciplina supera el promedio general.")
    print()


def main() -> None:
    archivo_alturas = "alturas.txt"
    archivo_promedios = "promedios.txt"

    while True:
        print("1. Grabar rango de alturas")
        print("2. Grabar promedios")
        print("3. Mostrar disciplinas con promedio superior al general")
        print("4. Salir")

        opcion = input("Seleccione una opcion (1-4): ").strip()
        if opcion == "1":
            nombre = input(f"Ingrese el nombre de archivo para guardar alturas [{archivo_alturas}]: ").strip()
            if nombre != "":
                archivo_alturas = nombre
            GrabarRangoAlturas(archivo_alturas)
        elif opcion == "2":
            nombre_in = input(f"Ingrese el nombre del archivo de alturas a leer [{archivo_alturas}]: ").strip()
            if nombre_in != "":
                archivo_alturas = nombre_in
            nombre_out = input(f"Ingrese el nombre del archivo de promedios a crear [{archivo_promedios}]: ").strip()
            if nombre_out != "":
                archivo_promedios = nombre_out
            GrabarPromedio(archivo_alturas, archivo_promedios)
        elif opcion == "3":
            nombre_prom = input(f"Ingrese el nombre del archivo de promedios a leer [{archivo_promedios}]: ").strip()
            if nombre_prom != "":
                archivo_promedios = nombre_prom
            MostrarMasAltos(archivo_promedios)
        elif opcion == "4":
            print("Saliendo...")
            break
        else:
            print("Opcion invalida. Ingrese un numero entre 1 y 4.")


main()