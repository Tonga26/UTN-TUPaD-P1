# 1. Crear una función llamada imprimir_hola_mundo que imprima por pantalla el mensaje: “Hola Mundo!”. 
# Llamar a esta función desde el programa principal.

# Definición de la funcion
def imprimir_hola_mundo():
    print("Hola Mundo!")
    
# Programa principal
imprimir_hola_mundo()

#------------------------------------------------------------------------------------------------------

# 2. Crear  una  función  llamada  saludar_usuario(nombre) que reciba como parámetro un nombre y devuelva un saludo personalizado. Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver: “Hola Marcos!”. Llamar a esta función desde el programa principal solicitando el nombre al usuario.

# Definición de la funcion
def saludar_usuario(nombre):
    print(f"Hola, {nombre}!")

# Programa principal
saludar_usuario(input("Ingrese su nombre: "))

#---------------------------------------------------------------------------------------------------------

# 3. Crear una función llamada informacion_personal(nombre, apellido, edad, residencia) que reciba cuatro parámetros e imprima:  “Soy [nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pedir los datos al usuario y llamar a esta función con los valores ingresados.

# Definición de funciones
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

# Programa principal
nombre = input(f"Ingresá tu nombre: ")
apellido = input(f"Ingresá tu apellido: ")
edad = int(input(f"¿Cuántos años tenes?: "))
residencia = input(f"¿En donde vivís?: ")

informacion_personal(nombre, apellido, edad, residencia)

#--------------------------------------------------------------------------------------------------------

# 4. Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el área del círculo. calcular_perimetro_circulo(radio) que reciba el radio como parámetro y devuelva el perímetro del círculo. Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados.

# Definición de funciones
import math

def calcular_area_circulo(radio):
    area_circulo = float(math.pi * (radio * radio))
    return print(f"El área del círculo es {area_circulo}")

def calcular_perimetro_circulo(radio):
    perimetro_circulo = float(2 * math.pi * radio)
    return print(f"El perímetro del círculo es {perimetro_circulo}")

# Programa principal
radio = int(input("Ingrese el radio del círculo: "))
calcular_area_circulo(radio)
calcular_perimetro_circulo(radio)

#----------------------------------------------------------------------------------------------------------

# 5. Crear una función llamada segundos_a_horas(segundos) que reciba una cantidad de segundos como parámetro y devuelva la cantidad de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta función.

# Definición de funciones
def segundos_a_horas(cant_segundos):
    cant_horas = cant_segundos // 3600
    segundos_restantes = cant_segundos % 3600
    cant_minutos = segundos_restantes // 60
    segundos_finales = segundos_restantes % 60
    return print(f"{cant_segundos} segundos equivalen a {cant_horas} hora(s), {cant_minutos} minuto(s) y {segundos_finales} segundo(s)")

# Programa principal
segundos_a_horas(int(input("Ingrese la cantidad de segundos: ")))

#---------------------------------------------------------------------------------------------------------

# 6. Crear una función llamada tabla_multiplicar(numero) que reciba un número como parámetro y imprima la tabla de multiplicar de ese número del 1 al 10. Pedir al usuario el número y llamar a la función.

# Definición de funciones
def tabla_multiplicar(numero):
    for i in range(1, 10 + 1):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")

# Programa principal
tabla_multiplicar(int(input("Ingrese un número: ")))

#---------------------------------------------------------------------------------------------------------

# 7. Crear  una  función  llamada  operaciones_basicas(a,  b)  que  reciba dos números como parámetros y devuelva una tupla con el resultado de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los resultados de forma clara.

# Definición de funciones
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    if b != 0:
        division = a / b
    else:
        division = None
    return (suma, resta, multiplicacion, division)

# Programa principal
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
resultado = operaciones_basicas(num1, num2)

print(f"La suma de {num1} y {num2} es: {resultado[0]}")
print(f"La resta de {num1} y {num2} es: {resultado[1]}")
print(f"La multiplicación de {num1} y {num2} es: {resultado[2]}")

if resultado[3] == None:
    mensaje = "No es posible dividir por cero."
else:
    mensaje = f"La división de {num1} y {num2} es: {resultado[3]}"

print(mensaje)

#-------------------------------------------------------------------------------------------------------

# 8. Crear una función llamada calcular_imc(peso, altura) que reciba el peso en kilogramos y la altura en metros, y devuelva el índice de masa corporal (IMC). Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales.

# Definición de funciones
def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

# Programa principal
peso_en_kg = float(input("Ingresa tu peso en kg: "))
altura_en_metros = float(input("Ingresa tu altura en metros: "))
imc_usuario = calcular_imc(peso_en_kg, altura_en_metros)
print(f"Tu índice de masa corporal (IMC) es de {imc_usuario:.2f}")

#------------------------------------------------------------------------------------------------------

# 9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba una temperatura en grados Celsius y devuelva su equivalente en Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el resultado usando la función.

# Definición de funciones
def celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# Programa principal
temp_fahrenheit = celsius_a_fahrenheit(float(input("Ingrese la temperaura en grados Celsius: ")))
print(f"La temperatura en grados Fahrenheit es de {temp_fahrenheit}°F")

#------------------------------------------------------------------------------------------------------

# 10.Crear una función  llamada calcular_promedio(a, b, c)  que reciba tres números como parámetros y devuelva el promedio de ellos. Solicitar los números al usuario y mostrar el resultado usando esta función.

# Definición de funciones
def calcular_promedio(a, b, c):
    promedio = (a + b + c) / 3
    return promedio

# Programa principal
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))
promedio_numeros = calcular_promedio(num1, num2, num3)
print(f"El promedio de los números es {promedio_numeros}")

