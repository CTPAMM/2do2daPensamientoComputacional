#Fecha:06/10/23
#Curso:2°2 da
#Estudiante:Thiago velasquez

while True:

    #Paso 1:Mostrar al usuario un menu de opciones 

    print("************Menu de juegos y precio*********")

    print("1- cuphead")
    print("2- mortal combat")
    print("3- friday night funkin")

    print("************************************")
    
    #Paso 2:Pedir al usuario ingrese su opcion
    opcion = int(input("ingrese su opcion"))
    
    #Paso 3:Decidir que operacion hacer
    if opcion == 1:
       print("el cuphead es muy bueno y barato") 
       
    elif opcion == 2:
        print("el mortal combat es exelente pero es muy caro")
        
    elif opcion == 3:
        print("el friday night funkin es uno de los mejores juegos para mi y es gratis")
        
    else:
        print("opcion incorrecta.vuelva a intertalo") 