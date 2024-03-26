path = "c:\\bdd\\datos.txt" #instancia fisica bdd
fil = open (path, "a")
while True:
    r = input("Rut...")
    if r.lower() == "s":
        break
    n = input("Nombre...")
    c = input("Correo...")
    f = input("Fono...")
    reg  =r,n,c,f
    fil.writelines (",".join(reg)+ "\n")
fil.close()