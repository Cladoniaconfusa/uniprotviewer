
import sqlite3


dates={}
names={}
features={}
codes={}
comments={}
protein={}
faste={}

def sql_insert(dates,names,features,comments,protein,fasta):
    hndlr= sqlite3.connect("try3.db")
    for i in [dates]:
        hndlr.execute("INSERT INTO Dates VALUES(?,?,?)",i[0],i[1],i[2])
    for i in [names]:
        hndlr.execute("INSERT INTO Dates VALUES(?,?,?)")
    for i in [features]:
        hndlr.execute("")
    for i in [comments]:
        hndlr.execute("")
    for i in [protein]:
        hndlr.execute("")
    for i in [fasta]:
        hndlr.execute("")

    hndlr.commit
    hndlr.close



