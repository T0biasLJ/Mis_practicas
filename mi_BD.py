import sys
import sqlite3
from sqlite3 import Error

try:
    with sqlite3.connect("PrimerIntentoDemo.db") as conn: #Puente
        c = conn.cursor() #MENSAJERO
        c.execute("CREATE TABLE IF NOT EXISTS familia (clave INTEGER PRIMARY KEY, nombre TEXT NOT NULL, edad number);")
        c.execute("INSERT INTO familia values (1,'Luis Jair',39); ")
        c.execute("INSERT INTO familia values (100,'Irvin Tobias',15);")
        print("Tabla creada exitosamente")
except Error as e:
    print (e)
except:
    print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")