import niveles
import usuario
#import tablero

def inicializarJuego ():
    niveles.movimientos = 0

    ganar = False
    niveles.inicializarNiveles()
    usuario.inicializarUsuario()
    #tablero.inicializarTablero()
    desarrolloJuego ()

    #esto deberia ser despues de generar tamaño, y quizas sirve meterlo en una funcion
    niveles.limite = tablero.tamaño * 3

def desarrolloJuego ():
    while(True): #Aca tengo que meter todo el despligue de logica de principal.py


def control(ganar,puntaje):
    niveles.movimientos = niveles.movimientos + 1
    print("Movimientos: ", str(niveles.movimientos), "de" , str(niveles.limite))

    if(niveles.movimientos == niveles.limite):
        print("Ha superado la cantidad de movimientos maximos, el juego sera reiniciado")
        #Deberia reiniciar con una funcion
        niveles.movimientos = 0
        ganar = 2 #Voy a cambiar totalmente el concepto de la variable ganar
        puntaje = puntaje - 300 #deberia avisarle a usuario.py q modifique el valor de puntaje
        print()
    return (ganar,puntaje)