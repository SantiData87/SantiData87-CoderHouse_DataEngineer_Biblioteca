#Cargar los archivos csv de las Tablas en la base de datos PostgreSQL desde Python
#Momento 1 Creación de tablas calls, agents y customers para dar cumplimiento con el requerimiento que se necesita teniendo en cuenta la información que se provee 

#Primero instalar estas librerias y Crear en PostgreSQL la base de datos "DE_s2"
#pip install sqlalchemy
#pip install psycopg2

import pandas as pd
from sqlalchemy import create_engine #Libreria para conectar con la base de datos PostgreSQL

# Conexión a la base de datos PostgreSQL 
engine = create_engine("postgresql://postgres:467985@localhost/DE_S2")
#                                    usuario: pasword @ host /  base_de_datos

# Cargar datos desde archivos CSV usando pandas

#1) Creo una Lista de los archivos que voy a cargar
csv_files = ["agents.csv", "calls.csv", "customers.csv","calls_with_dates.csv"]
#csv_files = ["agents.csv", "calls.csv", "customers.csv"] 



#2) Aplico un for sobre la lista de los archivos apra que los cargue a todos
for csv_file in csv_files:
    table_name = csv_file.split(".")[0]                              # Tomar el nombre del archivo sin la extensión
    df = pd.read_csv(csv_file)                                       # Guardo en DataFrame
    df.to_sql(table_name, engine, if_exists='replace', index=False)  # Utilizar el motor de SQLAlchemy para escribir en PostgreSQL

# Cierra la conexión del motor de SQLAlchemy
engine.dispose()
