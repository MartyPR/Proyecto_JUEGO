
import sqlite3 as sql

def createDB():
    conn = sql.connect("Jugadores.db")
    conn.commit()
    conn.close()

def createTable():
    conn = sql.connect("Jugadores.db")
    cursor=conn.cursor()
    cursor.execute(
        """CREATE TABLE Jugadores( 
        Name text,
        Time text,
        Score integer        
       )"""
    )
    conn.commit()
    conn.close()
    
def insertRow(Nombre,Tiempo,Score):
    conn = sql.connect("Jugadores.db")
    cursor=conn.cursor()
    instru=f"INSERT INTO Jugadores VALUES  ('{Nombre}','{Tiempo}',{Score})"
    cursor.execute(instru)
    conn.commit()
    conn.close()

def readRow():
    conn = sql.connect("Jugadores.db")
    cursor = conn.cursor()
    instru = f"SELECT * FROM Jugadores "
    cursor.execute(instru)
    datos = cursor.fetchall()
    conn.commit()
    conn.close()
    #print(datos)
    return datos
    
def readOrdered(field):
    conn = sql.connect("Jugadores.db")
    cursor = conn.cursor()
    instru = f"SELECT * FROM Jugadores ORDER BY {field} DESC"
    cursor.execute(instru)
    datos = cursor.fetchall()
    conn.commit()
    conn.close()
    #print(datos)
    return datos