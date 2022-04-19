
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
        conn.execute("INSERT INTO Dates VALUES(?,?,?)",dates)
    conn.commit

def sql_insert_features(features):
    conn = connect_db()
    with conn:
        for i in features:
            conn.execute("INSERT INTO Features VALUES(?,?,?,?)",i)
    conn.commit

def sql_insert_codes(codes):
    conn = connect_db()
    with conn:
        conn.execute("INSERT INTO Codes VALUES(?,?)",codes)
    conn.commit

def sql_insert_comments(registro):
    conn = connect_db()
    with conn:
        conn.execute("INSERT INTO Comments VALUES(?,?)",registro)
    conn.commit

def connect_db():
    rutadb = get_rutadb()
    conn = sqlite3.connect(rutadb)
    return(conn)

