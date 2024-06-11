"""Leer el código de un empleado, el valor de la hora y el número de horas trabajadas en la semana-11. Calcule el salario semanal, teniendo en cuenta que si trabaja más de 48 horas le debe pagar un 35% de recargo por cada hora de más. """

id_employee = input("Ingrese el código del empleado: ")
valor_hora = float(input("Ingrese el valor por hora: "))
horas = int(input("Ingrese las horas trabajadas en la semana-11: "))

if horas > 48:
    horas_adicionales = horas - 48
    pago_semanal = (48 * valor_hora) + (horas_adicionales * (valor_hora * 1.35))
else:
    pago_semanal = horas * valor_hora

print(f"el pago del empleado con id {id_employee} es: ${pago_semanal}")
