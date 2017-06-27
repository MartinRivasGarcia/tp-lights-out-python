import log

archivo_log = "errores.txt"

def abrir():
    global archivo
    archivo = log.abrir(archivo_log)

def guardar(texto):
    log.guardar(archivo,texto)

def cerrar():
    log.cerrar(archivo)