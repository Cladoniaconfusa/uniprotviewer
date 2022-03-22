
#from PRINTER import mostrar_tablas


from os import remove


def tabla_names(memory,ID):
    print("\n==TABLE NAMES--")
    for line in memory:
        names=[ID]
        if line.startswith("DE"):
            names.extend(line[3:].split(";"))
            print(names)
    return(names)

def tabla_dates(memory,ID):
    print("\n==TABLE DATES--")
    for line in memory:
        dates=[ID]
        if line.startswith("DT"):
            dates.extend(line[3:].split(","))
            print(dates)
    return(dates)

def tabla_features(memory,ID):
    print("\n==TABLE FEATURES--")
    features=[ID]
    l=0
    for line in memory:
         if line.startswith("FT"):
            features.extend(line[3:].split("        "))
            if len(features) >= 6:
                print(features)
                features = [ID]
    return(features)

def tabla_codes(memory,ID):
    print("\n==TABLE CODES--")
    for line in memory:
        codes=[ID]
        if line.startswith("DR"):
            codes.extend(line[3:].split(";"))
            print(codes)
    return(codes)

def tabla_comments(memory,ID):
    comments=[ID]
    print("\n==TABLE COMMENTS--")
    for line in memory:
         if line.startswith("CC"):
            comments.append(line[3:])
         elif line.startswith(""):
           if len(comments) != 1:
               z = "".join(comments[2:])
               comments = [ID, z]
               print(comments)
           comments=[ID] 
    return(comments)

def tabla_protein(memory,ID):
    protein=[ID]
    for line in memory:
        if line.startswith("AC"):
            protein.append(line.split())
        elif line.startswith("GN"):
            protein.append(line.split())
        elif line.startswith("OC"):
            protein.append(line.split())
        elif line.startswith("OS"):
            protein.append(line.split())
        elif line.startswith("OX"):
            protein.append(line.split())
        elif line.startswith("SQ"):
            protein.append(line.split())
    return(protein)







def tabla_fasta(memory,ID):
    fasta=[]
    return(fasta)