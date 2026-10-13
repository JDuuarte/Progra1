#Todas las funciones que usara el programa
import random

# if cantidad_contraseña[0] == "-" or (cantidad_contraseña[0] >= 0 and cantidad_contraseña[0] <= 9)
        # print("ingresaste un valor incorrecto")


def extencion_contraseña():

    longitud_contraseña = random.randint(8,16)

    contraseña = ""
    i = 1
            
    while i <= longitud_contraseña:
    
        azar = random.randint(1,4)
    
        match azar:
            case 1:
                contraseña += chr(random.randint(65,90))
                i += 1
    
            case 2:
                contraseña += chr(random.randint(97,122))
                i += 1
    
            case 3:
                contraseña += chr(random.randint(48,57))
                i += 1

    return contraseña
       
def generar_contraseña():
    cantidad_contraseña = int(input("¿Cuántas contaseñas queres generar?: "))
    Lista_vacia = []
    
    while cantidad_contraseña > 0:
        
        cantidad_contraseña -= 1

        password = extencion_contraseña()
        Lista_vacia += [password]

    for i in Lista_vacia:
        print(i)

def seleccionar_menu():
    print("=========== MENU ===========\n")
    print("1. Generar contraseñas")
    print("2. Buscar contraseña")
    print("3. Informar estadísticas")
    print("4. Ordenar y mostrar contraseñas")
    print("5. Generar Salir\n")

    opcion = input("Selecciona una opcion: ")

    match opcion:

        case "1":
            print(opcion)

        case "2":
                print(opcion)

        case "3":
                print(opcion)

        case "4":
                print(opcion)

        case "5":
                print(opcion)

        case _:
                print("Opción incorrecta")                                
