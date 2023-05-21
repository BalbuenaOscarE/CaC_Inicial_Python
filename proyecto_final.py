import random
import string

pregunta = ""

contraseñas = []

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


print(contraseñas)





 



    
  






