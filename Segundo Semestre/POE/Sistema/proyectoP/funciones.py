import re
import time
import datetime

# Definir variables globales


def definirVariables():
    global rut, nombre, dire, edad, email, telefono, ciudad
    rut, nombre, dire, edad, email, telefono, ciudad = "", "", "", "", "", "", ""


# Hora


def hora():
    tt = time.strftime("%H:%M:%S", time.localtime())
    return tt


# Valida que rut contenga 0123456789.,-K


def lee_rut(resp):
    while True:
        respuesta = resp.upper()
        nn = "0123456789.,-K"
        l = list(nn)

        for x in respuesta:
            # print(x)
            if x not in l:
                return 0
        else:
            # print("OkElse!")
            return respuesta


# Validador de Rut


def vrut(rut):
    r = rut
    if len(r) >= 9 and len(r) <= 11:
        r = r.replace(".", "")  # remplaza . por vacio ""
        r = r.replace("-", "")
        r = r.replace(",", "")
        dv = r[-1]  # saca el ultimo numero de r
        # print("ultimo numero", dv)  # sapo
        r = r[0 : len(r) - 1]  # en r voy a dejar desde 0 hasta el largo de rut - 1
        r = list(r)  # list() crea un vector ['1', '2', '3'...]
        # print("Lista ['','',] + dv: ", r, dv)  # sapo
        s = 0  # suma de los valores
        c = 2
        # para x en {da vuelta la lista r}  (x=al primer numero del rut)
        for x in reversed(r):
            if c == 8:
                c = 2
            s = s + (int(x) * c)
            # print("Calculo: ", x, c, s)
            c += 1

        s = 11 - (s % 11)
        # print("Resultado calculo + Tipo: ", s, type(s))
        if s == 10:
            if dv.upper() == "K":  # pasa dv a mayus
                return 1
            else:
                return 0

        if s == 11:
            if dv == "0":
                return 1
            else:
                return 0

        if s != 10 and s != 11:
            # print("entro",s,dv)
            if s == int(dv):
                return 1
            else:
                return 0
    else:
        return 0


# Credito


def credito():
    obten_fecha = datetime.datetime.now()
    date = obten_fecha.date()
    year = date.strftime("%Y")
    # print(f"Current Year -> {year}")
    return """====================================
    {} CREATE BY EXPLODING TEAM             
====================================
        """.format(
        year
    )


# Menu Principal


def creamenu():
    return """\n----\033[1m \033[44mM E N U  P R I N C I P A L \033[0m\033[0m----\n
    1 ---- Ingresar Usuario
    2 ---- Modificar Usuario
    3 ---- Eliminar Usuario
    4 ---- Consultar Usuario
    5 ---- Salir\n"""


# Menu Modificar Usuario


def creamenu_mod():
    return """
    1 ---- Modificar Nombre        5 ---- Modificar Telefono
    2 ---- Modificar Dirección     6 ---- Modificar Ciudad
    3 ---- Modificar Edad          7 ---- Modificar Todos los Datos
    4 ---- Modificar Email         8 ---- Regresar\n"""


# Menu Modificar Usuario


def creamenu_usuarioExiste():
    return """\n
    1 ---- Modificar Usuario
    2 ---- Eliminar Usuario
    3 ---- Regresar\n"""


# Validador de Opcion


def n_P():
    while True:
        try:
            o = int(input("Ingrese opción (1-5): "))
            if o < 1 or o > 5:
                print("\033[91m\033[107m>>>\033[0m Error, solo se permite 1 a 5")
                time.sleep(1)
            else:
                break
        except:
            print(
                "\033[91m\033[107m>>>\033[0m Error, el valor ingreado debe ser un numero entre 1 y 5"
            )
            time.sleep(1)
    return o


# Validador de Opcion2 en Mod Usuario


def n_P2():
    while True:
        try:
            o = int(input("Ingrese opción (1-8): "))
            if o < 1 or o > 8:
                print("\033[91m\033[107m>>>\033[0m Error, solo se permite 1 a 8")
                time.sleep(1)
            else:
                break
        except:
            print(
                "\033[91m\033[107m>>>\033[0m Error, el valor ingreado debe ser un numero entre 1 y 8"
            )
            time.sleep(1)
    return o


# Validador de Opcion3 Usuario Existe


def n_P3():
    while True:
        try:
            o = int(input("Ingrese opción (1-3): "))
            if o < 1 or o > 3:
                print("\033[91m\033[107m>>>\033[0m Error, solo se permite 1 a 3")
                time.sleep(1)
            else:
                break
        except:
            print(
                "\033[91m\033[107m>>>\033[0m Error, el valor ingreado debe ser un numero entre 1 y 3"
            )
            time.sleep(1)
    return o


# Ingreso de Usuario


def ingresoUsuario():
    global rut, nombre, dire, edad, email, telefono, ciudad
    while True:
        print(
            "\n----\033[1m \033[44m I N G R E S O  D E  U S U A R I O \033[0m\033[0m----"
        )
        if rut != "":
            print(
                "\033[91m\033[107m>>>\033[0m Sistema: Ya hay un usuario registrado. Si desea ingresar otro usuario, primero elimine o modifique el usuario actual."
            )
            time.sleep(1.5)
            print(creamenu_usuarioExiste())
            op = n_P3()
            if op == 1:
                modificarUsuario()
            elif op == 2:
                eliminarUsuario()
            elif op == 3:
                print("\033[91m\033[107m>>>\033[0m Regresando...")
                time.sleep(1.5)
                break
        else:
            print(
                "\033[91m\033[107m>>>\033[0m c: Cancelar y volver al Menu Principal\n"
            )
            # RESPUESTA
            respuesta = input("Rut de Usuario: ")
            try:
                if respuesta.upper() == "C":
                    (
                        tempRut,
                        tempNombre,
                        tempDire,
                        tempEdad,
                        tempEmail,
                        tempFono,
                        tempCiudad,
                    ) = ("", "", "", "", "", "", "")
                    print(
                        "\033[91m\033[107m>>>\033[0m Cancelado. Volviendo al Menu Principal..."
                    )
                    # gracias al import time, agrega una pausa al programa (s)
                    time.sleep(1.5)
                    break
                else:
                    # RUT

                    if lee_rut(respuesta) == 0:
                        print(
                            "\033[91m\033[107m>>>\033[0m Solo puede ingresar 0-9 y K. Vuelva a intentarlo. "
                        )
                        time.sleep(1.5)
                        respuesta = ""
                        continue
                    else:
                        tempRut = respuesta.upper()
                    # rut = respuesta

                    if vrut(tempRut) == 1:
                        # sapo + \u2713= caracter unicode check
                        print("{:>20}".format("Rut valido " + "\u2713"))
                    else:
                        print(
                            "\033[91m\033[107m>>>\033[0m El rut ingresado no es valido. Vuelva a intentarlo."
                        )
                        time.sleep(1.5)
                        tempRut = ""
                        continue
            except:
                print(
                    "\033[91m\033[107m>>>\033[0m Error Sistema: El rut debe ser formato 11111111-K. Vuelva a intentarlo."
                )
                time.sleep(1.5)
                continue
            # NOMBRE
            while True:
                tempNombre = input("Nombre de Usuario: ")
                if tempNombre.upper() == "C":
                    (
                        tempRut,
                        tempNombre,
                        tempDire,
                        tempEdad,
                        tempEmail,
                        tempFono,
                        tempCiudad,
                    ) = ("", "", "", "", "", "", "")
                    print(
                        "\033[91m\033[107m>>>\033[0m Cancelado. Volviendo al Menu Principal..."
                    )
                    time.sleep(1.5)
                    break
                elif tempNombre.isnumeric() == True or tempNombre == "":
                    tempNombre = ""
                    print(
                        "\033[91m\033[107m>>>\033[0m Error Sistema: El nombre no puede ser vacio o un numero. Vuelva a intentarlo."
                    )
                    time.sleep(1.5)
                    # continue
                else:
                    while True:
                        # DIRECCION
                        tempDire = input("Dirección: ")
                        if tempDire.upper() == "C":
                            (
                                tempRut,
                                tempNombre,
                                tempDire,
                                tempEdad,
                                tempEmail,
                                tempFono,
                                tempCiudad,
                            ) = ("", "", "", "", "", "", "")
                            print(
                                "\033[91m\033[107m>>>\033[0m> Cancelado. Volviendo al Menu Principal..."
                            )
                            time.sleep(1.5)
                            break
                        elif tempDire == "":
                            tempDire = ""
                            print(
                                "\033[91m\033[107m>>>\033[0m Error Sistema: La dirección no puede ser vacio. Vuelva a intentarlo."
                            )
                            time.sleep(1.5)
                        else:
                            while True:
                                # EDAD
                                try:
                                    tempEdad = input("Edad: ")
                                    if tempEdad.upper() == "C":
                                        (
                                            tempRut,
                                            tempNombre,
                                            tempDire,
                                            tempEdad,
                                            tempEmail,
                                            tempFono,
                                            tempCiudad,
                                        ) = ("", "", "", "", "", "", "")
                                        print(
                                            "\033[91m\033[107m>>>\033[0m Cancelado. Volviendo al Menu Principal..."
                                        )
                                        time.sleep(1.5)
                                        break
                                    elif int(tempEdad) < 1 or int(tempEdad) > 120:
                                        print(
                                            "\033[91m\033[107m>>>\033[0m Error Sistema: Edad debe ser entre 1 y 120. Vuelva a Intentarlo."
                                        )
                                        time.sleep(1.5)
                                    else:
                                        while True:
                                            # EMAIL
                                            tempEmail = input(
                                                "Email (ej: aaaa@bbb.cc): "
                                            )
                                            if tempEmail.upper() == "C":
                                                (
                                                    tempRut,
                                                    tempNombre,
                                                    tempDire,
                                                    tempEdad,
                                                    tempEmail,
                                                    tempFono,
                                                    tempCiudad,
                                                ) = ("", "", "", "", "", "", "")
                                                print(
                                                    "\033[91m\033[107m>>>\033[0m Cancelado. Volviendo al Menu Principal..."
                                                )
                                                time.sleep(1.5)
                                                break
                                            elif (
                                                not verificar_correo(tempEmail)
                                                or tempEmail == ""
                                            ):
                                                print(
                                                    "El correo ingresado no es valido. Vuelva a intentarlo."
                                                )
                                            else:
                                                while True:
                                                    # TELEFONO
                                                    tempFono = input(
                                                        "Telefono (ej: 912345678 o 56912345678): "
                                                    )
                                                    if tempFono.upper() == "C":
                                                        (
                                                            tempRut,
                                                            tempNombre,
                                                            tempDire,
                                                            tempEdad,
                                                            tempEmail,
                                                            tempFono,
                                                            tempCiudad,
                                                        ) = ("", "", "", "", "", "", "")
                                                        print(
                                                            "\033[91m\033[107m>>>\033[0m Cancelado. Volviendo al Menu Principal..."
                                                        )
                                                        time.sleep(1.5)
                                                        break
                                                    elif (
                                                        tempFono.isdigit() == False
                                                        or len(tempFono) not in [9, 11]
                                                        or tempFono == ""
                                                    ):
                                                        tempFono = ""
                                                        print(
                                                            "\033[91m\033[107m>>>\033[0m> Error Sistema: El telefono debe ser numerico y tener 9 o 11 digitos. Vuelva a intentarlo."
                                                        )
                                                    else:
                                                        while True:
                                                            # CIUDAD
                                                            tempCiudad = input(
                                                                "Ciudad: "
                                                            )
                                                            if (
                                                                tempCiudad.upper()
                                                                == "C"
                                                            ):
                                                                (
                                                                    tempRut,
                                                                    tempNombre,
                                                                    tempDire,
                                                                    tempEdad,
                                                                    tempEmail,
                                                                    tempFono,
                                                                    tempCiudad,
                                                                ) = (
                                                                    "",
                                                                    "",
                                                                    "",
                                                                    "",
                                                                    "",
                                                                    "",
                                                                    "",
                                                                )
                                                                print(
                                                                    "\033[91m\033[107m>>>\033[0m> Cancelado. Volviendo al Menu Principal..."
                                                                )
                                                                time.sleep(1.5)
                                                                break
                                                            elif tempCiudad == "":
                                                                tempCiudad = ""
                                                                print(
                                                                    "\033[91m\033[107m>>>\033[0m Error Sistema: La ciudad no puede ser vacio. Vuelva a intentarlo."
                                                                )
                                                                time.sleep(1.5)
                                                            elif (
                                                                tempCiudad.isnumeric()
                                                                == True
                                                            ):
                                                                tempCiudad = ""
                                                                print(
                                                                    "\033[91m\033[107m>>>\033[0m Error Sistema: La ciudad no puede ser un numero. Vuelva a intentarlo."
                                                                )
                                                                time.sleep(1.5)
                                                            else:
                                                                (
                                                                    rut,
                                                                    nombre,
                                                                    dire,
                                                                    edad,
                                                                    email,
                                                                    telefono,
                                                                    ciudad,
                                                                ) = (
                                                                    tempRut,
                                                                    tempNombre,
                                                                    tempDire,
                                                                    tempEdad,
                                                                    tempEmail,
                                                                    tempFono,
                                                                    tempCiudad,
                                                                )
                                                                print(
                                                                    "\n\033[91m\033[107m>>>\033[0m Usuario {}, rut {} ingresado con exito \u2713.\n".format(
                                                                        nombre, rut
                                                                    )
                                                                )
                                                                time.sleep(1.3)
                                                                print(
                                                                    "\033[91m\033[107m>>>\033[0m Volviendo al Menu Principal..."
                                                                )
                                                                time.sleep(1.3)
                                                                break
                                                        break
                                                break
                                        break
                                except:
                                    print(
                                        "\033[91m\033[107m>>>\033[0m Error Sistema: Edad debe ser un número entero. Vuelva a Intentarlo."
                                    )
                                    time.sleep(1.5)
                                    continue
                            break
                    break
            break


# Modificar Usuario


def modificarUsuario():
    global rut, nombre, dire, edad, email, telefono, ciudad
    while True:
        print(
            "\n----\033[1m\033[44m M O D I F I C A R  U S U A R I O \033[0m\033[0m----\n"
        )

        if rut != "":
            # Obtener la longitud de cada campo en la tabla
            longitud_rut = len(rut)
            longitud_nombre = len(nombre)
            longitud_dire = len(dire)
            longitud_edad = len("Edad")
            longitud_email = len(email)
            longitud_telefono = len(telefono)
            longitud_ciudad = len(ciudad)

            # Imprimir la tabla
            print("Usuarios registrados: ")
            print(
                "+{:-^{}}+{:-^{}}+{:-^{}}+{:-^{}}+{:-^{}}+{:-^{}}+{:-^{}}+".format(
                    "",
                    longitud_rut + 2,
                    "",
                    longitud_nombre + 2,
                    "",
                    longitud_dire + 2,
                    "",
                    longitud_edad + 2,
                    "",
                    longitud_email + 2,
                    "",
                    longitud_telefono + 2,
                    "",
                    longitud_ciudad + 2,
                    "",
                )
            )
            print(
                "| {:{}} | {:{}} | {:{}} | {:{}} | {:{}} | {:{}} | {:{}} |".format(
                    "Rut",
                    longitud_rut,
                    "Nombre",
                    longitud_nombre,
                    "Dirección",
                    longitud_dire,
                    "Edad",
                    longitud_edad,
                    "Email",
                    longitud_email,
                    "Telefono",
                    longitud_telefono,
                    "Ciudad",
                    longitud_ciudad,
                )
            )
            print(
                "+{:-^{}}+{:-^{}}+{:-^{}}+{:-^{}}+{:-^{}}+{:-^{}}+{:-^{}}+".format(
                    "",
                    longitud_rut + 2,
                    "",
                    longitud_nombre + 2,
                    "",
                    longitud_dire + 2,
                    "",
                    longitud_edad + 2,
                    "",
                    longitud_email + 2,
                    "",
                    longitud_telefono + 2,
                    "",
                    longitud_ciudad + 2,
                    "",
                )
            )
            print(
                "| {:{}} | {:{}} | {:{}} | {:{}} | {:{}} | {:{}} | {:{}} |".format(
                    rut,
                    longitud_rut,
                    nombre,
                    longitud_nombre,
                    dire,
                    longitud_dire,
                    edad,
                    longitud_edad,
                    email,
                    longitud_email,
                    telefono,
                    longitud_telefono,
                    ciudad,
                    longitud_ciudad,
                )
            )
            print(
                "+{:-^{}}+{:-^{}}+{:-^{}}+{:-^{}}+{:-^{}}+{:-^{}}+{:-^{}}+".format(
                    "",
                    longitud_rut + 2,
                    "",
                    longitud_nombre + 2,
                    "",
                    longitud_dire + 2,
                    "",
                    longitud_edad + 2,
                    "",
                    longitud_email + 2,
                    "",
                    longitud_telefono + 2,
                    "",
                    longitud_ciudad + 2,
                    "",
                )
            )

            print("\n¿Qué datos desea modificar?")
            print(creamenu_mod())
            try:
                o = n_P2()
                if o == 1:
                    # MODIFICAR NOMBRE
                    while True:
                        tempNombre = input("Ingrese nuevo nombre (c: Cancelar): ")
                        if tempNombre.upper() == "C":
                            print(
                                "\033[91m\033[107m>>>\033[0m Cancelado. Volviendo al menu anterior..."
                            )
                            time.sleep(1.5)
                            break
                        elif tempNombre.isnumeric() == True or tempNombre == "":
                            tempNombre = ""
                            print(
                                "\033[91m\033[107m>>>\033[0m Error Sistema: El nombre no puede ser vacio o un numero. Vuelva a intentarlo."
                            )
                            time.sleep(1.5)
                            # continue
                        else:
                            nombre = tempNombre
                            print("El nombre ha sido modificado con exito \u2713.")
                            time.sleep(1.5)
                            break
                    continue
                elif o == 2:
                    # MODIFICAR DIRECCION
                    while True:
                        tempDire = input("Ingrese nueva dirección (c: Cancelar): ")
                        if tempDire.upper() == "C":
                            print(
                                "\033[91m\033[107m>>>\033[0m Cancelado. Volviendo al menu anterior..."
                            )
                            time.sleep(1.5)
                            break
                        elif tempDire == "":
                            tempDire = ""
                            print(
                                "\033[91m\033[107m>>>\033[0m Error Sistema: La dirección no puede ser vacio. Vuelva a intentarlo."
                            )
                            time.sleep(1.5)
                        else:
                            dire = tempDire
                            print("La dirección ha sido modificada con exito \u2713.")
                            time.sleep(1.5)
                            break
                    continue
                elif o == 3:
                    # MODIFICAR EDAD
                    while True:
                        try:
                            tempEdad = input("Ingrese nueva edad (c: Cancelar): ")
                            if tempEdad.upper() == "C":
                                print(
                                    "\033[91m\033[107m>>>\033[0m Cancelado. Volviendo al menu anterior..."
                                )
                                time.sleep(1.5)
                                break
                            elif int(tempEdad) < 1 or int(tempEdad) > 120:
                                print(
                                    "\033[91m\033[107m>>>\033[0m Error Sistema: Edad debe ser entre 1 y 120. Vuelva a Intentarlo."
                                )
                                time.sleep(1.5)
                            else:
                                edad = tempEdad
                                print("La edad ha sido modificada con exito \u2713.")
                                time.sleep(1.5)
                                break
                        except:
                            print(
                                "\033[91m\033[107m>>>\033[0m Error Sistema: Edad debe ser un número entero. Vuelva a Intentarlo."
                            )
                            time.sleep(1.5)
                            continue
                    continue
                elif o == 4:
                    # MODIFICAR EMAIL
                    while True:
                        tempEmail = input("Ingrese nuevo email (c: Cancelar): ")
                        if tempEmail.upper() == "C":
                            print(
                                "\033[91m\033[107m>>>\033[0m Cancelado. Volviendo al menu anterior..."
                            )
                            time.sleep(1.5)
                            break
                        elif not verificar_correo(tempEmail) or tempEmail == "":
                            print(
                                "El correo ingresado no es valido. Vuelva a intentarlo."
                            )
                        else:
                            email = tempEmail
                            print("El email ha sido modificado con exito \u2713.")
                            time.sleep(1.5)
                            break
                    continue
                elif o == 5:
                    # MODIFICAR TELEFONO
                    while True:
                        tempFono = input("Ingrese nuevo telefono (c: Cancelar): ")
                        if tempFono.upper() == "C":
                            print(
                                "\033[91m\033[107m>>>\033[0m Cancelado. Volviendo al menu anterior..."
                            )
                            time.sleep(1.5)
                            break
                        elif (
                            tempFono.isdigit() == False
                            or len(tempFono) not in [9, 11]
                            or tempFono == ""
                        ):
                            tempFono = ""
                            print(
                                "\033[91m\033[107m>>>\033[0m Error Sistema: El telefono debe ser numerico y tener 9 o 11 digitos. Vuelva a intentarlo."
                            )
                        else:
                            telefono = tempFono
                            print("El telefono ha sido modificado con exito \u2713.")
                            time.sleep(1.5)
                            break
                    continue
                elif o == 6:
                    # MODIFICAR CIUDAD
                    while True:
                        tempCiudad = input("Ingrese nueva ciudad (c: Cancelar): ")
                        if tempCiudad.upper() == "C":
                            print(
                                "\033[91m\033[107m>>>\033[0m Cancelado. Volviendo al menu anterior..."
                            )
                            time.sleep(5)
                            break
                        elif tempCiudad == "":
                            tempCiudad = ""
                            print(
                                "\033[91m\033[107m>>>\033[0m Error Sistema: La ciudad no puede ser vacio. Vuelva a intentarlo."
                            )
                            time.sleep(1.5)
                        elif tempCiudad.isnumeric() == True:
                            tempCiudad = ""
                            print(
                                "\033[91m\033[107m>>>\033[0m Error Sistema: La ciudad no puede ser un numero. Vuelva a intentarlo."
                            )
                        else:
                            ciudad = tempCiudad
                            print("La ciudad ha sido modificada con exito \u2713.")
                            time.sleep(1.5)
                            break
                    continue
                elif o == 7:
                    # MODIFICAR TODOS LOS DATOS
                    while True:
                        tempNombre = input("Ingrese nuevo nombre (c: Cancelar): ")
                        if tempNombre.upper() == "C":
                            (
                                tempNombre,
                                tempDire,
                                tempEdad,
                                tempEmail,
                                tempFono,
                                tempCiudad,
                            ) = ("", "", "", "", "", "")
                            print(
                                "\033[91m\033[107m>>>\033[0m Cancelado. Volviendo al menu anterior..."
                            )
                            time.sleep(1.0)
                            break
                        elif tempNombre.isnumeric() == True or tempNombre == "":
                            tempNombre = ""
                            print(
                                "\033[91m\033[107m>>>\033[0m Error Sistema: El nombre no puede ser vacio o un numero. Vuelva a intentarlo."
                            )
                            time.sleep(1.5)
                        else:
                            tempDire = input("Ingrese nueva dirección (c: Cancelar): ")
                            if tempDire.upper() == "C":
                                (
                                    tempNombre,
                                    tempDire,
                                    tempEdad,
                                    tempEmail,
                                    tempFono,
                                    tempCiudad,
                                ) = ("", "", "", "", "", "")
                                print(
                                    "\033[91m\033[107m>>>\033[0m Cancelado. Volviendo al menu anterior..."
                                )
                                time.sleep(1.0)
                                break
                            elif tempDire == "":
                                tempDire = ""
                                print(
                                    "\033[91m\033[107m>>>\033[0m Error Sistema: La dirección no puede ser vacio. Vuelva a intentarlo."
                                )
                                time.sleep(1.5)
                            else:
                                while True:
                                    try:
                                        tempEdad = input(
                                            "Ingrese nueva edad (c: Cancelar): "
                                        )
                                        if tempEdad.upper() == "C":
                                            (
                                                tempNombre,
                                                tempDire,
                                                tempEdad,
                                                tempEmail,
                                                tempFono,
                                                tempCiudad,
                                            ) = ("", "", "", "", "", "")
                                            print(
                                                "\033[91m\033[107m>>>\033[0m Cancelado. Volviendo al menu anterior..."
                                            )
                                            time.sleep(1.5)
                                            break
                                        elif int(tempEdad) < 1 or int(tempEdad) > 120:
                                            print(
                                                "\033[91m\033[107m>>>\033[0m Error Sistema: Edad debe ser entre 1 y 120. Vuelva a Intentarlo."
                                            )
                                            time.sleep(1.5)
                                        else:
                                            while True:
                                                # EMAIL
                                                tempEmail = input(
                                                    "Ingrese nuevo Email (ej: aaaa@bbb.cc) (c: Cancelar): "
                                                )
                                                if tempEmail.upper() == "C":
                                                    (
                                                        tempNombre,
                                                        tempDire,
                                                        tempEdad,
                                                        tempEmail,
                                                        tempFono,
                                                        tempCiudad,
                                                    ) = ("", "", "", "", "", "")
                                                    print(
                                                        "\033[91m\033[107m>>>\033[0m Cancelado. Volviendo al menu anterior..."
                                                    )
                                                    time.sleep(1.5)
                                                    break
                                                elif (
                                                    not verificar_correo(tempEmail)
                                                    or tempEmail == ""
                                                ):
                                                    print(
                                                        "\033[91m\033[107m>>>\033[0m El correo ingresado no es valido. Vuelva a intentarlo."
                                                    )
                                                else:
                                                    while True:
                                                        # TELEFONO
                                                        tempFono = input(
                                                            "Ingrese nuevo Telefono (ej: 912345678 o 56912345678) (c: Cancelar): "
                                                        )
                                                        if tempFono.upper() == "C":
                                                            (
                                                                tempNombre,
                                                                tempDire,
                                                                tempEdad,
                                                                tempEmail,
                                                                tempFono,
                                                                tempCiudad,
                                                            ) = ("", "", "", "", "", "")
                                                            print(
                                                                "\033[91m\033[107m>>>\033[0m Cancelado. Volviendo al menu anterior..."
                                                            )
                                                            time.sleep(1.5)
                                                            break
                                                        elif (
                                                            tempFono.isdigit() == False
                                                            or len(tempFono)
                                                            not in [9, 11]
                                                            or tempFono == ""
                                                        ):
                                                            tempFono = ""
                                                            print(
                                                                "\033[91m\033[107m>>>\033[0m Error Sistema: El telefono debe ser numerico y tener 9 o 11 digitos. Vuelva a intentarlo."
                                                            )
                                                        else:
                                                            while True:
                                                                # CIUDAD
                                                                tempCiudad = input(
                                                                    "Ingrese nueva Ciudad (c: Cancelar): "
                                                                )
                                                                if (
                                                                    tempCiudad.upper()
                                                                    == "C"
                                                                ):
                                                                    (
                                                                        tempNombre,
                                                                        tempDire,
                                                                        tempEdad,
                                                                        tempEmail,
                                                                        tempFono,
                                                                        tempCiudad,
                                                                    ) = (
                                                                        "",
                                                                        "",
                                                                        "",
                                                                        "",
                                                                        "",
                                                                        "",
                                                                    )
                                                                    print(
                                                                        "\033[91m\033[107m>>>\033[0m Cancelado. Volviendo al menu anterior..."
                                                                    )
                                                                    time.sleep(1.5)
                                                                    break
                                                                elif tempCiudad == "":
                                                                    tempCiudad = ""
                                                                    print(
                                                                        "\033[91m\033[107m>>>\033[0m Error Sistema: La ciudad no puede ser vacio. Vuelva a intentarlo."
                                                                    )
                                                                    time.sleep(1.5)
                                                                elif (
                                                                    tempCiudad.isnumeric()
                                                                    == True
                                                                ):
                                                                    tempCiudad = ""
                                                                    print(
                                                                        "\033[91m\033[107m>>>\033[0m Error Sistema: La ciudad no puede ser un numero. Vuelva a intentarlo."
                                                                    )
                                                                    time.sleep(1.5)
                                                                else:
                                                                    (
                                                                        nombre,
                                                                        dire,
                                                                        edad,
                                                                        email,
                                                                        telefono,
                                                                        ciudad,
                                                                    ) = (
                                                                        tempNombre,
                                                                        tempDire,
                                                                        tempEdad,
                                                                        tempEmail,
                                                                        tempFono,
                                                                        tempCiudad,
                                                                    )
                                                                    print(
                                                                        "\n\033[91m\033[107m>>>\033[0m Usuario rut {} modificado con exito \u2713.\n".format(
                                                                            rut
                                                                        )
                                                                    )
                                                                    time.sleep(1.3)
                                                                    break
                                                            break
                                                    break
                                            break
                                    except:
                                        print(
                                            "\033[91m\033[107m>>>\033[0m Error Sistema: Edad debe ser un número entero. Vuelva a Intentarlo."
                                        )
                                        time.sleep(1.5)
                                        continue
                                break
                    continue
                else:
                    print("\033[91m\033[107m>>>\033[0m Regresando...")
                    time.sleep(1.5)
                    break
            except:
                print(
                    "\033[91m\033[107m>>>\033[0m Error, el valor ingreado debe ser un numero entre 1 y 7"
                )
                time.sleep(1.5)
                continue
        else:
            print("\033[91m\033[107m>>>\033[0m No hay usuarios registrados.")
            time.sleep(1.5)
            break


# Eliminar Usuario


def eliminarUsuario():
    global rut, nombre, dire, edad, email, telefono, ciudad
    while True:
        print(
            "\n----\033[1m\033[44m E L I M I N A R  U S U A R I O \033[0m\033[0m----\n"
        )
        # sapo
        # print(nombre, rut, dire, edad)
        if rut != "":
            print("Realmene desea eliminar el usuario {}?\n".format(nombre))
            res = input("Ingrese opción (s/n): ")
            if res.upper() == "S":
                rut, nombre, dire, edad, email, telefono, ciudad = (
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                )
                print("\033[91m\033[107m>>>\033[0m Usuario eliminado con exito \u2713.")
                time.sleep(1.5)
                break
            elif res.upper() == "N":
                print("\033[91m\033[107m>>>\033[0m Regresando...")
                time.sleep(1.5)
                break
            else:
                print(
                    "\033[91m\033[107m>>>\033[0m Opción no valida. Vuelva a intentarlo."
                )
                time.sleep(1.5)
                continue
        else:
            print("\033[91m\033[107m>>>\033[0m No hay usuarios registrados.")
            time.sleep(1.5)
            break


# Consultar Usuario
def consultarUsuario():
    global rut, nombre, dire, edad, email, telefono, ciudad
    while True:
        print(
            "\n----\033[1m\033[44m C O N S U L T A R  U S U A R I O \033[0m\033[0m----\n"
        )
        # MOSTRAR LOS DATOS DEL USUARIO
        if rut != "":
            print("\nRut: ".ljust(13), "\033[33m", rut, "\033[0m")
            time.sleep(0.3)
            print("Nombre: ".ljust(12), "\033[33m", nombre, "\033[0m")
            time.sleep(0.3)
            print("Dirección: ".ljust(12), "\033[33m", dire, "\033[0m")
            time.sleep(0.3)
            print("Edad: ".ljust(12), "\033[33m", edad, "\033[0m")
            time.sleep(0.3)
            print("Email: ".ljust(12), "\033[33m", email, "\033[0m")
            time.sleep(0.3)
            print("Telefono: ".ljust(12), "\033[33m", telefono, "\033[0m")
            time.sleep(0.3)
            print("Ciudad: ".ljust(12), "\033[33m", ciudad, "\033[0m")
            time.sleep(0.3)
            a = input(
                "\n\033[91m\033[107m>>>\033[0m Ingresa cualquier tecla para volver al Menu Principal..."
            )
            break
        else:
            print("\033[91m\033[107m>>>\033[0m No hay usuarios registrados.")
            time.sleep(1.5)
            break


"""""
- Agregar Email con validador
- Agregar Telefono con validador
- Agregar Ciudad con validador
"""

# Validador de Correo


def verificar_correo(correo):
    """Verifica si un correo electrónico es válido"""
    patron = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.match(patron, correo)
