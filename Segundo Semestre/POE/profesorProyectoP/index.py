import funcion as f

print(f.hora())

rut=input("Ingrese Rut !!!!")
if f.vrut(rut)==1:
    print("OK")
else:
    print("Malo")