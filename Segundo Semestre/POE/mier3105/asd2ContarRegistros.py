import os
path = "c:\\bdd\\"
# ABRE UN ARCHIVO EN MODO ESCRITURA
archivo = open(path+'archivo.txt', 'r')
tupla = archivo.read()
print(tupla)
cont = 1
for x in tupla: # CUENTA LOS CARACTERES, NO LOS REGISTROS
    cont+=1
print(cont)
archivo.close()