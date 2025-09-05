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
