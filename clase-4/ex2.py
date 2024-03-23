"""
Crea un juego parecido a piedra, papel o tijeras, algo así como adivina la respuesta correcta o lo que se te ocurra.
"""

import random


def adivinaElNumero():
    numbers = (1, 2, 3, 4, 5)
    print("")
    number_user = int(input("adivina el numero del 1 - 5: "))
    if number_user > 5 or number_user < 1:
        print("argumento invalido")

    number_system = random.choice(numbers)

    if number_system == number_user:
        print("correcto")
    else:
        print("incorrecto")


print("")
print("--adivina el numero--")
adivinaElNumero()
