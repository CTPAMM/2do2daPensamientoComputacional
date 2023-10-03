# PROBLEMA:Un usario necesita calcular la SUMA y la RESTA de 2 números.
# SOLUCIÓN:Crear un algoritmo que solucione su problema.
# PROGRAMA:La solución va ser un programa para calcular la suma y la resta de 2 números.

# PASO 1: Pedir al usuario que ingrese los númeron a operar.
numero1 = int(input("Ingresá el primer número: "))
numero2 = int(input("Ingresá el segundo número:"))

#print("El número 1 es: (numero1)y el número 2 es:(numero2)")

# PASO 2: Preguntar al usuario qué operación quiere realizar.

opcion = input("¿Qué operación desea realizar (suma/resta)?")



# PASO 3: Imprimir al usuario el resultado de la operación seleccionada.

if opcion == "suma":
    resultado = numero1 + numero2
else:
    resultado= numero1 - numero2
    
#PASO 4:Imprimir el resultado

print(f"El resultado de la {opcion} entre el {numero1} y el {numero2} el: {resultado}")