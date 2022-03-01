
import sys

 
def arg():
    
    dbpath = sys.argv[1]
    sarg = sys.argv[2].split(".contains.") 
    campo = sarg[0]
    value_to_match = sarg[1]
    
    
    return (dbpath,value_to_match, campo)

    

