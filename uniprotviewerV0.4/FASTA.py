#### Separa FASTA #####
import sys

def fasta_generator(memory):
    headr = header(memory)[0]
    seq = sequence(memory)
    fasta_info = headr + '\n' + seq
    if 'FASTA' in sys.argv:
        print(fasta_info)
    return(fasta_info)

def sequence(memory):
    sequenc = ''
    for line in memory:
        if line.startswith("SQ") and not line[5:].startswith('SEQUENCE'):
            sequenc += line[5:].replace(" ", "").replace("\n", "")
    seq = ''
    for chr in range(0,len(sequenc),60):
        seq += sequenc[chr: chr+60] + "\n"
    return(seq)

def header(memory):
    headr=''
    for line in memory:
        if line.startswith('ID'):
            line = line.replace(' ', '')
            ID_AA = line.split("Reviewed")
            ID = ID_AA[0][2:]
            aa = ID_AA[1][1:]
        elif line.startswith('AC'):
            AC = line[5:]
        elif line.startswith('OS'):
            OS = line[5:]
    headr = '>id=' + ID + '; acc=' + AC + ' name=' + OS 
    return(headr,AC,aa)


