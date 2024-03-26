import terceraparte as t

p="c:\\bdd\\datos.txt"
fil=open(p,"a")
idx = t.contar(p)+1
while True:
    r=input("Rut... ")
    if r.lower()=="s":
        break
    n=input("Nombre... ").lower()
    c=input("Correo... ")
    f=input("Fono... ")
    reg=str(idx),r,n,c,f

    print(t.buscar(r))

    if t.buscar(r) == 1:
        print("Rut existente...")
        break
    else:
        fil.write(",".join(reg)+"\n") #diferencia con .writelines?
        idx += 1
     
fil.close()