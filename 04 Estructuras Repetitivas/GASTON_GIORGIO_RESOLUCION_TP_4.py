# 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100 (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

for i in range(101):
    print(i) 

#----------------------------------------------------------------------------------------------------------

# 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de dígitos que contiene.
numero = int(input("Ingrese un número entero: "))

cant_digitos = len(str(abs(numero)))

print(f"El número ingresado tiene {cant_digitos} digitos.")

#----------------------------------------------------------------------------------------------------------

# 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores dados por el usuario, excluyendo esos dos valores.
numero_1 = int(input("Ingrese el primer número: "))
numero_2 = int(input("Ingrese el segundo número: "))
suma = 0

for cont in range(numero_1 + 1,numero_2):
    suma += cont

print(suma)

#----------------------------------------------------------------------------------------------------------

# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0.
numero = int(input("Ingrese un número: "))
suma_total = 0

while numero > 0:
    suma_total += numero
    numero = int(input("Ingrese un número: "))

print(suma_total)

#----------------------------------------------------------------------------------------------------------

# 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el programa debe mostrar cuántos intentos fueron necesarios para acertar el número.
import random
num_aleatorio =  random.randint(0,9)

print("*** JUEGO ADIVINA EL NÚMERO ***") 
num_usuario = int(input("Adivina un número entre 0 y 9, en la menor cantidad de intentos posibles: "))
intentos = 1

if num_usuario >= 0 and num_usuario <= 9:
    while not (num_usuario == num_aleatorio):
        num_usuario = int(input("Número incorrecto. Intenta nuevamente: "))
        intentos += 1
    print(f"¡Adivinaste! El numero correcto es {num_aleatorio}, y lo lograste en {intentos} intentos.")
else:
    print("Número fuera de rango. Por favor, ingresa un número entre 0 y 9.")

#----------------------------------------------------------------------------------------------------------

# 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos entre 0 y 100, en orden decreciente.
for i in range(100,-2,-2):
    print(i) 

#----------------------------------------------------------------------------------------------------------

# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un número entero positivo indicado por el usuario.

num_usuario = int(input("Ingrese un número positivo: "))
suma_numeros = 0

if num_usuario >= 0:
    for i in range(num_usuario + 1):
        print(i)
        suma_numeros += i
    print(f"La suma de todos los números entre 0 y el número ingresado es {suma_numeros}")
else:
    print("El número ingresado debe ser positivo. Intente nuevamente: ")

#---------------------------------------------------------------------------------------------------------

# 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el  programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad menor, pero debe estar preparado para procesar 100 números con un solo cambio).

cont_pares = 0
cont_impares = 0
cont_positivos = 0
cont_negativos = 0

for i in range(100):
    numero = int(input("Ingrese un número: "))
    # contador de números pares e impares
    if numero % 2 == 0:
        cont_pares += 1
    else:
        cont_impares += 1

    #contador de números positivos y negativos
    if numero >= 0:
        cont_positivos += 1
    else:
        cont_negativos += 1

print(f"La cantidad de números pares es {cont_pares}")
print(f"La cantidad de números impares es {cont_impares}")
print(f"La cantidad de números positivos es {cont_positivos}")
print(f"La cantidad de números negativos es {cont_negativos}")

#----------------------------------------------------------------------------------------------------------

# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe poder procesar 100 números cambiando solo un valor).

contador = 0
suma = 0
promedio = 0

for i in range(100):
    numero = int(input("Ingrese un número: "))
    suma += numero
    contador += 1

promedio = suma / contador

print(f"El promedio de los {contador} números ingresados es {promedio}")

#----------------------------------------------------------------------------------------------------------

# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

num_invertido = 0
digito = 0

num_usuario = int(input("Ingrese un número: "))

while num_usuario > 0:
    digito = num_usuario % 10 # Extraemos el último dígito
    num_invertido = num_invertido * 10 + digito # Añadimos el dígito al número invertido
    num_usuario = num_usuario // 10 # Eliminamos el último dígito del número original

print(f"El número invertido es {num_invertido}")