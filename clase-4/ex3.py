"""
    Escribir un programa que gestione los pedidos por cobrar de una cafetería, los pedidos se almacenaran en un diccionario donde la clave
    de cada pedido es el numero de pedido y el valor el costo del pedido. Se debe preguntar si desea añadir un nuevo pedido, pagar el pedido
    o terminar. Si desea añadir un nuevo pedido, se le preguntara el numero del pedido y el costo del pedido y se agregara al diccionario.
    Si desea pagar el pedido, se preguntará por el numero de pedido y se eliminará del diccionario. Después de cada operación el programa debe
    mostrar por pantalla la cantidad cobrada hasta el momento de pedidos y lo que falta por cobrar de los pedidos 
"""


def options():
    option =  int(
        input(
            """ -- Gestión de pedidos -- 
              1. Ingresar un nuevo pedido
              2. Pagar un pedido
              3. Terminar """
        )
    )
    if option != 1 and  option != 2 and option != 3: options()


my_dict = dict()
ban = True
while ban:
    option = options()
    if
