import pyodbc

# Establecer la cadena de conexión a la base de datos de Access
conn =pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=c:\bdd\data1.mdb;')  

rs = conn.cursor()
r=input("rut...") 
q = rs.execute("SELECT c.nombre, f.fono FROM cliente c inner join fono f on c.rut = f.fk_rut where  rut ='{}'".format(r))
rows = q.fetchall() 
n=0

print("{0:15}{1:30} ".format("rut","nombre"))    
if rows is not None:
    for row in rows:
        l=list(row)
        
        print("{0:15}{1:30}".format( row[n],row[n+1]))
       
        
else:
    print("No hay datos en la tabla.")
    
# Cerrar la conexión y el cursor

conn.close()
 