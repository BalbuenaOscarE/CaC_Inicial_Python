import random
import string
import sqlite3

pregunta = ""

contraseñas = []

print("Hola!! Bienvenidos a nuestro programa generador y encriptador de contraseñas, esperamos que les sea de utilidad!!!")

def generar_contrasena(longitud):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contrasena = ''.join(random.choice(caracteres) for i in range(longitud))
    return contrasena

while pregunta != "NO" :

 longitud = int(input("Ingresa la longitud de la contraseña: "))
 contrasena_generada = generar_contrasena(longitud)

 print("Tu contraseña generada es: ", contrasena_generada)

 cuenta = str(input("Ingresa el nombre de su cuenta: "))

 tupla = (cuenta,contrasena_generada)

 contraseñas.append(tupla)

 pregunta = str(input("¿Quiere guardar alguna otra contraseña? (SI/NO) ").upper())

 if pregunta != "SI" and pregunta != "NO" :
    print("Por favor, introduzca una respuesta válida")


conexion = sqlite3.connect('datos.db')

cursor = conexion.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS datos (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    cuenta TEXT,
                    contrasena_generada INTEGER
                )''')

cursor.executemany('INSERT INTO datos (cuenta, contrasena_generada) VALUES (?, ?)', contraseñas)

print(contraseñas)

conexion.commit()
conexion.close()
