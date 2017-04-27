import menu
import niveles

menu.bienvenida()
juego,tamaño = menu.modos_de_juego(0)
if((juego == "0") and (tamaño == 0)):
    juego,tamaño = menu.instrucciones()

nivel = 1
if(juego=="3"):
        print("Gracias por jugar a lights out")
        print("Vuelva pronto")
        exit()

while (True):
    if (juego == "1"):
        grilla = niveles.generacion(nivel)
        niveles.imprimir(nivel,grilla)
        nivel = nivel + 1
        coordenadas = niveles.usuario_jugando(tamaño)
        juego,tamaño = menu.modos_de_juego(1)

    if(juego=="3" or juego=="2"):
        print("Gracias por jugar a lights out")
        print("Vuelva pronto")
        exit()