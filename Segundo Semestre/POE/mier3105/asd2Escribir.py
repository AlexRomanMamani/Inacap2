import os
path = "c:\\bdd\\"
# ABRE UN ARCHIVO EN MODO ESCRITURA
archivo = open(path+'archivo.txt', 'w')
# ABRE CONTENIDO EN EL ARCHIVO
for x in range(1,11):
    archivo.write('Hola, este es el registro {}.\n'.format(x))
# CIERRO EL ARCHIVO
archivo.close()