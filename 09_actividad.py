'''
Se pide ingresar una letra del alfabeto y mostrar si dicha letra es vocal o consonante. Nota: Opcional investigar y usar operador ‘in’, método isalpha() y función len().
'''

def verificar_letra(letra):
    #Verificar si la entrada es una letra del alfabeto
    if letra.isalpha() and len(letra) == 1:
        #convertir la letra a minúscula para simplificar la comparación
        letra = letra.lower()
        #Verificar so la letra es una vocal usando el operador "in"
        if letra in 'aeiou':
            print("La letra ingresada es una vocal.")
        else:
            print("La letra ingresada es una consonante.")
    else:
        print("Por favor ingrese una sola letra del alfabeto.")

#Solicitar al usuario que ingrese una letra del alfabeto
letra_usuario = input("Ingrese una letra del alfabeto: ")

#Llamar a la función para verificar la letra ingresada
verificar_letra(letra_usuario)