# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import sqlite3
numero = 0
def menu():
    print( "\n1. Registrar" )
    print( "2. Eliminar" )
    print( "3. Editar" )
    print( "4. Listar" )
    print( "5. Salir" )

def listar():
    print("\n** LISTAR PRODUCTOS ** \n")
    consulta = """ SELECT * 
                FROM producto
                """
                
    cursor =conexion.cursor()        
    cursor.execute(consulta)
    proc = cursor.fetchall()    
    
    for producto in proc:
        print(producto)

    

menu()
opcion = input("escoga una accion: ")
if (opcion ==4):
    print("489465468")
        




conexion = sqlite3.connect("Apellidos_almacen.db")

tabla_producto =""" CREATE TABLE producto(
                idproducto INTEGER PRIMARY KEY AUTOINCREMENT,
                codigo INTEGER,
                nombre TEXT UNIQUE,
                precio REAL
                )
            """


        
cursor = conexion.cursor()
cursor.execute(tabla_producto)

conexion.close()

