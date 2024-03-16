"""
Se tiene un código, número de artículos vendidos y el valor de cada artículo. Calcule el valor de la compra, tiendo en cuenta lo siguiente: compra 50 o más artículos se le da al cliente 10% de descuento; si la compra es menor de 50 artículos no se hace descuento. Mostrar el código, el total de la venta y el valor del descuento. 
"""

code = "#123AQ"
number_of_articles = 100
value_of_article = 1000e

if number_of_articles >= 50:
    total = number_of_articles * value_of_article
    discount = total * 0.1
    total -= discount
else:
    total = number_of_articles * value_of_article
    discount = 0

print(
    f"El código es: {code}, el total de la venta es: {total} y el valor del descuento es: {discount}"
)
