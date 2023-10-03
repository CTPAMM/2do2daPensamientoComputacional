#PROBLEMA:Un usuario necesita calcular la SUMA y RESTA de 2 numeros.
#SOLUCION:Crear un algoritmo que solucione su problema.
#PROGRAMA:La  solucion va a ser un programa para calcular la suma y la resta de 2 numeros.

# PASO 1:Pedir al usuario que ingrese los numeros a operar
numero1 = int(input("ingresa el primer numero "))
numero2 = int(input("ingresa el segundo numero "))

#print(f"El numero 1 es {numero1} y el numero 2 es: {numero2}")

# PASO 2:preguntar al usuario que operacion quiere realizar.

opcion = input("¿Que operacion desea realizar (suma/resta)?")


# PASO 3: Realizar la operacion que seleciono el usuario.
if opcion == "suma":
    resultado = numero1 + numero2
else:
    resultado = numero1 - numero2
    
# PASO 4: imprimir el resultado

print(f"El resultado de la {opcion} entre el {numero1} y el {numero2} es: {resultado}")