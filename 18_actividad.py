'''
    Continuando el ejercicio anterior, ahora se pedirá una frase o palabra y se validara si
    la primera letra de la frase es igual a la última letra de la frase. Se deberá de imprimir
    un mensaje por pantalla que diga “CORRECTO”, en caso contrario, se deberá imprimir
    “INCORRECTO”.
'''

def main():
    # Solicitar al usuario que ingrese una frase o palabra
    frase = input("Por favor ingresa una frase o palabra que inicie y termine con la misma letra: ")

    # Verificar si la primera letra de la frase es igual a la ultima letra utilizando indexación
    if frase[0].lower() == frase[-1].lower():
        print("CORRECTO")
    else:
        print("INCORRECTO")

if __name__ == "__main__":
    main()