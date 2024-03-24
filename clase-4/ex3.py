"""
    Escribir un programa que gestione los pedidos por cobrar de una cafetería, los pedidos se almacenaran en un diccionario donde la clave
    de cada pedido es el numero de pedido y el valor el costo del pedido. Se debe preguntar si desea añadir un nuevo pedido, pagar el pedido
    o terminar. Si desea añadir un nuevo pedido, se le preguntara el numero del pedido y el costo del pedido y se agregara al diccionario.
    Si desea pagar el pedido, se preguntará por el numero de pedido y se eliminará del diccionario. Después de cada operación el programa debe
    mostrar por pantalla la cantidad cobrada hasta el momento de pedidos y lo que falta por cobrar de los pedidos
"""


def options():
    option = int(
        input(
            """
              -- Gestión de pedidos --
              Ingrese la opción deseada:
              1. Ingresar un nuevo pedido
              2. Pagar un pedido
              3. Terminar:         """
        )
    )
    if option < 1 or option > 3:
        options()
    return option


my_dict = dict()
ban = True
cantidad_cobrada = 0
falta_cobrar = 0

while ban:
    option = options()
    if option == 1:
        key = input("Ingrese el numero de pedido: ")
        value = input("Ingrese el costo del pedido: ")
        my_dict[key] = value
        falta_cobrar += float(value)
        print("Su pedido:", value, "ha sido agregado!")
        print("Cantidad cobrada hasta el momento:", cantidad_cobrada)
        print("Falta por cobrar:", falta_cobrar)

    if option == 2:
        for key, value in my_dict.items():
            print("Pedido:", key, "Costo:", value)
        key = input("Ingrese el numero de pedido a pagar: ")
        if key in my_dict:
            costo_pedido = float(my_dict.pop(key))
            cantidad_cobrada += costo_pedido
            falta_cobrar -= costo_pedido
            print("El pedido ha sido pagado!")
            print("Cantidad cobrada hasta el momento:", cantidad_cobrada)
            print("Falta por cobrar:", falta_cobrar)
        else:
            print("El pedido no existe!")

    if option == 3:
        ban = False
        print("Gracias por su visita")
        print("Cantidad cobrada total:", cantidad_cobrada)
        print("Falta por cobrar total:", falta_cobrar)
