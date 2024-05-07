#De la base de datos dada. Escribir una consulta que produzca una lista, en orden alfabético, de todas las distintas 
#ocupaciones en la tabla Customer que contengan la palabra "Engineer".

import pandas as pd
import sqlite3

# Abrir el archivo CSV con pandas
df = pd.read_csv('DE_S1/customers.csv')

# Crear una conexión a una base de datos SQLite en memoria
conn = sqlite3.connect(':memory:')

# Guardar el DataFrame en la base de datos SQLite
df.to_sql('customers', conn, index=False)

# Consulta SQL 
#SELECT DISTINCT en SQL trae valores únicos de una columna específica de una tabla, eliminando los duplicados. Si existen dos "Engineer aeronautical" trae UNO
#Los % sirven para que me traiga todo lo que esta entre Engineer
query = "SELECT DISTINCT occupation FROM customers WHERE occupation LIKE '%Engineer%' ORDER BY occupation"

# Ejecutar la consulta
resultado = pd.read_sql_query(query, conn)

# Mostrar el resultado
print(resultado)

# Cerrar la conexión
conn.close()