import math

# Ejercicio 1

def imprimir_hola_mundo():
    print("Hola Mundo!")


# Ejercicio 2

def saludar_usuario(nombre):
    return f"Hola {nombre}!"


# Ejercicio 3

def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")


# Ejercicio 4

def calcular_area_circulo(radio):
    return math.pi * radio ** 2


def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio


# Ejercicio 5

def segundos_a_horas(segundos):
    return segundos / 3600


# Ejercicio 6

def tabla_multiplicar(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")


# Ejercicio 7

def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b
    return suma, resta, multiplicacion, division


# Ejercicio 8

def calcular_imc(peso, altura):
    return peso / (altura ** 2)


# Ejercicio 9

def celsius_a_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


# Ejercicio 10

def calcular_promedio(a, b, c):
    return (a + b + c) / 3


# Programa principal

imprimir_hola_mundo()

nombre = input("Ingrese su nombre: ")
print(saludar_usuario(nombre))

nombre = input("Nombre: ")
apellido = input("Apellido: ")
edad = int(input("Edad: "))
residencia = input("Residencia: ")
informacion_personal(nombre, apellido, edad, residencia)

radio = float(input("Ingrese el radio del círculo: "))
print(f"Área: {calcular_area_circulo(radio):.2f}")
print(f"Perímetro: {calcular_perimetro_circulo(radio):.2f}")

segundos = float(input("Ingrese cantidad de segundos: "))
print(f"Horas: {segundos_a_horas(segundos):.2f}")

numero = int(input("Ingrese un número para la tabla: "))
tabla_multiplicar(numero)

resultado = operaciones_basicas(10, 5)
print("Suma:", resultado[0])
print("Resta:", resultado[1])
print("Multiplicación:", resultado[2])
print("División:", resultado[3])

peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en metros: "))
print(f"IMC: {calcular_imc(peso, altura):.2f}")

temperatura_c = float(input("Ingrese la temperatura en °C: "))
print(f"{temperatura_c}°C = {celsius_a_fahrenheit(temperatura_c):.2f}°F")

a = float(input("Ingrese el primer número: "))
b = float(input("Ingrese el segundo número: "))
c = float(input("Ingrese el tercer número: "))
print(f"Promedio: {calcular_promedio(a, b, c):.2f}")
