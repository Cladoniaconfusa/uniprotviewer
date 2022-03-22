#### Separa FASTA #####


def fasta_generator(memory):
    headr = header(memory)
    sequenc = sequence(memory)
    fasta_info = sequenc + headr 
    return(fasta_info)

def sequence(memory):
    sequenc = []
    for i in memory:
        if i.startswith("SQ"):
            sequenc.append(i)
    return(sequenc)

def header(memory):
    headr=[]
    return headr
