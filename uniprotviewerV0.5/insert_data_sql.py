import sqlite3
import sys


def get_rutadb():
    for i in sys.argv:
        if i.startswith("db="):
            z = i.split("=")
            rutadb = z[1]
    return(rutadb)

def sql_insert_names(names):
    conn = connect_db()
    with conn:
        conn.execute("INSERT INTO Names VALUES(?,?)",names)
    conn.commit

def sql_insert_dates(dates):
    conn = connect_db()
    with conn:
        conn.execute("INSERT INTO Names VALUES(?,?)",dates)
    conn.commit

def connect_db():
    rutadb = get_rutadb()
    conn = sqlite3.connect(rutadb)
    return(conn)

