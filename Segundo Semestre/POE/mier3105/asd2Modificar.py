import os
path = "c:\\bdd\\"

if os.path.exists(path + 'archivo.txt'):
    # ABRE EL ARCHIVO EN MODO LECTURA
    archivo = open(path +'archivo.txt', 'r')
    # LEE EL CONTENIDO DEL ARCHIVO
    contenido = archivo.read()
    # CIERRA EL ARCHIVO
    archivo.close()
    # MODIFICA EL CONTENIDO
    contenido_modificado = contenido + '\n Esto es una modificacion'
    # ABRE EL ARCHIVO EN MODO ESCRITURA
    archivo = open(path + 'archivo.txt', 'w')
    # ESCRIBE EL CONTENIDO MODIFICADO EN EL ARCHIVO, ELIMINANDO EL ANTERIOR
    archivo.write(contenido_modificado)
    # CIERRA EL ARCHIVO
    archivo.close()
    print("hola")
else:
    print("El archivo no existe")

