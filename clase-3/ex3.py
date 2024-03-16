"""
Lea dos números NRO1 y NRO2 y escriba ambos números sólo si son de diferente signo y distintos de cero. 
"""

numero_1 = int(input("ingrese el numero 1 "))
numero_2 = int(input("ingrese el numero 2 "))


if (numero_1 > 0 and numero_2 < 0) or (numero_1 < 0 and numero_2 > 0):
    print(f"el numero 1 es {numero_1} y el numero 2 es {numero_2}")
