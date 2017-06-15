import niveles

def inicializarTablero(recibo):

    global tablero
    global tamaño
    tablero = niveles.devolverTablero(1)
    tamaño = recibo

def verificarJuegoGanado(grilla,tamaño):

    for numero in range(0,tamaño):
        posicionV = numero
        for caracter in grilla[posicionV]:
            if(caracter == "0"):
                return False
    return (True)

def bajarNuevoTabblero(nivel):

    global tablero
    tablero = niveles.devolverTablero(nivel)


def imprimirTablero (nivel):
    print("Nivel " + str(nivel) + ":")
    print("    ",end='')
    for a in range(1,tamaño+1):
        letra = niveles.limite(a)
        print(letra[1],end=' ')
    print()
    for numero in range(0,(tamaño)):
        print(str(numero+1) + " | ",end="")
        for elemento in tablero[numero]:
            print(elemento, end=" ")
        print()
    print()

def verificarSiEligioReiniciar():
    import usuario
    coordenadas = niveles.usuario_jugando(tamaño)

    if(coordenadas != "r" and coordenadas != "R"):
        interactuar_con_el_tablero(coordenadas)
        return False
    else:
        usuario.puntaje_por_encendidas(tablero, tamaño)
        return True

def interactuar_con_el_tablero(coordenadas):
    global tablero
    filas,columnas = niveles.convertir_coordenadas(coordenadas,tamaño)
    if(tablero[filas][columnas] == '0'):
        tablero[filas][columnas] = '.'
    else:
        tablero[filas][columnas] = '0'
    if(columnas > 0):
        if (tablero[filas][columnas-1] == '0'):
            tablero[filas][columnas-1] = '.'
        else:
            tablero[filas][columnas-1] = '0'
    if(columnas < (tamaño-1)):
        if (tablero[filas][columnas+1] == '0'):
            tablero[filas][columnas+1] = '.'
        else:
            tablero[filas][columnas+1] = '0'
    if(filas > 0):
        if (tablero[(filas)-1][columnas] == '0'):
            tablero[(filas)-1][columnas] = '.'
        else:
            tablero[(filas)-1][columnas] = '0'
    if (filas < (tamaño-1)):
        if (tablero[filas+1][columnas] == '0'):
            tablero[filas+1][columnas] = '.'
        else:
            tablero[filas+1][columnas] = '0'

def verificarTableroVacio():
    for numero in range(0, tamaño):
        for caracter in tablero[numero]:
            if (caracter == "0"):
                return False
    return True