import terceraparte as t

pat="c:\\bdd\\datos.txt" 
l =[]
fil=open(pat,"r")
reg=fil.readlines()
for x in reg:
    #print("x",x)
    data = x.strip().split(',')  # formateo de valores(quita los espacios)
    print("data",data)
    if "Alex" in data:
        i = data.index("Alex")
        print("esta", data.index("Alex"))
        print(data[i])
        l=l+data

print(l)