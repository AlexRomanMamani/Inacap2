d={1:"juan", 2:"maria",3:"Pedro"} #1,2,3 = Key (indice)
#print(d.get(3)) #d.get(#) trae el valor alojado en la key #
print(d.setdefault(1,"Alex"))
print(d.get(1))

""""
items = d.items()

print(items)
"""

"""""
for x,y in d.items(): #recorre key(x) valor (y)
    print("{0} {1}".format(x,y))

"""

d2={1:["matematicas","electricidad","mecanica", 2],
    2:["Carlos","Luis", 3]}

print(d2[1][1])
print(d2.get(2))
print(d2[1][3] * d2[2][2]) #imprime 2*¨3