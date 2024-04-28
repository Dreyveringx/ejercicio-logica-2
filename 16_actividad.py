'''
    Escriba un programa que pida 3 notas y valide si esas notas están entre 1 y 10. Si están
    entre esos parámetros se debe poner en verdadero una variable de tipo lógico y si no
    ponerla en falso. Al final el programa debe decir si las 3 notas son correctas usando la
    variable de tipo lógico.
'''
def main():
    # Solicitar al usuario que ingrese las notas
    nota1 = float(input("Ingrese la primera nota: "))
    nota2 = float(input("Ingrese la segunda nota: "))
    nota3 = float(input("Ingrese la tercera nota: "))

    # Verificar si las notas están entre 1 y 10
    notas_correctas = (1 <= nota1 <= 10) and (1 <= nota2 <= 10) and (1 <= nota3 <= 10)

    # Mostrar si las notas son correctas
    if notas_correctas:
        print("Las tres notas son correctas.")
    else:
        print("Al menos una de las notas no está entre 1 y 10.")

if __name__ == "__main__":
    main()

