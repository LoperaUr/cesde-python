import pandas as pd

notas = {
    "Estudiante 1": 4.5,
    "Estudiante 2": 3.5,
    "Estudiante 3": 2.5,
    "Estudiante 4": 4.0,
    "Estudiante 5": 3.0,
}


def get_est(dict_input):
    serie = pd.Series(dict_input)
    nota_minima = serie.min()
    nota_maxima = serie.max()
    nota_media = serie.mean()
    deviation = serie.std()

    return pd.Series(
        {
            "Nota mínima": nota_minima,
            "Nota máxima": nota_maxima,
            "Nota media": nota_media,
            "Desviación": deviation,
        }
    )

print(get_est(notas))
