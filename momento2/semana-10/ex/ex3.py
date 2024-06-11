import pandas as pd
import matplotlib.pyplot as plt

dataframe = pd.DataFrame({
    "Cod.": [10, 40, 3, 5, 30, 2, 11],
    "Nombre": ["Libreta-50", "Lápiz-2B", "Borrador", "Plumón", "Cuaderno", "Lápiz-2H", "Libreta-100"],
    "Precio": [50, 5, 10, 20, 100, 5, 100],
    "Proveedor": ["Agisa", "Agisa", "Agisa", "Agisa", "Agisa", "Agisa", "Agisa"],
    "Cantidad": [100, 200, 300, 400, 500, 600, 700]
})

dataframe["Precio"] = dataframe["Precio"] * dataframe["Cantidad"]

plt.pie(dataframe["Precio"], labels=dataframe["Nombre"], autopct="%1.1f%%")
plt.show()

