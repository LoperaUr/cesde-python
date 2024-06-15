import pandas as pd
import matplotlib.pyplot as plt
import requests

## URL de la API
url = "https://api.covidtracking.com/v1/us/daily.json"

## Realizamos la petición y guardamos la respuesta como un JSON
response = requests.get(url).json()

## Convertimos la respuesta a un DataFrame de Pandas
df = pd.DataFrame(response)

## Mostramos las primeras filas del DataFrame
print(df.head())

## Graficamos el número de casos positivos
plt.plot(df['date'], df['positive'])
plt.xlabel('Fecha')
plt.ylabel('Casos positivos')
plt.title('Casos positivos de COVID-19 en EE. UU.')
plt.show()

