path = "c:\\bdd\\datos.txt" #instancia fisica bdd
fil = open (path, "r")
reg = fil.readlines()
for r in reg:
    datos = r.strip(). split(",")
    print(datos)
idx = max(datos[0])
idx = int(idx)+1
print(idx+1)