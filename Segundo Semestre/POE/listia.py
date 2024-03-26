bod = []  # Lista para almacenar los artículos

while True:
    art = input("Ingrese Articulo (S)alir: ")

    # Salida
    if art.lower() == "s":
        break

    encontrado = False  # Bandera para indicar si se encontró el artículo

    for item in bod:
        if art.capitalize() == item["Articulo"].capitalize():
            encontrado = True
            er = input("Articulo ingresado (E)liminar (M)odificar: ")
            if er.lower() == "m":
                print("Modificar")
                # Realizar acciones de modificación del artículo aquí
            elif er.lower() == "e":
                print("Eliminar")
                # Realizar acciones de eliminación del artículo aquí
            break  # Salir del bucle for si se encontró el artículo

    if not encontrado:
        print("Articulo no encontrado")
        # Realizar acciones de creación del artículo aquí
