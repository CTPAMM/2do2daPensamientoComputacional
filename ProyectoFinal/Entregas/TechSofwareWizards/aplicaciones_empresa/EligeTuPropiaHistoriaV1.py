# PROBLEMA: Un usuario necesita crear un juego del tipo Elige tu propia aventura.
# SOLUCION: Crear un ALGORITMO del juego.
# ALGORITMO: Creo un programa del juego

while True:
    # PASO 1: Pedir el nombre del usuario.
    nombre = input("ingrese su nombre de usuario")
    
    # PASO 2: Imprimir la bienvenida al usuario
    
    print(f"Bienvenido {nombre}")
    
    # PASO 3: Iniciar el juego
    
    input("Estas en un camino de tierra, ha llegado a su fin puedes ir hacia la izquierda o a la derecha ¿Que eliges? (derecha/izquierda)")
    if resultado == "derecha":
        print("un leon aparecio y te mato, perdiste")
    elif resultado == "izquierda":
        input("te encuentras con un hombre con vestimenta rara, supuestamente es un mago y te ofrece una bebida que te hara inmortal ¿La aceptas o la rechazas? (aceptar/rechazar)")
    if resultado == "aceptar":
        print("Te bebiste la bebida y moriste al instante por envenenamiento, perdiste")
        break
    elif resultado == "rechazar"
    print("Rechazaste la bebida y llegaste a tu destino, ganaste")