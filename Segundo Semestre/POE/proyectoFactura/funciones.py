import re
import time
import datetime
import os
import traceback

path = "c:\\bdd\\"
clienteTxt = "usuarios.txt"
productoTxt = "articulos.txt"
facturaTxt = "facturas.txt"
articulos = [
    [1, 'Tijera', 30, 750],
    [2, 'Cuaderno College', 200, 660],
    [3, 'Lapiz Pasta', 500, 1100],
    [4, 'Plasticina', 35, 1500],
    [5, 'Tempera', 10, 1350],
    [6, 'Block de Dibujo', 6, 990],
    [7, 'Cuaderno Universitario', 70, 1250],
    [8, 'Destacador', 10, 800],
    [9, 'Goma', 30, 450],
    [10, 'Estuche', 2, 5000],
]

def definirVariables(): # Define variables globales
    global rut, nombre, ap, am, email, telefono
    rut, nombre, ap, am, email, telefono = (
        "",
        "",
        "",
        "",
        "",
        ""
    )
def hora(): # Retorna hora actual
    tt = time.strftime("%H:%M:%S", time.localtime())
    return tt
def lee_rut(resp): # Valida que rut contenga 0123456789.,-K
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
def vrut(rut): # Valida rut
    r = rut
    if len(r) >= 9 and len(r) <= 11:
        r = r.replace(".", "")  # remplaza . por vacio ""
        r = r.replace("-", "")
        r = r.replace(",", "")
        dv = r[-1]  # saca el ultimo número de r
        # print("ultimo número", dv)  # sapo
        r = r[0 : len(r) - 1]  # en r voy a dejar desde 0 hasta el largo de rut - 1
        r = list(r)  # list() crea un vector ['1', '2', '3'...]
        # print("Lista ['','',] + dv: ", r, dv)  # sapo
        s = 0  # suma de los valores
        c = 2
        # para x en {da vuelta la lista r}  (x=al primer número del rut)
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
def credito(): # Imprime mensaje de bienvenida
    obten_fecha = datetime.datetime.now()
    date = obten_fecha.date()
    year = date.strftime("%Y")
    # print(f"Current Year -> {year}")

    return """\n====================================
    {} created by EXPLODING TEAM             
====================================
        """.format(
        "__NOMBRE APP__"
    )
def creamenu(): # Imprime menu principal (1-4)
    return """\n----\033[1m\033[42m\033[37m M E N U  P R I N C I P A L \033[0m\033[0m\033[0m----\n
    1 ---- Clientes
    2 ---- Facturación
    3 ---- Reportes
    4 ---- Salir Sistema\n"""
def creaMenu_cliente(): # Imprime menu cliente (1-4)
    return """\n----\033[1m\033[42m\033[37m M E N U  C L I E N T E \033[0m\033[0m\033[0m----\n
    1 ---- Ingreso de Cliente
    2 ---- Modifica Cliente
    3 ---- Elimina Cliente
    4 ---- Volver a Menu Principal\n"""
def creaMenu_facturacion(): # Imprime menu facturacion (1-5)
    return """\n----\033[1m\033[42m\033[37m M E N U  F A C T U R A C I O N \033[0m\033[0m\033[0m----\n
    1 ---- Ingreso de Factura
    2 ---- Modifica Factura
    3 ---- Anula Factura
    4 ---- Elimina Factura
    5 ---- Volver a Menu Principal\n"""
def menu_cliente(): #  Muesta menu cliente y valida opcion (1-4)
    while True:
        print(creaMenu_cliente())
        try:
            op2 = n_P(4)
            if op2 == 1:
                ingresoCliente()
            elif op2 == 2:
                modificarCliente()
            elif op2 == 3:
                eliminarCliente()
            else:
                print("\033[91m\033[107m>>>\033[0m Regresando...")
                time.sleep(1)
                break
        except:
            print(
                "\033[91m\033[107m>>>\033[0m Error, el valor ingreado debe ser un numero entre 1 y 4"
            )
            time.sleep(1)
            continue
def ingresoCliente(): #  I N G R E S O  D E  C L I E N T E
    global rut, nombre, ap, am, email, telefono, clienteTxt, productoTxt, facturaTxt
    while True:
        print(
            "\n----\033[1m \033[44m I N G R E S O  D E  C L I E N T E \033[0m\033[0m----"
        )
        print("\033[91m\033[107m>>>\033[0m c: Cancelar y volver al Menu Cliente\n")
        respuesta = input("Rut de Cliente: ")
        try:
            if respuesta.upper() == "C":
                (tempRut, tempNombre, tempAP, tempAM, tempEmail, tempFono) = (
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                )
                print(
                    "\033[91m\033[107m>>>\033[0m Cancelado. Volviendo al Menu Cliente..."
                )
                # gracias al import time, agrega una pausa al programa (s)
                time.sleep(1)
                break
            else:
                # RUT
                if lee_rut(respuesta) == 0:
                    print(
                        "\033[91m\033[107m>>>\033[0m Solo puede ingresar 0-9 y K. Vuelva a intentarlo. "
                    )
                    time.sleep(1)
                    respuesta = ""
                    continue
                else:
                    tempRut = respuesta.upper()
                # rut = respuesta

                if buscar(clienteTxt, tempRut) == 1:
                    print(
                        "\033[91m\033[107m>>>\033[0m El rut ingresado ya existe. Vuelva a intentarlo."
                    )
                    time.sleep(1)
                    tempRut = ""
                    continue
                else:
                    if vrut(tempRut) == 1:
                        # sapo + \u2713= caracter unicode check
                        print("{:>20}".format("Rut valido " + "\u2713"))
                    else:
                        print(
                            "\033[91m\033[107m>>>\033[0m El rut ingresado no es valido. Vuelva a intentarlo."
                        )
                        time.sleep(1)
                        tempRut = ""
                        continue
        except:
            print(
                "\033[91m\033[107m>>>\033[0m Error Sistema: El rut debe ser formato 11111111-K. Vuelva a intentarlo."
            )
            time.sleep(1)
            continue
        # NOMBRE
        while True:
            tempNombre = input("Nombre de Cliente: ")
            if tempNombre.upper() == "C":
                (tempRut, tempNombre, tempAP, tempAM, tempEmail, tempFono) = (
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                )
                print(
                    "\033[91m\033[107m>>>\033[0m Cancelado. Volviendo al Menu Cliente..."
                )
                time.sleep(1)
                break
            # strip() elimina espacios en blanco al inicio y al final
            elif tempNombre.strip().isnumeric() == True or tempNombre.strip() == "":
                tempNombre = ""
                print(
                    "\033[91m\033[107m>>>\033[0m Error Sistema: El nombre no puede ser vacio o un número. Vuelva a intentarlo."
                )
                time.sleep(1)
                # continue
            else:
                while True:
                    # APELLIDO PATERNO
                    tempAP = input("Apellido Paterno: ")
                    if tempAP.upper() == "C":
                        (
                            tempRut,
                            tempNombre,
                            tempAP,
                            tempAM,
                            tempEmail,
                            tempFono,
                        ) = ("", "", "", "", "", "")
                        print(
                            "\033[91m\033[107m>>>\033[0m> Cancelado. Volviendo al Menu Cliente..."
                        )
                        time.sleep(1)
                        break
                    elif tempAP.strip().isnumeric() == True or tempAP.strip() == "":
                        tempAP = ""
                        print(
                            "\033[91m\033[107m>>>\033[0m Error Sistema: El apellido no puede ser vacio o un número. Vuelva a intentarlo."
                        )
                        time.sleep(1)
                    else:
                        while True:
                            # APELLIDO MATERNO
                            tempAM = input("Apellido Materno: ")
                            if tempAM.upper() == "C":
                                (
                                    tempRut,
                                    tempNombre,
                                    tempAP,
                                    tempAM,
                                    tempEmail,
                                    tempFono,
                                ) = ("", "", "", "", "", "")
                                print(
                                    "\033[91m\033[107m>>>\033[0m Cancelado. Volviendo al Menu Cliente..."
                                )
                                time.sleep(1)
                                break
                            elif tempAM.strip().isnumeric() == True or tempAM.strip() == "":
                                print(
                                    "\033[91m\033[107m>>>\033[0m Error Sistema:El apellido no puede ser vacio o un número. Vuelva a intentarlo."
                                )
                                time.sleep(1)
                            else:
                                while True:
                                    # EMAIL
                                    tempEmail = input("Email (ej: aaaa@bbb.cc): ")
                                    if tempEmail.upper() == "C":
                                        (
                                            tempRut,
                                            tempNombre,
                                            tempAP,
                                            tempAM,
                                            tempEmail,
                                            tempFono,
                                        ) = ("", "", "", "", "", "")
                                        print(
                                            "\033[91m\033[107m>>>\033[0m Cancelado. Volviendo al Menu Cliente..."
                                        )
                                        time.sleep(1)
                                        break
                                    elif (
                                        not verificar_correo(tempEmail)
                                        or tempEmail.strip() == ""
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
                                                    tempAP,
                                                    tempAM,
                                                    tempEmail,
                                                    tempFono,
                                                ) = ("", "", "", "", "", "")
                                                print(
                                                    "\033[91m\033[107m>>>\033[0m Cancelado. Volviendo al Menu Cliente..."
                                                )
                                                time.sleep(1)
                                                break
                                            elif (
                                                tempFono.strip().isdigit() == False
                                                or len(tempFono) not in [9, 11]
                                                or tempFono.strip() == ""
                                            ):
                                                tempFono = ""
                                                print(
                                                    "\033[91m\033[107m>>>\033[0m> Error Sistema: El telefono debe ser numerico y tener 9 o 11 digitos. Vuelva a intentarlo."
                                                )
                                            else:
                                                try:
                                                    idx = obtener_siguiente_indice(clienteTxt)
                                                   
                                                    reg = (
                                                        str(idx),
                                                        tempRut.lower(),
                                                        tempNombre.lower(),
                                                        tempAP.lower(),
                                                        tempAM.lower(),
                                                        tempEmail.lower(),
                                                        tempFono.lower(),
                                                    )
                                                    guardarCliente(reg)
                                                    print(
                                                        "\n\033[91m\033[107m>>>\033[0m Cliente {}, rut {} ingresado con exito \u2713.\n".format(
                                                            tempNombre.capitalize(), tempRut.upper()
                                                        )
                                                    )
                                                    time.sleep(1)
                                                    otroCliente = input("¿Desea ingresar otro Cliente? (S/N): ")
                                                    if otroCliente.upper() == "S":
                                                        (
                                                            tempRut,
                                                            tempNombre,
                                                            tempAP,
                                                            tempAM,
                                                            tempEmail,
                                                            tempFono,
                                                        ) = (
                                                            "",
                                                            "",
                                                            "",
                                                            "",
                                                            "",
                                                            "",
                                                        )
                                                        ingresoCliente()
                                                    else:
                                                        (
                                                            tempRut,
                                                            tempNombre,
                                                            tempAP,
                                                            tempAM,
                                                            tempEmail,
                                                            tempFono,
                                                        ) = (
                                                            "",
                                                            "",
                                                            "",
                                                            "",
                                                            "",
                                                            "",
                                                        )
                                                        print(
                                                            "\033[91m\033[107m>>>\033[0m Cancelado. Volviendo al Menu Cliente..."
                                                        )
                                                        time.sleep(1)
                                                        break
                                                except Exception as e:
                                                    print(
                                                        "\033[91m\033[107m>>>\033[0m Error Sistema: No se pudo guardar el Cliente. Vuelva a intentarlo."
                                                    )
                                                    print(e)
                                                    time.sleep(1)
                                                break
                                        break
                                break

                        break
                break
        break
def modificarCliente(): # M O D I F I C A R  C L I E N T E
    global rut, nombre, ap, am, email, telefono, clienteTxt
    while True:
        resp = ""
        print(
            "\n----\033[1m\033[44m M O D I F I C A R  C L I E N T E \033[0m\033[0m----\n"
        )
        # Mostrar Clientes
        verClientes()

        resp = input("\nIngrese el numero de indice del cliente a modificar(c: Cancelar): ")
        if resp.upper() == "C":
            print("\033[91m\033[107m>>>\033[0m Cancelado. Volviendo al Menu Cliente...")
            time.sleep(1)
            break
        elif resp.isdigit() == False:
            print("\033[91m\033[107m>>>\033[0m Error Sistema: El indice debe ser numerico. Vuelva a intentarlo.")
            time.sleep(1)
        else:
            # Menu Modificar Cliente
            menuModCliente(resp)  
def menuModCliente(indice): # indice = indice del cliente a modificar, muestra el menu de modificacion de cliente
    while True:
        try:
            # Mostrar Cliente a Modificar
            if verDato(indice, clienteTxt) == False:
                print("\033[91m\033[107m>>>\033[0m Error Sistema: El cliente no existe. Vuelva a intentarlo.")
                time.sleep(1)
                break
            # Menu Modificar Cliente
            print("\n¿Que desea modificar?")
            time.sleep(0.5)
            print(creamenu_mod())
            resp = n_P(6)

            if resp == 1:
                while True:
                    # Mofificar Nombre
                    nuevoNombre = input("Ingrese el nuevo Nombre (c: Cancelar): ")
                    if nuevoNombre.upper() == "C":
                        print("\033[91m\033[107m>>>\033[0m Cancelado. Volviendo al Menu Anterior...")
                        time.sleep(1)
                        break
                    elif nuevoNombre.strip() != "" and nuevoNombre.strip().isnumeric() == False:
                        modificarDatos(indice, nuevoNombre, 2, clienteTxt)
                        print("\033[91m\033[107m>>>\033[0m Nombre modificado con exito \u2713.")
                        time.sleep(1)
                        break
                    else:
                        print("\033[91m\033[107m>>>\033[0m Error Sistema: El campo no puede ser vacio o numerico. Vuelva a intentarlo.")
                        time.sleep(1)
                        continue
                break
            elif resp == 2:
                while True:
                    # Mofificar Apellido Paterno
                    nuevoAP = input("Ingrese el nuevo Apellido Paterno (c: Cancelar): ")
                    if nuevoAP.upper() == "C":
                        print("\033[91m\033[107m>>>\033[0m Cancelado. Volviendo al Menu Anterior...")
                        time.sleep(1)
                        break
                    elif nuevoAP.strip() != "" and nuevoAP.strip().isnumeric() == False:
                        modificarDatos(indice, nuevoAP, 3, clienteTxt)
                        print("\033[91m\033[107m>>>\033[0m Apellido Paterno modificado con exito \u2713.")
                        time.sleep(1)
                        break
                    else:
                        print("\033[91m\033[107m>>>\033[0m Error Sistema: El campo no puede ser vacio o numerico. Vuelva a intentarlo.")
                        time.sleep(1)
                        continue
                break
            elif resp == 3:
                while True:
                    # Mofificar Apellido Materno
                    nuevoAM = input("Ingrese el nuevo Apellido Materno (c: Cancelar): ")
                    if nuevoAM.upper() == "C":
                        print("\033[91m\033[107m>>>\033[0m Cancelado. Volviendo al Menu Anterior...")
                        time.sleep(1)
                        break
                    elif nuevoAM.strip() != "" and nuevoAM.strip().isnumeric() == False:
                        modificarDatos(indice, nuevoAM, 4, clienteTxt)
                        print("\033[91m\033[107m>>>\033[0m Apellido Materno modificado con exito \u2713.")
                        time.sleep(1)
                        break
                    else:
                        print("\033[91m\033[107m>>>\033[0m Error Sistema: El campo no puede ser vacio o numerico. Vuelva a intentarlo.")
                        time.sleep(1)
                        continue
                break
            elif resp == 4:
                while True:
                    # Mofificar Email
                    nuevoEmail = input("Ingrese el nuevo Email (ej: aaaa@bbb.cc) (c: Cancelar): ")
                    if nuevoEmail.upper() == "C":
                        print("\033[91m\033[107m>>>\033[0m Cancelado. Volviendo al Menu Anterior...")
                        time.sleep(1)
                        break
                    elif (not verificar_correo(nuevoEmail.strip()) or nuevoEmail.strip() == ""):
                        print("El correo ingresado no es valido. Vuelva a intentarlo.")
                        time.sleep(1)
                        continue
                    else:
                        modificarDatos(indice, nuevoEmail, 5, clienteTxt)
                        print("\033[91m\033[107m>>>\033[0m Email modificado con exito \u2713.")
                        time.sleep(1)
                        break
                break
            elif resp == 5:
                while True:
                    # Mofificar Telefono
                    nuevoTelefono = input("Ingrese el nuevo Telefono (ej: 912345678 o 56912345678) (c: Cancelar): ")
                    if nuevoTelefono.upper() == "C":
                        print("\033[91m\033[107m>>>\033[0m Cancelado. Volviendo al Menu Anterior...")
                        time.sleep(1)
                        break
                    elif (nuevoTelefono.strip().isdigit() == False or len(nuevoTelefono.strip()) not in [9, 11] or nuevoTelefono.strip() == ""):
                        print("El telefono ingresado no es valido. Vuelva a intentarlo.")
                        time.sleep(1)
                        continue
                    else:
                        modificarDatos(indice, nuevoTelefono, 6, clienteTxt)
                        print("\033[91m\033[107m>>>\033[0m Telefono modificado con exito \u2713.")
                        time.sleep(1)
                        break
                break
            elif resp == 6:
                print("\033[91m\033[107m>>>\033[0m Volviendo al menu anteior...")
                time.sleep(1)
               
                break
            else:
                print("\033[91m\033[107m>>>\033[0m Error Sistema: Opcion no valida. Vuelva a intentarlo.")
                time.sleep(1)
                continue
        except Exception as e:
            print("\033[91m\033[107m>>>\033[0m Error Sistema: No se pudo modificar Cliente. Vuelva a intentarlo.")
            print(f"Se produjo una excepción: {e}")
            traceback.print_exc()
            time.sleep(1)
def modificarDatos(indice, nuevoDato, columna, n_a):  # Funcion para modificar datos de un txt (indice, nuevoDato, columna, n_a)
    datos = []
    
    lineas = leer(n_a)

    # Recorrer las líneas
    for l in lineas:
        data = l.strip().split(',')

        # Si el índice coincide con el que se busca, cambiar el dato
        if int(data[0]) == int(indice):
            data[columna] = nuevoDato

        datos.append(','.join(data))  # Recompone la línea y la añade a la lista

    # Escribe todas las líneas de nuevo al archivo
    with open(path + n_a, 'w') as f:
        for l in datos:
            f.write(l + '\n')
def verClientes(): # Funcion para ver los clientes registrados
    global clienteTxt
    try:
        if contar(clienteTxt) != 0:
            longitudes = [7, 12, 25, 25, 25, 30, 15]  # Ajusta estas longitudes según tus necesidades
            linea = "=" * 148
            formato = "{:<{}}"  # < alineado a la izquierda

            msg = "C L I E N T E S  R E G I S T R A D O S"
            msg_centered = msg.center(148, " ")
            msg_final = "\033[1m\033[44m" + msg_centered + "\033[0m\033[0m"

            # Imprimir el mensaje
            print(msg_centered)

            columnas = [
                "Indice",
                "Rut",
                "Nombre",
                "Apellido Paterno",
                "Apellido Materno",
                "Email",
                "Telefono",
            ]
            datos = leer(clienteTxt)

            for i, col in enumerate(columnas):
                print(formato.format(col, longitudes[i]), end="  ")
            print()  # nueva línea
            print(linea)

            # Imprimir los datos
            for x in datos:
                data = x.strip().split(",")
                for i, dat in enumerate(data):
                    print(formato.format(dat.upper(), longitudes[i]), end="  ")
                    time.sleep(0.01)
                print()  # nueva línea
            print(linea)

        else:
            print("\033[91m\033[107m>>>\033[0m No hay clientes registrados.")
            time.sleep(1)
    except Exception as e:
        print("\033[91m\033[107m>>>\033[0m Error al mostrar clientes registrados.")
        print(f"Se produjo una excepción: {e}")
        time.sleep(1)
def verProductos(stock_temp): # Funcion para ver los productos registrados
    global productoTxt
    try:
        if len(stock_temp) != 0:
            longitudes = [7, 30, 15, 15]  # Ajusta longitudes
            linea = "=" * 68
            formato = "{:<{}}"  # < alineado a la izquierda

            msg = "P R O D U C T O S  R E G I S T R A D O S"
            msg_centered = msg.center(68, " ")
            msg_final = "\033[1m\033[44m" + msg_centered + "\033[0m\033[0m"

            # Imprimir el mensaje
            print(msg_centered)

            columnas = [
                "ID",
                "Articulo",
                "Saldo",
                "Precio"
            ]
            datos = stock_temp

            for i, col in enumerate(columnas):
                print(formato.format(col, longitudes[i]), end="  ")
            print()  # nueva línea
            print(linea)

            # Imprimir los datos
            for x in datos:
                data = x.strip().split(",")
                for i, dat in enumerate(data):
                    print(formato.format(dat.upper(), longitudes[i]), end="  ")
                    time.sleep(0.01)
                print()  # nueva línea
            print(linea)

        else:
            print("\033[91m\033[107m>>>\033[0m No hay productos registrados.")
            time.sleep(1)
    except Exception as e:
        print("\033[91m\033[107m>>>\033[0m Error al mostrar productos registrados.")
        print(f"Se produjo una excepción: {e}")
        time.sleep(1)
def verDato(indice, n_a): # Ver dato(linea) de un txt, C L I E N T E  A  M O D I F I C A R
    longitudes = [7, 12, 25, 25, 25, 30, 15]  # Longitudes de cada columna
    linea = "=" * 148
    formato = "{:<{}}"  # < alineado a la izquierda
    columnas = [
        "Indice",
        "Rut",
        "Nombre",
        "Apellido Paterno",
        "Apellido Materno",
        "Email",
        "Telefono",
    ]
    try:
        datos = leer(n_a)
        for x in datos:
            data = x.strip().split(",")
            if int(data[0]) == int(indice):
                data2 = data

                print()
                msg = "C L I E N T E  A  M O D I F I C A R"
                msg_centered = msg.center(148, " ")
                msg_final = "\033[1m\033[44m" + msg_centered + "\033[0m\033[0m"

                # Imprimir el mensaje
                print(msg_centered)

                for i, col in enumerate(columnas):
                    print(formato.format(col, longitudes[i]), end="  ")
                print()  # nueva línea
                print(linea)

                # Imprimir los datos
                for i, x in enumerate(data2):
                    print(formato.format(x.upper(), longitudes[i]), end="  ")
                print()  # nueva línea
                
                return True
        return False
    except Exception as e:
        print("\033[91m\033[107m>>>\033[0m Error al mostrar dato.")
        print(f"Se produjo una excepción: {e}")
        time.sleep(1)
def eliminarCliente(): # Menu E L I M I N A R  C L I E N T E
    global rut, nombre, ap, am, email, telefono
    while True:
        print(
            "\n----\033[1m\033[44m E L I M I N A R  C L I E N T E \033[0m\033[0m----\n"
        )
        verClientes()
        print()
        indice = input("Ingrese el indice del cliente a eliminar (c: Cancelar): ")
        if indice.upper() == "C":
            print("\033[91m\033[107m>>>\033[0m Cancelado. Volviendo al Menu Cliente...")
            time.sleep(1)
            break
        elif indice.isdigit() == False or int(indice) > contar(clienteTxt):
            print("\033[91m\033[107m>>>\033[0m Error Sistema: Ingrese un indice valido. Vuelva a intentarlo.")
            time.sleep(1)
        else:
            eliminarDato(indice, clienteTxt)
            print("\033[92m\033[107m>>>\033[0m Cliente eliminado con exito \u2713.")
            time.sleep(1)
            resp = input("\033[92m\033[107m>>>\033[0m ¿Desea Eliminar otro cliente? S/N .")
            if resp.upper() == "S":
                continue
            else:
                print("\033[92m\033[107m>>>\033[0m Volviendo al Menu Cliente...")
                break
def eliminarDato(indice, n_a): # Elimina una línea de un archivo txt
    datos = []
    lineas = leer(n_a)

    # Recorrer las líneas
    for l in lineas:
        data = l.strip().split(',')

        # Si el índice coincide con el que se busca, cambiar el dato
        if int(data[0]) != int(indice):
            datos.append(','.join(data))  # Recompone la línea y la añade a la lista

    # Escribe todas las líneas de nuevo al archivo
    with open(path + n_a, 'w') as f:
        for l in datos:
            f.write(l + '\n')
def creamenu_mod(): # Imprime menu modificar cliente (1-6)
    return """
    1 ---- Modificar Nombre                        4 ---- Modificar Email         
    2 ---- Modificar Apellido Paterno              5 ---- Modificar Telefono
    3 ---- Modificar Apellido Materno              6 ---- Regresar\n"""    
def n_P(max_option): # max_option = maxima opcion, Ingrese opcion
    while True:
        try:
            o = int(input(f"Ingrese opción (1-{max_option}): "))
            if o < 1 or o > max_option:
                print(f"\033[91m\033[107m>>>\033[0m Error, solo se permite 1 a {max_option}")
                time.sleep(1)
            else:
                break
        except:
            print(
                f"\033[91m\033[107m>>>\033[0m Error, el valor ingresado debe ser un número entre 1 y {max_option}"
            )
            time.sleep(1)
    return o
def verificar_correo(correo): # Verifica si un correo es válido
    """Verifica si un correo electrónico es válido"""
    patron = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.match(patron, correo)
def crearArchivo(n_a): # Verifica y Crea los archivos txt
    if os.path.exists(path + n_a):
        print("\033[91m\033[107m>>>\033[0m El archivo {} ya existe.".format(n_a))
        time.sleep(0.3)
    else:
        file = open(path + n_a, "w")
        file.write("")
        file.close()
        print( 
            "\033[91m\033[107m>>>\033[0m Archivo {} creado con exito en \u2713.".format(
                n_a
            )
        )
        time.sleep(0.3)
def usarCrearArchivo(): # Usa la funcion crearArchivo para crear los archivos txt
    print("Buscando archivos en {}...".format(path))
    archivos = "usuarios.txt,articulos.txt,facturas.txt"
    archivos = archivos.split(",")
    for i in archivos:
        crearArchivo(i)
    print("\nIniciando programa...")
    time.sleep(0.5)
def guardarCliente(a): # a = lista con datos del cliente, guarda los datos en el clienteTxt
    file = open(path + clienteTxt, "a")
    file.write(",".join(a) + "\n")
    file.close()
def contar(n_a): # n_a = nombre archivo, devuelve la cantidad de lineas
    file = open(path + n_a, "r")
    return len(file.readlines())
def buscar(n_a, x): # n_a = nombre archivo, x = dato a buscar, si encuentra devuelve 1, sino 0
    file = open(path + n_a, "r")
    for i in file.readlines():
        if x.upper() in i.upper():
            return 1
    return 0
def buscar_en_columna(n_a, x, columna): # n_a = nombre archivo, x = dato a buscar, columna = columna a buscar, si encuentra devuelve 1, sino 0
    file = open(path + n_a, "r")
    for i in file.readlines():
        elemento = i.strip().split(",")
        if x.upper() == elemento[columna].upper():
            return 1
    return 0
def leer(n_a): # n_a = nombre archivo, devuelve una lista con las lineas del archivo
    file = open(path + n_a, "r")
    return file.readlines()
def obtener_siguiente_indice(n_a): # n_a = nombre archivo, devuelve el siguiente indice correlativo
    datos = leer(n_a)
    indices = [int(x.strip().split(",")[0]) for x in datos]  # Extraer los índices
    max_index = max(indices)  # Obtener el máximo índice
    return max_index + 1  # Devolver el próximo índice correlativo
def rellenar_articulos(): # Rellena el archivo articulos.txt
    with open(path + productoTxt, 'w') as file:
        #file.write("id,nombre_articulo,saldo,precio\n")
        for articulo in articulos:
            # Escribe cada artículo en una nueva línea
            file.write("{},{},{},{}\n".format(*articulo))
def menu_facturacion(): 
    while True:
        print(creaMenu_facturacion())
        try:
            op3 = n_P(5)
            if op3 == 1:
                ingreso_factura()
            elif op3 == 2:
                modificar_factura()
            elif op3 == 3:
                anula_factura()
            elif op3 == 4:
                elimina_factura()
            elif op3 == 5:
                print("\033[91m\033[107m>>>\033[0m Regresando...")
                time.sleep(1)
                break
        except Exception as e:
            print("\033[91m\033[107m>>>\033[0m Error inesperado Menu Facturacion: {}".format(e))
            time.sleep(1)

def ingreso_factura():
    while True:
        print(
            "\n----\033[1m\033[44m I N G R E S O  D E  F A C T U R A \033[0m\033[0m----"
        )
        try:
            if contar(productoTxt) == 0:
                print("\033[91m\033[107m>>>\033[0m No hay productos registrados")
                time.sleep(1)
                break
            elif contar(clienteTxt) == 0:
                print("\033[91m\033[107m>>>\033[0m No hay clientes registrados")
                time.sleep(1)
                break
            else:
                print("\nIngrese los siguientes datos:\n")
                if contar(facturaTxt) == 0:
                    id_factura = 1
                else:
                    id_factura = obtener_siguiente_indice(facturaTxt)
                while True:
                    rut = input("Rut cliente (c: Cancelar): ")
                    if rut.upper() == "C":
                        print("\033[91m\033[107m>>>\033[0m Cancelando...")
                        time.sleep(1)
                        break
                    elif rut.strip() == "":
                        print("\033[91m\033[107m>>>\033[0m Rut no puede estar vacio. Vuelva a intentarlo")
                        time.sleep(1)
                        continue
                    elif buscar_en_columna(clienteTxt, rut, 1) == 0:
                        print("\033[91m\033[107m>>>\033[0m Cliente no registrado. Vuelva a intentarlo")
                        time.sleep(1)
                        continue
                    else:
                        print("Cliente encontrado \u2713")
                        # MOSTRAR LOS DATOS DEL CLIENTE ENCONTRADO
                        datos_cliente = leer(clienteTxt)
                        for i in datos_cliente:
                            if rut.upper() in i.upper():
                                datos_cliente = i.strip().split(",")
                                print("Rut: {},  Nombre: {} {} {},  Correo: {}, Telefono: {}".format(datos_cliente[1], datos_cliente[2], datos_cliente[3], datos_cliente[4], datos_cliente[5], datos_cliente[6])) 
                                time.sleep(1)
                                break
                        # SOLICITAR INGRESO DE FECHA DE FACTURA
                        while True:
                            fecha = input("Fecha (dd/mm/aaaa) (c: Cancelar): ")
                            if fecha.upper() == "C":
                                print("\033[91m\033[107m>>>\033[0m Cancelando...")
                                time.sleep(1)
                                break
                            elif fecha.strip() == "":
                                print("\033[91m\033[107m>>>\033[0m Fecha no puede estar vacia. Vuelva a intentarlo")
                                time.sleep(1)
                                continue
                            elif not validar_fecha(fecha):
                                print("\033[91m\033[107m>>>\033[0m Fecha no valida. Vuelva a intentarlo")
                                time.sleep(1)
                                continue
                            else:
                                fecha = fecha.split("/")
                                dia = fecha[0]
                                mes = fecha[1]
                                año = fecha[2]
                                print("Ingrese los productos:")
                                # lista temporal
                                productos_aFacturar = []
                               
                                while True:
                                    
                                    # lista temporal
                                    stock_temp = []
                                    stock_temp = leer(productoTxt)
                                    verProductos(stock_temp)
                                    id_producto = input("ID producto (c: Cancelar): ")
                                    if id_producto.upper() == "C":
                                        print("\033[91m\033[107m>>>\033[0m Cancelando...")
                                        time.sleep(1)
                                        break
                                    elif id_producto.strip() == "":
                                        print("\033[91m\033[107m>>>\033[0m ID producto no puede estar vacio")
                                        time.sleep(1)
                                        break
                             
                                    else:
                                        cantidad = int(input("Cantidad (0: Cancelar):"))
                                        # Obtener Saldo Producto
                                        saldo_producto = int(obtener_dato_producto(productoTxt, id_producto, 2))
                                        if cantidad < 0:
                                            print("\033[91m\033[107m>>>\033[0m Cantidad no puede ser menor a 0. Vuena a intentarlo")
                                            time.sleep(1)
                                            continue
                                        elif cantidad == 0:
                                            print("\033[91m\033[107m>>>\033[0m Cancelando...")
                                            time.sleep(1)
                                            break
                                        elif cantidad > saldo_producto:
                                            print("\033[91m\033[107m>>>\033[0m Cantidad no puede ser mayor al saldo del producto. Vuelva a intentarlo")
                                            time.sleep(1)
                                            continue
                                        else:
                                            precio  = int(obtener_dato_producto(productoTxt, id_producto, 3))
                                            nombre_producto = obtener_dato_producto(productoTxt, id_producto, 1)
                                            total_producto = precio * cantidad
                                            productos_aFacturar.append([nombre_producto, cantidad, precio, total_producto])
                                            otroProducto = input("¿Desea agregar otro producto?(s/n): ")
                                            if otroProducto.upper() != "S":
                                                break
                                if len(productos_aFacturar) == 0:
                                    print("\033[91m\033[107m>>>\033[0m Cancelando...")
                                    time.sleep(1)
                                    break
                                else:
                                    total_factura = 0
                                    for i in productos_aFacturar:
                                        total_factura += i[2]
                                    print("Total factura: {}".format(total_factura))
                                    while True:
                                        confirmacion = input("¿Desea confirmar la factura?(s/n): ")
                                        if confirmacion.upper() == "S":
                                            print("\033[91m\033[107m>>>\033[0m Factura ingresada con exito")
                                            time.sleep(1)
                                            # Ingreso factura
                                            with open(path + facturaTxt, "a") as file:
                                                for producto in productos_aFacturar:
                                                    file.write("{},{},{},{},{},{},{},{},{},1\n".format(
                                                    id_factura, rut, dia, mes, año, producto[0], producto[1], producto[2], producto[3]
                                                    ))
                                            break
                                        elif confirmacion.upper() == "N":
                                            print("\033[91m\033[107m>>>\033[0m Cancelando...")
                                            time.sleep(1)
                                            break
                                        else:
                                            print("\033[91m\033[107m>>>\033[0m Opcion no valida. Vuelva a intentarlo")
                                            time.sleep(1)
                                            continue
                                    break
                        break
                break                               
        except Exception as e:
            print("\033[91m\033[107m>>>\033[0m Error inesperado Ingreso Factura: {}".format(e))
            time.sleep(1)

                    
def validar_fecha(fecha):
    try:
        datetime.datetime.strptime(fecha, '%d/%m/%Y') or datetime.datetime.strptime(fecha, '%d-%m-%Y')
        return True
    except ValueError:
        return False
def obtener_dato_producto(n_a, id_producto, col):
    file = open(path + n_a, "r")
    for i in file.readlines():
        elementos = i.strip().split(",")
        if id_producto == elementos[0]:
            return (elementos[col])
    return 0