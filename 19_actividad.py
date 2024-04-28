'''
    Realizar un programa que pida tres notas y determine si un alumno aprueba o reprueba un curso, sabiendo que aprobará el curso si su promedio de tres calificaciones es mayor o igual a 70; y reprueba en caso contrario.
'''
def main():
    # Solicitar al usuario que ingrese las notas
    nota1 = float(input("Ingrese la primera nota: "))
    nota2 = float(input("Ingrese la segunda nota: "))
    nota3 = float(input("Ingrese la tercera nota: "))

    # Calcular el promedio de las notas
    notas_correctas = (nota1 + nota2 + nota3) / 3

    # Mostrar si el alumno aprueba o reprueba el curso
    if notas_correctas >= 70:
        print("Aprobado.")
    else:
        print("Reprobado.")

if __name__ == "__main__":
    main()