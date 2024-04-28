'''
Realiza un programa que sólo permita introducir los caracteres ‘S’ y ‘N’. Si el usuario
ingresa alguno de esos dos caracteres se deberá de imprimir un mensaje por pantalla
que diga “CORRECTO”, en caso contrario, se deberá imprimir “INCORRECTO”.
'''

def entrada(caracter):
    # Convertir el carácter a minúsculas para hacer la comparación insensible a mayúsculas/minúsculas
    caracter = caracter.lower()

    #Lista caracteres válidos
    caracter_valido = ["s", "n"]

    #Verificar si el carácter ingresado corresponde a "S" o "N"
    if caracter in caracter_valido:
        return True
    else:
        return False
    
def main ():
    #Solicitar al usuario que ingrese un caracter
    caracter = input("Ingresar carácter S o N: ")

    #Verificar si es "CORRECTO" o "INCORRECTO"
    if entrada (caracter):
        print(f"{caracter.capitalize()} es CORRECTO.")

    else:
        print(f"{caracter.capitalize()} es INCORRECTO")

if __name__ == "__main__":
    main()    