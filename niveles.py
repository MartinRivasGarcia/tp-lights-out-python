def Generacion(nivel):
    if (nivel == 1):
        lista = [
            '0 0 . 0 0',
            '0 . 0 . 0',
            '. 0 0 0 .',
            '0 . 0 . 0',
            '0 0 . 0 0',
        ]
    if (nivel == 2):
        lista = [
            '. 0 . 0 .',
            '0 0 . 0 0',
            '. 0 . 0 .',
            '0 . 0 . 0',
            '0 . 0 . 0',
        ]
    if (nivel == 3):
        lista = [
            '0 . . . 0',
            '0 0 . 0 0',
            '. . 0 . .',
            '0 . 0 . .',
            '0 . 0 0 .',
        ]
    if (nivel == 4):
        lista = [
            '0 0 . 0 0',
            '. . . . .',
            '0 0 . 0 0',
            '. . . . 0',
            '0 0 . . .',
        ]
    if (nivel == 5):
        lista = [
            '. . . 0 0',
            '. . . 0 0',
            '. . . . .',
            '0 0 . . .',
            '0 0 . . .',
        ]
    return (lista)

def Imprimir (nivel,grilla):
    print("Usted esta jugando el nivel " + str(nivel) + ":")
    print("   A B C D E ")
    numero = 1
    for renglon in grilla:
        print(str(numero) + " |" + renglon)
        numero = numero + 1

def UsuarioJugando (tamaño):
    a = input("Ingrese las coordenadas a utilizar: ")
    if ((int(a[0]) > tamaño) or (int(a[0]) <= 0)):
        print("El numero de las filas ingresado es invalido")
        error = 1
    if ((a[1] < "a" or a[1] > "e") and (a[1] > "A" or a[1] < "E")):
        print("La letra referida a las columnas ingresada es invalida")
        error = 1
    while(error == 1):
        a = input("Reingrese las coordenadas a utilizar: ")
        if ((int(a[0]) > tamaño) or (int(a[0]) <= 0)):
            print("El numero de las filas ingresado es invalido")
            error = 1
        else:
            error = 0
        if ((a[1] < "a" or a[1] > "e") and (a[1] > "A" or a[1] < "E")):
            print("La letra referida a las columnas ingresada es invalida")
            error = 1
    print(a)

#Tener en cuenta para el modo de juego alternativo
def GenerarRandom():
    import random
    caracter = random.random() #Devuelve entre 0.0 y 1.0
    if (caracter > 0.5):
        caracter = 0
    else:
        caracter = "."
    return(caracter)