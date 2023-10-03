# PROBLEMAS:Un usuario necesita calcular la division y multiplicacion de 2 numeros. 
# SOLUCION:Crear un algorimo que soluciones su problema.
# PROGRAMAS:La solucion va a ser un programa para calcular la multiplicacion y la division de 2 numeros.

# PASO 1: Pedir al usuario que ingrese los numeros a operar. 

Numero1 = int(input ("ingresa el primer numero:"))
Numero2 = int(input("ingresa el segundo numero"))

# print(f"El numero 1 es: {Numero1} y el numero 2 es {Numero2})
      
# PASO 2:Preguntar al usuario que peracion quiere realizar.

opcion = input("¿Que opercion desea realizar (multiplicaion/division)?")

# PASO 3: Imprimir al usuario el resultado de la operacion selecionada.


if opcion == "multiplicacion":
    resultado = Numero1 *  Numero2
else:
   resultado  = Numero1 / Numero2
# PASO 4: Imprimir el resultado

print(f"El resultado de la {opcion} entre el {Numero1} y el {Numero2} es: {resultado}")