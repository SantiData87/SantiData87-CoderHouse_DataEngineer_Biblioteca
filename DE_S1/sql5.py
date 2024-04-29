#Escribir dos consultas: 
#Una que calcule las ventas totales y las llamadas totales realizadas a los clientes de la profesión de ingeniería.
#Otra que calcule las mismas métricas para toda la base de clientes.

import pandas as pd
import sqlite3

# # Abrir el archivo CSV con pandas
calls_df = pd.read_csv("DE_S1/calls.csv")
customers_df = pd.read_csv("DE_S1/customers.csv")

# Crear una conexión a una base de datos SQLite en memoria
conn = sqlite3.connect(":memory:")  # Crear base de datos en memoria

# Guardar el DataFrame en la base de datos SQLite
calls_df.to_sql("calls", conn, index=False)
customers_df.to_sql("customers", conn, index=False)

# Consulta 1: Ventas totales y llamadas totales para clientes de la profesión de ingeniería
query_engineer = """
SELECT SUM(Ca.ProductSold) AS TotalSales,
       COUNT(*) AS NCalls
FROM calls Ca
JOIN customers Cu ON Ca.CustomerID = Cu.CustomerID
WHERE Cu.Occupation LIKE '%Engineer%';
"""

result_engineer_df = pd.read_sql_query(query_engineer, conn)
print("-------------------------Resultados para clientes de la profesión de ingeniería:")
print(result_engineer_df)
print()

# Consulta 2: Ventas totales y llamadas totales para toda la base de clientes
query_all = """
SELECT SUM(Ca.ProductSold) AS TotalSales,
       COUNT(*) AS NCalls
FROM calls Ca;
"""

result_all_df = pd.read_sql_query(query_all, conn)
print("-------------------------Resultados para toda la base de clientes:")
print(result_all_df)



# Ejecutar la consulta 
result_df = pd.read_sql_query(query_engineer, conn)
result_df2 = pd.read_sql_query(query_all, conn)

# Mostrar el resultado
print(result_df)
print(result_df2)


# Cerrar la conexión
conn.close()
