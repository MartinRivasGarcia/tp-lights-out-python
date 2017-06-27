import datetime

def abrir(nombre_log):
    archivo_log = open(nombre_log, "a")
    guardar(archivo_log, "Iniciando registro de errores")
    return archivo_log

def guardar(archivo_log, mensaje):
    hora_actual = str(datetime.datetime.now())
    archivo_log.write("[{}] {} \n".format(hora_actual,mensaje))

def cerrar(archivo_log):
    guardar(archivo_log, "Fin del registro de errores")
    archivo_log.close()