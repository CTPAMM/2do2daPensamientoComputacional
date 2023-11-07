# FECHA: 06/10/23
# CURSO: 2do 2da
# ESTUDIANTE: Acosta Keila

while True:
    
    # PASO 1: Mostrar al usuario un menu de opciones
    
    print ("*****Menu de grupos musicales****")
    print ("1-Miranda!")
    print ("2-Queen")
    print ("3-Nirvana")
    
    print ("*********************************")
    
    # PASO 2: Pedir al usuario ingrese su opcion.
    
    opcion = int(input("Ingrese su opcion: "))
    
    # PASO 3: Decidir que operacion hacer
    
    if opcion == 1:
        print("Una de las mejores bandas argentinas, segun mi opinion")
    
    elif opcion == 2:
        print ("Unas leyendas del rock")
    
    elif opcion == 3:
        print ("Una banda bastante conocida")
       
    else : 
        print ("Opcion incorrecta.Vuelva a intentarlo")