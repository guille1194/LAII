"""turistico = {'Zona Turistica': ["CECUT", "Av. Revolucion", "Playas de Tijuana", "Parque Morelos",
             "El Vergel", "Museo del Trompo", "Parque de la amistad", "Museo de Cera",
             "Casino Caliente", "Mundo Divertido"]}

print (tabulate(turistico, showindex=True))
print turistico[0:4]
turistico.extend(["Museo de las Californias", "Malecon", "Flyers", "arco monumental"])
print turistico
del turistico[0:4]
print turistico"""

menulist= '''1. Imprimir la lista,
    2. Agregar un elemento a la lista,
    3. Eliminar un elemento de la lista,
    4. Cambiar un elemento de la lista,
    5. Buscar un elemento de la lista
    9. Salir''' #assuming you want to display menulist, having it as a tuple is useless

lst=["CECUT", "Av. Revolucion", "Playas de Tijuana", "Parque Morelos",
     "El Vergel", "Museo del Trompo", "Parque de la amistad", "Museo de Cera",
     "Casino Caliente", "Mundo Divertido"] #don't use reserved names for variables, may mess up things

print lst
print menulist
target=raw_input("Elegir un elemento del menu:")

if target=="1": #this is an equality operator, whereas = is used to assign a variable (This checks the equality basically)
    print lst

elif target=="2":
    Addname=raw_input("Escribe un elemento a agregar:")
    list=lst.append(Addname) #use append instead of insert, insert is for a specific position in list
    print lst
    print menulist #no parentheses, menulist is not a function; also this doesn't have to be indented

elif target=="3":
    Removename=raw_input("Cual elemento de la lista deseas eliminar:")
    list=lst.remove(Removename)
    print lst
    print menulist #again, I took the parentheses away

elif target=="4":
    Changename=raw_input("Cual elemento quieres cambiar:") #you'd missed the " at the beginning
    changetoname=raw_input("Cual es el nuevo elemento:")
    list=lst.replace(Changename, changetoname) #removed the '. They're the variables, not the strings 'Changename' etc that you want to replace.
    print lst
    print menulist

elif target=="5":
    nombreBusqueda=raw_input("Cual elemento de la lista deseas buscar:")
    list=lst.index(nombreBusqueda)
    print nombreBusqueda
    print menulist #again, I took the parentheses away

elif target=="9":
    print"Hasta luego" #excessive indenting

else: #this replaces the initial while
    #do nothing if the initial input is not 1,2,3,4 or 9
    print menulist
