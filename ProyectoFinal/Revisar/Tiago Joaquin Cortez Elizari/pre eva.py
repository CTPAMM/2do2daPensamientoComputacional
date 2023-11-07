#Fecha: 06-10-23
#curso: 2°2
#Estudiante:Tiago Cortez 

while True:
   #PASO 1: Mostrar al usuario un menu de opciones
   print("******* Menu de jugadores********")
   print("1-Messi")
   print("2-Ronaldo")
   print("3-Neymar")
   print("****************")
   
   #PASO 2: Pedir al usuario ingrese su opcion
   
   opcion = int(input("Ingrese su opcion"))
   
   #PASO 3: Decir que operacion hacer
   if opcion == 1:
       print("El 10 de Argentina")
   elif opcion == 2:
       print("El 7 de Portugal")
   elif opcion == 3:
        print("El 10 de Brasil")
   else:
    print("opcion incorrecta vuelva a intertarlo") 