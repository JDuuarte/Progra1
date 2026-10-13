#Todas las funciones que usara el programa
import random

# if cantidad_contraseña[0] == "-" or (cantidad_contraseña[0] >= 0 and cantidad_contraseña[0] <= 9)
        # print("ingresaste un valor incorrecto")


def generar_contraseña():
    cantidad_contraseña = int(input("¿Cuántas contaseñas queres generar?: "))

    if cantidad_contraseña > 0:
        longitud_contraseña = random.randint(8,16)
        print("longitud de contraseña es:" , longitud_contraseña)

        i = 1
        j = 0

        contraseña = []
        lista_de_contraseña = [0]
        
        while i <= longitud_contraseña:

            azar = random.randint(1,4)

            match azar:
                case 1:
                    contraseña += [chr(random.randint(65,91))]
                    i += 1

                case 2:
                    contraseña += [chr(random.randint(97,123))]
                    i += 1

                case 3:
                    contraseña += [chr(random.randint(48,58))]
                    i += 1
        
        print("contraseña generada:", contraseña)
        # provisorio el print pero hay que hacer un for para que lo muestre correctamente

        if len(lista_de_contraseña) <= cantidad_contraseña:
        
                    for j in lista_de_contraseña:
                        lista_de_contraseña[j] = [contraseña] 
        

        print("lista de contraseña:",lista_de_contraseña)

generar_contraseña()      
       

# def seleccionar_menu():
    # print("=========== MENU ===========\n")
    # print("1. Generar contraseñas")
    # print("2. Buscar contraseña")
    # print("3. Informar estadísticas")
    # print("4. Ordenar y mostrar contraseñas")
    # print("5. Generar Salir\n")

    # opcion = input("Selecciona una opcion: ")

    # match opcion:

    #     case "1":
    #         print(opcion)

    #     case "2":
    #             print(opcion)

    #     case "3":
    #             print(opcion)

    #     case "4":
    #             print(opcion)

    #     case "5":
    #             print(opcion)

    #     case _:
    #             print("Opción incorrecta")                                
