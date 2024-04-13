"""
Una agencia de alquiler de autos cobra la hora de uso del vehículo a un valor determinado. Si el cliente usa el carro por más de 10 horas, le hacen un descuento del 20% por cada hora de más. Haga un programa que lea horas de uso, valor hora, y determine el total a pagar. 
"""

horas = int(input("Ingrese las horas de uso del vehículo: "))
valor_hora = float(input("Ingrese el valor por hora: "))

if horas > 10:
    adicional = horas - 10
    total = (10 * valor_hora) + (adicional * (valor_hora * 0.8))
else:
    total = horas * valor_hora

print(f"El total a pagar es: {total}")
