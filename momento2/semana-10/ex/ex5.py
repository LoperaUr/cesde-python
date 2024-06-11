import pandas as pd
import matplotlib.pyplot as plt


dataframe = pd.DataFrame({
    "Vendedor": ["Juan", "Pedro", "María", "Luis", "Ana", "Carlos"],
    "T1": [100, 200, 300, 400, 500, 600],
    "T2": [200, 300, 400, 500, 600, 700],
    "T3": [300, 400, 500, 600, 700, 800],
    "T4": [400, 500, 600, 700, 800, 900],
})

dataframe["Total por Vendedor"] = dataframe["T1"] + dataframe["T2"] + dataframe["T3"] + dataframe["T4"]

plt.pie(dataframe["Total por Vendedor"], labels=dataframe["Vendedor"])
plt.show()

