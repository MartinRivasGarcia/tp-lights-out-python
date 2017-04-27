import menu
import niveles

menu.bienvenida()
juego,tamaño = menu.modos_de_juego(0)
if((juego == "0") and (tamaño == 0)):
    juego,tamaño = menu.instrucciones()

if(juego=="3" or juego=="2"):
        print("Gracias por jugar a lights out")
        print("Vuelva pronto")
        exit()
nivel = 1
ganar = 0
reiniciar = 0
puntaje = 0
if (juego == "1"):
    while(True):
        grilla = niveles.generacion(nivel)
        while (ganar != 1):
            niveles.imprimir(nivel,grilla)
            coordenadas = niveles.usuario_jugando(tamaño) #Falta definir que hago si elige reiniciar, tambien falta ver como juego
            if(coordenadas == "2"):
                print("Gracias por jugar a lights out")
                print("Vuelva pronto")
                exit()
            if(coordenadas == "1"):
                grilla = niveles.usuario_jugo(coordenadas)
    nivel = nivel + 1