# PROBLEMA: Un usuario necesita crear un juego del tipo Elige tu propia historia.
# SOLUCIÓN: Crear un ALGORITMO del juego.
# ALGORITMO: Creo un programa del juego.

while True:
    # PASO 1: Pedir el nombre del usuario.
    nombre = input("Ingrese su nombre de usuario:")
    
    # PASO 2:  Imprimir la bienvenida al usuario.
    
    print(f"Bienvenido/a {nombre}")
    
    # PASO 3: Iniciar el juego
    
    input("Es de noche y saliste a dar un paseo, pero tenés el presentimiento de que alguien te está siguiendo. ¿Qué harás? ¿Esconderte o correr? (Correr/Esconderte)")
    
    
    if resultado == "correr":
        print("Corriste, pero la persona logró alcanzarte")
    if resultado == "Esconderte":
        resultado = input("Encontraste un almacén, así que te metiste ahí y esperaste a que la persona pasara")
    
        