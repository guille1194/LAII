import os
import sys

platillo=[]
ingredientes=[]
ingredienteextra=[]
i=set(["Tomate", "Lechuga", "Pepino", "Zanahoria", "Aceitunas", "Adereso"])
ie=set(["Aguacate", "Tocino", "Queso", "Adereso"])

def Platillo():
	
	print ("Platillos: ")
	print ("1. Chico - $50.00")
	print ("2. Mediano - $80.00")
	print ("3. Grande - $95.00")

	opcion = input("\nElija un platillo: ")
	if opcion==1:
		platillo.append("Chico")
		platillo.append(50)
		Ingredientes()
	if opcion==2:
		platillo.append("Mediano")
		platillo.append(80)
		Ingredientes()
	if opcion==3:
		platillo.append("Grande")
		platillo.append(95)
		Ingredientes()
	


def Ingredientes():
	print "Ingredientes"
	print "1.- Tomate"
	print "2.- Lechuga"
	print "3.- Pepino"
	print "4.- Zanahoria"
	print "5.- Aceitunas"
	print "6.- Adereso"
	
	for i in [0,1,2]:
		opcionIngrediente = input("\nElija un ingrediente: ")
		if opcionIngrediente == 1:
			ingredientes.append("Tomate")
		if opcionIngrediente == 2:
			ingredientes.append("Chile")
		if opcionIngrediente == 3:
			ingredientes.append("Queso")
		if opcionIngrediente == 4:
			ingredientes.append("Cebolla")
		if opcionIngrediente == 5:
			ingredientes.append("Esparragos")
		if opcionIngrediente == 6:
			ingredientes.append("Adereso")
		
	Extra()

def Extra():
	opcionextra = input ("\nDesea otro ingrediente (SI=1/NO=2): ")
	
	if opcionextra == 1:
		print "Ingredientes\n"
		print "1.- Aguacate"
		print "2.- Tocino"
		print "3.- Queso"
		print "4.- Adereso"
		
		opcionIngredientextra = input("\nElija un ingrediente: ")
		if opcionIngredientextra == 1:
			ingredientes.append("Aguacate")
			platillo[1]=platillo[1]+15
			ingredienteextra.append("Aguacate")
			Extra()
		if opcionIngredientextra == 2:
			ingredientes.append("Tocino")
			platillo[1]=platillo[1]+15	
			ingredienteextra.append("Tocino")	
			Extra()
		if opcionIngredientextra == 3:
			ingredientes.append("Queso")
			platillo[1]=platillo[1]+15
			ingredienteextra.append("Queso")
			Extra()
		if opcionIngredientextra == 4:
			ingredientes.append("Adereso")
			platillo[1]=platillo[1]+15
			ingredienteextra.append("Adereso")
			Extra()
	if opcionextra == 2:
		Imprimir()

def Imprimir():
	i=set(ingredientes)
	e=set(ingredienteextra)
	#ingredientes extras
	print "\nIngredientes extras"
	print ie&e
	#todos los ingredientes
	print "\nTodos los ingredientes"
	print i|e
	print "\nPrecio Total"
	print platillo


		
	
Platillo()

