print("Bienvenido a ... ")
print("""

__________          __  .__                  ________                     
\______   \___.__._/  |_|  |__   ____   ____ \______ \   _______  ________
 |     ___<   |  |\   __\  |  \ /  _ \ /    \ |    |  \_/ __ \  \/ /  ___/
 |    |    \___  | |  | |   Y  (  <_> )   |  \|    `   \  ___/\   /\___ \ 
 |____|    / ____| |__| |___|  /\____/|___|  /_______  /\___  >\_//____  >
           \/                \/            \/        \/     \/         \/ 


""")

#Primera interacción. Solicitamos al usuario que ingrese su nombre,
#y lo guardamos en una variable de tipo str
nombre = input("Para empezar, dime como te llamas. ")
print()
print("Hola ", nombre, ", bienvenido a Mi Red")
print()

#Segunda interacción. Solicitamos el ingreso del año, y utilizamos este
#dato para estimar la edad de la persona. ¿Por qué decimos que solo estamos "estimando" su edad?
#¿Qué ocurre si eliminamos la conversión a tipo de dato 'int' de la siguiente línea?
agno = int(input("Para preparar tu perfil, dime en qué año naciste. "))
edad = 2024-agno-1
print()

#Tercera interacción. Solicitamos la estatura, medida en metros.
#Utilizamos la conversión a 'int', y una expresión para convertir esto
#a una medida en metros y centímetros
estatura = float(input("Cuéntame más de ti, para agregarlo a tu perfil. ¿Cuánto mides? Dímelo en metros. "))
estatura_m = int(estatura)
estatura_cm = int( (estatura - estatura_m)*100 )
print()

#Cuarta interacción. Consultamos cuántos amigos tiene el usuario.
num_amigos = int(input("Muy bien. Cuéntame cuantos amigos tienes. "))
print()
#Quinta interacción. Indagamos por el sexo del usuario,  numero de telefono y ciudad donde vive
sexo = input("""Cual es tu Sexo, dimelo de la siguiente manera:
Hombre: H
Mujer: M
Otro: O
""")
print()
numeroTel = input("Cuál es tu número telefónico?.")
print()
ciudad = input("y Finalmente dime en que ciudad vives.")

#Con los datos recolectados escribimos en pantalla un texto que resuma los datos que hemos obtenido
print()
print("Muy bien,", nombre, ". Entonces podemos crear un perfil con estos datos.")
print("--------------------------------------------------")
print("Nombre:              ", nombre)
print("Edad:                ", edad, "años")
print("Estatura:            ", estatura_m, "metros y", estatura_cm, "centímetros")
print("Amigos:              ", num_amigos)
print("Sexo:                ", sexo)
print("Numero telefónico:   ", numeroTel)
print("Ciudad:              ", ciudad)
print("--------------------------------------------------")
print("Gracias por la información. Esperamos que disfrutes con Mi Red")
print()

#Finalmente, solicitamos un mensaje de prueba que sirva para publicar un estado del usuario.
mensaje = input("Ahora vamos a publicar tu primer mensaje. ¿Qué piensas hoy? ")
print()
print("--------------------------------------------------")
print(nombre, "dice:", mensaje)
print("--------------------------------------------------")