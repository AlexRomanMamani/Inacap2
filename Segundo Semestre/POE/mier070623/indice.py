path = "c:\\bdd\\datos.txt" #instancia fisica bdd
fil = open (path, "a")
idx =0
while True:
    r = input("Rut...")
    if r.lower() == "s":
        break
    n = input("Nombre...")
    c = input("Correo...")
    f = input("Fono...")
    reg  =str(idx),r,n,c,f
    fil.writelines (",".join(reg)+ "\n")
    idx+=1
fil.close()