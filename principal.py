import menu
import niveles
import aleatorio

menu.bienvenida()
juego,tamaño = menu.modos_de_juego(0)
if((juego == "0") and (tamaño == 0)):
    juego,tamaño = menu.instrucciones()

if(juego == "3"):
        print("Gracias por jugar a lights out")
        print("Vuelva pronto")
        exit()
nivel = 1
ganar = 0
reiniciar = 0
puntaje = 0
movimientos = 0
limite = tamaño*3

if (juego == "1"):
    grilla = niveles.generacion_grilla(nivel)
if (juego == "2"):
    grilla = aleatorio.generar_grilla(tamaño)

while(True):
    while (ganar != 1):
        niveles.imprimir_grilla(nivel,grilla,tamaño)
        coordenadas = niveles.usuario_jugando(tamaño) #Falta definir que hago si elige reiniciar, tambien falta ver como juego
        if(coordenadas == "2"): #Elijio salir
            print("Su puntaje final fue " + str(puntaje))
            print("Gracias por jugar a lights out")
            print("Vuelva pronto")
            exit()
        elif(coordenadas == "1"): #Reinicio
            puntaje = niveles.puntaje_por_encendidas(puntaje,grilla,tamaño)
            print("Usted a reiniciado el nivel " + str(nivel))
            print("Su puntaje actual es " + str(puntaje))
            print()
            if(juego == "1"):
                grilla = niveles.generacion_grilla(nivel)
            else:
                grilla = aleatorio.generar_grilla(tamaño)
        else: #Jugo
            grilla = niveles.interactuar_con_el_tablero(grilla,coordenadas,tamaño)
            ganar = niveles.verificar_juego(grilla,tamaño)
            movimientos,ganar,puntaje = niveles.control(movimientos,ganar,puntaje,limite)
            if(ganar == 2):
                ganar = 0
                if(juego == "1"):
                    grilla = niveles.generacion_grilla(nivel)
                else:
                    grilla = aleatorio.generar_grilla(tamaño)

    if(nivel < 5):
        puntaje = puntaje + 500
        print("Felicidades a logrado completar el nivel " + str(nivel))
        print("Su puntaje acutal es de " + str(puntaje))
        print()
        nivel = nivel + 1
        if(juego == "1"):
            grilla = niveles.generacion_grilla(nivel)
        else:
            grilla = aleatorio.generar_grilla(tamaño)
        ganar = 0
        movimientos = 0
    else:
        print("Felicidades a logrado completar todos los niveles con un puntaje de",str(puntaje))
        exit()


