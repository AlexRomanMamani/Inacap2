import os
path = "c:\\bdd\\"
# ABRE UN ARCHIVO EN MODO ESCRITURA
archivo = open(path+'archivo.txt', 'w')
# ESCRIBE CONTENIDO EN EL ARCHIVO
archivo.write('Hola, este es un archivo de 1.\n')
archivo.write('Hola, este es un archivo de 2.\n')
archivo.write('Hola, este es un archivo de 3.\n')
archivo.write('Hola, este es un archivo de 4.\n')
archivo.write('Hola, este es un archivo de 5.\n')
# CIERRO EL ARCHIVO
archivo.close()