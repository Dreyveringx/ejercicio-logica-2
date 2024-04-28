'''
    Escriba un programa que pida una frase o palabra y valide si la primera letra de esa
    frase es una ‘A’. Si la primera letra es una ‘A’, se deberá de imprimir un mensaje por
    pantalla que diga “CORRECTO”, en caso contrario, se deberá imprimir
    “INCORRECTO”. Nota: investigar/usar la indexación de cadenas.
'''

def main():
    # Solicitar al usuario que ingrese una frase o palabra
    frase = input("Por favor ingresa una frase o palabra que inicie con la letra A: ")

    # Verificar si la primera letra de la frase es "A" utilizando indexación
    if frase and frase[0].lower() == "a":
        print("CORRECTO")
    else:
        print("INCORRECTO")

if __name__ == "__main__":
    main()
