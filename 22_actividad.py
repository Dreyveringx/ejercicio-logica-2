'''
    Solicitar al usuario que ingrese dos números enteros y determinar si ambos son pares
    o impares. Mostrar en pantalla un mensaje que indique “Ambos números son pares”
    siempre y cuando cumplan con la condición. En caso contrario se deberá imprimir el
    siguiente mensaje “Los números no son pares, o uno de ellos no es par”.
'''

def main():
    # Solicitar al usuario que ingrese dos números enteros
    num1 = int(input("Por favor ingrese dos números enteros\nPrimer número entero: "))
    num2 = int(input("Segundo número entero: "))

    # Verificar si ambos números son pares
    if num1 % 2 == 0 and num2 % 2 == 0:
        print("\nAmbos números son pares.")
    else:
        print("\nLos números no son pares, o uno de ellos no es par.")

if __name__ == "__main__":
    main()
