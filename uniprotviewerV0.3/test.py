

from ntpath import join


memory = ["ID 003L_IIV3 Reviewed; 156 AA."
    "AC Q197F7;",
    "DT 16-JUN-2009, integrated into UniProtKB/Swiss-Prot.",
    "DT 11-JUL-2006, sequence version 1.",
    "DT 12-AUG-2020, entry version 23.",
    "DE RecName: Full=Uncharacterized protein 003L;",
    "GN ORFNames=IIV3-003L;",
    "OS Invertebrate iridescent virus 3 (IIV-3) (Mosquito iridescent virus).",
    "OC Viruses; Varidnaviria; Bamfordvirae; Nucleocytoviricota; Megaviricetes;",
    "OC Pimascovirales; Iridoviridae; Betairidovirinae; Chloriridovirus.",
    "OX NCBI_TaxID=345201;",
    "OH NCBI_TaxID=7163; Aedes vexans (Inland floodwater mosquito) (Culex vexans).",
    "OH NCBI_TaxID=42431; Culex territans.",
    "OH NCBI_TaxID=332058; Culiseta annulata.",
    "OH NCBI_TaxID=310513; Ochlerotatus sollicitans (eastern saltmarsh mosquito).",
    "OH NCBI_TaxID=329105; Ochlerotatus taeniorhynchus (Black salt marsh mosquito) (Aedes taeniorhynchus).",
    "OH NCBI_TaxID=7183; Psorophora ferox.",
    "RN [1]",
    "RP NUCLEOTIDE SEQUENCE [LARGE SCALE GENOMIC DNA].",
    "RX PubMed=16912294; DOI=10.1128/jvi.00464-06;",
    "RA Delhon G., Tulman E.R., Afonso C.L., Lu Z., Becnel J.J., Moser B.A.,",
    "RA Kutish G.F., Rock D.L.;",
    "RT Genome of invertebrate iridescent virus type 3 (mosquito iridescent",
    "RT virus).;",
    "RL J. Virol. 80:8439-8449(2006).",
    "",
    "CC -!- FUNCTION: Involved in the regulation of homocysteine metabolism.",
    "CC Converts betaine and homocysteine to dimethylglycine and methionine,",
    "CC respectively. This reaction is also required for the irreversible",
    "CC oxidation of choline (By similarity). {ECO:0000250}.",
    "",
    "CC -!- CATALYTIC ACTIVITY:",
    "CC Reaction=glycine betaine + L-homocysteine = L-methionine + N,NCC dimethylglycine; Xref=Rhea:RHEA:22336, ChEBI:CHEBI:17750,",
    "CC ChEBI:CHEBI:57844, ChEBI:CHEBI:58199, ChEBI:CHEBI:58251; EC=2.1.1.5;",
    "",
    "CC -!- COFACTOR:",
    "CC Name=Zn(2+); Xref=ChEBI:CHEBI:29105; Evidence={ECO:0000250};",
    "CC Note=Binds 1 zinc ion per subunit. {ECO:0000250};",
    "",
    "CC -!- PATHWAY: Amine and polyamine degradation; betaine degradation;",
    "CC sarcosine from betaine: step 1/2.",
    "",
    "CC -!- PATHWAY: Amino-acid biosynthesis; L-methionine biosynthesis via de novo",
    "CC pathway; L-methionine from L-homocysteine (BhmT route): step 1/1.",
    "CC -!- SUBUNIT: Homotetramer. {ECO:0000250}.",
    "",
    "CC -!- SUBCELLULAR LOCATION: Cytoplasm {ECO:0000250}.",
    "CC ---------------------------------------------------------------------------",
    "CC Copyrighted by the UniProt Consortium, see https://www.uniprot.org/terms",
    "CC Distributed under the Creative Commons Attribution (CC BY 4.0) License",
    "CC ---------------------------------------------------------------------------",
    "DR EMBL; DQ643392; ABF82033.1; -; Genomic_DNA.",
    "DR RefSeq; YP_654575.1; NC_008187.1.",
    "DR GeneID; 4156252; -.",
    "DR KEGG; vg:4156252; -.",
    "DR Proteomes; UP000001358; Genome.",
    "PE 4: Predicted;",
    "KW Reference proteome.",
    "FT CHAIN 1..156",
    "FT   /note=Uncharacterized protein 003L",
    "FT   /id=PRO_0000377939",
    "FT CHAIN 1..403",
    "FT   /note=Betaine--homocysteine S-methyltransferase 1",
    "FT   /id=PRO_0000273223",
    "FT DOMAIN 8..311",
    "FT   /note=Hcy-binding",
    "FT   /evidence=ECO:0000255|PROSITE-ProRule:PRU00333",
    "FT METAL 214",
    "FT   /note=Zinc",
    "FT   /evidence=ECO:0000255|PROSITE-ProRule:PRU00333",
    "FT METAL 296",
    "FT   /note=Zinc",
    "FT   /evidence=ECO:0000255|PROSITE-ProRule:PRU00333",
    "FT METAL 297",
    "FT   /note=Zinc",
    "FT   /evidence=ECO:0000255|PROSITE-ProRule:PRU00333",
    "SQ SEQUENCE 156 AA; 17043 MW; D48A43940FF8C815 CRC64;",
    "   MYQAINPCPQ SWYGSPQLER EIVCKMSGAPiubdsfahgiuygvaiuyfrghrsauhvaiyfrgviuerahgfoirgfyierwafuheryoiugriushfgiusybgsuyrbguytrsbguyerg HYPNYYPVHP NALGGAWFDT SLNARSLTTT",
    "   PSLTTCTPPS LAACTPPTSL GMVDSPPHIN PPRRIGTLCFdkjhfsiuyfrtehgiuhteriughtriughrsgtrsherytjh DFGSAKSPQR CECVASDRPS",
    "   TTSNTAPDTY RLLITNSKTR KNNYGTCRLE PLTYGI",
    "//"
    ]
ID = "sucara908"

def tabla_comments(memory,ID):
    comments=[ID]
    print("\n==TABLE COMMENTS--")
    for line in memory:
         if line.startswith("CC"):
            comments.append(line[3:])
         elif line.startswith(""):
#            j = " ".join(comments[2:])
#            comments = [ID,j]
           if len(comments) != 1:
               z = "".join(comments[2:])
               comments = [ID, z]
               print(comments)
           comments=[ID] 
    return(comments)


tabla_comments(memory,ID)