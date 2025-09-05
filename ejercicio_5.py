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
