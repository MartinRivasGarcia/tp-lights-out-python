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
    return (0,0)

def validar_coordenadas_ingresadas (a,tamaño):
    import rogger

    final = limite(tamaño)
    global coordenadas
    if(len(a) < 1):
        rogger.guardar("El dato ingresado esta vacio")
        return False

    if ((len(a) == 1) and (a != "R" and a != "r")):
        rogger.guardar("El dato ingresado no indica ninguna accion")
        return False

    if((len(a) == 1) and (a == "R" or a == "r")):
        return True

    if(len(a) > 2):
        print("Recuerde ingresar solo dos valores")
        rogger.guardar("El dato ingresado es mayor a dos valores")
        return False

    if(a[1] < "A" and a[1] > "/"):
        if ((int(a[1]) > tamaño) or (int(a[1]) <= 0)):
            print("El numero de las filas ingresado es invalido")
            rogger.guardar("El numero de las filas ingresado es invalido")
            return False
    else:
        print("La segunda coordenada debe ser un numero referido a las filas")
        rogger.guardar("Se ingreso un caracter incorrecto referido a las filas")
        return False
    if(final[0] == 0):
        return False
    if ((a[0] < "a" or a[0] > final[0]) and (a[0] < "A" or a[0] > final[1])):
        print("La letra referida a las columnas ingresada es invalida")
        rogger.guardar("La letra referida a las columnas ingresada es invalida")
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
        return (False,False)
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

    if str(nivel) > '5' or str(nivel) < '1':
        return False
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