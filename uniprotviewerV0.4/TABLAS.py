
from PRINTER import mostrar_comments, mostrar_dates, mostrar_fasta, mostrar_names,mostrar_features, mostrar_codes, mostrar_protein
from FASTA import sequence,header
import sys

def tabla_fasta(memory,ID):

    seq = sequence(memory)
    headr = header(memory)[0]  
    fasta = [ID,headr,seq]
    mostrar_fasta(fasta)

def tabla_names(memory,ID):
    if 'VERBOSE' in sys.argv:
        print("\n==TABLE NAMES==")
    cnt=0
    for line in memory:
        names=[ID]
        cnt+=1
        if cnt < len(memory):
            nxt_line = memory[cnt]
        line.replace(" ", "")
        if line.startswith("DE") and line[6] != ' ':
            names.extend(line[5:].split(";"))
            names.remove('')
            if nxt_line[6] == ' ':
                names[1] +=  nxt_line[10:]
            mostrar_names(names)   

def tabla_dates(memory,ID):
    if 'VERBOSE' in sys.argv:
        print("\n==TABLE DATES==")
    for line in memory:
        dates=[ID]
        if line.startswith("DT"):
            dates.extend(line[5:].split(","))
            dates[2] = dates[2][1:]
            mostrar_dates(dates)
    return(dates)

def tabla_features(memory,ID):
    allfeatures = []
    features=[]
    feature=[]
    l=0
    for line in memory:
         if line.startswith("FT"):
            allfeatures.append(line)
    for element in allfeatures:
        if element[5] != ' ': # Aqui entran los titulos donde está type y loc
            doomie = element.split('   ')
            if feature != []:
                features.append(feature)
            feature = [ID, doomie[1], doomie[-1]]
        elif element[5] == ' ':
            if len(feature) == 3:
                feature.append(element[20:]) 
            elif len(feature) > 3:
                feature[3] += element[20:]
    mostrar_features(features)

    return(features)

def tabla_codes(memory,ID):
    if 'VERBOSE' in sys.argv:
        print("\n==TABLE CODES==")
    for line in memory:
        codes=[ID]
        if line.startswith("DR"):
            line.replace(' ','')
            codes.append(line[5:])
            mostrar_codes(codes)
        
    return(codes)

def tabla_comments(memory,ID):
    if 'VERBOSE' in sys.argv:
        print("\n==TABLE COMMENTS==")
    commnts = []
    registro= []
    for line in memory:
        if line.startswith('CC'):
            commnts.append(line)
            
            if line[6].startswith('!'): #significa que la línea es un titulo
                if len(registro) > 1:
                    mostrar_comments(registro)
                registro = [ID]
                registro.append(line[5:])
                
            if line[6].startswith(' ') and len(registro) > 1: # adicionar al titulo sus respectivas lineas
                registro[1] += line[8:]                          
        
def tabla_protein(memory,ID):
    
    SQ = sequence(memory) # sequence
    AC = header(memory)[1] # accesion
    aa = header(memory)[2].replace('AA.','') # AA number
    OX = '' # taxonomy id
    for line in memory:
        if line.startswith('OX'):
            OX += line[5:]
    OC = '' # taxonomy
    for line in memory:
        if line.startswith('OC'):
            OC += line[5:]
    OS = '' # name
    for line in memory:
        if line.startswith('OS'):
            OS += line[5:]
    KW = '' # kewywords
    for line in memory:
        if line.startswith('KW'):
            KW += line[5:]
    PE = '' # Predicted
    for line in memory:
        if line.startswith('PE'):
            PE += line[5:]
    GN = '' # Orfnames
    for line in memory:
        if line.startswith('GN'):
            GN += line[5:]

    protein=[ID,AC,OS,OC,OX,SQ,aa,KW,PE,GN]
    mostrar_protein(protein)
    return(protein)
