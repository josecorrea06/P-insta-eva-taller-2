def obtener_precio_base():
    while True:
        try:
            precio_base= float(input("Ingrese precio base de la motocicleta"))
            if precio_base>0:
                return precio_base
            else:
                print("Precio base debe ser mayor de 0")
        except ValueError:
            print("Error de entrada.Por favor,ingrese un numero")

def obtener_marca():
    marcas=["Honda","Yamaha","Suzuki","Otra"]
    print("Marcas disponibles")
    for i,marca in enumerate(marcas):
        print(f"{i+1}.{marca}")
        while True:
            try:
                opcion=int(input("Ingrese numero de marca:"))
                if 1<=opcion<=4:
                    return marcas[opcion-1]
                else:
                    print("Opcion  invalida.Por favor ingrese un numero entre 1 y 4.")
            except ValueError:
                print("Error de entrada.Por favor ingrese un numero")

def obtener_es_feriado():
    while True:
        respuesta=input("¿Es feriado? (S/N):")
        if respuesta.upper()== "S":
            return True
        elif respuesta.upper()== "N":
            return False
        else:
            print("Respuesta invalida.Por favor ingrese S o N.")

def calcular_descuento_marca(marca):
    descuentos= {
        "Honda":0.05,
        "Yamaha":0.18,
        "Feriado":0.25
    }

def obtener_es_feriado():
    while True:
        respuesta = input("¿Es feriado? (S/N): ")
        if respuesta.upper() == "S":
            return True
        elif respuesta.upper() == "N":
            return False
        else:
            print("Respuesta inválida. Por favor, ingrese S o N.")


def calcular_descuento_marca(marca):
    descuentos = {
        "Honda": 0.05,
        "Yamaha": 0.08,
        "Suzuki": 0.10,
        "Otra": 0.02
    }
    return descuentos[marca]


def calcular_descuento_dia(dia_semana, es_feriado):
    descuentos = {
        "Martes": 0.12,
        "Sábado": 0.18,
        "Feriado": 0.25
    }
    if es_feriado:
        return descuentos["Feriado"]
    elif dia_semana == "Martes":
        return descuentos["Martes"]
    elif dia_semana == "Sábado":
        return descuentos["Sábado"]
    else:
        return 0


import datetime

dia_semana = datetime.datetime.today().strftime("%A")


def calcular_descuento_total(descuento_marca, descuento_dia):
    return min(descuento_marca + descuento_dia, 0.30)


def calcular_precio_final(precio_base, descuento_total):
    return precio_base * (1 - descuento_total)


def main():
    precio_base = obtener_precio_base()
    marca = obtener_marca()
    es_feriado = obtener_es_feriado()

    descuento_marca = calcular_descuento_marca(marca)
    descuento_dia = calcular_descuento_dia(dia_semana, es_feriado)
    descuento_total = calcular_descuento_total(descuento_marca, descuento_dia)

    precio_final = calcular_precio_final(precio_base, descuento_total)
    ahorro_total = precio_base - precio_final

    print("\nResultados:")
    print(f"Precio base: ${precio_base:.2f}")
    print(f"Marca: {marca}")
    print(f"Descuento por marca: {descuento_marca * 100}%")
    print(f"Descuento por día: {descuento_dia * 100}%")
    print(f"Descuento total: {descuento_total * 100}%")
    print(f"Precio final: ${precio_final:.2f}")
    print(f"Ahorro total: ${ahorro_total:.2f}")


if __name__ == "__main__":
    main()












