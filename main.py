mantener_activo = True

while mantener_activo:
    print("=== Gestion de Servicios Fotograficos ===")
    print("1. Registrar servicio")
    print("2. Listar servicios (implementando)")
    print("3. Eliminar servicio (implementando)")
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
                # Funcionalidad de agregar servicio
                pass
            case 2:
                # Funcionalidad de listar servicios
                pass
            case 3:
                # Funcionalidad de eliminar un servicio
                pass
            case 4:
                mantener_activo = False
            case _:
                print("\n\nERROR ---> Esa opcion no esta disponible, vuelve a intentarlo\n")
    