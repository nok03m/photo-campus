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
        
def listar_servicios():
    datos = list(leer_json())
    
    print("\n- Lista de servicios -")
    for servicio in datos:
        print(servicio)

def modificar_servicio():
    listar_servicios()
    datos = leer_json()
    servicio_actualizado = {}
    existe_servicio = False
    
    while not existe_servicio:
        codigo = input("Ingresa el codigo del servicio a editar: ")
        
        if not codigo:
            print("\nERROR -> No puede estar vacio\n")
            continue
        
        i = 0
        for servicio in datos:
            if servicio["codigo"] == codigo:
                print("\n\n\t\t--- Edicion de campos ---")
                print("*Enter para dejar el campo por defecto\n")
                
                existe_servicio = True
                nombre_paquete = input(f"Nombre anterior -> [{servicio["nombre_paquete"]}], Ingresa el nuevo: ")
                precio = input(f"Precio anterior -> [{servicio["precio"]}], Ingresa el nuevo: ")
                tipo_evento = input(f"Tipo de evento anterior -> [{servicio["tipo_evento"]}], Ingresa el nuevo: ")
                duracion_horas = input(f"Duracion horas anterior -> [{servicio["duracion_horas"]}], Ingresa la nueva: ")
                    
                servicio_actualizado = {
                    "codigo": servicio["codigo"],
                    "nombre_paquete": nombre_paquete if nombre_paquete else servicio["nombre_paquete"],
                    "precio": int(precio) if precio.isdigit() else servicio["precio"],
                    "tipo_evento": tipo_evento if tipo_evento else servicio["tipo_evento"],
                    "duracion_horas": int(duracion_horas) if duracion_horas.isdigit() else servicio["duracion_horas"]
                }
                
                datos[i] = servicio_actualizado
                break

            i += 1
    
        if servicio_actualizado == {}:
            print("\nERROR -> El codigo no existe")
            
    print("\nModificando servicio...\n...\n...\nServicio modificado!!!\n")
    modificar_json(datos)

def eliminar_servicio():
    listar_servicios()
    datos = list(leer_json())
    servicio_eliminado = False
    
    codigo = input("Ingresa el codigo del servicio a editar: ")
        
    if codigo:
        i = 0
        
        for servicio in datos:
            if servicio["codigo"] == codigo:
                datos.pop(i)
                modificar_json(datos)
                servicio_eliminado = True
                break
            i += 1
    
    if servicio_eliminado:
        print("\nEliminando servicio...\n...\n...\nServicio eliminado!!!\n")
    else:
        print("\nNo hubo ninguna coincidencia... Regresando")