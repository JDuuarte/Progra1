
import random
#solamente van las variables y el menu
control = False



#Todas las funciones que usara el programa
import random


# PUNTO 1



def extencion_contraseña():

    longitud_contraseña = random.randint(8,16)
    
    contraseña = ""
    i = 1
            
    while i <= longitud_contraseña:
    
        azar = random.randint(1,3)
        
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

    return Lista_vacia    

def agregar_contraseñas(lista):

    cantidad_contraseña = int(input("¿Cuántas contaseñas queres agregar?: "))

    while cantidad_contraseña > 0:

        repetida = False
        password = extencion_contraseña()
        agregar_lista = []

        for i in agregar_lista:
            if i == password:
                print("Contraseña existente, volviendo a generar una nueva")
                repetida = True
                break

        if repetida == False:
            agregar_lista += [password]
            cantidad_contraseña -= 1
            
    lista += [agregar_lista]
    print(lista)

    return lista  

# lista_contraseñas_generadas = generar_contraseña()

# PUNTO 3

def lista_porcentajes(lista):


    lista2 = [0, 0, 0, 0, 0, 0, 0, 0]

    contador_estadisticas = 0

    for i in lista:

        contador_estadisticas += 1

        match len(i):
            case 8:
                lista2[0] += 1

            case 9:
                lista2[1] += 1

            case 10:
                lista2[2] += 1

            case 11:
                lista2[3] += 1

            case 12:
                lista2[4] += 1

            case 13:
                lista2[5] += 1

            case 14:
                lista2[6] += 1

            case 15:
                lista2[7] += 1

    print(lista2)
    print("contador estadisticas", contador_estadisticas)

    print("========= PORCENTAJE ========")
    m = 8
    for l in lista2:
        print(f"{m} caracteres: {((l * 100)/contador_estadisticas)}%")
        m += 1                             

def promedio_minusculas(lista):

    contador_minusculas = 0
    acumulador = 0
    for contraseña in lista:

        acumulador += len(contraseña)
        
        for letra in contraseña:
         
            if 97 <= ord(letra) and ord(letra) <= 122:
                
                contador_minusculas += 1

        promedio_minus = (contador_minusculas * 100) / acumulador

        
    print("contador minúsculas: ",contador_minusculas)
    print("Promedio minúsculas: ", promedio_minus)
    print("----- *** -----")

def promedio_mayusculas(lista):

    contador_mayusculas = 0
    acumulador = 0
    for contraseña in lista:

        acumulador += len(contraseña)
        
        for letra in contraseña:
         
            if 65 <= ord(letra) and ord(letra) <= 90:
                
                contador_mayusculas += 1

        promedio_mayus = (contador_mayusculas * 100)/ acumulador

        
    print("contador mayúsculas: ",contador_mayusculas)
    print("Promedio mayúsculas: ", promedio_mayus)
    print("----- *** -----")
    
def promedio_numerico(lista):

    contador_numerico = 0
    acumulador = 0
    for contraseña in lista:

        acumulador += len(contraseña)
        
        for letra in contraseña:
         
            if 48 <= ord(letra) and ord(letra) <= 57:
                
                contador_numerico += 1

        promedio_numerico = (contador_numerico * 100) / acumulador

    print("contador numérico: ",contador_numerico)
    print("Promedio numérico: ", promedio_numerico)
    print("----- *** -----")


    contador_mayusculas = 0
    acumulador = 0
    for contraseña in lista:

        acumulador += len(contraseña)
        
        for letra in contraseña:
         
            if 65 <= ord(letra) and ord(letra) <= 90:
                
                contador_mayusculas += 1

        promedio_minus = contador_mayusculas / acumulador

        
    print("contador mayúsculas: ",contador_mayusculas)
    print("Promedio mayúsculas: ", promedio_minus)

def contraseñas_unicas(lista):
    contador = 0
    comparador = ""
    
    for i in lista:

        if i == comparador:
            contador += 1
            print("Contraseñas iguales, revisar algoritmo")
            break

        elif comparador == "":
            comparador = i
            contador += 1

        else:
            contador += 1

    if contador == len(lista):        

        print("contraseñas no repetidas")


# PUNTO 4
def ordenar_lista(lista):

    retorno = []
        
    print("Elegí un criterio de ordenamiento: ")
    print("----- *** -----")
    print("1. Asc = Ascendente")
    print("2. Desc = Descendente")
    opcion = input("Colocá 1(asc) o 2 (Desc): ")
    print()
    
    if opcion != "1" and opcion != "2":
        print("/" * 50)
        print()
        print("Opción no válida. Volve a seleccionar, por favor.")
        print()
        print("/" * 50)
        
    if opcion == "1":
        for i in range(len(lista) - 1):

            for j in range(i + 1, len(lista)):

                if lista[i] > lista[j]:
                    aux = lista[i]
                    lista[i] = lista[j]
                    lista[j] = aux
        print(lista)
    
    elif opcion == "2":

        for i in range(len(lista) - 1):

            for j in range(i + 1, len(lista)):

                if lista[i] < lista[j]:
                    aux = lista[i]
                    lista[i] = lista[j]
                    lista[j] = aux
        print(lista)


# OTROS PUNTOS
def menu_completo():

    print("Bienvenido al gestor de contraseñas\n")

    print("=========== MENU ===========\n")
    print("1. Generar Contraseñas.")
    print("2. Buscar Contraseña.")
    print("3. Informar estadisticas.")
    print("4. Ordenar y mostrar contraseñas.")
    print("5. Salir.\n")
    print("=========== **** ===========\n")

def seleccionar_menu():
    control = ""
    while control == "":
        print("=========== MENU ===========\n")
        print("1. Agregar más contraseñas")
        print("2. Buscar contraseña")
        print("3. Informar estadísticas")
        print("4. Ordenar y mostrar contraseñas")
        print("5. Generar Salir\n")

        opcion = input("Selecciona una opcion: ")

        match opcion:

            case "1":
                agregar_contraseñas(lista_contraseñas_generadas)

            case "2":
                    print(opcion)

            case "3":
                    lista_porcentajes(lista_contraseñas_generadas)
                    promedio_mayusculas(lista_contraseñas_generadas)
                    promedio_minusculas(lista_contraseñas_generadas)
                    promedio_numerico(lista_contraseñas_generadas)
                    contraseñas_unicas(lista_contraseñas_generadas)

            case "4":
                    ordenar_lista(lista_contraseñas_generadas)

            case "5":
                    print("Saliendo del programa")
                    control = False
                    return control
                    

            case _:
                    print("Opción incorrecta")   


while True:
    

    if control == False:
        print("=============== **** ===============\n")

        print("Bienvenido al gestor de contraseñas.\n")

        print("=============== MENU ===============")
        print("1. Generar Contraseñas\n")

        opcion = input("Seleccione una opción: ")
        print()
        print("... CARGANDO SISTEMA\n")
        

        
        lista_contraseñas_generadas = generar_contraseña()
        print(lista_contraseñas_generadas)
        
        control = True
    
    else:
        menu_completo()
        seleccionar_menu()