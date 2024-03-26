import funciones as f
import time
import os

 
ciclo = None
print(f.credito())
while ciclo != 5:
  try:
   print(f.creamenu())   
   while True:
       ciclo=input("Ingrese  : ")
       if ciclo=="" or ciclo.isalpha(): #valida que lo ingresado sea un numero
          print("Ingreso un caracter, solo números")
       else:
           ciclo=int(ciclo)
           break 
   #print(type(ciclo))    
   #print(ciclo)
   if ciclo==1:
     #os.system(f.limpip())
     
     print(f.ingresa_u())  
     rr=0
     while rr == 0 :
         r=input("Ingrese Rut  : ")
         rr=f.vrut(r)
         print("Error, Rut No Valido!!!!! " )
         
         
     n=input("Ingrese Nombre  : ")     
     p=f.Persona("111111", "Juan", "11-11-2000", "Su casa")
     print(p.nombre)
     print(p.rut)
     time.sleep(2)
  
    
  
    
  
    
  
    
  
    
  
    
  
    
  
    
  
    
  except:
     print("Error")
 