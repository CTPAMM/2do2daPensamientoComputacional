# Fecha: Viernes 6 de octubre.
# Curso: 2ndo 2nda.
# Estudiante: Fernández Malena Angelina.

while True:
    # Paso 1: Mostrar al usuario un menú de opciones
    print("**********Menú de bebidas**********")
    print("1- Gaseosa.")
    print("2- Jugo.")
    print("3- Agua.")
    print("***********************************")
   
    # Paso 2: Pedir al usuario que ingrese su opción.
    
    opción = int(input("Ingrese su bebida: "))
    
    # Paso 3: Decidir que operación hacer.
    
    if opción == 1:
        print("Dulce, refrescante y rica, buena opción para el verano.")
    elif opción == 2:
        print("Simple y delicioso")
    elif opción == 3:
        print("La opción más saludable. ¡Felicidades!")
    else:
        print("Opción icorrecta. Vuelva a intentarlo.")