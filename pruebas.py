import random
# Funciona la parte de generar contraseñas, solamente falta agregarlas a la lista. Por eso, hago una copia para intentar modificar esa parte 

def extencion_contraseña():

    longitud_contraseña = random.randint(8,16)
    
    contraseña = ""
    i = 1
            
    while i <= longitud_contraseña:
    
        azar = random.randint(1,3)
        print("numero random generado al azar",azar)
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

        repetida = False
        password = extencion_contraseña()
        
        for i in Lista_vacia:
            if i == password:
                print("Contraseña existente, volviendo a generar una nueva")
                repetida = True
                break

        if repetida == False:
            Lista_vacia += [password]
            cantidad_contraseña -= 1
            
    for j in Lista_vacia:
        print(j)
# generar_contraseña()
extencion_contraseña()


# lista_estadisticas = ["octavios", "penelope", "lewandosky"]

# ocho_caracteres = 0
# nueve_caracteres = 0
# diez_caracteres = 0
# once_caracteres = 0
# doce_caracteres = 0
# trece_caracteres = 0
# catorce_caracteres = 0
# quince_caracteres = 0

# for i in lista_estadisticas:
#     # print(len(i))
#     match len(i):
#         case 8 == 8:
#             ocho_caracteres += 1

#         case 9:
#                     ocho_caracteres += 1

#         case 10:
#                     ocho_caracteres += 1

#         case 11:
#                     ocho_caracteres += 1

#         case 12:
#                     ocho_caracteres += 1

#         case 13:
#                     ocho_caracteres += 1

#         case 14:
#                     ocho_caracteres += 1

#         case 15:
#                     ocho_caracteres += 1

#     print(ocho_caracteres)  
#     print(diez_caracteres)              