import niveles
import usuario
import tablero

def inicializarJuego ():
    global movimientos
    global limite
    global ganar
    global reiniciar
    movimientos = 0
    limite = 15
    ganar = False
    reiniciar = False


    niveles.inicializarNiveles()
    usuario.incializarUsuario()
    tablero.inicializarTablero()
    #desarrolloJuego ()

    #esto deberia ser despues de generar tamaño, y quizas sirve meterlo en una funcion
    #tablero.tamaño

#def desarrolloJuego ():
 #   while(True): #Aca tengo que meter todo el despligue de logica de principal.py


def control(puntaje):
    global movimientos
    global reiniciar
    movimientos = movimientos + 1

    print("Movimientos: ", str(movimientos), "de" , str(limite))

    if(movimientos == limite):
        print("Ha superado la cantidad de movimientos maximos, el juego sera reiniciado")
        #Deberia reiniciar con una funcion
        movimientos = 0
        reiniciar = True
        usuario.modificarPuntaje(-300)
        print()

    return (puntaje)

def reiniciarMovimientos():
    global movimientos
    movimientos = 0