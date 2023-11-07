#FECHA:3/11/237
#CURSO:2°2
#ESTUDIANTE:Caballero Maitena

#PROBLEMA: Crear un menú de opciones de evaluación 



while True:
    #PASO 1: Mostra el menú de opciones 
    print ("MENÚ DE OPCIONES DE EVALUACON")
    print("1-Encender un LED")
    print("2-Describir que es un ALGORITMO")
    print("3-Realizar una división entre 2 números")
    print("4-Describir que estructura se utiliza para repartir código")
    print("5-Describir qie estructura de utiliza para que la máquina decida")
    print("6-Salir")
    
    #PASO 2: Pedir al usuario ingrese su opción
   opcion = int(input("ingrese su opción: "))
    
    #PASO 3: Ejecutar la opción eleguida 
    
    if opcion == 1 :
        ("LED ENCENDIDO.")
    elif opcion == 2:
        ("Es una serie de pasos para resolver un prorblema")
    elif opcion == 3:
        num1=int(input("ingrece su opcion."))
        num2=int(input("ingrece su opcion."))
        
        division = num1/num2
        
        print("El resultado de la la divicion es:{division}")
        
    elif opcion == 4:
        print("la estructura que usamos para repetir es while True. ")
    elif opcion == 5:
        print("la estructura que utilizamos para que la máquina decida es if_elif y else")
    elif opcion == 6:
        print("gracias por utilizar nuestro programa.")
        break
    else:
    

        
    
    