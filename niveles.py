#Genera las grillas de los niveles predeterminados
def generacion_grilla(nivel): #no hay generacion de nada, tengo q validar lo datos de entrada!!
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
def imprimir_grilla (nivel,grilla,tamaño): #Grilla no, es un tablero
    print("Nivel " + str(nivel) + ":")
    final = limite(tamaño)
    print("    ",end='')
    for a in range(1,tamaño+1):
        letra = limite(a)
        print(letra[1],end=' ')
    print()
    for numero in range(1,(tamaño+1)):
        posicionG = str(numero)
        print(str(numero) + " | ",end="")
        for elemento in grilla[posicionG]:
            print(elemento, end=" ")
        print()
    print()

#Devuelve las coordenadas que el usuario ingreso
def limite(tamaño): #Reemplazar por una estructura de datos
    if (tamaño == 1):
        return ("a", "A")
    if (tamaño == 2):
        return ("b", "B")
    if (tamaño == 3):
        return ("c", "C")
    if (tamaño == 4):
        return ("d", "D")
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




def coordenadas_ingresadas (siguio,tamaño): #Deberia dividirlo ed forma tal q una fucion me avise si lo ingresado no es valido
    a = siguio
    final = limite(tamaño)
    error = 0
    if(len(a) != 2): #2 numero magico, funcion lonngitudInvalidaCoordenada (coordenadaDelUsuario)
        error = 1
        print("Recuerde ingresar solo dos valores")
    if((a[1] < "A") and (error != 1)):
        if ((int(a[1]) > tamaño) or (int(a[1]) <= 0)):
            print("El numero de las filas ingresado es invalido")
            error = 1
        else:
            error = 0
    else:
        print("La segunda coordenada debe ser un numero referido a las filas")
        error = 1
    if(error != 1):
        if ((a[0] < "a" or a[0] > final[0]) and (a[0] < "A" or a[0] > final[1])):
            print("La letra referida a las columnas ingresada es invalida")
            error = 1
    while(error == 1):
        a = input("Reingrese las coordenadas a utilizar: ")
        error = 0
        if (len(a) != 2):
            error = 1
            print("Recuerde ingresar solo dos valores")
        if ((a[1] < "A") and (error != 1)):
            if ((int(a[1]) > tamaño) or (int(a[1]) <= 0)):
                print("El numero de las filas ingresado es invalido")
                error = 1
            else:
                error = 0
        else:
            print("La segunda coordenada debe ser un numero referido a las filas")
            error = 1
        if(error != 1):
            if ((a[0] < "a" or a[0] > final[0]) and (a[0] < "A" or a[0] > final[1])):
                print("La letra referida a las columnas ingresada es invalida")
                error = 1
    print()
    return (a)
#Tener en cuenta para cuando el usuario reinicie el juego
def puntaje_por_encendidas(puntaje,grilla,tamaño):
    for numero in range(1,(tamaño+1)):
        posicion=str(numero)
        for caracter in grilla[posicion]:
            if(caracter == "0"):
                puntaje = puntaje-50
    return (puntaje)

def usuario_jugando(tamaño):
    print("¿Que desea hacer a continuacion?")
    print("Ingresar coordenadas para jugar")
    print("R - Reiniciar el nivel y restar 50  puntos por cada luz encendida")
    siguio = input("Opcion elegida: ")

    while(len(siguio) > 2 or ((len(siguio) == 1) and (siguio != "R" and siguio != "r"))):
        print("La opcion elegida no es valida, recuerde: ")
        print("Ingresar coordenadas para jugar")
        print("R - Reiniciar el nivel y restar 50  puntos por cada luz encendida")
        siguio = input("Opcion elegida: ")
    if(siguio != "R" and siguio != "r"):
        return (coordenadas_ingresadas(siguio,tamaño))
    else:
        return (siguio)

def interactuar_con_el_tablero(grilla,coordenadas,tamaño):
    filas,columnas = convertir_coordenadas(coordenadas)
    if(grilla[filas][columnas] == '0'):
        grilla[filas][columnas] = '.'
    else:
        grilla[filas][columnas] = '0'
    if(columnas > 0):
        if (grilla[filas][columnas-1] == '0'):
            grilla[filas][columnas-1] = '.'
        else:
            grilla[filas][columnas-1] = '0'
    if(columnas < (tamaño-1)):
        if (grilla[filas][columnas+1] == '0'):
            grilla[filas][columnas+1] = '.'
        else:
            grilla[filas][columnas+1] = '0'
    if(int(filas) > 1):
        if (grilla[str(int(filas)-1)][columnas] == '0'):
            grilla[str(int(filas)-1)][columnas] = '.'
        else:
            grilla[str(int(filas)-1)][columnas] = '0'
    if (int(filas) < tamaño):
        if (grilla[str(int(filas)+1)][columnas] == '0'):
            grilla[str(int(filas)+1)][columnas] = '.'
        else:
            grilla[str(int(filas)+1)][columnas] = '0'
    return(grilla)

def convertir_coordenadas(coordenadas):
    filas = int(coordenadas[1])-1
    if((coordenadas[0] == "A") or (coordenadas[0] =="a")): #Se puede simplificar en un diccionario
        columnas = 0
    if ((coordenadas[0] == "B") or (coordenadas[0] == "b")):
        columnas = 1
    if ((coordenadas[0] == "C") or (coordenadas[0] == "c")):
        columnas = 2
    if ((coordenadas[0] == "D") or (coordenadas[0] == "d")):
        columnas = 3
    if ((coordenadas[0] == "E") or (coordenadas[0] == "e")):
        columnas = 4
    if ((coordenadas[0] == "F") or (coordenadas[0] == "f")):
        columnas = 5
    if ((coordenadas[0] == "G") or (coordenadas[0] == "g")):
        columnas = 6
    if ((coordenadas[0] == "H") or (coordenadas[0] == "i")):
        columnas = 7
    if ((coordenadas[0] == "J") or (coordenadas[0] == "j")):
        columnas = 8

    return (filas,columnas)

def devolverTablero(nivel): #no hay generacion de nada, tengo q validar lo datos de entrada!!
    #La funcion unicamente te crea la grilla si la variable de entrada esta entre 1 y 5
    lista = [[['0','0','.','0','0'],['0','.','0','.','0'],['.','0','0','0','.'],['0','.','0','.','0'],['0','0','.','0','0']],
             [['.','0','.','0','.'],['0','0','.','0','0'],['.','0','.','0','.'],['0','.','0','.','0'],['0','.','0','.','0']],
             [['0','.','.','.','0'],['0','0','.','0','0'],['.','.','0','.','.'],['0','.','0','.','.'],['0','.','0','0','.']],
             [['0','0','.','0','0'],['.','.','.','.','.'],['0','0','.','0','0'],['.','.','.','.','0'],['0','0','.','.','.']],
             [['.','.','.','0','0'],['.','.','.','0','0'],['.','.','.','.','.'],['0','0','.','.','.'],['0','0','.','.','.']]]

    return (lista[nivel-1])




def verificar_juego(grilla,tamaño): #juego ganado
    ganar = 1
    for numero in range(1,(tamaño+1)):
        posicionV = str(numero)
        for caracter in grilla[posicionV]:
            if(caracter == "0"):
                ganar = 0
    return (ganar)

def control(movimientos,ganar,puntaje,limite):
    movimientos = movimientos + 1
    print("Movimientos: ", str(movimientos), "de" , str(limite))

    if(movimientos == limite):
        print("Ha superado la cantidad de movimientos maximos, el juego sera reiniciado")
        movimientos = 0
        ganar = 2
        puntaje = puntaje - 300
        print()
    return (movimientos,ganar,puntaje)

def inicializarNiveles():
    global nivel
    global reiniciar
    nivel = 1
    reiniciar = False