## Text menu in Python
lst=["CECUT", "Av. Revolucion", "Playas de Tijuana", "Parque Morelos",
     "El Vergel", "Museo del Trompo", "Parque de la amistad", "Museo de Cera",
     "Casino Caliente", "Mundo Divertido"]
resultados = []

def agregar_elemento(i):
    for i in range(0,4):
        valor = raw_input("Ingrese un elemento de la lista: ")
        lst.append(valor)
    return lst

def eliminar_elemento(i):
    for i in range(0,4):
        value = raw_input("Cual elemento de la lista deseas eliminar:")
        lst.remove(valor)
    return lst


def imprimir_menu():
    print 30 * "-" , "MENU" , 30 * "-"
    print "1. Imprimir la lista"
    print "2. Agregar un elemento a la lista"
    print "3. Eliminar un elemento derange la lista"
    print "4. Buscar un elemento de la lista"
    print "5. Salir"
    print 67 * "-"

ciclo=True

while ciclo:
    imprimir_menu()
    eleccion = input("Ingrese su opcion [1-5]: ")

    if eleccion==1:
        print "Imprimir la lista"
        print lst
    elif eleccion==2:
        agregar_elemento(4);
        print lst
    elif eleccion==3:
        print lst
        eliminar_elemento(1);
        print lst
    elif eleccion==4:
        def buscar_elemento(i):
            valores = i.split(",")
            for x in range(0, len(lst)):
                for i in range(0, len(valores)):
                    if valores[i] == lst[x]:
                        resultados.append(valores[i])

            if len(resultados)>0:
                print "Valor encontrado: "
                print resultados
            else:
                print "No se encontraron valores"
        lol = raw_input("Ingresar un valor a buscar: ")
        buscar_elemento(lol)
        print lst

    elif eleccion==5:
        print "Hasta Luego"
        ciclo=False

    else:
        raw_input("Esa opcion no existe, por favor ingrese un valor valido.")
