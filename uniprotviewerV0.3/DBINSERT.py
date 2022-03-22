import sys
from genericpath import isfile
import os
from attr import field
from TABLAS import tabla_codes,tabla_comments,tabla_dates,tabla_fasta,tabla_features,tabla_names,tabla_protein
#from PRINTER import mostrar_tablas

def dbinsert_arg():
    for i in sys.argv:
        if i.startswith("db="):
            z = i.split("=")
            rutadb = z[1]
    return(rutadb)

def dbinsert_ver(fieldlist,rutadb):
    for i in fieldlist :
        if not i.startswith("db=") and "INSERTDB" in fieldlist:
            print("falta base de datos")
            os._exit(0)
    if isfile(rutadb) == False:
        print("No existe base de datos")
        os._exit(0)
    return()
    
def dbinsert_tablas(memory):
    for i in memory:
        if i.startswith("ID"):
            a = i.split("  ")
            ID = a[1]
    tabla_names(memory,ID)
    tabla_protein(memory,ID)
    tabla_dates(memory,ID)
    tabla_codes(memory,ID)
    tabla_comments(memory,ID)
    tabla_features(memory,ID)
    tabla_fasta(memory,ID)
#    mostrar_tablas(names,protein,dates,codes,comments,features,fasta)

