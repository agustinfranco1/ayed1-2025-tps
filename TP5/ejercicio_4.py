"""
Ej 4: Todo programa Python es susceptible de ser interrumpido mediante la pulsación de 
las teclas Ctrl-C, lo que genera una excepción del tipo KeyboardInterrupt. Realizar 
un programa para imprimir los números enteros entre 1 y 100000, y que solicite 
confirmación al usuario antes de detenerse cuando se presione Ctrl-C.
"""
def imprimir_numeros() -> None:
    """
    Imprime numeros enteros de 1 hasta 100000, con opcion de interrumpir si el usuario lo desea.

    Pre: no recibe parametros.

    Post: no devuelve nada, pero imprime los numeros enteros del 1 al 100000 a no ser que se vea interrumpido.
    """
    try:
        for i in range(1, 100001):
            print(i)
    except KeyboardInterrupt:
        respuesta = input("\nDesea detener el programa? (s/n): ")
        if respuesta == "s":
            print("\nPrograma finalizado.")
            return
        else:
            imprimir_numeros() 


imprimir_numeros()