def taxons(fieldlist:list,memory:list):
    taxones1:dict = {}
    for t in memory:
        if "TAXONS" in fieldlist and t.startswith("OC"):
                lista_tx = t[:-1].split(";")
                for tx in lista_tx:
                    if not tx in taxones1.keys():
                        taxones1[tx] = 1
                    else:
                        taxones1[tx] = taxones1[tx] + 1
    return(taxones1)