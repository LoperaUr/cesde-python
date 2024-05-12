import pandas as pd
import matplotlib.pyplot as plt

dataframe = pd.DataFrame({
    "Mes": ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"],
    "Ingresos": [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000],
    "Gastos": [500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000]
})

dataframe["Beneficios"] = dataframe["Ingresos"] - dataframe["Gastos"]
dataframe["Porcentaje"] = dataframe["Beneficios"] * 0.14

plt.bar(dataframe["Mes"], dataframe["Beneficios"])
plt.show()

print(dataframe)
