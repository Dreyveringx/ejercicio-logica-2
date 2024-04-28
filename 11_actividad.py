'''
    Crea una aplicación que nos pida un día de la semana y que nos diga si es un día
    laboral o no.
'''
def es_dia_laboral(dia):
    # Convertir el día a minúsculas para hacer la comparación insensible a mayúsculas/minúsculas
    dia = dia.lower()
    
    # Lista de días laborales
    dias_laborales = ["lunes", "martes", "miércoles", "jueves", "viernes"]
    
    # Verificar si el día ingresado es un día laboral
    if dia in dias_laborales:
        return True
    else:
        return False

def main():
    # Solicitar al usuario que ingrese un día de la semana
    dia = input("Ingrese un día de la semana: ")
    
    # Verificar si es un día laboral
    if es_dia_laboral(dia):
        print(f"{dia.capitalize()} es un día laboral.")
    else:
        print(f"{dia.capitalize()} no es un día laboral.")

if __name__ == "__main__":
    main()
