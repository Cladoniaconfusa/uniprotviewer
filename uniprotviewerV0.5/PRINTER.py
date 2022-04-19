import sys
from insert_data_sql import sql_insert_codes, sql_insert_comments, sql_insert_names, sql_insert_dates, sql_insert_features

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

def mostrar_fasta(fasta):
    if 'VERBOSE' in sys.argv:
        print("\n==TABLE FASTA==")
        print(fasta)

def mostrar_names(names):
    if 'VERBOSE' in sys.argv:
        print(names)
    sql_insert_names(names)

def mostrar_dates(dates):
    if 'VERBOSE' in sys.argv:
        print(dates)
    sql_insert_dates(dates)

def mostrar_features(features):
        print("\n==TABLE FEATURES==")
        for i in features:
            if 'VERBOSE' in sys.argv:    
                print(i)
        sql_insert_features(features)

def mostrar_codes(codes):
    if 'VERBOSE' in sys.argv:
        print(codes)
    sql_insert_codes(codes)

def mostrar_comments(registro):
    if 'VERBOSE' in sys.argv:
        print(registro)
    sql_insert_comments(registro)

def mostrar_protein(protein):
    if 'VERBOSE' in sys.argv:
        print("\n==TABLE PROTEIN==")
        print(protein)

    