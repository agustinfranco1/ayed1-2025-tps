"""
Ej 3: Una persona desea llevar el control de los gastos realizados al viajar en el subte
rráneo dentro de un mes. Sabiendo que dicho medio de transporte utiliza un es
quema de tarifas decrecientes (detalladas en la tabla de abajo) se solicita desarro
llar una función que reciba como parámetro la cantidad de viajes realizados en un 
determinado mes y devuelva el total gastado en viajes. Realizar también un pro
grama para verificar el comportamiento de la función.
"""
def calcular_gasto_x_mes(cant_viajes: int) -> float:
    """
    Calcula el gasto total en subte en función de la cantidad de viajes ingresados.

    Pre: Cantidad de viajes realizados en el mes.

    Post: Devuelve el monto total gastado en la cantidad de dias ingresados.
    """
    tarifa = 1000
    total = 0 
    
    for viaje in range(1, cant_viajes + 1): 
        if viaje <= 20: precio = tarifa 

        elif viaje <= 30: precio = tarifa * 0.8 

        elif viaje <= 40: precio = tarifa * 0.7 

        else: precio = tarifa * 0.6 
        
        total += precio 
    
    return total



def main():
    """
    Solicita al usuario la cantidad de viajes realizados,
    e invoca otra funcion para calcular el monto total gastado y mostrarlo en pantalla.
    Pre: No recibe parametros.
    Post: Muestra el monto total en pantalla.
    """
    cant_viajes = int(input("Ingrese la cantidad de viajes en el mes: "))
    print(f"Ha gastado un total de ${calcular_gasto_x_mes(cant_viajes)} en viajes este mes")




main()
