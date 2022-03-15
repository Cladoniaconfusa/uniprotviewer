from TXONES import taxons
from Argumentos_entrada import arg,verificar_fieldlist
from AND import verificar_and
from COUNT import conteos
from PRINTER import mostrar_memoria,mostrar_taxones

def sondear_proteinas(dbpath,fieldlist,queries)-> tuple:
    handler = open(dbpath)    
    match:int=0
    archivos_procesados:int=0
    memory:list = []
   

    for line in handler:
        if line.startswith("ID"): # Si empieza en ID estoy en un registro
            memory.clear
            memory = [line[:-1]]
        elif line.startswith("//"): # Aqui se acabo el registro    
            if verificar_and(memory,queries):
                match +=1
                taxones = taxons(fieldlist,memory)
                mostrar_memoria(memory,fieldlist,taxones)
            archivos_procesados += 1  
        else:
            if line.startswith("  "):
                line = "SQ" + line[2:]
            memory.append(line[:-1])
    handler.close()
    mostrar_taxones(taxones)
    return(archivos_procesados,match)

def main():
    fieldlist = verificar_fieldlist()
    queries,dbpath = arg()
    archivos_procesados, coincidencias = sondear_proteinas(dbpath,fieldlist,queries)
    conteos(archivos_procesados, coincidencias)

if __name__ == "__main__":
    main()
