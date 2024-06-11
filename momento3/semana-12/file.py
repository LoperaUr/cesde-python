import pandas as pd
import matplotlib.pyplot as pyplot

dataframe = pd.DataFrame(
    {
        "Estudiante": ["Juan", "Ana", "Pedro", "Maria"],
        "Submodulo1": [3.4, 1.6, 4.6, 5.0],
        "Submodulo2": [2.4, 3.6, 4.6, 3.0],
        "Submodulo3": [3.4, 4.6, 4.6, 3.0],
        "Submodulo4": [4.4, 3.6, 4.6, 3.0],
    }
)


dataframe["Nota Final"] = dataframe[
    ["Submodulo1", "Submodulo2", "Submodulo3", "Submodulo4"]
].mean(axis=1)

print(f"Nota final minima: {dataframe['Nota Final'].min()}")
print(f"Nota final maxima: {dataframe['Nota Final'].max()}")
print(f"Nota media: {dataframe['Nota Final'].mean()}")

##pyplot.bar(dataframe["Estudiante"], dataframe["Nota Final"], color="red")
pyplot.pie(dataframe["Nota Final"], labels=dataframe["Estudiante"], autopct="%1.1f%%")
pyplot.show()
