# PROBLEMA: Un usuario necesita crear un juego del tipo Elige tu propia aventura.
# SOLUCION: Crear un ALGORITMO del juego.
# ALGORITMO: Creo un programa del juego.

while True:
    # PASO 1: Pedir el nombre del usuario.
    nombre = input("ingrese su nombre de usuario")
    
    # PASO 2: Imprimir la bienvenida al usuario
    
    print(f"Bienvenido {nombre}")
    
    # PASO 3: Iniciar el juego
    
    resultado = input("Estas por llegar al final del camino pero hay trampas ¿Que elegis? Avanzar/retroceder")
    
    if resultado == "avanzar" :
        print("se cruzo con un lobo y perdiste")
    elif resultado == "retroceder" :
        resultado = input("continuas y encontras una familia de cerdos  ¿Que elegis? comerlos/seguir avanzando")
        if resultado == "comerlos" :
            print("PERDISTE por que los comistes crudos")
        elif resultado == "seguir avanzando" :
           print("GANASTE pudiste escapar")
        