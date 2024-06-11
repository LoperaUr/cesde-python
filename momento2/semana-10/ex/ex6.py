import pandas as pd
import matplotlib.pyplot as plt

dataframe = pd.DataFrame({
    "Materiales": [100, 200, 105],
    "Horas de mano de obra": [10, 20, 15]
})

dataframe.index = ["Reparaciones", "Limpieza", "Pintura"]

dataframe["Mano de obra $"] = dataframe["Horas de mano de obra"] * 18
dataframe["Total"] = dataframe["Materiales"] + dataframe["Mano de obra $"]
dataframe["Subtotal"] = dataframe["Total"].sum()
dataframe["IVA"] = dataframe["Subtotal"] * 0.16
dataframe["Total a pagar"] = dataframe["Subtotal"] + dataframe["IVA"]

plt.plot(dataframe["Materiales"], dataframe["Mano de obra $"])
plt.show()

print(dataframe)
