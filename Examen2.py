empleados_db = []
eht_db = []
resultados = []

class Empleado:
    def __init__(self, nombre, horas_trabajo, sueldo_hora):
        self.sueldo = 0
        extras=horas_trabajo-40
        if horas_trabajo<=40 and horas_trabajo>0:
            self.sueldo=horas_trabajo*sueldo_hora
        elif horas_trabajo>40:
            self.sueldo_extra=(extras*sueldo_hora)*.1
            self.sueldo=(horas_trabajo*sueldo_hora)+self.sueldo_extra
        else:
            print "el numero que ingreso es incorrecto intente de nuevo POR FAVOR !"
        raw_input()

    nombre1 = list(empleados_db)[1]
    eht1 = list(eht_db)[1]

    empleado1 = Empleado(nombre1,eht1,28)

    print "El empleado", nombre1, "trabajo", eht1, "horas con un sueldo total de", empleado1.sueldo

    def agregar_elemento(i):
        for i in range(0,1):
            valor = raw_input("Ingrese un empleado a la lista: ")
            empleados_db.append(valor)
            valor = input("Ingrese sus horas de trabajo: ")
            eht_db.append(valor)
        return empleados_db, eht_db

    def buscar_elemento(i):
        valores = i.split(",")
        for x in range(0, len(empleados_db)):
            for i in range(0, len(valores)):
                if valores[i] == empleados_db[x]:
                    resultados.append(valores[i])

        if len(resultados)>0:
            print "Valor encontrado: "
            print resultados
        else:
            print "No se encontraron valores"

    def imprimir_menu():
        print 30 * "-" , "MENU" , 30 * "-"
        print "1. Imprimir suma de salario de empleados"
        print "2. Agregar Empleados"
        print "3. Buscar un empleado"
        print "4. Salir"
        print 67 * "-"

    ciclo=True

    while ciclo:
        imprimir_menu()
        eleccion = input("Ingrese su opcion [1-5]: ")

        if eleccion==1:
            print "Imprimir la lista"
            print empleados_db
            print eht_db
        elif eleccion==2:
            agregar_elemento(5);
            print empleados_db
        elif eleccion==3:
            lol = raw_input("Ingresar un valor a buscar: ")
            buscar_elemento(lol)
            print lol
        elif eleccion==4:
            print "Hasta Luego"
            ciclo=False

        else:
            raw_input("Esa opcion no existe, por favor ingrese un valor valido.")
