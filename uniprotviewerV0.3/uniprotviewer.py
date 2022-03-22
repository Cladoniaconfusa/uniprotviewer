from FASTA import fasta_generator
from TXONES import taxons
from Argumentos_entrada import arg,verificar_fieldlist
from VER_AND import verificar_and
from COUNT import conteos
from PRINTER import mostrar_memoria,mostrar_taxones
from DBINSERT import dbinsert_arg, dbinsert_tablas,dbinsert_ver

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
                if "DBINSERT" in fieldlist:
                    dbinsert_tablas(memory)
                taxones = taxons(fieldlist,memory)
                mostrar_memoria(memory,fieldlist)
                print("//")
            archivos_procesados += 1  
        else:
            if line.startswith("  "):
                line = "SQ" + line[2:]
            elif "FASTA" in fieldlist:
                fasta_generator(memory)
            memory.append(line[:-1])
    handler.close()
    mostrar_taxones(taxones,fieldlist)
    return(archivos_procesados,match)

def main():
    queries,dbpath = arg()
    rutadb = dbinsert_arg()
    fieldlist = verificar_fieldlist()
    dbinsert_ver(fieldlist,rutadb)
    archivos_procesados, coincidencias = sondear_proteinas(dbpath,fieldlist,queries)#rutadb j
    conteos(archivos_procesados, coincidencias)

if __name__ == "__main__":
    main()