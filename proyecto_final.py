"""Este código es un programa generador y encriptador de contraseñas que utiliza SQLite para almacenar y administrar los datos."""

#Importo los módulos random, string, sqlite3, y funciones.

import random
import string
import sqlite3
import funciones
import variables

#Inicio del programa

print("Hola!! Bienvenidos a nuestro programa generador y encriptador de contraseñas, esperamos que les sea de utilidad!!!")

print(variables.separador)

#Contraseña para acceso al programa

contrasena_maestra = input("Ingrese la clave: ")

#Acceso

if contrasena_maestra == variables.clave :
  
 while (variables.pregunta_cierre != "SI") :
  
   pregunta_principal = str(input("¿Quiere acceder a los datos o guardar nuevos? (ACCEDER/GUARDAR) ")).upper() #Acceder a la base de datos o sumar nuevos

   match pregunta_principal:

    case "GUARDAR": # Caso guardar

     while (pregunta_principal == "GUARDAR"):
   
      funciones.crear_tabla(variables.datos)

      while (variables.pregunta_continuar != "NO") :

       plataforma = str(input("Ingresa el nombre de la plataforma: ").title())

       cuenta = str(input("Ingresa el nombre de su cuenta: ").title())

       longitud = int(input("Ingresa la longitud de la contraseña: "))

       contrasena_generada = funciones.generar_contrasena(longitud)

       print("Tu contraseña generada es: ", contrasena_generada)

       data = [(plataforma, cuenta, contrasena_generada)]
   
       funciones.guardar_contrasena(variables.datos, plataforma, cuenta, contrasena_generada)

       variables.pregunta_continuar = str(input("¿Quiere guardar alguna otra contraseña? (SI/NO) ").upper())

       if (variables.pregunta_continuar != "SI" and variables.pregunta_continuar != "NO") :
      
          print("Por favor, introduzca una respuesta válida")

      
      print(variables.separador)



    case "ACCEDER":
 
      pregunta_base = input("¿Que quiere hacer con sus datos? (VER/BORRAR) ").upper()

      match pregunta_base:
   
   
   
       case "VER":
   
        pregunta_acceder = input("¿A que datos le interesa acceder? (TODOS/ESPECÍFICO) ").upper()
     
        match pregunta_acceder:
     
          case "TODOS":

            funciones.mostrar_contrasenas(variables.datos)

          case "ESPECÍFICO":
       
            incognita = input("Escriba la plataforma de la cual desea obtener la contraseña: ").title()

            funciones.obtener_contrasena(variables.datos,incognita)

          case _:
       
            pass
     



       case "BORRAR":
     
         pregunta_borrar = input("¿A que datos le interesa borrar? (TODOS/ESPECÍFICO) ").upper()
     
         match pregunta_borrar:

           case "TODOS":

            funciones.eliminar_contrasenas(variables.datos)

           case "ESPECÍFICO":
       
            incognita = input("Escriba la plataforma de la cual quiere borrar su información: ").capitalize()

            funciones.borrar_contrasena(variables.datos, incognita)

           case _:
       
            pass

       case _:
     
         pass

      variables.pregunta_cierre = input("¿Quiere cerrar el programa? SI/NO ").upper()

      print(variables.separador)



    case _:

     break
     

     
 print("Muchas gracias por utilizar nuestro programa, vuelva pronto")

 print(variables.separador)


 
else :
  
  print("Clave incorrecta, vuelva a iniciar el programa")

  pass

