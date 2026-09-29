
from pathlib import Path


DIRECTORIO_DATOS = Path(__file__).resolve().parent
RUTA_ALUMNOS = DIRECTORIO_DATOS / "alumnos.txt"
RUTA_APROBADOS = DIRECTORIO_DATOS / "aprobados.txt"


def leer_alumnos():
    alumnos_dicc = {}
    RUTA_ALUMNOS.touch(exist_ok=True)
    with RUTA_ALUMNOS.open("r", encoding="utf-8") as archivo:
        for linea in archivo:
            if not linea.strip():
                continue
            nombre, apellido, legajo, nota = linea.strip().split(";")
            alumnos_dicc[legajo]={"Nombre": nombre, "Apellido": apellido, "Nota": float(nota)}
    return alumnos_dicc


def leer_aprobados():
    aprobados_dicc = {}
    RUTA_APROBADOS.touch(exist_ok=True)
    with RUTA_APROBADOS.open("r", encoding="utf-8") as archivo:
        for linea in archivo:
            if not linea.strip():
                continue
            nombre, apellido, legajo, nota = linea.strip().split(";")
            aprobados_dicc[legajo] = {"Nombre": nombre, "Apellido": apellido, "Nota": float(nota)}
    return aprobados_dicc



alumnos_dicc = {}
def agregar_alumno(alumnos_dicc):
    legajo= input("Ingrese el legajo (5 dígitos): ")
    while not legajo.isdigit() or len(legajo)!= 5:
        print("El legajo debe tener exactamente 5 dígitos.")
        legajo= input("Ingrese el legajo (5 dígitos): ")

    if legajo in alumnos_dicc:
        print(f"El legajo {legajo} ya está registrado en alumnos.txt; no se agregará nuevamente.")
        return
    nombre=input("Ingrese el nombre: ")
    while not nombre.isalpha():
        print("El nombre solo puede contener letras, sin números ni espacios.")
        nombre= input("Ingrese el nombre: ")
    apellido= input("Ingrese el apellido: ")
    while not apellido.isalpha():
            print("El apellido solo puede contener letras, sin números ni espacios.")
            apellido= input("Ingrese el apellido: ")

    nota= input("Ingrese una nota entre 1 y 10: ")
    while not nota.replace(".", "", 1).isdigit() or float(nota) < 1 or float(nota) > 10:
        print("La nota ingresada no es válida.")
        nota = input("Ingrese una nota entre 1 y 10: ")

        while not nota.replace(".", "", 1).isdigit():
            print("Debe ingresar un valor numérico.")
            nota = input("Ingrese una nota entre 1 y 10: ")

    nota = float(nota)

    with RUTA_ALUMNOS.open("a", encoding="utf-8") as archivo:
        archivo.write(f"{nombre};{apellido};{legajo};{nota}\n")
        alumnos_dicc[legajo]={"Nombre": nombre, "Apellido": apellido, "Nota": float(nota)}


def guardar_aprobados(alumnos_dicc):

    with RUTA_APROBADOS.open("w", encoding="utf-8") as archivo:
        hay_aprobados= False
        for legajo,datos in alumnos_dicc.items():
            if datos["Nota"]>=6:
                hay_aprobados= True
                nombre= datos["Nombre"]
                apellido= datos["Apellido"]
                nota= datos["Nota"]
                archivo.write(f"{nombre};{apellido};{legajo};{nota}\n")
        if not hay_aprobados:
            print("Todavía no hay alumnos aprobados registrados.")


def mostrar_alumnos(alumnos_dicc):
    if not alumnos_dicc:
        print("Todavía no hay alumnos registrados.")
        return
    for legajo, datos in alumnos_dicc.items():
        print(f"Legajo: {legajo} | Nombre: {datos['Nombre']} {datos['Apellido']} | Nota: {datos['Nota']}")


def mostrar_aprobados():
    aprobados_dicc = leer_aprobados()
    if not aprobados_dicc:
        print("Todavía no hay alumnos aprobados registrados.")
        return
    for legajo, datos in aprobados_dicc.items():
        print(f"Legajo: {legajo} | Nombre: {datos['Nombre']} {datos['Apellido']} | Nota: {datos['Nota']}")



opcion = ""
while opcion != "5":
    print("1. Consultar alumnos")
    print("2. Registrar un alumno")
    print("3. Crear y mostrar el archivo de aprobados")
    print("4. Consultar aprobados")
    print("5. Cerrar el programa")
    opcion = input("Elija una opción: ")
    if opcion == "2":
        alumnos_dicc = leer_alumnos()
        agregar_alumno(alumnos_dicc)
    elif opcion == "3":
        alumnos_dicc = leer_alumnos()
        guardar_aprobados(alumnos_dicc)
        mostrar_aprobados()
    elif opcion == "1":
        mostrar_alumnos(leer_alumnos())
    elif opcion == "4":
        mostrar_aprobados()
    elif opcion == "5":
        print("Cerrando el programa...")
    else:
        print("La opción no es válida. Ingrese un número del 1 al 5.")







