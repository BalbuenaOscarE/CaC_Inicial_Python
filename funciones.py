import random
import string
import sqlite3

#Defino las funciones

def generar_contrasena(longitud):
    """
    Genera una contraseña aleatoria basada en la longitud especificada.

    Args:
        longitud (int): Longitud deseada de la contraseña.

    Returns:
        str: Contraseña generada.
    """
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contrasena = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contrasena

def crear_tabla(datos):
    """
    Crea la tabla en la base de datos si no existe.

    Args:
        datos (str): Nombre de la base de datos.
    """
    conexion = sqlite3.connect(datos)
    cursor = conexion.cursor()

    sentencia_create = '''
        CREATE TABLE IF NOT EXISTS datos
        (
            plataforma TEXT,
            cuenta TEXT,
            contrasena_generada TEXT,
            WITHOUT ROWID
        )
    '''

    cursor.execute(sentencia_create)
    conexion.commit()
    conexion.close()

def guardar_contrasena(datos, plataforma, cuenta, contrasena_generada):
    """
    Guarda la contraseña en la base de datos.

    Args:
        datos (str): Nombre de la base de datos.
        plataforma (str): Nombre de la plataforma.
        cuenta (str): Nombre de la cuenta.
        contrasena_generada (str): Contraseña generada.
    """
    data = [(plataforma, cuenta, contrasena_generada)]
    conexion = sqlite3.connect(datos)
    cursor = conexion.cursor()
    sentencia_insert = 'INSERT INTO datos (plataforma, cuenta, contrasena_generada) VALUES (?, ?, ?)'
    cursor.executemany(sentencia_insert, data)
    conexion.commit()
    conexion.close()

def mostrar_contrasenas(datos):
    """
    Muestra todas las contraseñas almacenadas en la base de datos.

    Args:
        datos (str): Nombre de la base de datos.
    """
    conexion = sqlite3.connect(datos)
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM datos")
    datos = cursor.fetchall()
    for fila in datos:
        plataforma = fila[0]
        cuenta = fila[1]
        contrasena = fila[2]
        print(f"Plataforma: {plataforma}")
        print(f"Cuenta: {cuenta}")
        print(f"Contraseña: {contrasena}")
        print("-----------------------------")
    conexion.close()

def obtener_contrasena(datos, incognita):
    """
    Obtiene y muestra una contraseña específica de la base de datos.

    Args:
        datos (str): Nombre de la base de datos.
        plataforma (str): Nombre de la plataforma.
    """
    conexion = sqlite3.connect(datos)
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM datos WHERE plataforma = ?", (incognita.capitalize(),))
    datos = cursor.fetchall()
    for fila in datos:
        cuenta = fila[1]
        contrasena = fila[2]
        print(f"Cuenta: {cuenta}")
        print(f"Contraseña: {contrasena}")
        print("-----------------------------")
    conexion.close()

def eliminar_contrasenas(datos):

    conexion = sqlite3.connect(datos)
 
    cursor = conexion.cursor()
       
    cursor.execute("DELETE FROM datos")

    conexion.commit()

    conexion.close()

def borrar_contrasena(datos, incognita):
    """
    Borra una contraseña específica de la base de datos.

    Args:
        datos (str): Nombre de la base de datos.
        plataforma (str): Nombre de la plataforma.
    """
    conexion = sqlite3.connect(datos)

    cursor = conexion.cursor()

    cursor.execute("DELETE FROM datos WHERE plataforma = ?", (incognita.capitalize(),))

    conexion.commit()

    conexion.close()