# Ref:https://drive.google.com/file/d/1VK68uuxdWezE-wxj2uaAIrg9_2bbZFTR/view?usp=drive_link
import numpy as np
import pandas as pd

df = pd.read_csv("archivo_act_colaborativa.csv")
df.replace('$null$', np.nan, inplace=True)

#Borrar duplicados
df = df.dropna()

#Precio promedio de autos en miles de dolares según tipo de fabricante (manufactu)
df["price"]= df["price"].astype(float)
df["NewPrice"] = df["price"]/1000
df.groupby(["manufact"])["NewPrice"].mean()

# 3ro Actualizar precio 5%
df["NewPrice2"] = df.apply(lambda x: x["price"] * 1.05, axis=1)

# 4to
df["horsepow"]= df["horsepow"].astype(float)
df["horsepow"].min()
df["horsepow"].max()
df["horsepow"].std()
df["horsepow"].describe()


