# FECHA: 03/11/23
# CURSO: 2do 2da
# ESTUDIANTE: Martina Fritz

# PROBLMA: Crear un menu de opciones de evaluacion

while True:
    # PASO 1: Mostrar el menu de opciones
    print("********MENU DE OPCIONES DE EVALUACION*********")
    print("1- Encender un LED.")
    print("2- Describir que es un algoritmo.")
    print("3- Realizar una division entre 2 numeros.")
    print("4- Describir que estructura se utiliza para repetir codigo.")
    print("5- Describir que estructura se utiliza para que la maquina decida.")
    print("6- Salir.")
    print("************************************************")

    # PASO 2: Pedir al usuario que ingrese su opcion.
    opcion = int(input("Ingrese su opcion: "))

    # PASO 3: Ejecuatar la opcion elegida.

    if opcion == 1:
        print("LED encendido")
    elif opcion == 2:
        print("Un algortimo es una serie de pasos para resolver un problema.")
    elif opcion == 3:
        num1 = int(input("Ingrese el primer numero: "))
        num2 = int(input("Ingrese el segundo numero: "))  

        division = num1/num2
        
        print("El resutado de la division es: {division}")
    elif opcion == 4:
        print("La estructura que se utiliza para repetir codigo es while True.")
    elif opcion == 5:
        print("Las estructuras que se utilizan para que la maquina decida son if, elif y else")
    elif opcion == 6:
        print("Gracias por utilizar nuestro programa.")
        break

    else: 
        print("Opcion incorrecta intentelo nuevamente.")
        


