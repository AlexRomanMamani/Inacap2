"""
#a = input("Ingrese Algo: ")
#a = int(a)
x = 0
n = 0

###########
while x <= a:
    while n <= x:
        print(n)
        n+=1
    x+=1
    print(x)

############
    
while True:
    if x == 100:
        break
    x+=1
    print(x)
else:
    print("Fin")

############

for x in range(100):
    print(x)
"""
a = input("Ingrese algo: ")
print(a.lower())
print(a.upper())
print(a.find("n"))
print(a.swapcase())
print(a.isalnum())
print(a.isalpha())
print(a.isnumeric())