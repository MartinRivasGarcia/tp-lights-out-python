import menu
menu.Bienvenida()
juego = menu.ModosDeJuego(0)
if(juego == 0):
    juego = menu.Instrucciones(2)