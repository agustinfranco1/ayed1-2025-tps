"""
Ej 9: Resolver el siguiente problema utilizando funciones:
Un productor frutihortícola desea contabilizar sus cajones de naranjas según el peso 
para poder cargar los camiones de reparto. La empresa cuenta con N camiones, y 
cada uno puede transportar hasta media tonelada (500 kilogramos). En un cajón 
caben 100 naranjas con un peso de entre 200 y 300 gramos cada una. Si el peso 
de alguna naranja se encuentra fuera del rango indicado se la clasifica para 
procesar como jugo. Desarrollar un programa para ingresar la cantidad de naranjas 
cosechadas e informar cuántos cajones se pueden llenar, cuántas naranjas son para 
jugo y si hay algún sobrante de naranjas que deba considerarse para el siguiente 
reparto. Simular el peso de cada unidad generando un número entero al azar entre 
150 y 350.
Además, se desea saber cuántos camiones se necesitan para transportar la cose
cha, considerando que la ocupación del camión no debe ser inferior al 80%; en 
caso contrario el camión no serán despachado por su alto costo. 

"""
import random 
from typing import List

def generar_pesos(naranjas: int) -> List[int]:
    """
    Genera pesos aleatorios de naranjas entre 150 y 350 gramos.

    Pre: Recibe un entero correspondiente al numero de naranjas cosechadas.

    Post: Retorna una lista de enteros correspondientes a los pesos en gramos de las naranjas cosechadas.
    """
    return [random.randint(150, 350) for x in range(naranjas)]

def filtrar_aptas(naranjas: List[int]) -> List[int]:
    """
    Cuenta solo las naranjas aptas (200 a 300 gramos).

    Pre: Recibe una lista de enteros correspondientes al peso en gramos de las naranjas cosechadas.

    Post: Devuelve una lista de enteros correspondientes a los pesos en gramos de las naranjas 
          aptas.
    """
    return [n for n in naranjas if 200 <= n <= 300]

def contar_para_jugo(naranjas: List[int]) -> int:
    """
    Cuenta las naranjas que se destinan a jugo (las que no entren en el rango de aptas).

    Pre: Recibe una lista de enteros correspondientes al peso en gramos de las naranjas cosechadas.

    Post: Retorna un numero entero correspondiente a la cantidad de naranjas destinadas a jugo.
    """
    return sum(1 for n in naranjas if n < 200 or n > 300)

def formar_cajas(aptas: List[int]) -> List[int]:
    """
    Forma cajas de 100 naranjas.

    Pre: Recibe una lista de enteros correspondiente a los pesos de las naranjas aptas totales.

    Post: Devuelve una lista de enteros correspondientes a los pesos de cada caja formada en gramos.
    """
    cajas = []
    for i in range(len(aptas) // 100):
        caja = aptas[i*100:(i+1)*100]
        cajas.append(sum(caja))
    return cajas

def contar_sobrantes(aptas: List[int]) -> int:
    """
    Calcula la cantidad de naranjas aptas sobrantes que no llenan una caja.

    Pre: Recibe una lista de enteros correspondiente a los pesos de las naranjas aptas totales.

    Post: Devuelve un numero entero correspondiente a las naranjas aptas sobrantes.
    """
    return len(aptas) % 100

def calcular_camiones(cajas: List[int]) -> int:
    """
    Calcula cuántos camiones se pueden despachar.

    Pre: Recibe una lista de enteros correspondiente a las cajas llenas de naranjas aptas.

    Post: Devuelve un numero entero, la cantidad de camiones que se podran despachar.
    """
    capacidad = 500000     
    minimo = 400000        

    camiones = 0
    peso_actual = 0

    for peso_caja in cajas:
        if peso_actual + peso_caja <= capacidad:
            peso_actual += peso_caja
        else:
            if peso_actual >= minimo:
                camiones += 1
            peso_actual = peso_caja

    if peso_actual >= minimo:
        camiones += 1

    return camiones

def main():
    """
    Solicita datos al usuario e invoca otras funciones para realizar los calculos necesarios.

    Pre: No recibe parametros.

    Post: Imprime las naranjas para jugo, los cajones llenos, las naranjas aptas sobrantes
          y los camiones que se podran despachar.
    """
    naranjas = int(input("Ingrese la cantidad de naranjas cosechadas: "))
    pesos = generar_pesos(naranjas)

    aptas = filtrar_aptas(pesos)
    jugo = contar_para_jugo(pesos)
    cajas = formar_cajas(aptas)
    sobrantes = contar_sobrantes(aptas)
    camiones = calcular_camiones(cajas)

    print(f"\nNaranjas para jugo: {jugo}")
    print(f"Cajones llenos: {len(cajas)}")
    print(f"Naranjas sobrantes: {sobrantes}")
    print(f"Camiones despachados: {camiones}")

main()
