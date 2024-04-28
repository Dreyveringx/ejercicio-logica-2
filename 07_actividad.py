'''
Un hombre desea saber si su sueldo es mayor al sueldo mínimo, el programa le pedirá al usuario su sueldo actual y el sueldo mínimo. Si el sueldo es mayor al mínimo se debe mostrar un mensaje por pantalla indicándolo.
'''
def comparar_sueldo():
    # Solicitar al usuario ingresar su sueldo actual
    sueldo_actual = float(input("Ingrese su sueldo actual: "))
    # Solicitar al usuario ingresar el sueldo mínimo
    sueldo_minimo = float(input("Ingrese el sueldo mínimo: "))

    # Comparar el sueldo actual con el sueldo mínimo
    if sueldo_actual > sueldo_minimo:
        # Si el sueldo actual es mayor que el sueldo mínimo, imprimir un mensaje indicándolo
        print("Su sueldo es mayor al sueldo mínimo.")
        # Si el sueldo actual no es mayor que el sueldo mínimo, imprimir un mensaje indicándolo
    else:
        print("Su sueldo no es mayor al sueldo mínimo.")

# Llamar a la función para ejecutar el programa
comparar_sueldo()