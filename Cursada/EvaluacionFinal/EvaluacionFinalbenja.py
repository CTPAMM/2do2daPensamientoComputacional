#Problema:Un usuario necesita encender y apagar un led con un menu de opciones
#Solucion:Crear un programa en python con un menu de opciones para encender y apagar un led

while True:
    #Paso 1: Mostrar el menu de opciones
    print("***************************MENU DE OPCIONES DE EVALUACION************************************")
    print("1-Encender (Encender)")
    print("2- Desribir que es un ALGORITMO")
    print("3- Realizar una divicion entre 2 numeros.")
    print("4- Describir que estructura se utiliza para repetir codigo.")
    print("5- Describir que estructura se utiliza para que la maquina decida.")
    print("6- Salir (Salir)")
    
    #Paso 2: Pedir al usuario que ingrese su opcion.
    int(input("ingrese su opcion:_"))

    #Paso 3: Ejecutar la opcion elegida
    if opcion == 1'encender':
       print("led encendido")

    elif opcion == 2'Desribir que es un ALGORITMO':
        print("es una serie de pasos para resolver problemas")
    elif opcion == 3'Realizar una divicion entre 2 numeros':
        num1 = int(input("ingrese el primer numero"))
        num2 = int(input("ingrese el segundo numero"))

        division = num1/num2
        print("El resultado de la divicion es: {division}")
    elif opcion == 4'Describir que estructura se utiliza para repetir codigo':
        print("la estructura que usamos para repetir los codigos es while true")
    elif opcion == 5'Describir que estructura se utiliza para que la maquina decida':
        print("la estructura que usamos para repetir los codigos es if-elif-else")
    elif opcion == 6'salir':
        print("gracia por utilizar nuestro programa.")
        break    
    else:
        print("opcion incorrecta. Vuelvalo a intentar")