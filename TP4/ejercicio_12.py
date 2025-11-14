"""
Ej 12: Escribir un programa para crear una lista por comprensión con los naipes de la ba
raja española. La lista debe contener cadenas de caracteres. Ejemplo: ["1 Oros", "2 
Oros"... ]. Imprimir la lista por pantalla. 
"""
def crear_baraja_espanola() -> list[str]:
    """
    Crea una lista con los naipes de la baraja española.

    Pre: no recibe parametros.

    Post: devuelve una lista de strings, correspondientes a los naipes españoles.
    """
    palos = ["Oros", "Copas", "Espadas", "Bastos"]
    numeros = [str(n) for n in range(1, 13)]
    baraja = [f"{numero} de {palo}" for palo in palos for numero in numeros]
    return baraja


def main():
    baraja = crear_baraja_espanola()
    for carta in baraja:
        print(carta)


main()