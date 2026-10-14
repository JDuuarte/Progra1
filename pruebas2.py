def promedio_minusculas(lista):

    contador_minusculas = 0
    acumulador = 0
    for contraseña in lista:

        acumulador += len(contraseña)
        
        for letra in contraseña:
         
            if 97 <= ord(letra) and ord(letra) <= 122:
                
                contador_minusculas += 1

        promedio_minus = contador_minusculas / acumulador

        
    print("contador minúsculas: ",contador_minusculas)
    print("Promedio minúsculas: ", promedio_minus)

def promedio_mayusculas(lista):

    contador_mayusculas = 0
    acumulador = 0
    for contraseña in lista:

        acumulador += len(contraseña)
        
        for letra in contraseña:
         
            if 65 <= ord(letra) and ord(letra) <= 90:
                
                contador_mayusculas += 1

        promedio_mayus = contador_mayusculas / acumulador

        
    print("contador mayúsculas: ",contador_mayusculas)
    print("Promedio mayúsculas: ", promedio_mayus)

def promedio_numerico(lista):

    contador_numerico = 0
    acumulador = 0
    for contraseña in lista:

        acumulador += len(contraseña)
        
        for letra in contraseña:
         
            if 48 <= ord(letra) and ord(letra) <= 57:
                
                contador_numerico += 1

        promedio_numerico = contador_numerico / acumulador

    print("contador numérico: ",contador_numerico)
    print("Promedio numérico: ", promedio_numerico)