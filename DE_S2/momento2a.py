#Pruebo imprimir todos los registros de cada tabla

import pandas as pd
from sqlalchemy import create_engine, text

# Conexión a la base de datos PostgreSQL
engine = create_engine("postgresql://postgres:467985@localhost/DE_S2b2a.py")
#                                    usuario: pasword @ host /  base_de_datos






# Ejemplo de consulta para mostrar todos los datos en las tablas
print("================================")
print("==========Agents================")
print("================================")
with engine.connect() as connection:
    # Utilizar text de SQLAlchemy para envolver la consulta SQL
    query = text("SELECT * FROM agents;")

    # Ejecutar la consulta
    result = connection.execute(query)

    # Obtener y mostrar los resultados
    rows = result.fetchall()

    # Convertir los resultados a un DataFrame de pandas para visualización
    df = pd.DataFrame(rows, columns=result.keys())
    print(df)







#!=======================================================================
print("================================")
print("==========Calls=================")
print("================================")
# Ejemplo de consulta para mostrar todos los datos en las tablas
with engine.connect() as connection:
    # Utilizar text de SQLAlchemy para envolver la consulta SQL
    query = text("SELECT * FROM calls;")

    # Ejecutar la consulta
    result = connection.execute(query)

    # Obtener y mostrar los resultados
    rows = result.fetchall()

    # Convertir los resultados a un DataFrame de pandas para visualización
    df = pd.DataFrame(rows, columns=result.keys())
    print(df)







#!=======================================================================
print("================================")
print("==========Customers=============")
print("================================")
# Ejemplo de consulta para mostrar todos los datos en las tablas
with engine.connect() as connection:
    # Utilizar text de SQLAlchemy para envolver la consulta SQL
    query = text("SELECT * FROM customers;")

    # Ejecutar la consulta
    result = connection.execute(query)

    # Obtener y mostrar los resultados
    rows = result.fetchall()

    # Convertir los resultados a un DataFrame de pandas para visualización
    df = pd.DataFrame(rows, columns=result.keys())
    print(df)




# Cierra la conexión del motor de SQLAlchemy
engine.dispose()
