'''
    La empresa “Te llevo a todos lados” está destinada al alquiler de autos y tiene un
    sistema de tarifa que consiste en cobrar el alquiler por hora. Si el cliente devuelve el
    auto dentro de las 2 horas de uso el valor que corresponde pagar es de 400 y el
    combustible va de regalo. Cuando el cliente regresa a la empresa pasadas las 2 horas,
    se ingresan la cantidad de litros de combustible gastados y el tiempo transcurrido en
    horas. Luego, se le cobra 40 por litro de combustible gastado, y la hora se fracciona en
    minutos, cobrando un total de 5,20 el minuto de uso. Realice un programa que permita
    registrar esa información y el total a pagar por el cliente.
'''

def calcular_pago(tiempo_transcurrido, litros_combustible):
    # Si el tiempo transcurrido es menor o igual a 2 horas
    if tiempo_transcurrido <= 2:
        total_pagar = 400  # Se cobra un monto fijo de 400
    else:
        # Se cobra 40 por litro de combustible gastado
        # y 5.20 por minuto de uso
        total_pagar = 40 * litros_combustible + 5.20 * tiempo_transcurrido * 60
    
    return total_pagar

def main():
    # Solicitar al usuario que ingrese el tiempo transcurrido en horas
    tiempo_transcurrido = float(input("Ingrese el tiempo transcurrido en horas: "))
    
    # Solicitar al usuario que ingrese la cantidad de litros de combustible gastados
    litros_combustible = float(input("Ingrese la cantidad de litros de combustible gastados: "))
    
    # Calcular el total a pagar utilizando la función calcular_pago
    total_a_pagar = calcular_pago(tiempo_transcurrido, litros_combustible)
    
    # Mostrar el total a pagar al cliente
    print("El total a pagar es: ${:.2f}".format(total_a_pagar))

if __name__ == "__main__":
    main()
