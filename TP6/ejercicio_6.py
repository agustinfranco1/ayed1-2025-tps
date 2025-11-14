"""
Ej 6:  Un hotel necesita un programa para gestionar la operación de sus habitaciones. El hotel 
cuenta con 10 pisos y 6 habitaciones por piso. Por cada huésped o grupo familiar que se aloja 
en el mismo se registra la siguiente información:
· DNI del cliente (número entero)
· Apellido y Nombre
· Fecha de ingreso (DDMMAAAA)
· Fecha de egreso  (DDMMAAAA)
· Cantidad de ocupantes
Se solicita desarrollar un programa para realizar las siguientes tareas:
· Registrar el ingreso de huéspedes al hotel, hasta que se ingrese un número de DNI -1. 
Esta información deberá grabarse en un archivo CSV donde cada registro incluirá todos 
los campos indicados más arriba. Tener en cuenta que los números de DNI no pueden 
repetirse y que la fecha de salida debe ser mayor a la de entrada.
· Finalizado el ingreso de huéspedes se solicita:
a. Leer el archivo de huéspedes y asignar la habitaciones a cada uno. El piso y 
habitación son asignados arbitrariamente, y no puede asignarse una habitación ya 
otorgada.
b. Mostrar el piso con mayor cantidad de habitaciones ocupadas.
c. Mostrar cuántas habitaciones vacías hay en todo el hotel.
d. Mostrar el piso con mayor cantidad de personas.
e. Mostrar cuál será la próxima habitación en desocuparse. La fecha actual se ingresa 
por teclado. Mostrar todas las que correspondan.
f. Mostrar un listado de todos los huéspedes registrados en el hotel, ordenado por 
cantidad de días de alojamiento.
"""
import csv
import os
from typing import List, Dict, Tuple
from datetime import datetime


def fecha_valida(fecha: str) -> bool:
    """
    Verifica si una fecha esta en formato DDMMAAAA.

    Pre: recibe un string correspondiente a una fecha de 8 digitos.

    Post: devuelve True si cumple el formato valido, o False en caso contrario.
    """
    try:
        datetime.strptime(fecha, "%d%m%Y")
        return True
    except ValueError:
        return False


def dias_entre(f1: str, f2: str) -> int:
    """
    Devuelve la diferencia en días entre dos fechas.

    Pre: recibe dos strings correspondientes a fechas en formato DDMMAAAA.

    Post: devuelve un entero correspondiente a la diferencia en dias.
    """
    d1 = datetime.strptime(f1, "%d%m%Y")
    d2 = datetime.strptime(f2, "%d%m%Y")
    return (d2 - d1).days


def registrar_huespedes(nombre_csv: str) -> None:
    """
    Registra huespedes ingresados por teclado y los almacena en un archivo CSV.

    Pre: recibe una cadena correspondiente al nombre del archivo CSV destino.

    Post: no devuelve nada, crea el CSV con todos los huespedes ingresados.
    """
    ruta = os.path.join(os.path.dirname(__file__), nombre_csv)

    dnis_registrados = set()

    print("Ingrese DNI, -1 para finalizar.")

    with open(ruta, "wt", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["DNI", "Nombre", "Ingreso", "Egreso", "Ocupantes"])

        while True:
            try:
                dni = int(input("DNI: "))
                if dni == -1:
                    break
                if dni <= 0:
                    print("DNI invalido.")
                    continue
                if dni in dnis_registrados:
                    print("Ese DNI ya fue registrado.")
                    continue

                nombre = input("Apellido y Nombre: ").strip()
                ingreso = input("Fecha ingreso (DDMMAAAA): ").strip()
                egreso = input("Fecha egreso  (DDMMAAAA): ").strip()

                if not fecha_valida(ingreso) or not fecha_valida(egreso):
                    print("Alguna fecha no es valida.")
                    continue
                if dias_entre(ingreso, egreso) <= 0:
                    print("La fecha de egreso debe ser posterior al ingreso.")
                    continue

                ocupantes = int(input("Cantidad de ocupantes: "))
                if ocupantes <= 0:
                    print("Debe haber al menos 1 ocupante.")
                    continue

                writer.writerow([dni, nombre, ingreso, egreso, ocupantes])
                dnis_registrados.add(dni)

            except ValueError:
                print("Error: Ingrese valores validos.")

    print("Registro finalizado. Archivo generado:", nombre_csv)


def asignar_habitaciones(huespedes: List[List[str]]) -> Dict[str, Tuple[int]]:
    """
    Asigna habitaciones automaticamente a los huespedes.

    Pre: huespedes debe ser una lista con registros del archivo CSV.

    Post: devuelve un diccionario: {DNI: (piso, hab)}
    """
    asignaciones = {}
    hab_usadas = set()

    for registro in huespedes:
        dni = registro[0]

        for piso in range(1, 11):        
            for hab in range(1, 7):     
                if (piso, hab) not in hab_usadas:
                    hab_usadas.add((piso, hab))
                    asignaciones[dni] = (piso, hab)
                    break
            if dni in asignaciones:
                break

    return asignaciones


def piso_mas_ocupado(asignaciones: Dict[str, Tuple[int]]) -> int:
    """
    Devuelve el piso con mayor cantidad de habitaciones ocupadas.

    Pre: asignaciones debe contener al menos 1 huesped.

    Post: devuelve un entero entre 1 y 10 segun el piso que tenga mas habitaciones ocupadas.
    """
    conteo = [0] * 11
    for piso, _ in asignaciones.values():
        conteo[piso] += 1
    return conteo.index(max(conteo))


def habitaciones_vacias(asignaciones: Dict[str, Tuple[int]]) -> int:
    """
    Devuelve cuantas habitaciones vacias quedan en el hotel.

    Pre: asignaciones puede estar vacio.

    Post: devuelve entero entre 0 y 60 segun la cantidad de habitaciones libres.
    """
    return 60 - len(asignaciones)


def piso_con_mas_personas(huespedes: List[List[str]], asignaciones: Dict[str, Tuple[int]]) -> int:
    """
    Devuelve el piso con mayor cantidad de personas.

    Pre: tanto huespedes como asignaciones deben corresponder al mismo CSV.

    Post: devuelve entero entre 1 y 10 segun el piso que tenga mayor cantidad de huespedes.
    """
    personas_por_piso = [0] * 11

    for registro in huespedes:
        dni, _, _, _, ocupantes = registro
        piso, _ = asignaciones[dni]
        personas_por_piso[piso] += int(ocupantes)

    return personas_por_piso.index(max(personas_por_piso))


def proximas_a_desocuparse(huespedes: List[List[str]], asignaciones: Dict[str, Tuple[int]], fecha_actual: str) -> List[Tuple[int, str]]:
    """
    Genera una lista de proximas habitaciones a desocuparse en orden cronologico.

    Pre: fecha_actual debe estar en formato valido y tanto huespedes como asignaciones deben tener contenido.

    Post: devuelve lista de tuplas correspondientes al piso, hab, fecha egreso.
    """
    resultado = []
    for dni, (piso, hab) in asignaciones.items():
        for reg in huespedes:
            if reg[0] == dni:
                egreso = reg[3]
                if egreso >= fecha_actual:
                    resultado.append((piso, hab, egreso))
    resultado.sort(key=lambda x: x[2])
    return resultado


def ordenar_por_dias(huespedes: List[List[str]]) -> List[Tuple[str, int]]:
    """
    Ordena huespedes por cantidad de dias de alojamiento en orden descendiente.

    Pre: huespedes debe contener registros validos.

    Post: devuelve lista [(Nombre, dias)]
    """
    lista = []
    for registro in huespedes:
        nombre = registro[1]
        dias = dias_entre(registro[2], registro[3])
        lista.append((nombre, dias))

    return sorted(lista, key=lambda x: x[1], reverse=True)


def main():
    nombre_csv = "huespedes.csv"
    ruta = os.path.join(os.path.dirname(__file__), nombre_csv)

    while True:
        print("1. Registrar huespedes")
        print("2. Procesar y mostrar informes")
        print("3. Salir")

        try:
            opcion = int(input("Opción: "))

            if opcion == 1:
                registrar_huespedes(nombre_csv)

            elif opcion == 2:
                if not os.path.exists(ruta):
                    print("Primero debe registrar huespedes.")
                    continue

                with open(ruta, "rt", encoding="utf-8") as f:
                    reader = csv.reader(f)
                    next(reader)
                    huespedes = list(reader)

                asignaciones = asignar_habitaciones(huespedes)

                print("\na) Piso mas ocupado:", piso_mas_ocupado(asignaciones))
                print("b) Habitaciones vacias:", habitaciones_vacias(asignaciones))
                print("c) Piso con mas personas:",
                      piso_con_mas_personas(huespedes, asignaciones))

                fecha_actual = input("Ingrese fecha actual (DDMMAAAA): ").strip()
                if not fecha_valida(fecha_actual):
                    print("Fecha invalida.")
                else:
                    print("\nd) Proximas habitaciones en desocuparse:")
                    for piso, hab, egreso in proximas_a_desocuparse(
                            huespedes, asignaciones, fecha_actual):
                        print(f"  Piso {piso}, Hab {hab}, Egreso: {egreso}")

                print("\ne) Listado por dias de alojamiento:")
                for nombre, dias in ordenar_por_dias(huespedes):
                    print(f"  {nombre}: {dias} dias")

            elif opcion == 3:
                print("Saliendo...")
                break

            else:
                print("Opcion invalida.")

        except ValueError:
            print("Error: ingrese un numero valido.")


main()