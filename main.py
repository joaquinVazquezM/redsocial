print("Bienvenido a ... ")
print("""
              _                  __
   ____ ___  (_)  ________  ____/ /
  / __ `__ \/ /  / ___/ _ \/ __  /
 / / / / / / /  / /  /  __/ /_/ /
/_/ /_/ /_/_/  /_/   \___/\__,_/

""")

nombre = input("Para empezar, dime como te llamas. ")
print()
print("Hola", nombre, ", binvenido a rednet")
print()

year = int(input("Para preparar tu perfil, dime en que año naciste. "))
edad = 2024 - year - 1
print()

estatura = float(input("Cuentame más de ti, para agregarlo a tu perfil. ¿Cuánto mides en metros? "))
estatura_m = int(estatura)
estatura_c = int( (estatura - estatura_m) * 100)

num_amigos = int(input("Muy bien. Finalmente, cuentame cuantos amigos tienes. "))
ciudad = input("Dinos en que ciudad vives actualmente ")
estado_c = input("¿Cuál es tu estado civil? ")
genero = input("¿Cuál es tu genero? ")

print()
print("Muy bien,", nombre, ". Entonces podemos crear un perfil con estos datos.")
print("----------------------------------------------------------------------------------------------------------")
print("Nombre: ", nombre)
print("Edad: ", edad, " años")
print("Estatura: ", estatura_m, " metros y ", estatura_c, " centimetros")
print("Ciudad: ", ciudad)
print("Estado civil ", estado_c)
print("Genero: ", genero)
print("----------------------------------------------------------------------------------------------------------")
print("Gracias por la información. Esperamos que disfrutes rednet")

mensaje = input("Ahora vamos a publicar tu primer mensaje. ¿Qué piensas hoy? ")
print()
print("----------------------------------------------------------------------------------------------------------")
print(nombre, " dice: ", mensaje)
print("----------------------------------------------------------------------------------------------------------")
