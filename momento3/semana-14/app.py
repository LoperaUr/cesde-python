from flask import Flask, render_template, render_template_string
import pandas as pd

app = Flask(__name__)

dataframe = pd.DataFrame(
    {
        "Nombre": ["Ana", "Luis", "María", "Juan"],
        "Edad": [28, 34, 29, 40],
        "Ciudad": ["Madrid", "Barcelona", "Valencia", "Sevilla"],
    }
)

html_page = """ 
    <!DOCTYPE html> 
    <html lang="es"> 
    <head> 
        <meta charset="UTF-8"> 
        <meta name="viewport" content="width=device-width, initial-scale=1.0"> 
        <title>Tabla de Pandas</title> 
        <style> 
            table { 
                width: 50%; 
                margin: 20px auto; 
                border-collapse: collapse; 
            } 
            th, td { 
                padding: 10px; 
                border: 1px solid #ccc; 
                text-align: left; 
            } 
            th { 
                background-color: #f4f4f4; 
            } 
        </style> 
    </head> 
    <body> 
        <h1>Tabla Generada con Pandas</h1> 
        {{html_table | safe}} 
    </body> 
    </html> 
    """


# Inyecta el dataframe en el template index.html
@app.route("/htmlV1")
def inyect_html():
    return render_template("index.html", dataframe=dataframe.to_html())


# Se crea el html desde el código python
@app.route("/htmlV2")
def create_html():
    return render_template_string(html_page, html_table=dataframe)


if __name__ == "__main__":
    app.run(debug=True)
