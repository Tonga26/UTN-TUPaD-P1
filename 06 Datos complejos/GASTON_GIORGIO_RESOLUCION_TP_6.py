# 1) Dado el diccionario precios_frutas 

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450} 

# Añadir las siguientes frutas con sus respectivos precios: 
# ● Naranja = 1200
# ● Manzana = 1500
# ● Pera = 2300 

print(precios_frutas)

precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

print(precios_frutas)

#----------------------------------------------------------------------------------------------------------

# 2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código desarrollado en el punto anterior, actualizar los precios de las siguientes frutas: 
# ● Banana = 1330
# ● Manzana = 1700
# ● Melón = 2800 

print(precios_frutas)

precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

print(precios_frutas)

#-----------------------------------------------------------------------------------------------------------

# 3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los precios. 

precios_frutas.keys()

#-----------------------------------------------------------------------------------------------------------

# 4) Escribí un programa que permita almacenar y consultar números telefónicos. 
# • Permití al usuario cargar 5 contactos con su nombre como clave y número como valor. 
# • Luego, pedí un nombre y mostrale el número asociado, si existe. 

# Ejemplo: 
# contactos = {"Juan": 123456, "Ana": 987654}
# Consultar: "Juan" -> muestra "123456" 

dict_contactos = {}

for i in range(1, 6):
    nombre_contacto = input(f"Ingrese el nombre del contacto {i}: ")
    numero_contacto = input(f"Ingrese el número de teléfono del contacto {i}: ")
    dict_contactos[nombre_contacto] = numero_contacto

print(dict_contactos)

contacto_solicitado = input("Ingrese el nombre del contacto a buscar: ")
print(f"El número de teléfono del contacto es: {dict_contactos[contacto_solicitado]}")

#----------------------------------------------------------------------------------------------------------------

# 5) Solicita al usuario una frase e imprime: 
# • Las palabras únicas (usando un set). 
# • Un diccionario con la cantidad de veces que aparece cada palabra. 

# Ejemplo: 
# Entrada -> "hola mundo hola"
# Salida:
# palabra_unicas = {'hola', 'mundo'}
# recuento = {'hola': 2, 'mundo': 1}

frase = input("Ingresa una frase: ").lower()

lista_de_palabras = frase.split()

palabras_unicas = set(lista_de_palabras)
print(palabras_unicas)

recuento_de_palabras = {}

for i in lista_de_palabras:
    if i in recuento_de_palabras:
        recuento_de_palabras[i] += 1
    else:
        recuento_de_palabras[i] = 1

print(recuento_de_palabras)

#----------------------------------------------------------------------------------------------------

# 6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas. Luego, mostrá el promedio de cada alumno. 

# Ejemplo: 
# alumnos = {
#     'Sofía': (10, 9, 8),
#     'Luis': (6, 7, 7)
# }

def calcular_promedios_alumnos():
    alumnos = {}
    num_alumnos = 3
    num_notas = 3

    for i in range(num_alumnos):
        while True:
            nombre_alumno = input(f"Ingresa el nombre del alumno {i+1}: ").strip()
            if nombre_alumno:
                break
            else:
                print("El nombre del alumno no puede estar vacío. Intenta de nuevo.")

        notas = []
        for j in range(num_notas):
            while True:
                try:
                    nota = float(input(f"Ingresa la nota {j+1} para {nombre_alumno}: "))
                    if 0 <= nota <= 10:  
                        notas.append(nota)
                        break
                    else:
                        print("La nota debe estar entre 0 y 10. Intenta de nuevo.")
                except ValueError:
                    print("Entrada inválida. Por favor, ingresa un número para la nota.")
        alumnos[nombre_alumno] = tuple(notas)

    print("\n--- Promedios de los Alumnos ---")
    for nombre, tupla_notas in alumnos.items():
        promedio = sum(tupla_notas) / len(tupla_notas)
        print(f"El promedio de {nombre} es: {promedio:.2f}")

calcular_promedios_alumnos()

#-----------------------------------------------------------------------------------------------------

# 7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1 y Parcial 2: 
# • Mostrá los que aprobaron ambos parciales. 
# • Mostrá los que aprobaron solo uno de los dos. 
# • Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir). 

aprobados_parcial1 = {101, 105, 108, 112, 115, 120}
aprobados_parcial2 = {101, 103, 108, 110, 115, 118}

print("--- Estudiantes que Aprobaron Parcial 1 ---")
print(aprobados_parcial1)
print("\n--- Estudiantes que Aprobaron Parcial 2 ---")
print(aprobados_parcial2)

ambos_parciales = aprobados_parcial1.intersection(aprobados_parcial2)

print("\n--- Estudiantes que Aprobaron AMBOS parciales ---")
print(ambos_parciales)

solo_uno = aprobados_parcial1.symmetric_difference(aprobados_parcial2)

print("\n--- Estudiantes que Aprobaron SOLO UNO de los dos parciales ---")
print(solo_uno)

al_menos_uno = aprobados_parcial1.union(aprobados_parcial2)

print("\n--- Lista TOTAL de estudiantes que Aprobaron AL MENOS UN parcial ---")
print(al_menos_uno)

#------------------------------------------------------------------------------------------------------

# 8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock.
# Permití al usuario: 
# • Consultar el stock de un producto ingresado. 
# • Agregar unidades al stock si el producto ya existe. 
# • Agregar un nuevo producto si no existe. 

def gestionar_stock():
    # Inicializamos el diccionario de stock con algunos productos de ejemplo
    stock_productos = {
        'Remera': 50,
        'Pantalón': 30,
        'Zapatillas': 25,
        'Medias': 100
    }

    while True:
        print("\n--- Menú de Gestión de Stock ---")
        print("1. Consultar stock de un producto")
        print("2. Agregar/Actualizar stock de un producto")
        print("3. Mostrar todo el stock")
        print("4. Salir")

        opcion = input("Elegí una opción (1-4): ").strip()

        if opcion == '1':
            producto = input("Ingresá el nombre del producto a consultar: ").strip()
            if producto in stock_productos:
                print(f"El stock de '{producto}' es: {stock_productos[producto]} unidades.")
            else:
                print(f"'{producto}' no se encuentra en el stock.")

        elif opcion == '2':
            producto = input("Ingresá el nombre del producto: ").strip()
            while True:
                try:
                    cantidad = int(input(f"Ingresá la cantidad a agregar para '{producto}': "))
                    if cantidad >= 0:
                        break
                    else:
                        print("La cantidad no puede ser negativa. Por favor, ingresá un número positivo.")
                except ValueError:
                    print("Entrada inválida. Por favor, ingresá un número entero para la cantidad.")

            if producto in stock_productos:
                stock_productos[producto] += cantidad
                print(f"Stock de '{producto}' actualizado. Nuevo stock: {stock_productos[producto]} unidades.")
            else:
                stock_productos[producto] = cantidad
                print(f"'{producto}' agregado al stock con: {stock_productos[producto]} unidades.")

        elif opcion == '3':
            if not stock_productos:
                print("El stock está vacío.")
            else:
                print("\n--- Stock Actual ---")
                for prod, stock in stock_productos.items():
                    print(f"- {prod}: {stock} unidades")

        elif opcion == '4':
            print("Saliendo del programa de gestión de stock. ¡Hasta luego!")
            break

        else:
            print("Opción inválida. Por favor, ingresá un número entre 1 y 4.")

# Ejecutar la función de gestión de stock
gestionar_stock()

#-----------------------------------------------------------------------------------------------------

# 9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.

# Ejemplo:
# agenda = {
#     ('Lunes', '10:00'): 'Reunión',
#     ('Martes', '15:00'): 'Clase de inglés'
# } 
#Permití consultar qué actividad hay en cierto día y hora. 

agenda_simple = {
    ('Lunes', '10:00'): 'Reunión con Pedro',
    ('Martes', '14:30'): 'Clase de Piano',
    ('Miércoles', '09:00'): 'Ir al Banco'
}

print("¡Hola! Esta es tu agenda simple.")
print("Eventos guardados:", agenda_simple) 


dia_a_consultar = input("\n¿Qué día querés consultar? (ej: Lunes): ").strip()
hora_a_consultar = input("¿Qué hora querés consultar? (ej: 10:00): ").strip()

clave_buscada = (dia_a_consultar, hora_a_consultar)


if clave_buscada in agenda_simple:
    evento_encontrado = agenda_simple[clave_buscada]
    print(f"\nPara el {dia_a_consultar} a las {hora_a_consultar} tenés: {evento_encontrado}")
else:
    print(f"\nNo hay nada programado para el {dia_a_consultar} a las {hora_a_consultar}.")

print("\n¡Eso es todo por ahora!")

#-----------------------------------------------------------------------------------------------------

# 10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo diccionario donde: 
# • Las capitales sean las claves. 
# • Los países sean los valores. 

# Ejemplo: 
# original = {'Argentina': 'Buenos Aires', 'Chile': 'Santiago'}
# invertido = {'Buenos Aires': 'Argentina', 'Santiago': 'Chile'}

# Diccionario original: Países como claves, Capitales como valores
paises_capitales_original = {
    'Argentina': 'Buenos Aires',
    'Chile': 'Santiago',
    'Uruguay': 'Montevideo',
    'Perú': 'Lima',
    'España': 'Madrid',
    'Francia': 'París'
}

print("--- Diccionario Original (País: Capital) ---")
print(paises_capitales_original)

# Construir el nuevo diccionario invertido
# Usamos un diccionario por comprensión (dictionary comprehension)
# Para cada 'pais', 'capital' en los pares clave-valor del diccionario original,
# creamos un nuevo par donde 'capital' es la nueva clave y 'pais' es el nuevo valor.
capitales_paises_invertido = {
    capital: pais
    for pais, capital in paises_capitales_original.items()
}

print("\n--- Diccionario Invertido (Capital: País) ---")
print(capitales_paises_invertido)


