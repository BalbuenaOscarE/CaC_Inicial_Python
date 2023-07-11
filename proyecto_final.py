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

while (variables.pregunta_cierre != "SI") :

 pregunta_comenzar = str(input("¿Quiere guardar alguna contraseña? (SI/NO) ")).upper()

 while (pregunta_comenzar == "SI" and variables.pregunta_continuar!= "NO"):
   
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

 pregunta_inicio = input("¿Quiere acceder a la base de datos?(SI/NO) ").upper()

 if pregunta_inicio == "SI" :
  
   contrasena_maestra = input("Ingrese la clave: ")

 if contrasena_maestra == variables.clave :
 
  pregunta_base = input("¿Que quiere hacer con sus datos? (ACCEDER/BORRAR) ").upper()

  match pregunta_base:
   
   
   
   case "ACCEDER":
   
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

 print(variables.separador)

 if pregunta_comenzar == "NO" :

  print("Vuelva prontos")
  
 else :

  print("Muchas gracias por utilizar nuestro programa, vuelva pronto")

 print(variables.separador)

 pregunta_cierre = input("¿Quiere cerrar el programa? SI/NO ").upper()

 if (pregunta_cierre != "SI") :
   
   print(variables.separador)

