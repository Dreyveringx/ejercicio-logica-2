'''
Realizar un programa que pida un número y determine si ese número es par o impar.
Mostrar en pantalla un mensaje que indique si el número es par o impar. (para que un
número sea par, se debe dividir entre dos y su resto debe ser igual a 0). Nota: USAR el
operador mod de Python.
'''

def es_par(numero):
    # Verificar si el número es par usando el operador módulo (%)
    # Si el residuo de dividir el número entre 2 es cero, entonces es par
    return numero % 2 == 0

def main():
    # Solicitar al usuario que ingrese un número entero
    numero = int(input("Ingrese un número entero: "))

    # Verificar si el número es par usando la función es_par()
    if es_par(numero):
        print(f"{numero} es un número par.")
    else:
        print(f"{numero} es un número impar.")

if __name__ == "__main__":
    main()
