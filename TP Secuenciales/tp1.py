#Ejercicio 1
print("Hola Mundo!")

#Ejercicio 2
nombre=str(input("Ingrese su nombre:"))
print(f"Hola {nombre}! ")

#Ejercicio 3
nombre=str(input("Ingrese su nombre: "))
apellido=str(input("Ingrese su apellido: "))
edad=int(input("Ingrese su edad: "))
lug_residencia=str(input("Ingrese su lugar de residencia: "))

print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {lug_residencia}")


#Ejercicio 4
import math

pi=math.pi
radio=float(input("Ingrese el radio:"))


area_circulo= (pi*(radio**2))
perimetro_circulo = (2*pi*radio)
print("El area del circulo es:",area_circulo)
print("El perimetro del circulo es:", perimetro_circulo)

#Ejercicio 5
segundos = int(input("Ingrese una cantidad de segundos: "))
horas = round(segundos / 3600, 2)  # Redondea a 2 decimales

print(f"Equivale a {horas} horas")

#Ejercicio 6
num=float(input("Ingrese un número, le mostraremos su tabla de multiplicar: "))
print(f"1x{num}= {1*num}")
print(f"2x{num}= {2*num}")
print(f"3x{num}= {3*num}")
print(f"4x{num}= {4*num}")
print(f"5x{num}= {5*num}")
print(f"6x{num}= {6*num}")
print(f"7x{num}= {7*num}")
print(f"8x{num}= {8*num}")
print(f"9x{num}= {9*num}")
print(f"10x{num}= {10*num}")

#Ejercicio 7
num1=float(input("Ingrese el primer numero, que NO sea 0:"))
num2=float(input("Ingrese el segundo numero, que NO sea 0:"))

suma=num1+num2
resta=num1-num2
multi=num1*num2
division=num1/num2

print("La suma es:",suma)
print("La resta es:",resta)
print("La multiplicacion es:",multi)
print("La division es:",division)

#Ejercicio 8
peso=float(input("Ingrese su peso: "))
altura=float(input("Ingrese su altura en metros:"))
imc=peso/(altura**2)
print(f"Tu IMC es: {imc}")


#Ejercicio 9
grados_c=float(input("Ingrese una temperatura en grados Celcius: "))
grados_f=((9/5)*grados_c)+32
print(f"Sus grados Celicius equivalen a {grados_f} grados Fahrenheit")


#Ejercicio 10
n1=float(input("Ingrese su primer número: "))
n2=float(input("Ingrese su segundo número: "))
n3=float(input("Ingrese su tercer número: "))

promedio=(n1+n2+n3)/3

print(f"El promedio de sus números es: {promedio}")