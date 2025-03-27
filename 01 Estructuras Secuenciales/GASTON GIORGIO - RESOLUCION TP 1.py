#1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.  

print ("Hola Mundo!")

#-----------------------------------------------------------------------------------------------

# 2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando
# el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir
# por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para
# realizar la impresión por pantalla. 

nombreUsuario = input("Por favor, ingresa tu nombre:")
print (f"Hola {nombreUsuario}!")

#-----------------------------------------------------------------------------------------------

# 3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e
# imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa
# “Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30
# años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar
# la impresión por pantalla. 

nombre = input ("Por favor, ingresa tu nombre:")
apellido = input("Por favor, ingresa tu apellido:")
edad = input ("¿Cuántos años tenés?")
lugarDeResidencia = input("¿En donde vivis?")

print (f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {lugarDeResidencia}.")

#------------------------------------------------------------------------------------------------

# 4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y
# su perímetro. 

PI = 3.14 #Declaramos una constante PI

radio = float(input("Ingresa el radio del círculo:"))

area = PI * radio * radio #Calculamos el área del círculo

perimetro = 2 * PI * radio #calculamos el perímetro del círculo

print (f"El área del círculo es: {area} y su perímetro es: {perimetro}")

#-------------------------------------------------------------------------------------------------

# 5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a
# cuántas horas equivale. 

segundos = int(input("Ingresa la cantidad de segundos:"))

horas = segundos // 3600 #Dividimos por 3600 para obtener las horas

print(f"{segundos} segundos equivalen a {horas} horas.")

#-------------------------------------------------------------------------------------------------

# 6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de
# multiplicar de dicho número.  

numero = int(input("Por favor, ingresa un número:"))

#Se podria hacer más rápido con un ciclo for, pero todavia no lo estamos utilizando

resultado1 = numero * 1
resultado2 = numero * 2
resultado3 = numero * 3
resultado4 = numero * 4
resultado5 = numero * 5
resultado6 = numero * 6
resultado7 = numero * 7
resultado8 = numero * 8
resultado9 = numero * 9
resultado10 = numero * 10

print(f"{numero} x 1 = {resultado1}")
print(f"{numero} x 2 = {resultado2}")
print(f"{numero} x 3 = {resultado3}")
print(f"{numero} x 4 = {resultado4}")
print(f"{numero} x 5 = {resultado5}")
print(f"{numero} x 6 = {resultado6}")
print(f"{numero} x 7 = {resultado7}")
print(f"{numero} x 8 = {resultado8}")
print(f"{numero} x 9 = {resultado9}")
print(f"{numero} x 10 = {resultado10}")

#-----------------------------------------------------------------------------------------

# 7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por
# pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos. 

numero1 = int(input("Ingresa un número entero (distinto de 0):"))
numero2 = int(input("Ingresa otro número entero (distinto de 0):"))

#habria que verificar antes que estos números sean distintos de cero a traves de un if

print(f"La suma es: {numero1} + {numero2}")
print(f"La resta es: {numero1} - {numero2}")
print(f"La multiplicación es: {numero1} * {numero2}")
print(f"La división es: {numero1} / {numero2}") 

#------------------------------------------------------------------------------------------

# 8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice
# de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente modo:
# IMC = peso / (altura * altura)  

altura = float(input("Ingresa tu altura:"))
peso = float(input("Ingresa tu peso:"))

indiceMasaCorporal = peso / (altura ** 2)

print(f"Su índice de masa corporal es: {indiceMasaCorporal}")

#-------------------------------------------------------------------------------------------

# 9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por
# pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia:
# Temperatura en Fahrenheit =  (9/5) . Temperatura en Celsius + 32

tempCelsius = float(input("Ingrese la temperatura en Celsius:"))

tempFahrenheit = (9/5) * tempCelsius + 32

print(f"EL equivalente en grados Fahrenheit es: {tempFahrenheit}")

#--------------------------------------------------------------------------------------------

# 10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de
# dichos números. 

num1 = int(input("Ingrese el primer número:"))
num2 = int(input("Ingrese el segundo número:"))
num3 = int(input("Ingrese el terer número:"))

promedio = (num1 + num2 + num3) / 3

print(f"El promedio de los números es: {promedio}")

#-------------------------------------------------------------------------------------------