#PROBLEMA: un usuario necesita calcular la multiplicacion y division de 2 Numeros
# SOLUCION: Crear un algoritmo que solucione su problema
# PROGRAMA: La solucion va a ser un programa para calcular la multiplicacion y la division de 2 numeros

# PASO 1:Pedir al usuario  que ingrese los numeros a operar.
numero1 = int(input("Ingresa el primer numero"))
numero2 = int(input("ingresa el segundo numero"))

print(f"EL numero 1 es: {numero1} y el numero2 es: {numero2}")

# PASO 2: prenguntar al usuario que operacion quiere utilizar


opcion = input("¿Que operacion desea realizar (multiplicacion/division)?")


# PASO 2: Preguntar al usuario que operacion quiere realizar

# PASO 3 : realizar la operacion que selecciono el usuario

if opcion == "multiplicacion":
     resultado = numero1 * numero2
else: 
      resultado = numero1 / numero2

# PASO 4: imprimir el resultado

print(f"El resultado de la {opcion} entre el {numero1} y el {numero2} es: {resultado}")
