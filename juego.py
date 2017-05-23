import niveles
import usuario
import tablero
import menu

def inicializarJuego():
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

    desarrolloJuego()

    # esto deberia ser despues de generar tamaño, y quizas sirve meterlo en una funcion
    # tablero.tamaño


def desarrolloJuego():
    menu.bienvenida()
    juegoElegido()
    while (True):  # Aca tengo que meter todo el despligue de logica de principal.py
        usuario.imprimirGrilla()
        tablero.modificarGrilla()
        if(tablero.verificarTableroVacio()):
            usuario.nivelSuperado()
        else:
            control()


def control():
    global movimientos
    global reiniciar
    movimientos = movimientos + 1

    print("Movimientos: ", str(movimientos), "de", str(limite))

    if (movimientos == limite):
        print("Ha superado la cantidad de movimientos maximos, el juego sera reiniciado")
        # Deberia reiniciar con una funcion
        movimientos = 0
        reiniciar = True
        usuario.modificarPuntaje(-300)
        print()


def reiniciarMovimientos():
    global movimientos
    movimientos = 0

def juegoElegido():
    global juego
    juego, tamaño = menu.modos_de_juego(0)  # tamaño va a tener q guardarse en tablero.py y juego en juego.py
    if ((juego == "0") and (tamaño == 0)):  # Tratar de cambiar quizas por una funcion q devuelva un booleano, no es claro 1 y 0
        juego, tamaño = menu.instrucciones()
    verificarSiEligioSalir()

    tablero.inicializarTablero(tamaño)

def verificarSiEligioSalir():
    if(juego == 3):
        print("Gracias por jugar a lights out")
        print("Vuelva pronto")
        exit()

def reiniciarMovimientos():
    global movimientos
    movimientos = 0
inicializarJuego()