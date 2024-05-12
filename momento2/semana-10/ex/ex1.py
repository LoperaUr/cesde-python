import pandas as pd
import matplotlib.pyplot as plt

dataframe = pd.DataFrame({
    "Cliente": ["Antonio", "Juan", "Amelia", "Marisa"],
    "Fecha Llegada": ["25/06/2002", "26/06/2002", "27/06/2002", "28/06/2002"],
    "Dias de estancia": [2, 3, 4, 5]
})

dataframe["Precio"] = dataframe["Dias de estancia"] * 53.49
dataframe["IVA"] = dataframe["Precio"] * 0.16
dataframe["TOTAL"] = dataframe["Precio"] + dataframe["IVA"]


plt.pie(dataframe["TOTAL"], labels=dataframe["Cliente"])

plt.show()

print(dataframe)
