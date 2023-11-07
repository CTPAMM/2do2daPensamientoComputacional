# PROBLEMA: Un usuario necesita crar un juego del tipo Elige tu propia aventura.
# SOLUCION: Crear un ALGORITMO del juego.
# ALGORITMO: Creo un programa del juego.

while True:
    # PASO 1: Pedir el nombre del usuario.
    nombre = input("Ingrese su nombre de usario")
    
    #PASO 2: Imprimir la bienvenida al usuario
    
    print(f"Bienvenido {nombre}")
    
    #PASO 3: Iniciar el juego 
    
    resultado = input("Estas en medio del bosque, hay dos caminos, uno a la derecha y otro a la izquierda. ¿Que camino elejis?(derecha/izquierda) ")
    
    if resultado == "izquierda":    
        print("Te caiste en un pozo y no pudiste salir")
    elif resultado == "derecha": 
        resultado == input("Seguis caminando hasta que te encontras una vieja casa. ¿Que haces? (entrar/seguir)")
        if resultado == "entrar":
            print("Perdes porque a casa era de una bruja y te convirtio en una cucaracha")
            break
        elif resultado == "seguir":
            print("Ganaste porque encontraste la salida del bosque y llegaste a tu casa") 