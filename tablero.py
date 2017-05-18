def inicializarTablero():
    import niveles

    global tablero
    global tamaño
    tablero = niveles.generacion_grilla(1)

def verificarJuegoGanado(grilla,tamaño):

    for numero in range(1,(tamaño+1)):
        posicionV = str(numero)
        for caracter in grilla[posicionV]:
            if(caracter == "0"):
                return False
    return (True)

def bajarNuevoTabblero(nivel):
    import niveles

    global tablero

    tablero = niveles.devolverTablero(nivel)


def imprimirTablero (nivel,tamaño): #Grilla no, es un tablero
    import niveles

    print("Nivel " + str(nivel) + ":")
    final = niveles.limite(tamaño)
    print("    ",end='')
    for a in range(1,tamaño+1):
        letra = niveles.limite(a)
        print(letra[1],end=' ')
    print()
    for numero in range(0,(tamaño)):
        print(str(numero) + " | ",end="")
        for elemento in tablero[numero]:
            print(elemento, end=" ")
        print()
    print()

inicializarTablero()
bajarNuevoTabblero(1)
imprimirTablero(3,5)