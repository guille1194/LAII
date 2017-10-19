lista_1 = [56, "Cambio, [665, 12345678], 'Carrera' 6, 8,[55656, 656], 'Temario, 456, 566",
'565656', 'Analistas, [98989, 84545 5656  5]']

lista_2 = [4565, "Es, [665, 56], 'Viernes' 6, 8,[5, 88], 'Errror, 456, 566", '565656',
'Analistas, [9.9989, 84}545 28923 26, 98 ]']

lista_3 = lista_2 + lista_1
print lista_3

from collections import deque
cola = deque([5656560,45454,455])
cola.append(4)
deque([5656560, 45454, 455, 5656])
cola.popleft()

print cola

print('Ingresa el orden de su Matriz 1')
filas1,columnas1 = int(input()),int(input())
print('Ingresa el orden de su Matriz 2')
filas2,columnas2 = int(input()),int(input())

if (columnas1==filas2):

	matriz1 = []
	for i in range(filas1):
		matriz1.append( [0] * columnas1 )

	matriz2 = []
	for i in range(filas2):
		matriz2.append( [0] * columnas2 )

	print 'Ingrese su Matriz 1'
	for i in range(filas1):
		for j in range(columnas1):
			matriz1[i][j] = float(raw_input('Elemento (%d,%d): ' % (i, j)))
	print 'Ingrese su Matriz 2'
	for i in range(filas2):
		for j in range(columnas2):
			matriz2[i][j] = float(raw_input('Elemento (%d,%d): ' % (i, j)))

	matriz3 = []
	for i in range(filas1):
		matriz3.append( [0] * columnas2 )

	for i in range(filas1):
		for j in range(columnas2):
			for k in range(filas2):
				matriz3[i][j] += matriz1[i][k] * matriz2[k][j]
	print ('Su matriz resultante es')
	print matriz3
else:
	print ('Recurda la multiplicacion entre matrices debe ser mxn * nxm')
