def mayor_estricto(a: int, b: int, c: int) -> int:
    """
    Evalua cual es el mayor estricto entre tres números enteros.
    Pre: 3 numeros enteros.
    Post: Devuelve el mayor estricto de los tres o -1 en caso de no haberlo.
    """
    numeros = [a, b, c]
    unicos = [x for x in numeros if numeros.count(x) == 1]  #Crea una lista con los elementos de la lista numeros que no se repiten
    
    if not unicos:
        return -1  
    
    return max(unicos) 

def validar_numeros_enteros(a: int, b: int, c: int) -> bool:
    """
    Evalua si los tres numeros ingresados son enteros positivos.
    
    Pre: 3 numeros enteros.

    Post: Devuelve False si algun numero no es un entero positivo y True si todos lo son.
    """
    for x in [a, b, c]:
        if x <= 0:
            return False
    return True

def main():
    """
    Solicita al usuario 3 numeros e invoca otras funciones para evaluarlos.

    Pre: No recibe parametros.

    Post: Imprime el mayor estricto o notifica que no lo hay.
    """
    a = int(input("Ingrese el primer número: "))
    b = int(input("Ingrese el segundo número: "))
    c = int(input("Ingrese el tercer número: "))

    mayor = mayor_estricto(a, b, c)

    if validar_numeros_enteros(a, b, c) == False:
        print("Error, alguno de los datos no fue ingresado correctamente, ingrese numeros enteros positivos")

    else:
        if mayor == -1:
            print("No existe un mayor estricto.")
        else:
            print(f"El mayor estricto es: {mayor}")

main()