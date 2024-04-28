'''
Escriba un programa que permita al usuario ingresar el valor de dos variables numéricas de tipo entero. Posteriormente, el programa debe intercambiar los valores de ambas variables y mostrar el resultado final por pantalla. Por ejemplo, si el usuario ingresa los valores num1 = 9 y num2 = 3, la salida a del programa deberá mostrar: num1 = 3 y num2 = 9
'''

#Se solicita al usuario que ingrese el valor de dos variables numéricas de tipo entero
num1 = int(input("Ingrese el primer número entero: "))
num2 = int(input("Ingrese el segundo número entero: "))

#Se intercambia valores en ambas variables
numero_1 = num2
numero_2 = num1

#Resultados
print("\nResultados:")
print("El primer número entero ingresado es:", numero_1)
print("El segundo número entero ingresado es:", numero_2)