
import sys
from genericpath import isfile

def arg():
    dbpath = sys.argv[1]
    if ".and." in sys.argv[2]:
        queries = sys.argv[2].split(".and.") 
    else:
        queries = [sys.argv[2]] 
    return(queries,dbpath)


def error1():
    print("Faltan argumentos")
    exit()


def error2():
    print("Archivo de datos invalido")
    exit()


def mostrar_memoria(memory,fieldlist,taxones):
    for line in memory:
        if "SHOWALL" in fieldlist or fieldlist == "allfields":
            print(line)
            print("//")
        elif "TAXONS" in fieldlist:
                print(taxones)
                print("//") 
        else:
            for j in fieldlist:
                if j == line[:2]:
                    print(line)
                    print("//")        


def verificar_fieldlist()->list:
    
    if len(sys.argv) == 3:
        fieldlist = "allfields"
    elif  len(sys.argv) <= 1:
            error1()
    elif  isfile(sys.argv[1]) == False or len(sys.argv) == 2:
            error2()
    else:
        fieldlist = sys.argv[3:]
    return(fieldlist)


def verificar_and(memory:list,queries:list)->bool:
    cnt = len(queries)
    for termino in queries:
        value_to_match,campo = termino.split(".in.")
        for line in memory:
            campo_bd = line[:2]
            value_bd = line[2:].strip()
            if campo == campo_bd and value_to_match in value_bd :
                cnt -=1
                break
    return(cnt == 0)


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


def taxons(fieldlist:list,memory:list,taxones:list):
    for t in memory:
        if "TAXONS" in fieldlist and t.startswith("OC"):
                lista_tx = t[:-1].split(";")
                for tx in lista_tx:
                    if not tx in taxones.keys():
                        taxones[tx] = 1
                    else:
                        taxones[tx] = taxones[tx] + 1
    return(taxones)


def sondear_proteinas(dbpath,fieldlist,queries)-> tuple:
    handler = open(dbpath)    
    match:int=0
    archivos_procesados:int=0
    memory:list = []
    taxones:dict = {}

    for line in handler:
        if line.startswith("ID"): # Si empieza en ID estoy en un registro
            memory.clear
            memory = [line[:-1]]
        elif line.startswith("//"): # Aqui se acabo el registro    
            if verificar_and(memory,queries):
                match +=1
                taxons(fieldlist,memory,taxones)
                mostrar_memoria(memory,fieldlist,taxones)
            archivos_procesados += 1  
        else:
            if line.startswith("  "):
                line = "SQ" + line[2:]
            memory.append(line[:-1])
    handler.close()
    return(archivos_procesados,match,taxones)


def main():
    fieldlist = verificar_fieldlist()
    queries,dbpath = arg()
    archivos_procesados, coincidencias,taxones = sondear_proteinas(dbpath,fieldlist,queries)
    conteos(archivos_procesados, coincidencias)


if __name__ == "__main__":
    main()


