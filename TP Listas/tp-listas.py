# Ejercicio 1
multiplos_de_4 = [num for num in range(1, 101) if num % 4 == 0]
print(f"Ejercicio 1 - Múltiplos de 4: {multiplos_de_4}")

# Ejercicio 2
mis_elementos = ["gato", "libro", "manzana", "guitarra", "computadora"]
penultimo = mis_elementos[-2]
print(f"Ejercicio 2 - Lista: {mis_elementos}")
print(f"Penúltimo elemento: {penultimo}")

# Ejercicio 3
lista_vacia = []
lista_vacia.append("python")
lista_vacia.append("programacion")
lista_vacia.append("listas")
print(f"Ejercicio 3 - Lista con palabras: {lista_vacia}")

# Ejercicio 4
animales = ["perro", "gato", "conejo", "pez"]
animales[1] = "loro"
animales[-1] = "oso"
print(f"Ejercicio 4 - Animales modificados: {animales}")

# Ejercicio 5
numeros = [8, 15, 3, 22, 7]
numeros.remove(max(numeros))
print(f"Ejercicio 5 - Números después de eliminar el máximo: {numeros}")

# Ejercicio 6
numeros_saltos = list(range(10, 31, 5))
dos_primeros = numeros_saltos[:2]
print(f"Ejercicio 6 - Lista completa: {numeros_saltos}")
print(f"Los dos primeros: {dos_primeros}")

# Ejercicio 7
autos = ["sedan", "polo", "suran", "gol"]
autos[1] = "corolla"
autos[2] = "civic"
print(f"Ejercicio 7 - Autos modificados: {autos}")

# Ejercicio 8
dobles = []
dobles.append(5 * 2)
dobles.append(10 * 2)
dobles.append(15 * 2)
print(f"Ejercicio 8 - Lista dobles: {dobles}")

# Ejercicio 9
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
compras[2].append("jugo")
compras[1][1] = "tallarines"
compras[0].remove("pan")

print(f"Ejercicio 9 - Compras modificadas: {compras}")

# Ejercicio 10
lista_anidada = [15, True, [25.5, 57.9, 30.6], False]

print(f"Ejercicio 10 - Lista anidada: {lista_anidada}")
print(f"  lista_anidada[0] = {lista_anidada[0]}")
print(f"  lista_anidada[1] = {lista_anidada[1]}")
print(f"  lista_anidada[2][0] = {lista_anidada[2][0]}")
print(f"  lista_anidada[2][1] = {lista_anidada[2][1]}")
print(f"  lista_anidada[2][2] = {lista_anidada[2][2]}")
print(f"  lista_anidada[3] = {lista_anidada[3]}")
