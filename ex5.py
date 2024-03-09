# Construya un algoritmo que resuelva un problema que tiene una gasolinera. Los dispensadores de esta registran lo que “surten” en galones,
# pero el precio de la gasolina está fijado en litros. El algoritmo debe calcular e imprimir lo que hay que cobrarle al cliente.

quantity = float(input("Introduce la cantidad de gasolina surtida en galones: "))
price_per_liter = float(input("Introduce el precio por litro de gasolina: "))

print("El monto a cobrar es: ", quantity * 3.78541 * price_per_liter)
