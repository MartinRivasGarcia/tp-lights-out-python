archivo_log = "puntaje.txt"

def guardar_puntajes(puntajes):
    with open(archivo_log, "w") as f:
        f.write("{},{}\n".format(puntajes[0],puntajes[1]))

def recuperar_puntajes():
    puntajes = []
    with open(archivo_log, "r") as f:
        for linea in f:
            puntaje, tiempo = linea.rstrip("\n").split(",")
            puntajes.append((int(puntaje),tiempo))
    return puntajes

def compararPuntaje(puntaje):
    puntajeViejo = recuperar_puntajes()

    from datetime import datetime
    now = datetime.now()

    if(puntaje > int(puntajeViejo[0][0])):
        puntajes = str(puntaje), str(now)
        guardar_puntajes(puntajes)