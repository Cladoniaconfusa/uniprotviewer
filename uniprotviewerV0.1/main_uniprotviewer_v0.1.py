#from json.tool import main
import sys
from arg import arg
from verification_bd import ver_fieldlist

fieldlist = ver_fieldlist()
dbpath,value_to_match, campo = arg()

def sondear_proteinas(dbpath,value_to_match,campo,fieldlist):
    
    
    handler = open(dbpath)    
    match=0
    archivos_procesados=0
    memory = []
    salida= []

    for line in handler:

        if line.startswith("ID"): # Si empieza en ID estoy en un registro
            
            memory.clear
            memory = [line[:-1]]
                       

        elif line.startswith("//"): # Aqui se acabo el registro
            
            for argum in memory:
                if argum.startswith(campo) and value_to_match in argum: #ocurre el match 
                    match=+1
                    if fieldlist == "allfields":
                        for n in memory:
                            print(n)
                    else:
                        for x in memory:
                            if x[:2] in fieldlist:
                                print(x) 
                        print(salida)
            
            archivos_procesados= archivos_procesados + 1                    
        else:
            memory.append(line[:-1])
    handler.close()
    return(archivos_procesados,match)

archivos_procesados, coincidencias = sondear_proteinas(dbpath,value_to_match, campo,fieldlist) 
print("Archivos procesados:")
print(archivos_procesados)
print("Matches:")
print(coincidencias)






#if __name__ == "__main__":
#    main()
