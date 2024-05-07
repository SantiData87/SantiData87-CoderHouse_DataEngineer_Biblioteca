# Escribir una consulta que devuelva todas las llamadas realizadas a clientes de la 
#profesión de ingeniería y muestre si son mayores o menores de 30, así como si terminaron comprando el producto de esa llamada.


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

# Consulta SQL
query = """
SELECT Ca.CallID, Ca.CustomerID, Cu.Name, Ca.ProductSold,
    CASE
        WHEN Cu.Age >= 30 THEN 'Yes'
        WHEN Cu.Age < 30 THEN 'No'
        ELSE 'Missing Data'
    END AS Over30
FROM calls Ca
JOIN customers Cu ON Ca.CustomerID = Cu.CustomerID
WHERE Cu.Occupation LIKE '%Engineer%'
ORDER BY Cu.Name DESC;
"""

# Ejecutar la consulta 
result_df = pd.read_sql_query(query, conn)

# Mostrar el resultado
print(result_df)

# Cerrar la conexión
conn.close()
