"""
Ej 13: Muchas aplicaciones financieras requieren que los números sean expresados tam
bién en letras. Por ejemplo, el número 2153 puede escribirse como "dos mil ciento 
cincuenta y tres". Escribir un programa que utilice una función para convertir un 
número entero entre 0 y 1 billón (1.000.000.000.000) a letras.
"""
def numero_a_letras(numero: int) -> str:
    """
    Convierte un numero entero entre 0 y 1 billon a letras.

    Pre: recibe un numero entero entre 0 y 1.000.000.000.000.

    Post: retorna un string con el numero expresado en palabras.
    """
    if numero < 0 or numero > 1_000_000_000_000:
        return "Numero fuera de rango"

    unidades = ["", "uno", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho", "nueve"]

    especiales = ["diez", "once", "doce", "trece", "catorce", "quince", "dieciseis", "diecisiete", 
                  "dieciocho", "diecinueve"]
    
    decenas = ["", "diez", "veinte", "treinta", "cuarenta", "cincuenta", "sesenta", "setenta", "ochenta", 
               "noventa"]
    
    centenas = ["", "ciento", "doscientos", "trescientos", "cuatrocientos", "quinientos", "seiscientos", 
                "setecientos", "ochocientos", "novecientos"]

    def convertir_a_menor_mil(n: int) -> str:
        """
        Convierte un numero de 3 digitos en palabras.

        Pre: Recibe un numero entero de 0 a 999.

        Post: Retorna un string correspondiente al numero recibido en palabras.
        """
        cen, dec, uni = n // 100, (n % 100) // 10, n % 10
        texto = ""

        # Centenas
        if cen == 1 and (dec == 0 and uni == 0):
            texto += "cien"
        elif cen > 0:
            texto += centenas[cen]

        # Decenas y unidades
        if dec == 1:
            texto += " " + especiales[uni] if texto else especiales[uni]
        elif dec == 2:
            if uni == 0:
                texto += " veinte" if texto else "veinte"
            else:
                texto += " veinti" + unidades[uni] if texto else "veinti" + unidades[uni]
        elif dec > 2:
            if uni == 0:
                texto += " " + decenas[dec] if texto else decenas[dec]
            else:
                texto += " " + decenas[dec] + " y " + unidades[uni] if texto else decenas[dec] + " y " + unidades[uni]
        elif dec == 0 and uni > 0:
            texto += " " + unidades[uni] if texto else unidades[uni]

        return texto.strip()

    if numero == 0:
        return "cero"

    partes = []
    grupos = [
        (1_000_000_000_000, "billon", "billon"),
        (1_000_000_000, "mil millones", "mil millones"),
        (1_000_000, "millon", "millones"),
        (1000, "mil", "mil"),
        (1, "", "")
    ]

    for valor, singular, plural in grupos:
        cantidad = numero // valor
        numero %= valor

        if cantidad == 0:
            continue

        if valor == 1:
            partes.append(convertir_a_menor_mil(cantidad))
        elif valor == 1000:
            if cantidad == 1:
                partes.append("mil")
            else:
                partes.append(f"{convertir_a_menor_mil(cantidad)} mil")
        elif valor == 1_000_000:
            if cantidad == 1:
                partes.append("un millon")
            else:
                partes.append(f"{convertir_a_menor_mil(cantidad)} millones")
        elif valor == 1_000_000_000:
            if cantidad == 1:
                partes.append("mil millones")
            else:
                partes.append(f"{convertir_a_menor_mil(cantidad)} mil millones")
        elif valor == 1_000_000_000_000:
            if cantidad == 1:
                partes.append("un billon")
            else:
                partes.append(f"{convertir_a_menor_mil(cantidad)} billones")

    return " ".join(partes).strip()


def main():
    numero = int(input("Ingrese un numero entre 0 y 1 billon: "))
    texto = numero_a_letras(numero)
    print(f"{numero} en letras es: {texto}")


main()