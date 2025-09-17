"""
Ej 8: Utilizar la técnica de listas por comprensión para construir una lista con todos los 
números impares comprendidos entre 100 y 200.
"""
def main():
    impares = [n for n in range(101, 200, 2)]
    print("\nNúmeros impares entre 100 y 200:")
    print(f"\n{impares}")

main()