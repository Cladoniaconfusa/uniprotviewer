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
