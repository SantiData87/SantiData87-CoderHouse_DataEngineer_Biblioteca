#Escribir una consulta que devuelva el ID del cliente, su nombre y una columna 
#nueva llamada “Mayor30” que contenga "Sí" si el cliente tiene más de 30 años y "No" en caso contrario.

import pandas as pd
import sqlite3

# Abrir el archivo CSV con pandas
df = pd.read_csv('DE_S1/customers.csv')

# Crear una conexión a una base de datos SQLite en memoria
conn = sqlite3.connect(':memory:')

# Guardar el DataFrame en la base de datos SQLite
df.to_sql('customers', conn, index=False)


# Consulta SQL 
#CASE es similar a una estructura de control condicional DE python "if-else"
query = "SELECT customerid, Name, CASE WHEN Age >= 30 THEN 'Yes' WHEN Age < 30 THEN 'No' ELSE 'Missing Data' END AS Over30 FROM customers ORDER BY Name DESC"

# Ejecutar la consulta
resultado = pd.read_sql_query(query, conn)

# Mostrar el resultado
print(resultado)

# Cerrar la conexión
conn.close()