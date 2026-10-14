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

def promedio_mayuscula(lista):

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


lista = ["Perro", "Gato"]

promedio_minusculas(lista)
promedio_mayuscula(lista)