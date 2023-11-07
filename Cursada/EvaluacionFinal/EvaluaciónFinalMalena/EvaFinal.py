# FECHA: viernes 3 de noviembre del 2023.
# CURSO: 2ndo 2nda.
# ESTUDIANTE: Fernández Malena.

# PROBLEMA: Crear un menú de opciones de evaluación.

while True:
    # PASO 1: Mostrar el menú de opciones.
   
    print("******** MENÚ DE OPCIONES DE EVALUACIÓN ******")
    print("1- Encender un LED.")
    print("2- Describir qué es un algoritmo.")
    print("3- Realizar una división entre 2 números.")
    print("4- Describir que estructura se utiliza para repetir código.")
    print("5- Describir que estructura se utiliza para que la máquina decida.")
    print("6- Salir.")
    print("**********************************************")

    # PASO 2: Pedir al usuario ingrese su opción.
    opción = int(input("Ingrese su opción: "))

    # PASO 3: Ejecutar la opción elegida.

    if opción == 1:
        print("LED ENCENDIDO.")
    elif opción == 2:
        print("Es una serie de pasos para resolver un problema.")
    elif opción == 3:
        num1 = int(input("Ingrese su opción: "))
        num2 = int(input("Ingrese su opción: "))
        
        división = num1/num2

        print("El resultado de la división es: {división} ")
    elif opción == 4:
        print("La estructura que utilizamos para repetir código es while True.")
    elif opción == 5:
        print("La estructura que utilizamos para que la máquina decida es if, elif y else.")
    elif opción == 6:
        print("Gracias por utilizar nuestro programa.")
        break
    else:
        print("Opción incorrecta. Vuelva a intentarlo.")