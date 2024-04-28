'''
    Resolver el ejercicio anterior almacenando las tres notas en una lista, luego calcular el promedio sumando las notas y dividir por el número de elementos en esa lista.
'''

def main():
    #Almacenar las notas en una lista
    notas = []
    # Solicitar al usuario que ingrese las notas
    notas.append(float(input("Ingrese la primera nota: ")))
    notas.append(float(input("Ingrese la segunda nota: ")))
    notas.append(float(input("Ingrese la tercera nota: ")))

    # Calcular el promedio de las notas
    promedio = sum(notas) / len(notas)

    # Mostrar el promedio de las notas
    print("El promedio de las notas es: {:.2f}".format(promedio))

if __name__ == "__main__":
    main()