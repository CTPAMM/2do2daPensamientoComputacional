#Problema:Un usuario necesita encender y apagar un led con un menu de opciones
#Solucion:Crear un programa en python con un menu de opciones para encender y apagar un led

while True:
    #Paso 1.Crear un menu de opciones para encender y apagar led.
    print("***************************menu de opciones************************************")
    print("encender (encender)")
    print("apagar (apagar)")
    print("salir (salir)")
    print("*******************************************************************************")

    #Paso 2:Pedir al usuario que ingrese su opcion.
    opcion = input("ingrese su opcion:_")

    #Paso 3:Decidir la operacion a realizar segun la opcion del usuario
    if opcion == 'encender':
       print("led encendido")

    elif opcion == 'apagar':
        print("led apagado")

    elif opcion == 'salir':
        print("Gracias por utilizar nuestro programa")
        break    
    else:
        print("opcion incorrecta. Vuelvalo a intentar")