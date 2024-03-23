"""
    Cree una lista de países que mas le gusten 
    Aplíquele los métodos trabajados (obtener un elemento, actualizarlo, agregarle dos elementos, eliminar el ultimo y el primero,
    ordena la lista) 

"""

countries = ["colombia", "Italia", "Inglaterra"]

# obtener
print(countries[0])
print(countries.index("colombia")) # obtener position


# update
countries[0] = "Colombia"
print(countries)

# append
countries.append("Venezuela")
countries.append("Alemania")
print(countries)

countries.pop()
countries.remove("Colombia")
print(countries)
