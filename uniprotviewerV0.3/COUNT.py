import sys

def conteos(archivos_procesados,coincidencias)->None:
    if "COUNT" in sys.argv and "COUNTALL" in sys.argv:
        print("Archivos procesados:", archivos_procesados)
        print("Matches:", coincidencias)
        p = coincidencias/archivos_procesados
        print("Porcentaje de matches:", str(p*100) + "%" )
    elif "COUNTALL" in sys.argv:
        print("Archivos procesados:", archivos_procesados)
        print("Matches:", coincidencias)
    elif "COUNT" in sys.argv:
        print("Matches:", coincidencias)


