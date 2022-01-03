import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression


        
dataframe = pd.read_csv(self.file_name)


# trabajando con fechas
dataframe = dataframe.assign(
    new_date=pd.to_datetime(dataframe["fecha"]).apply(lambda date: date.toordinal()))

# # intercamiando nombres
dataframe.rename(columns={"fecha": "Original", "new_date": "fecha"}, inplace=True)


dataframe["infectados"].fillna(0, inplace=True)
dataframe["muertes"].fillna(1, inplace=False)

dependiente = np.array(dataframe["infectados"].values) // np.array(dataframe["muertes"].values)
independiente = np.array(dataframe["fecha"].values)


dependiente = np.around(dependiente,2)
print("="*20,"> Dependieente")
print(dependiente)

print("=" * 20, "> Dependieente")
print(independiente)

independiente = independiente[:, np.newaxis]
dependiente = dependiente[:, np.newaxis]

modelo = LinearRegression()
modelo.fit(X=independiente, y=dependiente)
x = independiente[:, np.newaxis]
y = independiente[:, np.newaxis]


fig, ax = plt.subplots()
fig.canvas.draw()

labels = [item.get_text() for item in ax.get_xticklabels()]
labels[0:] = dataframe["Original"].values

print("label")
print(dataframe["Original"].values)

ax.set_xticklabels(labels, fontsize=7)
plt.xticks(rotation=45)

plt.plot(independiente, modelo.predict(independiente), color="black")
plt.savefig("./static/img.png")
plt.close("all")

# return {
#     "Reporte": "Tasa de comportamiento de casos activos\n en relación al número de muertes en un continente.",
#     "Tipo": "Lineal ",
#     "Tasa De Comportamiento": "{}".format( modelo.coef_ ).replace("[","").replace("]",""),
#     "Continente": self.nombre_pais,

# }