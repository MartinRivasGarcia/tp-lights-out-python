def guardar_puntajes(puntajes):
    with open("puntaje.txt", "w") as f:
        for nombre, puntaje, tiempo in puntajes:
            f.write("{},{},{}\n".format(nombre,puntaje,tiempo))

def recuperar_puntajes():
    puntajes = []
    with open("puntaje.txt", "r") as f:
        for linea in f:
            nombre, puntaje, tiempo = linea.rstrip("\n").split(",")
            puntajes.append((nombre, int(puntaje),tiempo))
    return puntajes