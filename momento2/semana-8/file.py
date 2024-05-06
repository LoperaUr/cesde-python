import pandas as pd

df = pd.read_csv("employees.csv", sep=";")

print(df.to_string())

df = df.dropna(subset=["Salario Mensual"])
df = df.dropna(subset=["Edad"])

df = df.dropna(subset=["Apellido"])

df = df.drop_duplicates(subset=["Nombre"])
df = df.drop_duplicates(subset=["Departamento"])

mayores = df[df["Edad"] > 40]
print(mayores)

mayores = df[df["Edad"] < 40]
print(mayores[["Nombre", "Salario Mensual"]])

df["Salario Anual"] = df["Salario Mensual"] * 12

ventasdep = df[df["Departamento"] == "Ventas"]
print(ventasdep)
