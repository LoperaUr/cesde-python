correct_responses = int(input("Introduce el número de respuestas correctas: "))
incorrect_responses = int(input("Introduce el número de respuestas incorrectas: "))
blank_responses = int(input("Introduce el número de respuestas en blanco: "))

print(
    "el puntaje del postulante es: ",
    correct_responses * 3 + incorrect_responses * -1 + blank_responses * 0,
)
