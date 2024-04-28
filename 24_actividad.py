'''
    Construir un programa que simule un menú de opciones para realizar las cuatro
    operaciones aritméticas básicas (suma, resta, multiplicación y división) con dos valores numéricos enteros. 
    El usuario, además, debe especificar la operación con el primer carácter de la operación que desea realizar: ‘S' o ‘s’ para la suma, ‘R’ o ‘r’ para la resta, ‘M’ o ‘m’ para la multiplicación y ‘D’ o ‘d’ para la división. Nota: investigar/usar el manejo de errores con ‘try-except’.
'''

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    return a / b

def main():
    print("Bienvenido al programa de operaciones aritméticas básicas:")
    print("Opciones:")
    print("S/s - Suma")
    print("R/r - Resta")
    print("M/m - Multiplicación")
    print("D/d - División")

    # Solicitar al usuario que ingrese la operación deseada
    operacion = input("Ingrese el primer carácter de la operación que desea realizar: ").lower()

    # Verificar si la operación ingresada es válida
    if operacion not in ['s', 'r', 'm', 'd']:
        print("Operación no válida.")
        return

    # Solicitar al usuario que ingrese dos valores numéricos enteros
    try:
        a = int(input("Ingrese el primer número entero: "))
        b = int(input("Ingrese el segundo número entero: "))
    except ValueError:
        print("Por favor ingrese valores numéricos enteros.")
        return

    # Realizar la operación correspondiente
    try:
        if operacion == 's':
            resultado = suma(a, b)
            print(f"La suma de {a} y {b} es: {resultado}")
        elif operacion == 'r':
            resultado = resta(a, b)
            print(f"La resta de {a} y {b} es: {resultado}")
        elif operacion == 'm':
            resultado = multiplicacion(a, b)
            print(f"La multiplicación de {a} y {b} es: {resultado}")
        elif operacion == 'd':
            if b == 0:
                print("Error: No se puede dividir por cero.")
            else:
                resultado = division(a, b)
                print(f"La división de {a} entre {b} es: {resultado}")
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()


