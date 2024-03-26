import funciones as f
import time
import os
# asdasd
# asd2

f.usarCrearArchivo()
print(f.credito())
f.definirVariables()
while True:
    print("{:>20}".format(f.hora()))
    print(f.creamenu())
    f.rellenar_articulos()
    try:
        op = f.n_P(4)
        # Menu de Usuario
        if op == 1:
            f.menu_cliente()
        # Menu de Facturacion
        elif op == 2:
            f.menu_facturacion()
        # Menu de Reportes
        elif op == 3:
            f.reportes()
        # Salir
        elif op == 4:
            print(">>> Cerrando sistema... Adios!")
            break
    except:
        input(
            ">>> Se ha encontrado un error. Presione Enter para volver al Menu Principal..."
        )
