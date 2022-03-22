
from traceback import print_tb


def mostrar_memoria(memory,fieldlist):
    for line in memory:
        if "SHOWALL" in fieldlist or fieldlist == "allfields":
            print(line)
        else:
            for j in fieldlist:
                if j == line[:2]:
                    print(line)

def mostrar_taxones(taxones,fieldlist):
    if "TAXONS" in fieldlist:
        print(taxones)

#def mostrar_tablas(names,protein,dates,codes,comments,features,fasta):
#    print("\n--TABLE DATES--")
#    print(dates)
#    print("\n--TABLE NAMES--")
#    print(names)
#    print("\n--TABLE CODES--")
#    print(codes)
#    print("\n==TABLE FEATURES--")
#    print(features)
#    print("\n==TABLE COMMENTS--")
#    print(comments)
#    print("\n--TABLE FASTA--")
#    print(fasta)
#    print("\n--TABLE PROTEIN--")
#    print(protein)
#    return()