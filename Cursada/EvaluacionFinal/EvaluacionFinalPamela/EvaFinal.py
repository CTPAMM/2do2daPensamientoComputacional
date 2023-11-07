# FECHA:03/11/2023
# CURSO: 2do 2da   
# ESTUDIANTE:Pamela 

#PROBLEMA: Crear un menú de opciones de evaluación 

while True:
    #PASO 1: Mostrar el menu de opciones
    print("MENU DE OPCIONES DE EVALUACION")
    print("1-Encender un LED")
    print("2-Que es un ALGORITM") 
    print("3-Realizar una division entre 2 numero.")
    print("4-Describir que estructura se utiliza para repertir codigo".)
    print("5-Describir que estructura se utiliza para que la maquina decida".)
    print("6-Salir")

    # PASO 2:Pedir al usuario ingrese su opcion 
    opcion = int(input("Ingresar su opcion"))

    # PASO 3: Ejecutar la opcion elegida

    if opcion == 1:"Encender"
        print("LED ENCENDIDO")
    elif opcion == 2:"Describir"
        print("Es una seria de pasos para solucionar probema")
    elif opcion == 3:
        num1 = int("input(ingrese el 1er numero)")
        num2 = int("input(ingrese el 2do numero)")

        division = num1/num2
        print("El resultado de la divicion es: {division} ")
    elif opcion == 4:
        print("La estructura que usamos para repetir codigo es while True")
    elif opcion == 5:
        print("La estructura que usamos para repetir codigo es if-elif-else")
    elif opcion == 6:
        print("Gracias por utilizar nuestro programa") 
        break
    else:
        print("Opcion incorrecta")
    




