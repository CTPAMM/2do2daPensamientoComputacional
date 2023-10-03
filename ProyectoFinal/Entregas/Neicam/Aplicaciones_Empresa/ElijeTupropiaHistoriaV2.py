#PROBLEMA:Un usario necesita crear un juego del elije tu propia aventura
#SOLUCION:Crear un ALGORITMO de juego.
#ALGORITMO:Creo un programa de juego

while True:
     #PASO 1: Pedir el nombre del usuario.
     nombre =input("ingrece su nombre de usario")
     
     # PASO 2:Inprimir la bienvenida al usuario
     
    print(f"bienvenida{nombre}")
    
    #PASO 3:Iniciar el juego
    
   resultado =input("estas en en el camino de tierra tu decides derecha o izquierda.¿Cuál quieres ?(derecha/izquierda)")
     
     if resultado=="derecha":
         print("se cruzó con un sombi y perdiste.")
     elif resultado=="izquierda":
        resultado = input("continias caminando hasta que te quedes sin agua.¿que haces?(sigo/vuelvo)")
        if resultado =="vuelvo":
            print("perdiste porque te modío un sombi")
            break
        elif resultado =="sigo":
            print("ganas poque sobreviviste a los sombis")
         