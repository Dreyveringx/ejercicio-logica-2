'''
A partir de una conocida cantidad de metros que el usuario ingresa a través del teclado se debe obtener su equivalente en centímetros, en milímetros y en pulgadas.
'''

#Se solicita al usuario que ingrese cantidad de metros
metros = float(input("Ingrese cantidad de metros: "))

#Convertir metros a centímetros
centimetros = int(metros * 100)

#Convertir metros a milímetros
milimetros = int(metros * 1000)

#Convertir metros a pulgadas
pulgadas = int(metros * 39.37)

#Mostrar resultados
print("\nResultados:")
print("Longitud en centímetros:", centimetros)
print("Longitud en milímetros:", milimetros)
print("Longitud en pulgadas:", pulgadas)