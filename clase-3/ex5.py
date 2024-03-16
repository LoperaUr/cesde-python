"""
Un cliente tiene una inversión en el banco. El decidirá reinvertir con los intereses siempre y cuando estos excedan a $100.000, sino solo dejará el capital. Desea saber cuánto dinero tendrá finalmente en su cuenta. Se lee el valor invertido (que debe ser máximo de $90.000) y la tasa de interés. 
"""


def calc():
    inversion = float(input("Ingrese el valor de la inversión: "))
    if inversion > 90000:
        print("El valor de la inversión no puede ser mayor a $90.000")
        calc()
    tasa_interes = float(input("Ingrese la tasa de interés: "))
    intereses = inversion * tasa_interes

    if intereses > 100000:
        total = inversion + intereses
    else:
        total = inversion
    print(f"El total de la cuenta es: {total}")


calc()
