def generar_random():
    import random
    caracter = random.random() #Devuelve entre 0.0 y 1.0
    if (caracter > 0.5):
        caracter = 0
    else:
        caracter = "."
    return(caracter)

def generar_grilla(tamaño):
    grilla = []
    for a in range(0,tamaño):
        grilla.append([])
        for b in range(0,tamaño):
            grilla[a].append(generar_random())
    return grilla