import menu
import niveles

menu.bienvenida()
juego,tamaño = menu.modos_de_juego(0)
if((juego == "0") and (tamaño == 0)):
    juego,tamaño = menu.instrucciones()

if(juego == "3" or juego == "2"):
        print("Gracias por jugar a lights out")
        print("Vuelva pronto")
        exit()
nivel = 1
ganar = 0
reiniciar = 0
puntaje = 0

if (juego == "1"):
    while(True):
        grilla = niveles.generacion_grilla(nivel)
        while (ganar != 1):
            niveles.imprimir_grilla(nivel,grilla,tamaño)
            coordenadas = niveles.usuario_jugando(tamaño) #Falta definir que hago si elige reiniciar, tambien falta ver como juego
            if(coordenadas == "2"): #Elijio salir
                print("Gracias por jugar a lights out")
                print("Vuelva pronto")
                exit()
            elif(coordenadas == "1"): #Reinicio
                puntaje = niveles.puntaje_por_encendidas(puntaje,grilla,tamaño)
                print(puntaje)
            #else: #Jugo
        nivel = nivel + 1