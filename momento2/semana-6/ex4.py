import pandas as pd

rango = int(input("Ingrese el rango de años: "))
ventas = []
for i in range(rango):
    ventas_year = float(input(f"Ingrese las ventas del año #{i + 1}: "))
    ventas.append(ventas_year)

serie = pd.Series(ventas)

serie_descuento = serie * 0.9

print("Ventas originales: ")
print(serie)

print("Ventas con descuento: ")
print(serie_descuento)