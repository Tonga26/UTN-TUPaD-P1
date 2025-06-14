# 1) Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa  función para calcular y mostrar en pantalla el factorial de todos los números enteros entre 1 y el número que indique el usuario.

def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num-1) 

num = int(input("Ingrese un número para calcular su factorial: "))

for i in range(num + 1):
    resultado = factorial(i)
    print(f"El factorial de {i} es {resultado}")

# 2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario especifique.

def serie_fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return serie_fibonacci(n-1) + serie_fibonacci(n-2)
    
num = int(input("Ingrese un número para calcular la serie fibonacci: "))

for i in range(0, num + 1):
    valor = serie_fibonacci(i)
    print(f"Fibonacci({i}) = {valor}")


# 3) Crea una función recursiva que calcule la potencia de un número base elevado a un exponente, utilizando la fórmula 𝑛^𝑚 = 𝑛∗𝑚^(𝑚−1). Prueba esta función en un algoritmo general.

def potencia(num, m):
    if m == 0:
        return 1
    else:
        return num * potencia(num, m - 1) 
    
base = int(input("Ingrese la base: "))
exp = int(input("Ingrese el exponente: "))

resultado = potencia(base, exp)
print(f"El resultado de {base} elevado a {exp} es {resultado}")

# 4) Crear una función recursiva en Python que reciba un número entero positivo en base decimal y devuelva su representación en binario como una cadena de texto. Cuando representamos un número en binario, lo expresamos usando solamente ceros (0) y unos (1), en base 2. 

# Para convertir un número decimal a binario, se puede seguir este procedimiento: 
# 1. Dividir el número por 2. 
# 2. Guardar el resto (0 o 1). 
# 3. Repetir el proceso con el cociente hasta que llegue a 0. 
# 4. Los restos obtenidos, leídos de abajo hacia arriba, forman el número binario. 

# Convertir el número 10 a binario: 
# 10 ÷ 2 = 5     resto: 0   
#  5 ÷ 2 = 2     resto: 1   
#  2 ÷ 2 = 1     resto: 0   
#  1 ÷ 2 = 0     resto: 1   
# Leyendo los restos de abajo hacia arriba: 1 0 1 0 → El resultado binario es "1010".

def convertir_a_binario(num_decimal):
    resto = num_decimal % 2 
    if num_decimal == 0:
        return ""
    else:
        return convertir_a_binario(num_decimal // 2) + str(resto)

num_decimal = int(input("Ingrese un número decimal: "))
num_binario = convertir_a_binario(num_decimal)
print(f"El número en binario es {num_binario}")

# 5) Implementá una función recursiva llamada es_palindromo(palabra) que reciba una cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no lo es. 
# Requisitos: 
# - La solución debe ser recursiva. 
# - No se debe usar [::-1] ni la función reversed(). 

def es_palindromo(palabra):
        if len(palabra) == 0 or len(palabra) == 1:
            return True
        elif palabra[0] != palabra[-1]:
            return False
        else:
             return es_palindromo(palabra[1:len(palabra)-1])

palabra_ingresada = input("Ingrese una palabra para verificar si es o no un palíndromo: ")
palindromo = es_palindromo(palabra_ingresada)

if es_palindromo(palabra_ingresada):
    print(f"La palabra '{palabra_ingresada}' es un palíndromo.")
else:
    print(f"La palabra '{palabra_ingresada}' NO es un palíndromo.")

# 6) Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un número entero positivo y devuelva la suma de todos sus dígitos. 
# Restricciones: 
# - No se puede convertir el número a string. 
# - Usá operaciones matemáticas (%, //) y recursión. 

# Ejemplos: 
# suma_digitos(1234)   → 10  (1 + 2 + 3 + 4) 
# suma_digitos(9)      → 9 
# suma_digitos(305)    → 8   (3 + 0 + 5)

def suma_digitos(n):
    if n == 0:
        return 0
    else:
        ultimo_digito = n % 10
        return ultimo_digito + suma_digitos(n // 10)

numero = int(input("Ingrese un número entero positivo: "))
suma = suma_digitos(numero)
print(f"La suma de todos los digitos es {suma}.")

# 7) Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al último nivel con un solo bloque. 
 
#Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el nivel más bajo y devuelva el total de bloques que necesita para construir toda la pirámide. 

# Ejemplos: 
# contar_bloques(1)   → 1         (1) 
# contar_bloques(2)   → 3         (2 + 1) 
# contar_bloques(4)   → 10        (4 + 3 + 2 + 1)

def contar_bloques(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return n + contar_bloques(n - 1)

bloques = int(input("Ingrese el número de bloques de la base de la pirámide: "))
cant_bloques = contar_bloques(bloques)
print(f"Para construir la pirámide se necesitan {cant_bloques} bloques.")

# 8) Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces aparece ese dígito dentro del número. 

# Ejemplos: 
# - contar_digito(12233421, 2)   → 3   
# - contar_digito(5555, 5)       → 4  

def contar_digito(numero, digito):
    if numero == 0:
        return 0
    else:
        ultimo_digito = numero % 10
        resto = numero // 10
        if ultimo_digito == digito:
            return 1 + contar_digito(resto, digito)
        else: 
            return 0 + contar_digito(resto, digito)


numero = int(input("Ingrese un número entero positivo: "))
digito = int(input("Ingrese el dígito que quiere comparar (entre 0 y 9): "))
while digito < 0 or digito > 9:
    print("¡Error! Debe ingresar un dígito entre 0 y 9.")
    digito = int(input("Ingrese el dígito nuevamente (entre 0 y 9): "))
    
cantidad = contar_digito(numero, digito)
print(f"El dígito {digito} aparece {cantidad} veces en el número {numero}.")
