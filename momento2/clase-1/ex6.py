import pandas as pd

notas = {
    "Estudiante 1": 4.5,
    "Estudiante 2": 3.5,
    "Estudiante 3": 2.5,
    "Estudiante 4": 4.0,
    "Estudiante 5": 3.0,
}


def approve(dict):
    notas_serie = pd.Series(dict)
    approved = notas_serie[notas_serie >= 3]
    approved = approved.sort_values(ascending=False)
    print(approved)

approve(notas)