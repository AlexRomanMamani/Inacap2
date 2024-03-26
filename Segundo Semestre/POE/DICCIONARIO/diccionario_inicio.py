d=dict(nombre="Juan",apellido="Herrera",direcc="bajo Molle 333",edad=33)
print(d)
d2=dict(zip("abcd",[1,2,3,4]))
print(d2)

# Devuelve un valor, clave y valor items()
item=d.items()
print("Itemes  :",item)


# Devuelve un valor, clave   keys()

keys=d.keys()
print("Claves  :",keys)


#devuelve los valores   values()

valor=d.values()
print("Valores  :",valor)

d.clear()
print(d)

# ************************************


d2={"1":["Manzanas","Kg",220],
    "2":["Peras","Kg",220],
    "3":["Uvas","Caja",220],
    "4":["Sandía","Un",220],
    "5":["Melón","Un",220],
    "6":["Frutilla","Kg",220]}
print(d2)
print("""        
      
      
      """)
#recibe un parámetro u devuelve un objeto

valor=d2.get("1")
print("Valores  :",valor)

print("""        
       
       
       """)
 #recibe un parámetro u devuelve un objeto

valor=d2.setdefault("1")
print("Valores  :",valor)
print(d2['1'][0]) 
print("""        
       
       
       """)

#valor=d2.setdefault("1","111-1")
print("Valores  :",valor)
print(""" 

      
    """)
print(d2)
print(""" 

      
    """)
d2['6'][0]="Platanos" 
print(d2)


#Imprime valores
for x,y in d2.items():
 print("{0}   {1}  ".format(x,y))      

for x,y in d2.items():
    for z in range(3):
        print("{0} {1} {2}".format(x,z,d2[x][z]))      

