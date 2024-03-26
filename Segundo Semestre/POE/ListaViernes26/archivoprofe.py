import time
import json

"""
diccionario = {"clave1": "valor1", "clave2": "valor2", "clave3": "valor3"}
with open("archivo.txt", "w") as archivo:

    json.dump(diccionario, archivo)

"""
inv=[]

with open("c:\\bdd\\datos.txt", "w") as archivo:
    while True:
        ent=0
        art=input("Articulo  (s)alir...!!!")
        print()
        if art.lower()=="s":
            break
        for p in inv:
            if art.lower()==p["Articulo"].lower():
                ent=1
                #print("\t Articulo", p.index(art))
                me=input("Artículo existe  ...(M)odifica (E)limina...")
                if me.lower()=="m":
                    precio=input("precio a modificar... : ")  
                    inv.remove(p)
                    inv.append({"Articulo":art,"Precio": (precio)})
                    time.sleep(2)
                if me.lower()=="e":
                    inv.remove(p)
                    print(art)
                    time.sleep(2)

        if ent==0:          
            precio=input("precio... : ")          
            inv.append({"Articulo":art,"Precio": (precio)})
            json.dump(inv, archivo) 

print(inv) 

"""

with open("d:\\bdd\\datos.txt", "w") as archivo:

      for elemento in inv:

        archivo.write(elemento + "\n")           

"""