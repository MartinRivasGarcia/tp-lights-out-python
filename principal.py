import menu
import niveles
import aleatorio

menu.bienvenida()
entro = 0


while(True):
    #quizas todo esto conviene meterlo en un modulo por ejemplo juego.py
    if(entro == 0):
        juego, tamaño = menu.modos_de_juego(0) #tamaño va a tener q guardarse en tablero.py y juego en juego.py
        if ((juego == "0") and (tamaño == 0)): #Tratar de cambiar quizas por una funcion q devuelva un booleano, no es claro 1 y 0
            juego, tamaño = menu.instrucciones()

        if (juego == "3"):
            print("Gracias por jugar a lights out")
            print("Vuelva pronto")
            exit()
        #No deberia tener declaracion de variables o logica en el principal
        nivel = 1 #El nivel actual podría solo pertenecer a niveles.py
        ganar = 0 #Deberia pertenecer solo a juego.py
        reiniciar = 0 #Deberia pertenecer solo a niveles.py
        puntaje = [0, 0, 0, 0, 0] #Deberia pertenecer solo a usuario.py
        movimientos = 0  #Deberia pertenecer solo a juego.py
        limite = tamaño * 3 #Deberia pertenecer solo a juego.py

        #Grilla podria pertenecer unicamente al modulo niveles
        if (juego == "1"):
            grilla = niveles.generacion_grilla(nivel)
        if (juego == "2"):
            grilla = aleatorio.generar_grilla(tamaño)

        entro = 1 #la variable entro no tiene porque existir

    while ((ganar != 1) and (ganar != 2)):
        niveles.imprimir_grilla(nivel,grilla,tamaño)
        coordenadas = niveles.usuario_jugando(tamaño)

        if(coordenadas == "R" or coordenadas == "r"): #Esto no tiene porq estar aca, tranquilamente puede ser una funcion que resiva coordenadas
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
            movimientos,ganar,puntaje[nivel-1] = niveles.control(movimientos,ganar,puntaje[nivel-1],limite) #Esta funcion resive muchos parametros
            if(ganar == 2):
                menu.imprimir_puntaje(puntaje) #puntaje podria pertenecer solo a un modulo usuario.py
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