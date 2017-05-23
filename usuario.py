import tablero
import menu

def incializarUsuario():
    global puntaje
    global nivel
    puntaje = [0, 0, 0, 0, 0]
    nivel = 1

def puntaje_por_encendidas(grilla,tamaño):
    global puntaje
    global nivel

    for numero in range(1,(tamaño+1)):
        posicion = str(numero)
        for caracter in grilla[posicion]:
            if(caracter == "0"):
                puntaje[nivel-1] = puntaje[nivel-1]-50
    return (puntaje)

def modificarPuntaje (incremento):
    global puntaje
    global nivel
    puntaje[nivel] = puntaje[nivel] + incremento
    if(incremento < 0):
        tablero.bajarNuevoTabblero(nivel)

def usuarioGano():
    import juego
    global nivel
    global puntaje

    puntaje[nivel - 1] = puntaje[nivel - 1] + 500
    if(nivel < 5):
        print("Felicidades ha logrado completar el nivel " + str(nivel))
        print("Su puntaje actual es de " + str(puntaje[0]+puntaje[1]+puntaje[2]+puntaje[3]+puntaje[4]))
        print()
        nivel = nivel + 1

        tablero.bajarNuevoTabblero(nivel)
        juego.reiniciarMovimientos()
    else:
        print("Felicidades ha logrado completar todos los niveles")
        menu.imprimir_puntaje(puntaje)

def imprimirGrilla():
    tablero.imprimirTablero(nivel)

def nivelSuperado():
    #import juego
    global puntaje
    global nivel
    puntaje[nivel - 1] = puntaje[nivel - 1] + 500
    if (nivel < 5):
        print("Felicidades ha logrado completar el nivel " + str(nivel))
        print("Su puntaje actual es de " + str(puntaje[0] + puntaje[1] + puntaje[2] + puntaje[3] + puntaje[4]))
        print()
        nivel = nivel + 1
        tablero.bajarNuevoTabblero(nivel)
     #   juego.reiniciarMovimientos()
    else:
        print("Felicidades ha logrado completar todos los niveles")
        menu.imprimir_puntaje(puntaje)
        exit()