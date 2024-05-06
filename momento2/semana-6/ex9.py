import pandas as pd

data_frame = pd.DataFrame(
    {
        "Mes": ["Enero", "Febrero", "Marzo", "Abril", "Mayo"],
        "Ventas": [100, 150, 200, 180, 220],
    }
)


ventas_primer_trimestre = data_frame.loc[0:2, "Ventas"]
print("El total de ventas del primer trimestre es: ", ventas_primer_trimestre.sum())
