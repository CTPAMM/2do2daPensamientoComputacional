# PROBLEMA: Un usuario necesita crear un juego del tipo Elije tu propia aventura
# SOlUCION: Crear un ALGORITMO del juego.abs
# ALGORITMO: Creo un programa del juego

while True:
     # PASO 1: Pedir el nombre del usuario 
     nombre = input("Ingrese su nombre")
     
     # PASO 2: Imprimir la bienvenida al usuario 
     
     print(f"Bienvenido/a {nombre}")
     
     # PASO 3: Iniciar el juego
     
     resultado = input("Pasaste la capa de Ozono, felicidades, tienes que elegir a que planeta llegar, sí a Marte o a Venus, ¿que elijes? (Marte/Venus)")
     
     if resultado == "Venus":
        print("Al intertar llegar, se averió su nave y se perdió en la galaxia")
        break       
    elif resultado == "Marte":
        resultado = input("Llegó bastante bien, aunque tiene que arreglar unos problemas no tan importantes de la nave, ¿que decides? (Arreglarlos/No arreglarlos)")
        if  resultado == "No arreglarlos":
           print("Lastimosamente, los problemas se hicieron más grandes y la nave se descompuso")
           
        