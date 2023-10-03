#PROBLEMA: Un usuario necesita calcular la SUMA y la RESTA de 2 números.
#SOLUCIÓN:Crear un algoritmo que solucione su problema.
#PROGRAMA:La solución va a ser un programa para calcular la suma y la resta de 2 números.

# PASO 1: Pedir al usuario que ingrese los números a operar
numero1 = int(input("Ingresa el primer número "))
numero2 = int(input("ingresá el segundo número: "))

#print(f"El número 1 es: {número1} y el número 2 es: {numero2}")

# PASO 2: Preguntar al usuario qué operación quiere realizar

opcion = input("¿Qué operación desea realizar (suma/resta)?")

# PASO 3: Imprimir al usuario el resultado de la operación seleccionada.

if opcion == "suma":
    resultado = numero1 + numero2
else:
    resultado = numero1 - numero2
    
# PASO 4: Imprimir el resultado

print(f"el resultado de la {opcion} entre el {numero1} y el {numero2} es: {resultado}")