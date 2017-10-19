from tabulate import tabulate

"""las tuplas son inmutables, es decir, no se pueden modificar ni crear elementos una vez creados"""

t = ("a", "b", "python", "z", "Ejemplo1")

print t
print t[-1]
print t[1]
"""print t[5]"""
print t[1:3]
print t[3:3]

li = ["a", "b", "python", "z", "Ejemplo2"]
print li
print li[0]
print li[0]
print li[4]

print li
print li[-0]
print li[-4]

print li[1:3]
print li[1:-1]
print li[0:3]

print li[:3]
print li[3:]
print li[:]

li.append("new")
li.insert(2, "new")
li.extend(["two", "elements"])
print li

"""li.index("example")"""
print li.index("new")
print li.index("z")
"""li.index("e")"""

li.remove("z")
li.remove("new")
li.remove("a")
li.pop()
print li

li = ['a', 'b', 'ejemplo3']
print li
li = li + ['ejemplo2', 'new']
print li
li += ['two']
print li
li = [1, 2] * 3
print li

nombres = ("Juan", "Jose", "Jesus",
           "Maria", "Aaron", "Marco",
           "Guillermo", "Daniel", "Julio",
           "Luis", "Miguel", "Francisco",
           "Javier", "Rafael", "David",
           "Jorge", "Ismael", "Samuel",
           "Pedro", "Israel")
print nombres
print nombres[15]

"""del nombres[12]"""

nombresl = list(nombres)
nombresl.pop(12)
print nombresl

b = "Julian"
print nombres + (b, )


colonias = ["Francisco Villa", "Hidalgo", "Jardin", "Patrimonial Benito Juarez",
            "Altamira Sur", "Canon K", "Primer Ayuntamiento", "Santa Rosa",
            "Herrera", "Lomas del Pacifico", "Lomas Tijuana", "Palmeras",
            "Hacienda Linda Vista", "Canon Maclovio Herrera", "Canon Guerrero"]

print colonias
"""colonias.pop(80)"""
print colonias[12]
colonias.append("Guerrero")
print colonias

turistico = {'Zona Turistica': ["CECUT", "Av. Revolucion", "Playas de Tijuana", "Parque Morelos",
             "El Vergel", "Museo del Trompo", "Parque de la amistad", "Museo de Cera",
             "Casino Caliente", "Mundo Divertido"]}

print (tabulate(turistico, showindex=True))
print turistico[0:4]
turistico.extend(["Museo de las Californias", "Malecon", "Flyers", "arco monumental"])
print turistico
del turistico[0:4]
print turistico
