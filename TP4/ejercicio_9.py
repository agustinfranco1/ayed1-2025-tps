"""
Ej 9: Escribir una función que reciba como parámetro una cadena de caracteres en la que 
las palabras se encuentran separadas por uno o más espacios. Devolver otra 
cadena con las palabras ordenadas según su longitud, dejando un espacio entre 
cada una. Los signos de puntuación no deben ser tenidos en cuenta al medir la 
longitud de las palabras, pero deberán conservarse en la cadena final.
"""
def ordenar_x_longitud(frase: str) -> str:
    """
    Ordena las palabras de una frase segun su longitud, ignorando signos de puntuacion
    para el conteo pero conservandolos en el resultado final.

    Pre: recibe un string correspondiente a una frase con al menos un espacio entre dos palabras.

    Post: devuelve un nuevo string con las palabras ordenadas por longitud.
    """
    signos = ".,;:!¡¿?\"'()[]{}"

    palabras = frase.split()

    palabras_limpias = []
    for palabra in palabras:
        palabra_sin_signos = "".join([c for c in palabra if c not in signos])
        palabras_limpias.append((palabra, len(palabra_sin_signos)))

    palabras_ordenadas = sorted(palabras_limpias, key=lambda x: x[1]) # Ordena segun la longitud sin signos

    resultado = " ".join([p[0] for p in palabras_ordenadas])  # Reconstruye la frase con las palabras originales

    return resultado


def main():
    frase = input("Ingrese una frase: ")
    print(f"\nFrase ordenada por longitud: \n{ordenar_x_longitud(frase)}")


main()