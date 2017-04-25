import menu
import niveles

menu.Bienvenida()
juego,tamaño = menu.ModosDeJuego(0)
if((juego == 0) and (tamaño==0)):
    juego,tamaño = menu.Instrucciones(2)

nivel = 1
while (juego != 3):
    if (juego == 1):
        grilla = niveles.Generacion(nivel)
        niveles.Imprimir(nivel,grilla)
        nivel = nivel + 1
    juego,tamaño = menu.ModosDeJuego(1)