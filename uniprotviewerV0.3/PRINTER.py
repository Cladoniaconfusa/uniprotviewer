

from Argumentos_entrada import verificar_fieldlist


def mostrar_memoria(memory,fieldlist,taxones):
    for line in memory:
        if "SHOWALL" in fieldlist or fieldlist == "allfields":
            print(line)
        else:
            for j in fieldlist:
                if j == line[:2]:
                    print(line)
    print("//")

def mostrar_taxones(taxones):
    fieldlist = verificar_fieldlist(fieldlist)
    if "TAXONS" in fieldlist:
        print(taxones)
    print(taxones)

