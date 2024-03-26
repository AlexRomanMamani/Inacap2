import funciones as f
import time

print(f.credito())
f.definirVariables()
while True:
    print("{:>20}".format(f.hora()))
    print(f.creamenu())
    try:
        op = f.n_P()
        if op == 1:
            f.ingresoUsuario()
        elif op == 2:
            f.modificarUsuario()
        elif op == 3:
            f.eliminarUsuario()
        elif op == 4:
            f.consultarUsuario()
        elif op == 5:
            print(">>> Cerrando sistema... Adios!")
            break
    except:
        input(
            ">>> Se ha encontrado un error. Presione Enter para volver al Menu Principal..."
        )
