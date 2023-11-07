#Fecha: 06/10/2023
#Curso: segundo segunda
#estudiante: Pastor Benjamín Fabian

while True:
    #paso 1: Mostrar al usuario un menú de opciones
    print("###Menú de procesadores Amd###")
    print("1_AMD Ryzen Threadripper")
    print("AMD Raven Ridge (APU)")
    print("AMD Ryzen 9")
    print("##################################")

    #Paso 2: pedir al usuario que ingrese su opcion

    opcion = int(input("ingrese su opcion"))

    #Paso 3: Decidir que operación hacer
    if opcion == 1:
        
        print(" Mejor procesador de AMD ")
        
    elif opcion == 2:
        
        print("Segundo mejor procesador de AMD")
        
    elif opcion == 3:
        
        print("Tercer mejor procesador de AMD")
        
    else:
        
        print("opcion incorrecta, vuelve a intentarlo")