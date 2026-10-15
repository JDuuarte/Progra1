import random
# Funciona la parte de generar contraseñas, solamente falta agregarlas a la lista. Por eso, hago una copia para intentar modificar esa parte 

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

lista_contraseñas_generadas = generar_contraseña()

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

def lista_longitud_promedios(lista):
    longitud = 0
    contador_longitud = 0

    for i in lista_contraseñas_generadas:

        longitud += len(i)

        contador_longitud += 1

    print("promedio longitud: ", (longitud / contador_longitud))

# lista_longitud_promedios(lista_contraseñas_generadas)

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

# promedio_mayusculas(lista_contraseñas_generadas)
# promedio_minusculas(lista_contraseñas_generadas)
# promedio_numerico(lista_contraseñas_generadas)


lista = ["perro", "gato", "conejo"]


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

contraseñas_unicas(lista_contraseñas_generadas) 



