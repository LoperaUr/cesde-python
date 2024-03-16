# Se necesita elaborar un algoritmo que solicite el número de respuestas correctas, incorrectas y en blanco, correspondientes a postulantes,
# y muestre su puntaje final considerando que por cada respuesta correcta tendrá 3 puntos, respuestas incorrectas tendrá -1 y respuestas en blanco tendrá 0.

correct_responses = int(input("Introduce el número de respuestas correctas: "))
incorrect_responses = int(input("Introduce el número de respuestas incorrectas: "))
blank_responses = int(input("Introduce el número de respuestas en blanco: "))

print(
    "el puntaje del postulante es: ",
    correct_responses * 3 + incorrect_responses * -1 + blank_responses * 0,
)
