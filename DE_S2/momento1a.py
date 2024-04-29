#Cargar a la tabla calls una nueva columna con la diferencia de fechas


import pandas as pd
from datetime import datetime, timedelta
import random

# Cargar el archivo CSV
df = pd.read_csv('DE_S2/calls.csv')

# Crear una lista de fechas aleatorias para agregar al DataFrame
fecha_inicial = datetime(2024, 1, 1)  # Puedes ajustar la fecha inicial según tus necesidades
fecha_final = datetime(2024, 12, 31)  # Puedes ajustar la fecha final según tus necesidades

#Fechas ramdom para la columna (entre la fecha inicial y final definida arriba)
df['transaction_date'] = [fecha_inicial + timedelta(days=random.randint(0, (fecha_final - fecha_inicial).days)) for _ in range(len(df))]

# Guardar el DataFrame modificado en un nuevo archivo CSV
df.to_csv('DE_S2/calls_with_dates.csv', index=False)
