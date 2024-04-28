'''
Realizar un programa que pida una frase o palabra y si la frase o palabra es de 4
caracteres de largo, el programa le concatenara un signo de exclamación al final, y si
no es de 4 caracteres el programa le concatenara un signo de interrogación al final. El
programa mostrará después la frase final. Nota: usar la función len() y el operador de
concatenación.
'''

def main():
    # Solicitar al usuario que ingrese una frase o palabra
    caracteres = input("Por favor ingresa una frase o palabra: ")

    # Verificar la longitud de la entrada del usuario y concatenar el símbolo correspondiente
    if len(caracteres) == 4:
        resultado = caracteres.capitalize() + "!"
    else:
        resultado = caracteres.capitalize() + "?"

    # Imprimir el resultado
    print(resultado)

if __name__ == "__main__":
    main()
