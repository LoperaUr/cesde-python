import pandas as pd

series = pd.Series([100, 200, 300, 400], index=["a", "b", "c", "d"])

var = series["b"]
print(f'el valor en el indice b es: {var}')
