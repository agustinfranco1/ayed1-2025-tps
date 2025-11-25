"""
Ej 4: Desarrollar una función que devuelva el producto de dos números enteros por sumas sucesivas.
"""
def producto_por_sumas(a: int, b: int) -> int:
    """
    Calcula el producto de dos numeros enteros.

    Pre: recibe dos numeros enteros cuyo producto se va a calcular.

    Post: devuelve un numero entero correspondiente al producto de los numeros recibidos.
    """
    try:
        if a == 0 or b == 0:
            return 0
        
        if b < 0:
            return -producto_por_sumas(a, -b)

        # caso base
        if b == 1:
            return a
        
        return a + producto_por_sumas(a, b - 1)

    except (TypeError, ValueError):
        print("Error: Debe ingresar valores enteros validos.")
        return 0

def main():
    try:
        a = int(input("\nIngrese el primer numero entero: "))
        b = int(input("\nIngrese el segundo numero entero: "))

        resultado = producto_por_sumas(a, b)
        print(f"\nEl producto de {a} y {b} es: {resultado}")

    except ValueError:
        print("Error: Debe ingresar valores enteros validos.")


main()