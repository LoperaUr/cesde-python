matches_won = int(input("Introduce el número de partidos ganados: "))
matches_lost = int(input("Introduce el número de partidos perdidos: "))
matches_drawn = int(input("Introduce el número de partidos empatados: "))

print(
    "El puntaje total del ABC club es: ",
    matches_won * 3 + matches_lost * 0 + matches_drawn * 1,
)
