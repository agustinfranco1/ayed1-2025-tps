"""
Ej 7: Intercalar los elementos de una lista entre los elementos de otra. La intercalación 
deberá realizarse exclusivamente mediante la técnica de rebanadas y no se creará 
una lista nueva sino que se modificará la primera. Por ejemplo, si lista1 = [8, 1, 3] 
y lista2 = [5, 9, 7], lista1 deberá quedar como [8, 5, 1, 9, 3, 7]. Las listas pueden 
tener distintas longitudes.

"""
from typing import List

def intercalar(lista1: List[int], lista2: List[int]) -> None:
    """
    Intercala los elementos de dos listas de enteros modificando la primera.

    Pre: Recibe dos listas de enteros, de las cuales se modificara la primera.

    Post: No retorna nada, modifica la primera lista recibida.
    """
    for i, elem in enumerate(lista2):
        pos = 2 * i + 1  # índice donde va a insertarse
        if pos > len(lista1):
            lista1.append(elem)   # si el índice se pasa, agrego al final
        else:
            lista1.insert(pos, elem)


def main():
    lista1 = [8, 1, 3]
    lista2 = [5, 9, 7, 75, 103, 756]

    print(f"Primera lista original: {lista1}")
    print(f"Segunda lista: {lista2}")
    intercalar(lista1, lista2)
    print(f"Lista1 intercalada: {lista1}")


main()
