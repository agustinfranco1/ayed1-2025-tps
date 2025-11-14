"""
Ej 12: Una librería almacena su lista de precios en un diccionario. Diseñar un programa 
para crearlo, incrementar los precios de los cuadernos en un 15%, imprimir un 
listado con todos los elementos de la lista de precios e indicar cuál es el ítem más 
costoso que venden en el comercio
"""
from typing import Dict, Tuple

def incrementar_valores(diccionario: Dict[str, float], incremento: float) -> Dict[str, float]:
    """
    Incrementa el valor asociado a los cuadernos en un porcentaje dado.

    Pre: recibe un diccionario de claves string y valores flotantes.

    Post: devuelve un diccionario con los valores de las claves que contengan 
          la palabra "cuaderno" actualizados.
    """
    try:
        if incremento < 0:
            raise ValueError("El incremento no puede ser negativo.")

        precios_actualizados = {}
        for articulo, precio in diccionario.items():
            if "cuaderno" in articulo.lower():
                precios_actualizados[articulo] = round(precio * (1 + incremento / 100), 2)
            else:
                precios_actualizados[articulo] = precio

        return precios_actualizados

    except Exception as e:
        print(f"Error al actualizar los precios: {e}")
        return diccionario


def articulo_mas_costoso(diccionario: Dict[str, float]) -> Tuple[str, float]:
    """
    Determina la clave con el valor mas alto en un diccionario.

    Pre: recibe un diccionario de claves string y valores float.

    Post: devuelve una tupla con un string y un float correspondientes al elemento del 
          diccionario recibido con el valor con el numero flotante mas grande.
    """
    try:
        if not diccionario:
            raise ValueError("La lista de precios esta vacia.")
        return max(diccionario.items(), key=lambda x: x[1])
    except Exception as e:
        print(f"Error al buscar el articulo mas costoso: {e}")
        return ("", 0.0)


def main():
    try:
        lista_precios = {}
        try:
            cantidad = int(input("\nCuantos articulos desea ingresar?: "))
            if cantidad <= 0:
                raise ValueError

            for i in range(cantidad):
                nombre = input(f"\nIngrese el nombre del articulo {i + 1}: ").strip()
                if not nombre:
                    raise ValueError
                precio = float(input(f"Ingrese el precio de '{nombre}': "))
                if precio <= 0:
                    raise ValueError
                lista_precios[nombre] = precio

        except ValueError:
            print("Error: tanto la cantidad de articulos como el precio deben ser numeros positivos y el nombre no puede estar vacio.")
            return

        lista_actualizada = incrementar_valores(lista_precios, 15)

        print("\nLista de precios actualizada:")
        for articulo, precio in lista_actualizada.items():
            print(f"{articulo}: ${precio:.2f}")

        mas_caro = articulo_mas_costoso(lista_actualizada)
        if mas_caro[1] != 0:
            print(f"\nEl articulo mas costoso es '{mas_caro[0]}': ${mas_caro[1]:.2f}")

    except Exception as e:
        print(f"Error: {e}")


main()