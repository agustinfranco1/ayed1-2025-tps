"""
Ej 7: Definir un conjunto con números enteros entre 0 y 9. Luego solicitar valores al 
usuario y eliminarlos del conjunto mediante el método remove, mostrando el con
tenido del conjunto luego de cada eliminación. Finalizar el proceso al ingresar -1. 
Utilizar manejo de excepciones para evitar errores al intentar quitar elementos 
inexistentes.
"""
def eliminar_numeros() -> None:
    """
    Permite eliminar numeros de un conjunto del 0 al 9 por teclado.

    Pre: no recibe parametros.

    Post: no devuelve nada pero solicita valores a eliminar al usuario e 
          imprime el conjunto tras cada eliminacion hasta que el usuario ingrese -1.
    """
    numeros = set(range(10))
    print(f"\nConjunto inicial: {numeros}")

    while True:
        try:
            valor = int(input("\nIngrese un numero para eliminar (-1 para salir): "))

            if valor == -1:
                print("\nPrograma finalizado..")
                break

            numeros.remove(valor)
            print(f"Se elimino {valor}. Conjunto actual: {numeros}")

        except ValueError:
            print("Error: Debe ingresar un numero entero valido.")
        except KeyError:
            print("Error: El numero no se encuentra en el conjunto.")


eliminar_numeros()