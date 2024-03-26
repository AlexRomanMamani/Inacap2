path = "c:\\bdd\\datos.txt" #instancia fisica bdd
fil = open (path, "r")
reg = fil.readlines()
for r in reg:
    datos = r.strip(). split(",")
    if "3333" in datos: #si valor 3333 se encuentra en la lista datos
        print("encontrado!")
        print(datos.index("3333")) #encontrado en posicion
        print(datos[datos.index("3333")]) # es igual a datos[1]
    print(datos)
fil.close()