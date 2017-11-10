usuarios_db = [['admin','123','Administrador']]
empleados_db = []

#metodos con init
class Usuario:
    def __init__(self, nombreu, clave, rol):
        self.nombreu = nombreu
        self.clave = clave
        self.rol = rol

class Empleado:
    def __init__(self, nombree, horas_trabajo, sueldo_hora):
        self.nombree = nombree
        self.horas_trabajo = horas_trabajo
        self.sueldo_hora = sueldo_hora

def inicio_sesion(nombreu, clave):
    for usuario in usuarios_db:
        if usuario[0] == nombreu:
            if usuario[1] == clave:
                return True

def imprimir_menu():
    print 30 * "-" , "MENU" , 30 * "-"
    print "1. Calcular nomina"
    print "2. Registrar Empleados"
    print "3. Desplegar Empleados"
    print "4. Salir"
    print 67 * "-"

def nomina():
    sueldo_total = 0
    extras_totales = 0
    print 67 * "-"
    for empleado in empleados_db:
        if empleado.horas_trabajo > 0:
            extra = empleado.horas_trabajo - 30
            sueldo = (empleado.sueldo_hora * 30) + (extra * (empleado.sueldo_hora * 1.03))
            sueldo_total += sueldo
            extras_totales += extra
            print "Empleado: " + empleado.nombree +", " + "Horas Trabajadas: " + str(empleado.horas_trabajo) + ", " + "Horas Extra: " + str(extra) +", "+ "Sueldo Total: " + str(sueldo)
    print 67 * "-"
    print "Resumen"
    print "Nomina Total: " + str(sueldo_total)
    print "Total de Horas Extra en Horas: " + str(extras_totales)
    print
    print

def registro():
    print
    print "Ingrese los sigientes datos"
    print
    nombree = raw_input("Nombre Empleado: ")
    horas_trabajo = input("Horas Trabajadas: ")
    sueldo_hora = 28
    empleados_db.append(Empleado(nombree,horas_trabajo,sueldo_hora))
    print "Exito"
    print

def lista():
    i = 1
    for empleado in empleados_db:
        print str(i) +".- " + empleado.nombree + ", " + "Horas Trabajadas: " + str(empleado.horas_trabajo)
        ++i

funciones = { '1': nomina , '2': registro, '3': lista }

print 67 * "-"
print "Bienvenido al Sistema"
print 67 * "-"
print
print "Inicie Sesion para acceder al sistema"
nombreu = raw_input("Nombre Usuario: ")
clave = raw_input("Contrasenia: ")

if inicio_sesion(nombreu, clave):
    funcionando = True
    while funcionando:
        imprimir_menu()
        opcion = raw_input("Escoger opcion: ")
        print
        if opcion == 4:
            print "Hasta luego"
            funcionando = False
        else:
            funciones[opcion]()
            print
else:
    print "Error al iniciar sesion"
