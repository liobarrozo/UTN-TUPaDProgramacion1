# Ejercicio 1
for i in range(2, 21, 2):
    print(i, end=" ")
print()

# Ejercicio 2
suma = 0
while suma <= 100:
    numero = int(input("Número: "))
    suma += numero
print(f"Total: {suma}")

# Ejercicio 3: Filtrar palabras que empiezan con "a"
palabras = ["apple", "banana", "avocado"]
resultado = [p for p in palabras if p[0].lower() == "a"]
print(resultado)

# Ejercicio 4: Tabla de multiplicar del 7
for i in range(1, 11):
    print(f"7 × {i} = {7 * i}")

# Ejercicio 5: Contar vocales
texto = input("Texto: ").lower()
vocales = "aeiou"
print(f"Vocales: {sum(1 for c in texto if c in vocales)}")

# Ejercicio 6: Números repetidos manteniendo orden
numeros = [3, 1, 3, 5, 1]
repetidos = []
vistos = set()
for num in numeros:
    if num in vistos and num not in repetidos:
        repetidos.append(num)
    vistos.add(num)
print(repetidos)

# Ejercicio 7: FizzBuzz
for i in range(1, 101):
    if i % 15 == 0:
        print("FizzBuzz", end=" ")
    elif i % 3 == 0:
        print("Fizz", end=" ")
    elif i % 5 == 0:
        print("Buzz", end=" ")
    else:
        print(i, end=" ")
print()

# Ejercicio 8: Frecuencia de palabras
cadena = "hola hola mundo"
palabras = cadena.split()
frecuencia = {}
for p in palabras:
    frecuencia[p] = frecuencia.get(p, 0) + 1
print(frecuencia)

# Ejercicio 9: Filtrar consonantes
cadena = "Hola"
vocales = "aeiouáéíóuAEIOUÁÉÍÓU "
consonantes = "".join([c for c in cadena if c not in vocales and c.isalpha()])
print(consonantes)

# Ejercicio 10: Números primos
n = int(input("Número: "))
primos = []
for num in range(2, n + 1):
    es_primo = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            es_primo = False
            break
    if es_primo:
        primos.append(num)
print(primos)
