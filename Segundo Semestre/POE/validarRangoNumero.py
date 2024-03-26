def n_P():
    # como validar que a sea solo numero de rango 1 a 5 y no string
    while True:
        try:
            a = int(input("Ingrese opción (1-5): "))
            if a < 1 or a > 5:
                print("Error, solo se permite 1 a 5")
            else:
                break
        except:
            print("Error, el valor ingreado debe ser un numero")
    return a
