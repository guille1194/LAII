#!/usr/bin/python
import cgi   
import string

def consonantes(cadena):    #funcion para encontrar la primera consonante de una cadena
	for index in range(len(cadena)):
		if cadena[index]=='a'or cadena[index]=='e'or cadena[index]=='i'or cadena[index]=='o'or cadena[index]=='u'or cadena[index]==cadena[0]:
			print""
		else:
			primer_consonante=cadena[index]
			return string.upper(primer_consonante)
def vocales(cadena):         #funcion para encontrar la primera vocal de una cadena
	for index in range(len(cadena)):
		if cadena[index]=='a'or cadena[index]=='e'or cadena[index]=='i'or cadena[index]=='o'or cadena[index]=='u'or cadena[index]!=cadena[0]:
			primer_vocal=cadena[index]
			return string.upper(primer_vocal)
ifila="<tr>"
icelda="<td>"
ffila="</tr>"  #Cadenas para tablas en html usadas para imprimir la base de datos en una pagina web
fcelda="</td>"

def CURP():  #Funcion para calcular el CURP
	print "Content-type: text/html\n"
	print "<html><head><title>CURP</title></head><body><p>\n"    # Prints para dar inicio a la pagina web
	datos = cgi.FieldStorage()
	if datos.has_key("Name") \
		and datos["Name"].value != "":  #Buscamos si existe la llave Name, y si tiene valor
		nombres=datos["Name"].value    #Asignamos el contenido de Name a la variable nombres, que seran el o los nombres de la persona
		Primer_Nombre=nombres.split(" ")[0]
		Se
		gundo_Nombre=nombres.split(" ")[1]
		C3=consonantes(Primer_Nombre)#Se usa la funcion consonantes para encontrar la primera consonante del primer nombre
		if Primer_Nombre=="Maria" or Primer_Nombre=="Jose":
			N1=Segundo_Nombre[0]
		else:
			N1=Primer_Nombre[0] #N1 sera igual a la primera letra del primer nombre
	else:   
		return 0 #Si no se encuentra la llave Name, o no tiene contenidose retorna 0
	if datos.has_key("Ap") \
		and datos["Ap"].value !="":  #se busca la llave Ap y si tienen valor...
		apellidos=datos["Ap"].value 
		Primer_Apellido=apellidos.split(" ")[0] #Separamos las cadenas por el espacio para obtener el primer y segundo apellido
		C1=consonantes(Primer_Apellido)#Usamos la funcion consonantes para encontrar la primera consonante interna
		A1_A=Primer_Apellido[0]#Obtenemos la inicial del primer apellido y su primera vocal interna...
		A1_B=vocales(Primer_Apellido)
		A1="".join([A1_A,A1_B])#Las juntamos con join
		A1=string.upper(A1)#Y se convierten en mayusculas
		for index in range(len(apellidos)):
			if apellidos[index]==" ":
				Segundo_Apellido=apellidos.split(" ")[1]
				C2=consonantes(Segundo_Apellido)
				A2=Segundo_Apellido[0]#Obtenemos la inicial del segundo apellido
				break
			else:
				C2="X"
				A2="X"	
	else:   
		return 0 
	if datos.has_key("FN") \
		and datos["FN"].value !="":
		FN=datos["FN"].value 
		dia=FN.split("/")[0]#Se separan las cadenas usando "/" como separador...  la primer cadena sera el dia
		mes=FN.split("/")[1]#La segunda cadena el mes
		anio=FN.split("/")[2]#Y la tercera el anio
	else:  
		return 0 
	if datos.has_key("GN")\
		and datos["GN"].value !="":
		gen=datos["GN"].value #Se asigna el contenido de GN a la variable gen,si existe
	else:
		return 0
	if datos.has_key("LN")\
		and datos["LN"].value !="":
		LN= datos["LN"].value #Si no esta vacia y existe LN, se asigna su contenido a la variable LN
	else:
		return 0

	SEMICURP="".join([A1,A2,N1,anio,mes,dia,gen,LN,C1,C2,C3]) #Juntamos los datos obtenidos para generar los primeros 16 caracteres del CURP
	bd = open("bd.html","r")                                  
	basedatos=bd.readlines()#Se abre un archivo para lectura y se lee su contenido por lineas
	contador=0 
	for index in range(len(basedatos)): 
		if basedatos[index].find(SEMICURP)>=0: #Se busca la cadena SEMICURP para saber si esta repetida
			contador=contador+1 #Si ya se encuentra se agrega 1 al contador el numero de veces que fue encontrada
	homoclave="0%d" %contador
	bd.close()
	CURP="".join([SEMICURP,homoclave]) #Juntamos las cadenas SEMICURP y homoclave, para obtener el "CURP" completo
	info=[nombres,apellidos,FN,gen,LN,CURP] #Creamos una variable con todos los datos personales
	newline="\n" 
	bdhtml = open("bd.html","a") #Abrimos un archivo html
	bdhtml.write(newline)
	bdhtml.write(ifila) #Se escriben caracteres para acomodar el contenido en una tabla	
	for index in range(len(info)): #Barremos el contenido de la lista info
		bdhtml.write(icelda) #Ecribimos la cadena icelda que es '<td>'
		bdhtml.write(info[index]) #Se escribe el contenido info[index] el cual sera diferente cada vuelta
		bdhtml.write(fcelda) #Se escribe el fin de la celda'</td>'
	bdhtml.write(ffila)#Se imprime el fin de la fila'</tr>'
	bdhtml.close()
	print "Tu CURP es %s<br/><br/>" % CURP #Se escribe el Curp en html para saber si funciono
	print '<A HREF="file:///usr/lib/cgi-bin/bd.html">Ver la base de datos</A>'
	return 1 #Retornamos 0

campos=CURP() #Asignamos a la variable campos el contenido de CURP, sera un 0 si falto algun campo, o un 1 si se completaron todos
if campos==0:
	print "Por favor llene TODOS los campos"
	print "</p></body></html>"
