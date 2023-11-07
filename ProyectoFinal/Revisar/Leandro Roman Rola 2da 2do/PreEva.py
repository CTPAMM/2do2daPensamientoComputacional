#Fecha:04/10/2023
#Curso:2do 2da
#Estudiante:Leandro Roman Rola

while True:
    
    #Paso 1: mostrar al asuario un menu de opciones
    print("*************MENU DE SAMSUNG******************")
    print("1- samsung A04")
    print("2-Samsung Galaxy A54")
    print("3-Samsung note 10")
    print("**********************************************")
    
    #Paso 2:Pedir al usuario que ingrese su opcion
    opcion =int(input("ingrese su opcion"))
    
    # Paso 3:Decidir que operacion hacer
    if opcion == 1:
        print("Gama media")
    elif opcion == 2:
        print("El mas caro")
    elif opcion == 3:
       print ("El mas barato")
    else:
         print("opcion incorrecta. Vuelva a intentarlo")
    