import threading, time
import time
import cProfile, pstats, io

pr = cProfile.Profile()
pr.enable()

t0 = time.time()


curp=[]
def buscardosletras():
	B = []
	C = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
	for i in x:
		for J in C:
			if i == J:
				B.append(i)
	curp.append(B[0])
	curp.append(B[1])

def buscarmaterno():
	E = []
	C = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
	for i in y:
		for J in C:
			if i == J:
				E.append(i)
	curp.append(E[0])

def buscarnombre():
	E = []
	C = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
	for i in w:
		for J in C:
			if i == J:
				E.append(i)
	curp.append(E[0])

def buscarconsonante():
	F = []
	C = ["B","C","D","F","G","H","J","K","L","M","N","P","Q","R","S","T","V","W","X","Y","Z"]
	for i in x:
		for J in C:
			if i == J:
				F.append(i)
	if len(F)<=1:
		curp.append("X")
	else:
		curp.append(F[1])

	R = []
	for i in y:
		for J in C:
			if i == J:
				R.append(i)
	if len(R)<=1:
		curp.append("X")
	else:
		curp.append(R[1])

	T = []
	for i in w:
		for J in C:
			if i == J:
				T.append(i)
	if len(T)<=1:
		curp.append("X")
	else:
		curp.append(T[1])

x = str(raw_input("Inserte el apellido paterno: "))
x.upper()
buscardosletras()
y = str(raw_input("Inserte el apellido materno: "))
y.upper()
buscarmaterno()
w = str(raw_input("Inserte el nombre: "))
w.upper()
buscarnombre()
z = str(raw_input("Inserte la fecha de nacimiento YY/MM/DD sin espacio (solo las ultimas dos digitos del anio): "))
z.upper()
curp.append(z)
s = str(raw_input("Inserte su genero H(Hombre)/M(Mujer): "))
curp.append(s)
estados = {'AGUASCALIENTES':'AS','BAJA CALIFORNIA':'BC','BAJA CALIFORNIA SUR':'BS','CAMPECHE':'CC','COAHUILA':'CL','COLIMA':'CM','CHIAPAS':'CS','CHIHUAHUA':'CH','DISTRITO FEDERAL':'DF','DURANGO':'DG','GUANAJUATO':'GT','GUERRERO':'GR','HIDALGO':'HG','JALISCO':'JC','MEXICO':'MC','MICHOACAN':'MN','MORELOS':'MS','NAYARIT':'NT','NUEVO LEON':'NL','OAXACA':'OC','PUEBLA':'PL','QUERETARO':'QT','QUINTANA ROO':'QR','SAN LUIS POTOSI':'SP','SINALOA':'SL','SONORA':'SR','TABASCO':'TC','TAMAULIPAS':'TS','TLAXCALA':'TL','VERACRUZ':'VZ','YUCATAN':'YN','ZACATECAS':'ZS', 'NACIDO EN EXTRANJERO':'NE'}
estado = str(raw_input("Inserte el nombre de la entidad federativa donde nacio: "))
estado.upper()
buscarconsonante()
n=str(raw_input("Inserte un numero de dos digitos: "))
n.upper()
curp.append(n)
print()
print ("El curp es: ", curp[0],curp[1],curp[2],curp[3],curp[4],curp[5],estados[estado], curp[6],curp[7], curp[8],curp[9])
print()

class Mithread (threading.Thread):
	def __init__ (self, evento):
		threading.Thread.__init__(self)
		self.evento = evento

	def run (self):
		print (self.getName(), "OBTENIENDO RESULTADOS")
		self.evento.wait()
		print (self.getName(), "RESULTADOS OBTENIDOS")

evento = threading.Event()
t1 = Mithread(evento)
t1.start()

time.sleep(6)
evento.set()

print ()
print ('el tiempo de ejecucion en total',time.time()-t0)
print ()
pr.disable()
s=io.StringIO()
sortby='cumulative'
ps=pstats.Stats(pr, stream=s).sort_stats(sortby)
ps.print_stats()
print()
print (s.getvalue())
