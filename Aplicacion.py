# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import sqlite3

def menu():
    print( "\n1. Registrar" )
    print( "2. Eliminar" )
    print( "3. Editar" )
    print( "4. Listar" )
    print( "5. Salir" )


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

menu()
