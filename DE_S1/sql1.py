#De la base de datos dada. Extraer agentes cuyo nombre empieza por M o termina en O.

import pandas as pd
import sqlite3

# Abrir el archivo CSV con pandas
df = pd.read_csv('agents.csv')

# Crear una conexión a una base de datos SQLite en memoria
conn = sqlite3.connect(':memory:')

# Guardar el DataFrame en la base de datos SQLite
df.to_sql('agents', conn, index=False)

# Consulta SQL 
query = "SELECT * FROM agents WHERE name LIKE 'M%' OR name LIKE '%o'"


# Ejecutar una consulta SQL
resultado = pd.read_sql_query(query, conn)

# Mostrar el resultado
print(resultado)

# Cerrar la conexión
conn.close()

