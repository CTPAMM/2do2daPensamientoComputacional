# FECHA:06/10/23
# CURSO:2 2DA
# ESTUDIANTE:THIAGO MAMANI
while True:
    # PASO 1: mostrar al usuario un menu de opciones 
    print ("*****menu de juegos******")
    print("1 call of duty")
    print("2 mortal kombat")
    print("3 uncharted") 
    print("***************************")
    
    # PASO 2: pedir al usuario ingrese su opcion 
    opcion = int(input("ingrese su opcion"))
    # PASO 3: decidir que operacion hacer
    if opcion == 1: 
        print("apunta y dispara")  
    elif opcion == 2:
        print("fatality")
    elif opcion == 3:
        print("descubre la aventura")
    else:
        print("opcion incorrecta vuelva a intentarlo")