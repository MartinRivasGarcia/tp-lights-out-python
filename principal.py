import menu
import niveles
import aleatorio

menu.bienvenida()
entro = 0


while(True):
    if(entro == 0):
        juego, tamaño = menu.modos_de_juego(0)
        if ((juego == "0") and (tamaño == 0)):
            juego, tamaño = menu.instrucciones()

        if (juego == "3"):
            print("Gracias por jugar a lights out")
            print("Vuelva pronto")
            exit()
        nivel = 1
        ganar = 0
        reiniciar = 0
        puntaje = [0, 0, 0, 0, 0]
        movimientos = 0
        limite = tamaño * 3

        if (juego == "1"):
            grilla = niveles.generacion_grilla(nivel)
        if (juego == "2"):
            grilla = aleatorio.generar_grilla(tamaño)

        entro = 1

    while ((ganar != 1) and (ganar != 2)):
        niveles.imprimir_grilla(nivel,grilla,tamaño)
        coordenadas = niveles.usuario_jugando(tamaño) #Falta definir que hago si elige reiniciar, tambien falta ver como juego
        '''
        if(coordenadas == "2"): #Elijio salir
            print("Su puntaje final fue " + str(puntaje[0]+puntaje[1]+puntaje[2]+puntaje[3]+puntaje[4]))
            print("Gracias por jugar a lights out")
            print("Vuelva pronto")
            exit()
        '''
        if(coordenadas == "R" or coordenadas == "r"): #Reinicio
            puntaje[nivel-1] = niveles.puntaje_por_encendidas(puntaje[nivel-1],grilla,tamaño)
            print("Usted ha reiniciado el nivel " + str(nivel))
            print("Su puntaje actual es " + str(puntaje[0]+puntaje[1]+puntaje[2]+puntaje[3]+puntaje[4]))
            print()
            if(juego == "1"):
                grilla = niveles.generacion_grilla(nivel)
            else:
                grilla = aleatorio.generar_grilla(tamaño)
        else: #Jugo
            grilla = niveles.interactuar_con_el_tablero(grilla,coordenadas,tamaño)
            ganar = niveles.verificar_juego(grilla,tamaño)
            movimientos,ganar,puntaje[nivel-1] = niveles.control(movimientos,ganar,puntaje[nivel-1],limite)
            if(ganar == 2):
                menu.imprimir_puntaje(puntaje)
                entro = 0
    if(ganar == 1):
        puntaje[nivel - 1] = puntaje[nivel - 1] + 500
        if(nivel < 5):
            print("Felicidades ha logrado completar el nivel " + str(nivel))
            print("Su puntaje actual es de " + str(puntaje[0]+puntaje[1]+puntaje[2]+puntaje[3]+puntaje[4]))
            print()
            nivel = nivel + 1
            if(juego == "1"):
                grilla = niveles.generacion_grilla(nivel)
            else:
                grilla = aleatorio.generar_grilla(tamaño)
            ganar = 0
            movimientos = 0
        else:
            print("Felicidades ha logrado completar todos los niveles")
            menu.imprimir_puntaje(puntaje)
            entro = 0