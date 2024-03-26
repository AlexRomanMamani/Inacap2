path = "c:\\bdd\\datos.txt"  # instancia fisica bdd
fil = open(path, "r")
reg = fil.readlines()
reg2 = reg
for r in reg:
    datos = r.strip().split(",")
print(datos)
idx = max(datos[0])  # 0 es el indice de cada linea
idx = int(idx) + 1  # luego de obtener el indice maximo, le suma 1 para el sig. reg.
print("El siguiente registro es {}".format(idx))
fil.close()

fil = open(path, "a")

while True:
    r = input("Rut...")
    if r.lower() == "s":
        break
    n = input("Nombre...")
    c = input("Correo...")
    f = input("Fono...")
    reg = str(idx), r, n, c, f
    if r in reg2:  # consulta si el rut existe en la lista
        print("El registro ya existe")
        continue
    fil.writelines(",".join(reg) + "\n")
    idx += 1
fil.close()

"""""
ingreso usuario
ingreso factura
ingreso mercaderia

3 archivos de texto
usuario fact, merc (articulo)

ingrese factura
- nombre cliente, 
- fecha, 
- art1 (buscar art, art encontrado, saca y muestra los datos del articulo)

listar las ventas de hoy (guardar por mes y por año (numerico))
- los datos a listar deben estar escritos a mano (las bases de dato no deben estar vacias para que se pueda listar)


""" ""
