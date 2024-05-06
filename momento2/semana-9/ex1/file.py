import pandas as pd

dataframe = pd.read_csv("./ventas.csv")

print(dataframe.head(5), "\n")

print(
    f"El dataframe tiene {dataframe.shape[1]} columnas y {dataframe.shape[0]} filas \n"
)

nulos_por_columna = dataframe.isnull().sum()

for key, value in nulos_por_columna.items():
    print(f"Columna: {key}, cantidad de nulos: {value}")

print(f"\nSuma de la columna ventas {dataframe['sales'].sum()}\n")

dataframe["date"] = pd.to_datetime(dataframe["date"])

dataframe["year"] = dataframe["date"].dt.year
dataframe["month"] = dataframe["date"].dt.month

promedio_ventas = dataframe.groupby(["month"])["sales"].mean()

print(promedio_ventas)

ventas_por_producto = dataframe.groupby('product')['sales'].sum()

producto_mas_vendido = ventas_por_producto.idxmax()
ventas_producto_mas_vendido = ventas_por_producto.max()

print(f"El producto más vendido es {producto_mas_vendido} con un total de {ventas_producto_mas_vendido} ventas.")

dataframe_electronica = dataframe[dataframe['category'] == 'Electronica']
print(dataframe_electronica)

dataframe_electronica.to_csv('csv_electronica.csv', index=True)
