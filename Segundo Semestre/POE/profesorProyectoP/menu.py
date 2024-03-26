import funcion as f
#acá va su función, que crearon en clases

while True:
    print(f.hora())
    print('M e n ú   P r i n ci p a l')
    print('1.. Ingresa Usuario')
    print('2.. Elimina usuario')
    print('3.. Actualiza Usuario')
    print('4.. Modifica Usuario')
    print('5.. Salir')
    try:
        o=int(input("Ingrese opción"))
        if o==1:
            print(11111)
            while True:
               print(" ****  Ingreso de Usuario  ****")
               s=input("[s] Salir de sub menú")
               if s.upper()=="S":
                break
               u=input("Ingrese Rut Válido !!!!!")
               if f.vrut(u)==1:
                  print("Ingreso.......")
               else:
                  print("!!!!Rut Válido!!!!!")

        elif o==2:
         print(2)
        elif o==3:
            print(3)
        elif o==3:
            print(3)
        elif o==5:
            break
    except:
      print("Error")
      
 

