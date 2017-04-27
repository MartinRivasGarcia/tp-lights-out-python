def bienvenida(): #Imprime texto en pantalla solo si se llama
    print("Binvenido a: ")
    print("         Lights out!!!!")
    print()

def instrucciones(): #Imprime el texto en pantalla q sea requerido
    print("Este juego consiste en lograr apagar todas las luces de un tablero, las cuales")
    print("estaran simbolizadas por 0 si estan prendidas o por . si estan apagadas. Para ")
    print("lograr apagar todas las luces se debe ingresar la direccion de la luz que quiere")
    print("apagar. Al tocarse una luz no solo se cambiara el estado de la misma sino tambien")
    print("de aquellas que esten tanto a sus lados como arriba y abajo.")
    print()
    print("Modo aleatorio: Se genera un tablero al azar de medidas al azar")
    print()
    print("Modo predeterminado: Consiste en pasar una secuencia de niveles preestablecida, los caules")
    print(" deben ser superados en 15 movimientos, en la cual ademas se llevara la cuenta del puntaje")
    print()
    juego = modos_de_juego(1)
    return juego

def modos_de_juego(paso):
    tamaño=0
    if(paso == 0):
        print("Eliga una de las siguientes opciones para iniciar: ")
        print("1 - Predeterminado")
        print("2 - Aleatorio")
        print("3 - Salir")
        print("0 - Instrucciones")
        juego = input("Opcion elegida: ")

        while ((juego != "0") and (juego != "1") and (juego != "2") and (juego != "3")):
            print("El valor ingresado no es valido, recuerde:")
            print("1 - Predeterminado")
            print("2 - Aleatorio")
            print("3 - Salir")
            print("0 - Instrucciones")
            juego = input("Reingrese su eleccion: ")
        print()

    if(paso == 1):
        print("Eliga una de las siguientes opciones para continuar: ")
        print("1 - Predeterminado")
        print("2 - Aleatorio")
        print("3 - Salir")
        juego = input("Opcion elegida: ")
        while ((juego != "1") and (juego != "2") and (juego!="3")):
            print("El valor ingresado no es valido, recuerde:")
            print("1 - Predeterminado")
            print("2 - Aleatorio")
            print("3 - Salir")
            juego = input("Reingrese su eleccion: ")
        print()

    if(juego == "1"):
        print("Usted ha elegido el modo predeterminado")
        print()
        tamaño = 5
    if(juego == "2"):
        print("Usted ha elegido el modo aleatorio")
        print()
        tamaño = 6
    return (juego,tamaño)