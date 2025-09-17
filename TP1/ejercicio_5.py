"""
Ej 5: Escribir funciones lambda para:
a. Informar si un número es oblongo. Se dice que un número es oblongo cuando 
se puede obtener multiplicando dos números naturales consecutivos. Por ejem
plo 6 es oblongo porque resulta de multiplicar 2 * 3.
b. Informar si un número es triangular. Un número se define como triangular si 
puede expresarse como la suma de un grupo de números naturales consecuti
vos comenzando desde 1. Por ejemplo 10 es un número triangular porque se 
obtiene sumando 1+2+3+4.
Ambas funciones lambda reciben como único parámetro el número a evaluar y de
vuelven True o False. No se permite utilizar ayudas externas a las mismas.
"""
def main():
    es_oblongo = lambda n: ((-1 + (1 + 4*n)**0.5) / 2) == ((-1 + (1 + 4*n)**0.5) // 2)

    es_triangular = lambda n: ((-1 + (1 + 8*n)**0.5) / 2) == ((-1 + (1 + 8*n)**0.5) // 2)

    numero = int(input("Ingrese un número: "))
    
    if numero <= 0:
        print("Valor invalido, ingrese numeros enteros")
        return 

    print(f"¿Es oblongo? {es_oblongo(numero)}")
    print(f"¿Es triangular? {es_triangular(numero)}")



main()
