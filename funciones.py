import json
import sys

def Leer_Json(fichero):
    try:
        with open(fichero) as f:
            datos = json.load(f)
        return datos
    except:
        print("Error al leer el fichero")
        sys.exit
