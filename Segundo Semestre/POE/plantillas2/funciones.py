import time 
import datetime	
import os
from pymongo import MongoClient # El cliente de MongoDB
 
from bson.objectid import ObjectId # Para crear ObjectId, porque _id como cadena no funciona

def limpip():
    if os.name == "posix":
      return  "clear"       
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
      return "cls"
    
    
def hora():
    tt= (time.strftime("%H:%M:%S",time.localtime()))     
    return tt

class eso:
    def _init_(self):
         print("Esto es eso")

def vrut(rut):
    r=rut
    r=r.replace(".","")
    r=r.replace("-","")
    dv=r[-1]
    r=r[0:len(r)-1]
    r=list(r)
    print(r,dv)
    s=0
    c=2
    for x in reversed(r):      
     if c==8:
       c=2
     s=s+(int(x) * c)
     print(x,c,s)
     c+=1
     
    s=11-(s%11)
    print(s,type(s))    
    if s==10:
        
       if dv.upper()=="K":
           return 1
       else:
           return 0
           
    if s==11:
        if dv==0:
           return 1
        else:
           return 0
       
    if s!=10 and s!=11:
        #print("entro",s,dv)
        if s==int(dv):
            return 1
        else:
            return 0
        
        
def credito():
     obten_fecha = datetime.datetime.now()
     date = obten_fecha.date()
     year = date.strftime("%Y")
    #print(f"Current Year -> {year}")
     return """=================================
    
    {} CREATE  BY ..... 
               
=================================
        """.format(year)
def creamenu():
    return """Bienvenido al Programa V1.0.
    1 - Insertar Usuario
    2 - Actualizar Usuario
    3 - Lista Usuario (listar usuario)
    4 - Eliminar Usuario
    5 - Salir
    """
def ingresa_u():
    return """I n g r e s o .
        Insertar Usuario   
    """        

#clase
class Persona:
    def __init__(self, rut, nombre, fechan, dire):
        self.rut=rut
        self.nombre = nombre
        self.fechan = fechan
        self.dire = dire
        
        
        
        
        
        
        
        
        

def obtener_bd():
    host = "localhost"
    puerto = "27017"
    usuario = "parzibyte"
    palabra_secreta = "mitienda"
    base_de_datos = "producto"
    cliente = MongoClient("mongodb://{}:{}@{}:{}".format(usuario, palabra_secreta, host, puerto))
    return cliente[base_de_datos]

def insertar(producto):
    base_de_datos = obtener_bd()
    productos = base_de_datos.productos
    return productos.insert_one({
        "nombre": producto.nombre,
        "precio": producto.precio,
        "cantidad": producto.cantidad,
        }).inserted_id

def obtener():
    base_de_datos = obtener_bd()
    return base_de_datos.productos.find()

def actualizar(id, producto):
    base_de_datos = obtener_bd()
    resultado = base_de_datos.productos.update_one(
        {
        '_id': ObjectId(id)
        }, 
        {
            '$set': {
                "nombre": producto.nombre,
                "precio": producto.precio,
                "cantidad": producto.cantidad,
            }
        })
    return resultado.modified_count

def eliminar(id):
    base_de_datos = obtener_bd()
    resultado = base_de_datos.productos.delete_one(
        {
        '_id': ObjectId(id)
        })
    return resultado.deleted_count

    