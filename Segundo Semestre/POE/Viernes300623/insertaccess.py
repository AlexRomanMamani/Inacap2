import pyodbc
import time
# Establecer la cadena de conexión a la base de datos de Access
conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=c:\bdd\facturacion.mdb;')  


# Conectar a la base de datoss
 

# Crear un cursor para ejecutar consultas
cursor = conn.cursor()

# Insertar un nuevo registro en la tabla
cursor.execute("INSERT INTO usuario (rut, nombre) VALUES ('{0}', '{1}')".format("6", "Luchito"))
conn.commit()

# Cerrar la conexión y el cursor
cursor.close()
conn.close()