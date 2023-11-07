# Fecha: 06/10/2023
# Curso: 2°2
# Estudiante: Nicol Cruz 

while True:
    # Paso 1: Mostrar el usuario un menú de opciones
    print("**************MENÚ DE perros*************")
    print("1-Caniche")
    print("2-Pitbull")
    print("3-Ovejero")
    print("**********************************************")
    
    # Paso 2: Pedir al usuario ingrse su opción 
    opcion = int(input("ingrese su opcion: "))
    
    # Paso 3: Decidir que operación hacer 
    
    if opcion == 1:
         print("Buena opcion para mimarlo")
    elif opcion == 2:
         print("Perfecto para protegerte  ")
    elif opcion == 3:
         print("Perfecto para proteger un rebaño de ovejas")     
    else:
        print("opción incorrecta vuela o intentalo")