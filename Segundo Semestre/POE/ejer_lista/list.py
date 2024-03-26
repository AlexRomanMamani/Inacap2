import time
bod = []  # LISTA (MUTABLE, SE PUEDEN AGREGAR DATOS)
while True:
    art = input("Ingrese Articulo (S)alir: ")
    # SALIDA
    if art.lower() == "s":
        break
    precio = input("Ingrese Precio: ")
    # AGREGAR REGISTRO
    # APPEND = AGREGAR REGISTRO
    # capitalize primera Mayus
    bod.append({"Articulo": art.capitalize(), "Precio": int(precio)})
# ARTICULO Y PRECIO SON CASE SENSITIVE, ESTO IMPRIME TODOS LOS DATOS EN BOD

for x in bod:
    print("\t Articulo: ", x["Articulo"])
    print("\t Precio  : ", x["Precio"])
# IMPRIME TODOS LOS REGISTROS
print(bod)
# IMPRIME LA CANTIDAD DE ITEMS EN LA LISTA
print("Hay {} items en la lista".format(len(bod)))
# IMPRIME ITEM INDEXEADO EN 1 (0,1,2...)
print(bod[1])
# IMPRIMIR UN RANGO DE ITEMS INDEXEADOS 2:5
print(bod[2:5])
# IMPRIMIR DESDE EL INICIO AL INDEX 3 [:4]
print(bod[:4])
