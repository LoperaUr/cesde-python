"""
Mostrar los números pares entre 1 y 20, luego la suma de dichos números pares.
"""

suma_pares = 0
for i in range(1, 20):
    if i % 2 == 0:
        print(i)
        suma_pares = suma_pares + i

print(f"la suma de los pares es {suma_pares}")
