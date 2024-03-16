"""
Leer una palabra, mostrar cuantas vocales tiene  
"""

palabra = input("ingrese una palabra  :")

vocales = 0
for letra in palabra:
    if letra in "aeiou":
        vocales = vocales + 1

print(f"la palabra {palabra} tiene {vocales} vocales")
