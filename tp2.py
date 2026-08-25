#Ejercicio 1
edad=int(input("Ingrese su edad por favor: "))

if edad>=18:
    print("Es mayor de edad")

#Ejercicio 2
nota=int(input("Ingrese su nota: "))

if nota>=6:
    print("Aprobado")
else:
    print("Desaprobado")
#Ejercicio 3

num=int(input("ingrese un número:"))

if num%2==0:
    print("Ha ingresado un número par")
else:
    print("Ha ingresado un número impar")


#Ejercicio 4
edad=int(input("Ingrese su edad: "))

if edad<12:
    print("Sos un niño")
elif edad >=12 and edad<18:
    print("Sos un adolescente")
elif edad>=18 and edad<30:
    print("Sos un adulto joven")
else:
    print("Sos un adulto")

#Ejercicio 5

contrasenia=input("Ingrese una contraseña entre 8 y 14 caracteres: ")
contrasenia_len=len(contrasenia)

if contrasenia_len>=8 and contrasenia_len<=14:
    print("Contraseña válida")
else:
    print(f"Contraseña inválida, tiene {contrasenia_len} caracteres")

#Ejercicio 6
from statistics import mode, median, mean
import random
numeros_aleatorios=[random.randint(1,10) for i in range(10)]
media_n=mean(numeros_aleatorios)
mediana_n=median(numeros_aleatorios)
moda_n=mode(numeros_aleatorios)
print(f"Sus numeros aleatorios son: {numeros_aleatorios}")
print(f"La moda de sus números es: {moda_n}")
print(f"La media de sus números es: {media_n}")
print(f"La mediana de sus números es: {mediana_n}")


if media_n>mediana_n and mediana_n>moda_n:
    print("Sus números tienen sesgo positivo")
elif media_n<mediana_n and mediana_n<moda_n:
    print("Sus números tienen sesgo negativo")
else:
    print("Sus números no tienen sesgo")

#Ejercicio 7
texto=str(input("Ingrese una frase o nombre: "))
texto_len=len(texto)
ultima_letra=texto[texto_len-1]

if ultima_letra=="A" or ultima_letra=="a" or ultima_letra=="E" or ultima_letra=="e" or ultima_letra=="I" or ultima_letra=="i" or ultima_letra=="O" or ultima_letra=="o" or ultima_letra=="U" or ultima_letra=="u":
    print(texto+"!")
else:
    print(texto)

#Ejercicio 8
nombre=str(input("Ingrese su nombre: "))
print("Seleccione una opción:")
print("1. Convertir  todo su nombre en mayúsculas")
print("2. Convertir  todo su nombre en minúsculas")
print("3. Si quiere su nombre con la primera letra mayúscula")
eleccion=int(input("Ingrese 1, 2 o 3: "))

match eleccion:
    case 1:
        print(nombre.upper())
    case 2:
        print(nombre.lower())
    case 3:
        print(nombre.title())
    case _:
        print("Ingrese una opción válida (1, 2 o 3)")

#Ejercicio 9
magnitud=float(input("Ingrese la magnitud del terremoto: "))

if magnitud>=0 and magnitud<3:
    print("Muy Leve")
elif magnitud>=3 and magnitud<4:
    print("Leve")
elif magnitud>=4 and magnitud<5:
    print("Moderado")
elif magnitud>=5 and magnitud<6:
    print("Fuerte")
elif magnitud>=6 and magnitud<7:
    print("Muy fuerte")
else:
    print("Extremo")

#Ejercicio 10
print("Ingrese en que hemisferio se encuentra actualmente (1 o 2)")
hemisferio=int(input("1. Hemisferio Norte \n2. Hemisferio Sur \n")) 
mes_anio=int(input("Ingrese en número, el mes actual: "))
dia=int(input("Ingrese el dia actual (en número): "))

match  hemisferio:
    case 1:
        if (dia>=21 and dia <=30 and mes_anio==12) or (dia>=1 and dia<=30 and mes_anio>=1 and mes_anio<=2) or (dia>=1 and dia<=20 and mes_anio==3):
            print("Estas en Invierno")
        elif (dia>=21 and dia <=30 and mes_anio==3) or (dia>=1 and dia<=30  and mes_anio>=4 and mes_anio<=5) or (dia>=1 and dia<=20 and mes_anio==6):
            print("Estas en primavera")
        elif (dia>=21 and dia <=30 and mes_anio==6) or (dia>=1 and dia<=30 and mes_anio>=7 and mes_anio<=8) or (dia>=1 and dia <= 20 and mes_anio==9 ):
            print("Estas en Verano")
        elif (dia>=21 and dia <=30 and mes_anio==9) or (dia>=1 and dia<=30 and mes_anio>=10 and mes_anio<=11) or (dia>=1 and dia <= 20 and mes_anio==12 ):
            print("Estas en Otoño")
        else:
            print("Algun dato es inválido")
    case 2:
        if (dia>=21 and dia <=30 and mes_anio==12) or (dia>=1 and dia<=30 and mes_anio>=1 and mes_anio<=2) or (dia>=1 and dia<=20 and mes_anio==3):
            print("Estas en Verano")
        elif (dia>=21 and dia <=30 and mes_anio==3) or (dia>=1 and dia<=30  and mes_anio>=4 and mes_anio<=5) or (dia>=1 and dia<=20 and mes_anio==6):
            print("Estas en Otoño")
        elif (dia>=21 and dia <=30 and mes_anio==6) or (dia>=1 and dia<=30 and mes_anio>=7 and mes_anio<=8) or (dia>=1 and dia <= 20 and mes_anio==9 ):
            print("Estas en Invierno")
        elif (dia>=21 and dia <=30 and mes_anio==9) or (dia>=1 and dia<=30 and mes_anio>=10 and mes_anio<=11) or (dia>=1 and dia <= 20 and mes_anio==12 ):
            print("Estas en Primavera")
        else:
            print("Algun dato es inválido")
    case _:
        print("Algun dato es inválido")



