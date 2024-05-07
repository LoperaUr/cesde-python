import pandas as pd

dataframe = pd.read_csv("./temperaturas.csv")

print(dataframe.mean())

print(dataframe.head())

print(dataframe.info())

columna = dataframe["Temperatura 1"]

filtro = dataframe[dataframe["Temperatura 1"] > 10]

suma = dataframe["Temperatura 1"].sum()

dataframe["suma"] = dataframe["Temperatura 2"] + dataframe["Temperatura 3"]

dataframe = dataframe.drop("Temperatura 3", axis=1)

dataframe = dataframe.sort_values("Temperatura 1")

dataframe_agrupado = dataframe.groupby("Temperatura 1").mean()
