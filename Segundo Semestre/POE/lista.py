# si es mutable
l = list()
l = [1,2,3,4]
print(l)
while True:
    x = input("algo: ")
    if x.lower() == "s":
        break
    l.append(x) #agrega datos a la lista
print(l)

a = [100,2,3]
b = [1,4,3]
x = [a,b]
a.reverse() #lista al reverso
print(a)

#3, set(lista)
#4, reverse l = [a,z,v]
#5,  set(a) elimina los valores repetidos
#6,  tambien va un set()
#7, 