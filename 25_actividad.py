'''
    Escriba un programa para obtener el grado de eficiencia de un operario de una fábrica
    de tornillos, de acuerdo con las siguientes dos condiciones que se le imponen para un
    período de prueba:
    • Producir menos de 200 tornillos defectuosos.
    • Producir más de 10000 tornillos sin defectos.
    El grado de eficiencia se determina de la siguiente manera:
    a. Si no cumple ninguna de las condiciones, grado 5.
    b. Si sólo cumple la primera condición, grado 6.
    c. Si sólo cumple la segunda condición, grado 7.
    d. Si cumple las dos condiciones, grado 8
'''

def calcular_eficiencia(tornillos_defectuosos, tornillos_sin_defectos):
    if tornillos_defectuosos < 200 and tornillos_sin_defectos > 10000:
        return 8
    elif tornillos_defectuosos < 200:
        return 6
    elif tornillos_sin_defectos > 10000:
        return 7
    else:
        return 5

def main():
    # Solicitar al usuario que ingrese la cantidad de tornillos defectuosos y sin defectos
    tornillos_defectuosos = int(input("Ingrese la cantidad de tornillos defectuosos: "))
    tornillos_sin_defectos = int(input("Ingrese la cantidad de tornillos sin defectos: "))

    # Calcular el grado de eficiencia utilizando la función calcular_eficiencia
    grado_eficiencia = calcular_eficiencia(tornillos_defectuosos, tornillos_sin_defectos)

    # Mostrar el grado de eficiencia del operario
    print("El grado de eficiencia del operario es:", grado_eficiencia)

if __name__ == "__main__":
    main()
