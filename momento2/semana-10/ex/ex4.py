import pandas as pd
import matplotlib.pyplot as plt

dataframe = pd.DataFrame({
    "Volumen de ventas": [100, 200, 300, 400, 500, 600],
    "Ingresos por ventas": [1000, 2000, 3000, 4000, 5000, 6000]

})

dataframe.index = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio"]

dataframe["Costos Fijos"] = 50
dataframe["Costos Variables"] = dataframe["Volumen de ventas"] * 1.6
dataframe["Costos"] = dataframe["Costos Variables"] + dataframe["Costos Fijos"]
dataframe["Beneficios"] = dataframe["Ingresos por ventas"] - dataframe["Costos"]


plt.bar(dataframe.index, dataframe["Beneficios"])
plt.show()

print(dataframe)
