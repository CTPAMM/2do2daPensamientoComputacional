# PROBLEMA: Un usuario necesita calcular la MULTIPLICACION y DIVISION de 2  números
# SOLUCION: Crear un algoritmo que solucione su problema
# PROGAMA: La solución va a ser un programa para calcular la MULTIPLICACION y la DIVISION de 2 números

# PASO 1: Pedir al usuario que ingrese los numeros a operar
numero1 = int(input("Ingresá el primer número: "))
numero2 = int(input("Ingresá el segundo número: "))

#print(f"El número 1 es: {numero1} y el número 2 es: {numero2}" )

# PASO 2: Preguntar al usuario que operacion quiere realizar

opcion = input("¿Qué operación desea realizar (multiplicacion/division)?: ")

# PASO 3: Imprimir al usuario el resultado de la operacion seleccionada

if opcion == "multiplicacion":
    resultado  = numero1 * numero2
else:
    resultado = numero1 / numero2

# PASO 4: Imprimir el resultado

print(f"El resultado de la {opcion} entre el {numero1} y el {numero2} es: {resultado}")