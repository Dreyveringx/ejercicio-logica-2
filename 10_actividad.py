'''
Diseñe una aplicación que lea un número de tres cifras y determine si es o no
palíndromo o Capicúa (se refiere a cualquier número que se lee igual de izquierda a
derecha que de derecha a izquierda. Ejemplos: 161, 2992, 3003). Nota: Opcional
investigar/usar la técnica “slicing” (que se utiliza para obtener una reversión de una
cadena (o lista) de caracteres) y la función isdigit().
'''
def es_capicua(numero):
    # Verificar si el número es de tres dígitos
    if len(numero) != 3:
        return False
    
    # Verificar si todos los caracteres son dígitos
    if not numero.isdigit():
        return False
    
    # Verificar si el número es capicúa
    if numero == numero[::-1]:
        return True
    else:
        return False

# Función principal
def main():
    numero = input("Ingrese un número de tres cifras: ")
    
    if es_capicua(numero):
        print(f"El número {numero} es capicúa.")
    else:
        print(f"El número {numero} no es capicúa.")

if __name__ == "__main__":
    main()

