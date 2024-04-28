'''
Escribir un programa que calcule el precio promedio de un producto. El precio promedio se debe calcular a partir del precio del mismo producto en tres establecimientos distintos.
'''

#Solicitar al usuario que ingrese los precios del producto en tres establecimientos distintos
precio_establecimiento_1 = float(input("Ingrese el precio del producto en el primer establecimiento: "))
precio_establecimiento_2 = float(input("Ingrese el precio del producto en el segundo establecimiento: "))
precio_establecimiento_3 = float(input("Ingrese el precio del producto en el tercer establecimiento: "))

#Calcular el precio promedio del producto
precio_promedio = (precio_establecimiento_1 + precio_establecimiento_2 + precio_establecimiento_3) / 3

#mostrar resultado por pantalla
print("\nPrecio promedio del producto: ${:.2f}".format(precio_promedio))