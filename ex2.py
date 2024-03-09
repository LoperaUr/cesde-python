# Se desea calcular la distancia recorrida (m) por un automóvil que tiene velocidad constante(m/s) durante un tiempo t(s)
# velocidad = distancia / tiempo
# distancia = velocidad * tiempo

velocidad = float(input("Introduce la velocidad en m/s: "))
tiempo = float(input("Introduce el tiempo en segundos: "))

distancia = velocidad * tiempo

print("La distancia recorrida es: ", distancia, "metros")
