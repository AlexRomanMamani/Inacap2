import os
path = "c:\\bdd\\"
# ABRE UN ARCHIVO EN MODO ESCRITURA
archivo = open(path+'archivo.txt', 'r')

tupla = archivo.read()
print(tupla)
archivo.close()