import json
from config import *

ruta_servicios = ruta_data/"servicios.json"

try:
    with open(ruta_servicios):
        pass
except FileNotFoundError:
    with open(ruta_servicios, "w") as archivo:
        json.dump([], archivo, indent=4)
        pass

def leer_json():
    datos_servicios = {}

    with open(ruta_servicios) as archivo:
        datos_servicios = json.load(archivo)

    return datos_servicios

def modificar_json(datos):
    with open(ruta_servicios, "w") as archivo:
        json.dump(datos, archivo, indent=4)

def agregar_servicio():
    while True:
        try:
            print("\n\n--- Registro de servicio fotografico ---")
            nombre_paquete = input("Ingresa el nombre del paquete: ")
            precio = int(input("Ingresa el precio: "))
            tipo_evento = input("Ingresa el tipo de evento [Ej: Boda, Retrato, Producto, etc]: ") # Need
            duracion_horas = int(input("Ingresa la duracion en horas: "))

            if not nombre_paquete or precio < 1 or not tipo_evento or duracion_horas < 1:
                raise ValueError

        except ValueError:
            print("ERROR --> Al menos uno de los valores fue incorrecto, vuelve a intentar")
        
        else:
            datos = list(leer_json())
            
            datos.append({
                "codigo" : f"COD{len(datos) + 1000}",
                "nombre_paquete": nombre_paquete,
                "precio": precio,
                "tipo_evento": tipo_evento,
                "duracion_horas": duracion_horas
            })

            modificar_json(datos)
            break
        