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
    return ()

def validar_coordenadas_ingresadas (a,tamaño):
    final = limite(tamaño)
    global coordenadas
    if(len(a) < 1):
        return False

    if ((len(a) == 1) and (a != "R" and a != "r")):
        return False

    if((len(a) == 1) and (a == "R" or a == "r")):
        return True

    if(len(a) > 2):
        print("Recuerde ingresar solo dos valores")
        return False

    if(a[1] < "A"):
        if ((int(a[1]) > tamaño) or (int(a[1]) <= 0)):
            print("El numero de las filas ingresado es invalido")
            return False
    else:
        print("La segunda coordenada debe ser un numero referido a las filas")
        return False

    if ((a[0] < "a" or a[0] > final[0]) and (a[0] < "A" or a[0] > final[1])):
        print("La letra referida a las columnas ingresada es invalida")
        return False
    print()
    return True

def usuario_jugando(tamaño):
    global coordenadas
    print("¿Que desea hacer a continuacion?")
    print("Ingresar coordenadas para jugar")
    print("R - Reiniciar el nivel y restar 50  puntos por cada luz encendida")
    coordenadas = input("Opcion elegida: ")

    while(not validar_coordenadas_ingresadas(coordenadas,tamaño)):
        print("La opcion elegida no es valida, recuerde: ")
        print("Ingresar coordenadas para jugar")
        print("R - Reiniciar el nivel y restar 50  puntos por cada luz encendida")
        coordenadas = input("Opcion elegida: ")

    return (coordenadas)

def convertir_coordenadas(coordenadas,tamaño):
    if(not validar_coordenadas_ingresadas(coordenadas,tamaño)):
        return False
    filas = int(coordenadas[1])-1
    clave = coordenadas[0]
    columnas = {
        'A': 0,
        'B': 1,
        'C': 2,
        'D': 3,
        'E': 4,
        'G': 5,
        'H': 6,
        'J': 7
    }
    return (filas,columnas[clave.upper()])

def devolverTablero(nivel): #no hay generacion de nada, tengo q validar lo datos de entrada!!
    #La funcion unicamente te crea la grilla si la variable de entrada esta entre 1 y 5
    lista = [[['0','0','.','0','0'],['0','.','0','.','0'],['.','0','0','0','.'],['0','.','0','.','0'],['0','0','.','0','0']],
             [['.','0','.','0','.'],['0','0','.','0','0'],['.','0','.','0','.'],['0','.','0','.','0'],['0','.','0','.','0']],
             [['0','.','.','.','0'],['0','0','.','0','0'],['.','.','0','.','.'],['0','.','0','.','.'],['0','.','0','0','.']],
             [['0','0','.','0','0'],['.','.','.','.','.'],['0','0','.','0','0'],['.','.','.','.','0'],['0','0','.','.','.']],
             [['.','.','.','0','0'],['.','.','.','0','0'],['.','.','.','.','.'],['0','0','.','.','.'],['0','0','.','.','.']]]

    return (lista[nivel-1])

def inicializarNiveles():
    global nivel
    global reiniciar
    nivel = 1
    reiniciar = False