'''
Escribir un programa que calcule cuántos litros de combustible consumió un automóvil. El usuario ingresará una cantidad de litros de combustible cargados en la estación y una cantidad de kilómetros recorridos, después, el programa calculará el consumo (km/lt) y se lo mostrará al usuario.
'''

#Se solicita al usuario que ingrese cantidad de litros de combustible
litros = float(input("Ingrese cantidad de litros cargados en la estación: "))
kilometros_recorridos = float(input("Ingrese cantidad de kilómetros recorridos: "))

#Calcular el consumo de litros por recorrido
consumo_por_recorrido = kilometros_recorridos / litros

#mostrar resultado
print("\nresultado:")
print("El consumo es de {:.2f} km por litro" .format(consumo_por_recorrido))