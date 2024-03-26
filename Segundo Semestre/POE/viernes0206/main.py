path = "c:\\bdd\\datos2.txt" # UBICACION ARCHIVO

file = open(path, "w") # S: SI NO EXISTE, LO CREA
"""""
# file.write("Registro 1") # FILE HEREDA LOS METODOS DE OPEN()

for r in range(1,11):
    file.write("Registro {} \n".format(r))

file.close()
"""""
#________________________________________


cant = input("Cantidad usuarios: ")

for i in range(0,int(cant)):
    lista = [] # SE CREA UNA LISTA
    print(i)
    r = input("Rut...: ")
    n = input("Nombre...: ")
    f = input("Fono...: ")
    c = input("Correo...: ")

    ind = i # INDICE 0

    lista.append(str(ind))
    lista.append(r)
    lista.append(n)
    lista.append(f)
    lista.append(c)
    print(lista)
    
file.writelines(",".join(lista) + "\n") # METODO JOIN SEPARA CON DELIMITADOR (,)

file.close()