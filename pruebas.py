import random
# Funciona la parte de generar contraseñas, solamente falta agregarlas a la lista. Por eso, hago una copia para intentar modificar esa parte

# def generar_contraseña():
#     cantidad_contraseña = int(input("¿Cuántas contaseñas queres generar?: "))

#     if cantidad_contraseña > 0:
#         longitud_contraseña = random.randint(8,16)
#         print("longitud de contraseña es:" , longitud_contraseña)

#         i = 1
#         j = 0

#         contraseña = ""
#         lista_de_contraseña = []
        
#         while i <= longitud_contraseña:

#             azar = random.randint(1,4)

#             match azar:
#                 case 1:
#                     contraseña += chr(random.randint(65,91))
#                     i += 1

#                 case 2:
#                     contraseña += chr(random.randint(97,123))
#                     i += 1

#                 case 3:
#                     contraseña += chr(random.randint(48,58))
#                     i += 1
        
#         print("contraseña generada:", contraseña)
#         # provisorio el print pero hay que hacer un for para que lo muestre correctamente

#         if len(lista_de_contraseña) <= cantidad_contraseña:

#             lista_de_contraseña += contraseña
#             contraseña = ""
        

#         print("lista de contraseña:",lista_de_contraseña)

# generar_contraseña()  


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


generar_contraseña()