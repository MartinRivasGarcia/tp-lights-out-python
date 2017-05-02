#Genera las grillas de los niveles predeterminados
def generacion_grilla(nivel):
    #La funcion unicamente te crea la grilla si la variable de entrada esta entre 1 y 5
    if (nivel == 1):
        lista = {
            '1':['0','0','.','0','0'],
            '2':['0','.','0','.','0'],
            '3':['.','0','0','0','.'],
            '4':['0','.','0','.','0'],
            '5':['0','0','.','0','0']
        }
    if (nivel == 2):
        lista = {
            '1':['.','0','.','0','.'],
            '2':['0','0','.','0','0'],
            '3':['.','0','.','0','.'],
            '4':['0','.','0','.','0'],
            '5':['0','.','0','.','0']
        }
    if (nivel == 3):
        lista = {
            '1':['0','.','.','.','0'],
            '2':['0','0','.','0','0'],
            '3':['.','.','0','.','.'],
            '4':['0','.','0','.','.'],
            '5':['0','.','0','0','.']
        }
    if (nivel == 4):
        lista = {
            '1':['0','0','.','0','0'],
            '2':['.','.','.','.','.'],
            '3':['0','0','.','0','0'],
            '4':['.','.','.','.','0'],
            '5':['0','0','.','.','.']
        }
    if (nivel == 5):
        lista = {
            '1':['.','.','.','0','0'],
            '2':['.','.','.','0','0'],
            '3':['.','.','.','.','.'],
            '4':['0','0','.','.','.'],
            '5':['0','0','.','.','.']
        }
    #va a devolver una lista creada para ser la grilla del nivel sin afectar la variable de entrada
    return (lista)

#Imprime en pantalla la grilla del nivel inicial, la cual ira siendo modificada
def imprimir_grilla (nivel,grilla,tamaño):
    print("Usted esta jugando el nivel " + str(nivel) + ":")
    print("    A B C D E ")
    for numero in range(1,(tamaño+1)):
        posicionG = str(numero)
        print(str(numero) + " | ",end="")
        for elemento in grilla[posicionG]:
            print(elemento, end=" ")
        print()
    print()

#Devuelve las coordenadas que el usuario ingreso
def coordenadas_ingresadas (tamaño):
    a = input("Ingrese las coordenadas a utilizar: ")
    final = limite(tamaño)
    if(a[0] < "A"):
        if ((int(a[0]) > tamaño) or (int(a[0]) <= 0)):
            print("El numero de las filas ingresado es invalido")
            error = 1
        else:
            error=0
    else:
        print("La primer coordenada debe ser un numero referido a las filas")
        error = 1

    if ((a[1] < "a" or a[1] > final[0]) and (a[1] < "A" or a[1] > final[1])):
        print("La letra referida a las columnas ingresada es invalida")
        error = 1
    while(error == 1):
        a = input("Reingrese las coordenadas a utilizar: ")
        if (a[0] < "A"):
            if ((int(a[0]) > tamaño) or (int(a[0]) <= 0)):
                print("El numero de las filas ingresado es invalido")
                error = 1
            else:
                error = 0
        else:
            print("La primer coordenada debe ser un numero referido a las filas")
            error = 1

        if ((a[1] < "a" or a[1] > final[0]) and (a[1] < "A" or a[1] > final[1])):
            print("La letra referida a las columnas ingresada es invalida")
            error = 1
    print()
    return (a)

def limite(tamaño):
    if(tamaño == 5):
        return("e","E")
    if(tamaño == 6):
        return("f","F")
    if(tamaño == 7):
        return("g","G")
    if(tamaño == 8):
        return("h","H")
    if(tamaño == 9):
        return("i","I")
    if(tamaño == 10):
        return("j","J")

#Tener en cuenta para el modo de juego alternativo
def generar_random():
    import random
    caracter = random.random() #Devuelve entre 0.0 y 1.0
    if (caracter > 0.5):
        caracter = 0
    else:
        caracter = "."
    return(caracter)

#Tener en cuenta para cuando el usuario reinicie el juego
def puntaje_por_encendidas(puntaje,grilla,tamaño):
    for numero in range(1,(tamaño+1)):
        posicion=str(numero)
        for caracter in grilla[posicion]:
            if((caracter == "0") and (puntaje > 0)):
                puntaje = puntaje-50
    return (puntaje)

def usuario_jugando(tamaño):
    print("¿Que desea hacer a continuacion?")
    print("0 - Ingresar coordenadas para jugar")
    print("1 - Reiniciar el nivel y restar 50  puntos por cada luz encendida")
    print("2 - Salir del juego")
    siguio = input("Opcion elegida: ")
    if((siguio != "0") and (siguio != "1") and (siguio != "2")):
        print("La opcion elegida no es valida, recuerde: ")
        print("0 - Ingresar coordenadas para jugar")
        print("1 - Reiniciar el nivel y restar 50  puntos por cada luz encendida")
        print("2 - Salir del juego")
        siguio = input("Opcion elegida: ")
    if(siguio == "0"):
        return (coordenadas_ingresadas(tamaño))
    else:
        return (siguio)
