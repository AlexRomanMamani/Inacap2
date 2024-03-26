import os
import time

path = "c:\\bdd\\"


def valida_opcion():
    while True:
        try:
            opcion = int(input("Ingrese una opción: "))
            if opcion >= 1 and opcion <= 5:
                return opcion
                break
            else:
                print("Opcióm inválida.")
        except ValueError:
            print("Opción inválida.")


def menu():
    print("1. Agregar usuario")
    print("2. Listar usuarios")
    print("3. Modificar usuario")
    print("4. Eliminar usuario")
    print("5. Salir")
    opcion = valida_opcion()
    return opcion


def agregar_usuario(idx):
    rut = input("Ingrese el rut del usuario: ")
    nombre = input("Ingrese el nombre del usuario: ")
    edad = input("Ingrese la edad del usuario: ")
    email = input("Ingrese el correo electrónico del usuario: ")

    # Crear un diccionario con los datos del usuario
    usuario = str(idx), rut, nombre, edad, email

    # Agregar el diccionario a la lista de usuarios
    return usuario


def crear_registro(archivo, datos):
    # Abre el archivo en modo "append" (agregar al final)
    with open(path + archivo, "a") as archivo:
        # Crea una línea de texto con los datos separados por comas
        linea = ",".join(datos) + "\n"  # AGREGA UNA , ENTRE VALORES
        # Escribe la línea en el archivo
        archivo.write(linea)


def contar_registros(archivo):
    contador = 0
    # Abre el archivo en modo lectura
    with open(path + archivo, "r") as archivo:
        # Itera sobre cada línea del archivo
        for linea in archivo:
            # Incrementa el contador por cada línea
            contador += 1
    return contador


def existe_archivo(archivo):
    if os.path.exists(path + archivo):
        return True
    else:
        return False


def crear_archivo(archivo):
    if not existe_archivo(archivo):
        with open(path + archivo, "w") as archivo:
            archivo.write("")
            archivo.close()
            print("Archivo creado correctamente.")
    else:
        print("El archivo ya existe.")


def leer_registros(archivo):
    registros = []
    # Abre el archivo en modo lectura
    with open(archivo, "r") as archivo:
        # Lee todas las líneas del archivo
        lineas = archivo.readlines()
        # Itera sobre las líneas
        for linea in lineas:
            # Elimina el carácter de salto de línea y separa los datos por comas
            datos = linea.strip().split(",")
            # Agrega los datos a la lista de registros
            registros.append(datos)
        archivo.close()
    return registros


def modificar_registro(archivo, indice, nuevos_datos):
    registros = leer_registros(archivo)
    # Verifica si el índice es válido
    if indice >= 0 and indice < len(registros):  # indice <= len(registros)
        # Reemplaza los datos del registro en la posición indicada
        registros[indice] = nuevos_datos
        # Abre el archivo en modo escritura
        with open(archivo, "w") as archivo:
            # Escribe todos los registros actualizados en el archivo
            for datos in registros:
                linea = ",".join(datos) + "\n"
                archivo.write(linea)
        archivo.close()
        print("Registro modificado correctamente.")
    else:
        print("Índice de registro inválido.")


def eliminar_registro(archivo, indice):
    registros = leer_registros(archivo)
    # Verifica si el índice es válido
    print(indice, "   ", len(registros))
    if indice >= 0 and indice < len(registros):
        # Elimina el registro en la posición indicada
        del registros[indice]
        # Abre el archivo en modo escritura
        with open(archivo, "w") as archivo:
            # Escribe todos los registros restantes en el archivo
            for datos in registros:
                linea = ",".join(datos) + "\n"
                archivo.write(linea)
        archivo.close()
        print("Registro eliminado correctamente.")
    else:
        print("Índice de registro inválido.")


def limpiar_pantalla():
    os.system("cls" if os.name == "nt" else "clear")
