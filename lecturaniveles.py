def crearTablero(tamaño):
    tablero = []
    for j in range (0,int(tamaño)):
        tablero.append([])
        for i in range (0,int(tamaño)):
            tablero[j].append([])

    return(tablero)

def validarNivelDelRenglon(caracter,nivel):
    if(caracter == str(nivel)):
        return True
    return False

def validarDatosRenglon(informacion):
    import rogger

    if (informacion[1] >= "0" and informacion[1] <= "9"):
        tamaño = int(informacion[1])
    else:
        rogger.guardar("El tamaño del nivel no es un numero posible")
        return False

    if (int(informacion[2]) > tamaño):
        rogger.guardar("El dato leido en la fila es mayor al tamaño posible")
        return False

    if(int(informacion[3]) > tamaño):
        rogger.guardar("El dato leido en la columna es mayor al tamaño posible")
        return False

    if(informacion[4] != "0" and informacion[4] != "."):
        rogger.guardar("El dato leido no es un caracter valido para el tablero")
        return False

    return True

def modificoTablero(datos,tablero):

    tablero[int(datos[2]) - 1][int(datos[3]) - 1] = datos[4]
    return (tablero)

def devolverTableroNuevo(nivel):
    with open("niveles.txt", "r") as f:

        cantidadCaracteres = 0
        for linea in f:
            informacion = []
            for caracter in linea:
                if(caracter != " " and caracter != None):
                    informacion.append(str(caracter))
                    cantidadCaracteres += 1

            if(validarNivelDelRenglon(informacion[0],nivel)):
                if(validarDatosRenglon(informacion)):
                    tablero = crearTablero(informacion[1])

    with open("niveles.txt", "r") as f:
        for linea in f:
            informacion = []
            for caracter in linea:
                if (caracter != " " and caracter != None):
                    informacion.append(str(caracter))
                    cantidadCaracteres += 1

            if (validarNivelDelRenglon(informacion[0], nivel)):
                if (validarDatosRenglon(informacion)):
                    tablero = modificoTablero(informacion, tablero)

    return tablero