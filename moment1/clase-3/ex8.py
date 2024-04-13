"""
Mostrar los números comprendidos entre 1 y 30 exceptuando los múltiplos de 3
"""

for i in range(1, 30):
    if i % 3 == 0:
        continue
    print(i)
