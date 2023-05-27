import random
import string
import sqlite3

def generar_contrasena(longitud):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contrasena = ''.join(random.choice(caracteres) for i in range(longitud))
    return contrasena

separador = "--------------------------------------------------"

contrasena_maestra = ""

pregunta_continuar = ""

clave = "Clave"

print("Hola!! Bienvenidos a nuestro programa generador y encriptador de contraseñas, esperamos que les sea de utilidad!!!")

print(separador)

pregunta_comenzar = str(input("¿Quiere guardar alguna contraseña? (SI/NO) ")).upper()

while (pregunta_comenzar == "SI" and pregunta_continuar!= "NO"):

  while (pregunta_continuar != "NO") :

   plataforma = str(input("Ingresa el nombre de la plataforma: ").capitalize())

   cuenta = str(input("Ingresa el nombre de su cuenta: ").capitalize())

   longitud = int(input("Ingresa la longitud de la contraseña: "))

   contrasena_generada = generar_contrasena(longitud)

   print("Tu contraseña generada es: ", contrasena_generada)

   data = [(plataforma, cuenta, contrasena_generada)]
   
   conexion = sqlite3.connect('datos.db')
 
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
   
   sentencia_insert = 'INSERT INTO datos (plataforma, cuenta, contrasena_generada) VALUES (?, ?, ?)'

   cursor.executemany(sentencia_insert, data)

   conexion.commit()

   conexion.close()

   pregunta_continuar = str(input("¿Quiere guardar alguna otra contraseña? (SI/NO) ").upper())

   if (pregunta_continuar != "SI" and pregunta_continuar != "NO") :
      print("Por favor, introduzca una respuesta válida")

      
print(separador)

pregunta_inicio = input("¿Quiere acceder a la base de datos?(SI/NO) ").upper()

if pregunta_inicio == "SI" :
  contrasena_maestra = input("Ingrese la clave: ")

if contrasena_maestra == clave :
 
 pregunta_base = input("¿Que quiere hacer con sus datos? (ACCEDER/BORRAR) ").upper()

 conexion = sqlite3.connect('datos.db')
 
 cursor = conexion.cursor()

 match pregunta_base:
   
   
   
  case "ACCEDER":
   
   pregunta_acceder = input("¿A que datos le interesa acceder? (TODOS/ESPECÍFICO) ").upper()
     
   match pregunta_acceder:
     
     case "TODOS":
       
       cursor.execute("SELECT * FROM datos")

       datos = cursor.fetchall()

       for fila in datos:
         
        plataforma = fila[0]
   
        cuenta = fila[1]
   
        contraseña = fila[2]

        cuentas = { "Nombre de la cuenta: " + cuenta : "Contraseña: " + contraseña}

        diccionario_cuentas = { plataforma : cuentas}

        print(diccionario_cuentas)

       conexion.commit()

       conexion.close()

     case "ESPECÍFICO":  #falta
       
       incognita = input("Selecciona la plataforma de la cual queres obtener la contraseña")

       cursor.execute("SELECT plataforma FROM datos")

       datos = cursor.fetchall()

       clave = {cuenta : contrasena_generada}

       conexion.commit()

       conexion.close()

     case _:
       
       pass

  case "BORRAR":  #falta
     
    pregunta_borrar = input("¿A que datos le interesa borrar? (TODOS/ESPECÍFICO) ").upper()
     
    match pregunta_borrar:

      case "TODOS":
       
       cursor.execute("DELETE FROM datos")

       conexion.commit()

       conexion.close()

      case "ESPECÍFICO":
       
       cursor.execute("DELETE plataforma FROM datos")

       conexion.commit()

       conexion.close()

      case _:
       
       pass

  case _:
     
    pass

print(separador)

if pregunta_comenzar == "NO" :
 print("Vuelva prontos")
else :
 print("Muchas gracias por utilizar nuestro programa, vuelva pronto")

print(separador)