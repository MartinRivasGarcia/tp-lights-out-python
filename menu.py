def Bienvenida(): #Imprime texto en pantalla solo si se llama
    print("Binvenido al juego light out")
    info = (input("Si desea saber las instrucciones presione 1: "))
    Instrucciones(int(info))

def Instrucciones(info): #Imprime el texto en pantalla q sea requerido
    if(info == 1):
        print("El juego consiste en lograr apagar todas las luces de un tablero, las cuales")
        print("estaran simbolizadas por 0 si estan prendidas o por . si estan apagadas.")
        print("Para lograr apagar todas las luces el usuario tiene que ingresar la direccion de")
        print("la luz que quiere apagar. Al tocarse una luz no solo se cambiara el estado de la ")
        print("misma sino tambien de aquellas q esten tanto a sus lador como arriba y abajo.")
    if(info == 2):
        print("Modo aleatorio: Se genera un tablero al azar de medidas al azar")
        print("Modo predeterminado: Consiste en pasar una secuencia de niveles preestablecida y")
        print("suma el correspondiente puntaje. El puntaje se cuenta sumando 500 si se apagaron")
        print("todas las luces, si se queda sin movimientos resta 300, si reinicia resta 50 por")
        print("por cada luz que haya quedado encendida.")
        juego = ModosDeJuego(1)
        return juego

def ModosDeJuego(paso):
    if(paso == 0):
        juego = int(input("Elegir modo de juego predeterminado con 1, aleatorio con 2 o cero si requiere instruciones. Presione 3 si desea salir: "))
        while ((juego != 1) and (juego != 2) and (juego != 0) and (juego != 3)):
            juego = int(input("Reingrese el valor, recuerde elergir 1 para predeterminado o 2 para aleatorio y 3 para salir, cero si necesita instrucciones: "))

    if(paso == 1):
        juego = int(input("Elegir modo de juego predeterminado con 1 o aleatorio con 2 y 3 para salir: "))
        while ((juego != 1) and (juego != 2)):
            juego = int(input("Reingrese el valor, recuerde elegir 1 para predeterminado o 2 para aleatorio o 3 si desea salir: "))
    return (juego)
def Adevertencia():
    print("Recuerde ingresar la valor de la fila y de la columna, de la siguiente forma: Letra columna Numero Fila")