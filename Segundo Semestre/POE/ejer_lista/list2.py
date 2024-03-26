import time
bod = []  # LISTA (MUTABLE, SE PUEDEN AGREGAR DATOS)
while True:
    art = input("Ingrese Articulo (S)alir: ")
    # SALIDA
    if art.lower() == "s":
        break
    for p in bod:
        if art.capitalize() == p["Articulo"].capitalize():
            er = input("Articulo ingresado (E)liminar (M)odificar: ")
            if er.lower() == "m":
                print("\nMODIFICAR: ")
                p["Articulo"] = input("Ingrese el nuevo Articulo: ")
                p["Precio"] = int(input("Ingrese el nuevo Precio: "))

            elif er.lower() == "e":
                print("\nELIMINAR")
                print("El siguiente Articulo ha sido eliminado: ")
                print("\t Articulo: ", p["Articulo"])
                print("\t Precio  : ", p["Precio"])
                bod.remove(p)
            break
    else:
        precio = input("Ingrese Precio: ")
        # AGREGAR REGISTRO
        # APPEND = AGREGAR REGISTRO
        # capitalize primera Mayus
        bod.append({"Articulo": art.capitalize(), "Precio": int(precio)})

for x in bod:
    print("\t Articulo: ", x["Articulo"])
    print("\t Precio  : ", x["Precio"])
