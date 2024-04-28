'''
Conocido el número en matemática PI π, pedir al usuario que ingrese el valor del radio de una circunferencia y calcular y mostrar por pantalla el área y perímetro. Recuerde que para calcular el área y el perímetro se utilizan las siguientes fórmulas: area = PI * radio2 perímetro = 2 * PI * radio
'''

import math
p = math.pi

radio = float(input("Ingrese valor del radio de la circunferencia: ")) #Se solicita al usuario que ingrese el valor del radio

#Calcular el area y el perímetro
area = int(p * radio**2)
perimetro = int(2 * p * radio)

#Mostar el area y el perímetro
print("\nResultados:")
print(f"El area de la circunferencia es: {area}")
print(f"El perímetro de la circunferencia es: {perimetro}")