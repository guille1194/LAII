T = ['Practica', 'Practica', 'Tareas', 'Tareas', 'Grupo', 'Grupo', 'Grupo']
conjuntoT = set(T)
print conjuntoT

#Union
A = set([1,2,3,4,5,20,34,25])
B = set([3,4,5,6,7,20,40,60])
print A|B

#interseccion
A = set([1,2,3,4,5,20,34,25,89,100])
B = set([3,4,5,6,7,20,40,70,7,60])
print A&B

#Diferencia
A = set([1,7,3,4,5,20,34,25])
B = set([3,4,5,6,7,20,40,7,60])
print A-B

#pertenencia
A = set([1,2,3,4,5,8,35,23,90])
print 6 in A
print 1 not in A
print 56 in A
print 68 not in A
print 1 not in B

print "A partir de la lista, tupla y de conjunto, crear un programa que gestione el precio de un...."

tamanios = ((1,'Grande',30), (2,'Mediano',20), (3, 'Pequenio',10))
lechugas = ((1, 'Lechuga romana'), (2, 'Lechuga bola'), (3, 'Repollo'))
tomates = ('tomate cherry', 'tomate bola')
aderezos = ('italiano', 'ranch')
tipos = (('lechugas', lechugas), ('tomates', tomates), ('aderezos', aderezos))
orden = []
print "Bienvenido al Restaurante Practica 3"
print "Por favor eliga una de las siguientes opciones"
print "1.- Elegir tamanio de la orden./n 2.- Agregar ingrediente/n 3.- Eliminar ingrediente/n 4.- Buscar ingredientes/n 5.- Mostrar Precio total."
a=int(input())

if a ==  1:
    print "Elige un tamanio (ingresa su numero): "
    print "Tamanios: ", tamanios
    b=int(input())
    orden.insert(b)
    print "Elije el tipo de verdura en tu ensalada (ingresa su numero):"
    for i in tipos:
        print ("Tipo de"+ i[0] +":")
        for j in i[1]:
            print (j)
        c= int(input())
        print orden.insert(c)
