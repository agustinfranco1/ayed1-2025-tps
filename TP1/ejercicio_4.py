"""
Ej 4: Un comercio de electrodomésticos necesita para su línea de cajas un programa que 
le indique al cajero el cambio que debe entregarle al cliente. Para eso se ingresan 
dos números enteros, correspondientes al total de la compra y al dinero recibido. 
Informar cuántos billetes de cada denominación deben ser entregados como vuelto, 
de tal forma que se minimice la cantidad de billetes. Considerar que existen billetes 
de $5000, $1000, $500, $200, $100, $50 y $10. Emitir un mensaje de error si el 
dinero recibido fuera insuficiente o si el cambio no pudiera entregarse debido a falta 
de billetes con denominaciones adecuadas. Ejemplo: Si la compra es de $3170 y se 
abona con $5000, el vuelto debe contener 1 billete de $1000, 1 billete de $500, 1 
billete de $200, 1 billete de $100 y 3 billetes de $10.
"""
from typing import List

def calcular_vuelto(total: int, recibido: int) -> List[int]:
    """
    Calcula el vuelto en billetes con las denominaciones disponibles.
    
    Pre: 2 numeros enteros, el total de la compra y el dinero recibido.

    Post: Devuelve una lista con la cantidad de billletes a dar por denominacion en orden decreciente
          o una lista vacia en caso de que o el dinero recibido sea insuficiente o no se pueda dar vuelto 
          con las denominaciones existentes, junto con un mensaje.
    """
    billetes = [5000, 1000, 500, 200, 100, 50, 10]
    resultado = []

    vuelto = recibido - total

    if vuelto < 0:
        print("Error: Dinero insuficiente.")
        return []
    if vuelto % 10 != 0:
        print("Error: No se puede entregar vuelto exacto con estas denominaciones.")
        return []

    for b in billetes:
        cantidad = vuelto // b
        resultado.append(cantidad)
        vuelto = vuelto % b

    return resultado


def main():
    """
    Solicita el total de la compra y el dinero recibido e invoca otra funcion para calcular el vuelto.

    Pre: No recibe parametros.

    Post: Imprime la cantidad de billetes a dar por cada denominacion en caso de pasar la validacion.
    """
    total = int(input("Ingrese el total de la compra: "))
    recibido = int(input("Ingrese el dinero recibido: "))

    vuelto = calcular_vuelto(total, recibido)

    if vuelto:  
        billetes = [5000, 1000, 500, 200, 100, 50, 10]
        print("Vuelto en billetes:")
        for i in range(len(billetes)):
            if vuelto[i] > 0:
                print(f"{vuelto[i]} billete(s) de ${billetes[i]}")



main()
