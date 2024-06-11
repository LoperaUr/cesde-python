import pandas as pd

df = pd.read_excel("./templates.xlsx", sheet_name=1)

df.to_csv("./market.csv", index=False)


df_productos = df[["Producto", "Cantidad"]]

print(df["Ventas_Octubre"].max())

df["Total 2"] = (
    df["Comisiones_Septiembre"] + df["Comisiones_Octubre"] + df["Comisiones_Noviembre"]
)

print(df["Total 2"].sum())