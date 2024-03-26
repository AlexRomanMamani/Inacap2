# declaracion tuplas, es inmutable, no se puede modificar los valores del arreglo
t = (1,2,3,4) 
print(t[-1:]) #[indice, cant de caracteres]
print(t[1:4])
print(t[:2])

t1 = 1,5,22,7,1,6,10,90,100
print(t1.index(22)) # busca el valor dentro de index en la tupla, si lo encuentra print la posicion

a = 100
if a in t1:
    print("si esta, posicion {}".format(t1.index(a)))
else:
    print("no esta")

t1 = sorted(t1) #ordena valores de la tupla, solo numeros
print(t1)

print (sum(t1)) # suma los valores de la tupla
print(max(t1)) # muestra el valor mayor de la tupla
print(min(t1)) # minimo de la tupla
print(t1[::-1])