# PROBLEMA:Un usuario necesita calcular la MULTIPLICACIÓN y la DIVISIÓN de 2 números.
# SOLUCIÓN:Crear un algoritmo que solucione su problema.
# PROGRAMA:La solución va a ser un programa para calcular la multiplicación y la división de 2 números.

# PASO 1: Pedir al usuario que ingrese los números a operar.
numero1 = int(input("Ingresá el primer número:"))
numero2 = int(input("Ingresá el segundo número:"))

#print("El número 1 es: (numero1) y el número 2 es: (numero2)")

# PASO 2: Preguntar al usuario que operación quiere realizar.

opción = input("¿Qué operación desea realizar?")



# PASO 3: Imprimir al usuario el resultado de la operación seleccionada.

if opción == "multiplicación":
    resultado = numero1 * numero2
else:
    resultado= numero1 / numero2
    
# PASO 4: Imprimir el resultado

print(f"El resultado de la {opción} entre el {numero1} y el {numero2} es: {resultado}")        