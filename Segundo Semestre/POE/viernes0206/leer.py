path = "c:\\bdd\\datos2.txt" # UBICACION ARCHIVO

file = open(path, "r") # S: SI NO EXISTE, LO CREA

r = file.read()
print(r)

file.close()