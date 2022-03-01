from genericpath import isfile
import sys

def ver_fieldlist():

    if len(sys.argv) == 3:
        fieldlist = "allfields" 
        return(fieldlist)
    elif  len(sys.argv) <= 2:
            print("Error en campos de busqueda")
    else:
        if isfile(sys.argv[1]) == False:
            print ("Nombre del archivo no valido")
        else:
            fieldlist = sys.argv[3:]
            return(fieldlist)
            
        

