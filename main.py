from service import *

mantener_activo = True

while mantener_activo:
    print("\n\n\t\t=== Gestion de Servicios Fotograficos ===")
    print("1. Registrar servicio.")
    print("2. Modificar servicio.")
    print("3. Eliminar servicio.")
    print("4. Salir")

    opcion = 0

    try:
        opcion = int(input("Ingresa la opcion: ")) 
    
    except ValueError:
        print("\n\nERROR ---> La opcion ingresada es invalida, vuelve a intentarlo\n")
        continue
    
    else:
        match opcion:
            case 1:
                agregar_servicio()
            case 2:
                modificar_servicio()
            case 3:
                eliminar_servicio()
                pass
            case 4:
                mantener_activo = False
            case _:
                print("\n\nERROR ---> Esa opcion no esta disponible, vuelve a intentarlo\n")
    