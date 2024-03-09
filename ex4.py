# Elaborar un algoritmo que permita ingresar el número de partidos ganados, perdidos y empatados, por ABC club en el torneo apertura,
# se debe de mostrar su puntaje total, teniendo en cuenta que por cada partido ganado obtendrá 3 puntos, empatado 1 punto y perdido 0 puntos.

matches_won = int(input("Introduce el número de partidos ganados: "))
matches_lost = int(input("Introduce el número de partidos perdidos: "))
matches_drawn = int(input("Introduce el número de partidos empatados: "))

print(
    "El puntaje total del ABC club es: ",
    matches_won * 3 + matches_lost * 0 + matches_drawn * 1,
)
