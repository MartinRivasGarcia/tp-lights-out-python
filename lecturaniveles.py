nivel = 1
def crearTablero(tamaño):
    tablero = []
    for j in range (0,tamaño):
        tablero.append([])
        for i in range (0,tamaño):
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

    if(int(informacion[3]) < tamaño):
        rogger.guardar("El dato leido en la columna es mayor al tamaño posible")
        return False

    if(informacion[4] != "0" and informacion[3] != "."):
        rogger.guardar("El dato leido no es un caracter valido para el tablero")
        return False

    return True

def modificoTablero(datos,tablero):
    print(tablero)
    print(datos[2])
    print(datos[3])
    print(datos[4])
    print(tablero[datos[2]][datos[3]])
    tablero[datos[2]][datos[3]] = datos[4]
    return (tablero)
'''
with open("niveles.txt", "r") as f:
    informacion = []
    a = 0
    nivel = 1
    cantidadCaracteres = 0
    for linea in f:
        if(a > 0):

            for caracter in linea:
                if(caracter != " " and caracter != None):
                    informacion.append(str(caracter))
                    cantidadCaracteres += 1

            if(validarNivelDelRenglon(informacion,nivel)):
                if(validarDatosRenglon(informacion)):
                    tablero = crearTablero(informacion[1])
                    tablero = modificoTablero(informacion,tablero)
        a += 1
        if(a == 3):
            exit()
'''
datos = (0,0,2,3,".")
tablero = crearTablero(5)
print(modificoTablero(datos,tablero))