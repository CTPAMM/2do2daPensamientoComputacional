# PROBLEMA:Un usuario necesita crear un juego del tipo Elije tu propia aventura. 
# SOLUCION:Crear un ALGORITMO del juego.
# ALGORITMO:Creonun programa del juego.

while True:
    # PASO 1: Pedir el nombre del usuario.
      nombre = input("ingrese su nombre")
      
    # PASO 2: Imprimir la bienvenida al usuario 
    
    print(f"Bienvenido {nombre}")

    # PASO 3: Iniciar el juego 
    
    resultado = input(" Estas en un camino de tierra a si fin y podes ir a la izquierda o a la derecha ¿ Que eliges? (deracha/izquierda)  ")
    
    if resultado == "derecha":
        print("se auto se cruzo y perdiste ")
    elif resultado == "izquierda":
   resultado == input ("continuamos manejando y seguimos en la ruta y nos encontramos un cartel que decia derecha o izquierda ¿ derecha o izquieda? (derecha/izquierda)")
   if resultado == "derecha":
       print("fui por la derecha y se te pincho la rueda")
       break
   elif resultado =="izquierda":
    print("fui por la izqiuerda y no me paso nada")






