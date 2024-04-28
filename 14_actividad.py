'''
Realizar un programa que pida introducir solo frases o palabras de 6 caracteres. Si el usuario ingresa una frase o palabra de 6 caracteres se deberá de imprimir un mensaje por pantalla que diga “CORRECTO”, en caso contrario, se deberá imprimir “INCORRECTO”. Nota: usar la función len().
'''

def main():
    # Solicitar al usuario que ingrese una frase o palabra
    caracteres = input("Por favor ingresa una frase o palabra de 6 caracteres: ")

    # Verificar si la longitud de la entrada es exactamente 6 caracteres
    if len(caracteres) == 6:
        print("La cantidad de caracteres ingresados es CORRECTA.")
    else:
        print("La cantidad de caracteres ingresados es INCORRECTA.")

if __name__ == "__main__":
    main()
