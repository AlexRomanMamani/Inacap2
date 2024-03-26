import os
path = "c:\\bdd\\"
# ABRE UN ARCHIVO EN MODO ESCRITURA
archivo = open(path+'archivo.txt', 'r')
t = archivo.read()
print(t)
archivo.close()