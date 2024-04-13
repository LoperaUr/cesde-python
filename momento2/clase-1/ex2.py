import pandas as pd

series = pd.Series([10, 20, 30, 40, 50])

suma = 0
for i in series:
    suma += i

print("La suma de los datos de la serie es: ", suma)
