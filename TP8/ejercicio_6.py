"""
Ej 6: Ingresar una frase desde el teclado y usar un conjunto para eliminar las palabras 
repetidas, dejando un solo ejemplar de cada una. Finalmente mostrar las palabras 
ordenadas según su longitud. Los signos de puntuación no deben afectar el 
proceso.
"""
from typing import List

def ordenar_frase(frase: str) -> List[str]:
    """
    Ordena una frase de menor a mayor longitud evitando palabras repetidas.

    Pre: recibe un string con la frase a evaluar.

    Post: devuelve una lista de strings con las palabas de la frase ordenadas como se establecio.
    """
    try:
        if not frase:
            raise ValueError("La frase no puede estar vacia.")

        signos = ",.;:!?¡¿\"'()[]{}"
        palabras = frase.split()

        unicas = set()
        regsitro = []

        for palabra in palabras:
            limpia = palabra.lower()
            for s in signos:
                limpia = limpia.replace(s, "")

            if limpia and limpia not in unicas:
                unicas.add(limpia)
                regsitro.append(palabra)

        resultado = sorted(regsitro, key=lambda p: len(''.join(ch for ch in p if ch not in signos)))

        return resultado

    except Exception as e:
        print(f"Error: {e}")
        return []


def main():
    texto = input("\nIngrese una frase: ")
    resultado = ordenar_frase(texto)

    if resultado:
        print("\nPalabras unicas:")
        for palabra in resultado:
            print(palabra)


main()