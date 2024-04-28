'''
    Una tienda ofrece para los meses de septiembre, octubre y noviembre un descuento
    del 10% sobre el total de la compra que realiza un cliente. Solicitar al usuario que
    ingrese un mes y el importe de la compra. El programa debe calcular cuál es el monto
    total que se debe cobrar al cliente e imprimirlo por pantalla.
'''
def main():
    # Solicitar al usuario que ingrese el mes y el importe de la compra
    mes = input("Ingrese el mes (septiembre, octubre o noviembre): ").lower()
    importe_compra = float(input("Ingrese el importe de la compra: "))

    # Verificar si el mes es septiembre, octubre o noviembre
    if mes == "septiembre" or mes == "octubre" or mes == "noviembre":
        # Calcular el monto total con descuento del 10%
        monto_total = importe_compra * 0.90
        print("El monto total a cobrar es: ${:.2f}".format(monto_total))
    else:
        print("El mes ingresado no es válido.")

if __name__ == "__main__":
    main()


