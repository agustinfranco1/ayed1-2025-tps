"""
Ej 2: Leer una cadena de caracteres e imprimirla centrada en pantalla. Suponer que la 
misma tiene 80 columnas.
"""
def centrar(texto: str) -> None:
    """
    Imprime una cadena de caracteres centrada en una pantalla de 80 columnas.

    Pre: recibe un string a acomodar.

    Post: No retorna nada, imprime la cadena ingresada de forma centrada considerando
          el ancho de pantalla establecido.
    """
    ancho = 80
    inicio = 0

    while inicio < len(texto):
        linea = texto[inicio:inicio + ancho]
        espacios = (ancho - len(linea)) // 2
        print(" " * espacios + linea)
        inicio += ancho


def main():
    texto = input("Ingrese una texto a centrar: ")
    centrar(texto)


main()