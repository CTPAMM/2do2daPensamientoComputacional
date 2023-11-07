# FECHA: 3 de nomviembre 
# curso:2 2da
# estudianto:thiago

# PROBLEMA: crear un menu de ocpiones de evualacion.

while True:
    # PASO 1: mostras menu de opciones 
    print("*******menu de opciones******")
    print("1- encender LED")
    print("2- describir que es un agoridmo")
    print("2- resliza una divicione entre 2 numero")
    print("4- describe que estructura se utiliza para repetir codigo.")
    print("5- describe que estructura se utiliza para que la maquina decida.")
    print("6- ********salir*************")

    # PASO 2: pedir al usuario ingrese su opcion 
    opcion = int(input("ingrese su opcion"))

    # PASO 3: ejecutar la opcion elegida

    if opcion == 1:
        print("LED encendido")
    elif opcion ==2:
        print("es una serie de paso para resolver un problemas)
    elif opcion == 3:
        num1 = int(input(""))
        num2 = int(input(""))

        divicion = num1/num2
        print("el resultado de la divicion es: {divicion} ")

    elif opcion == 4:
        print("la estructura que usamos es codigo es while true")
    elif opcion == 5:
        print("la estructura que usamos para que la maquina decida es if elif else")
    elif opcion == 6:
        print("grasias por usar nuestro programa chau")
        break
    else :
        print("opcion incorrecta vuelva a intentar")
        