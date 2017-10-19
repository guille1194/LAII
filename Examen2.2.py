
class Empleado:
    def  __init__(self, nombre, horas_trabajo, sueldo_hora, sueldo_total):

        def salario():
            extras=horas_trabajo-40
            if horas_trabajo<=40 and horas_trabajo>0:
                sueldo=horas_trabajo*sueldo_hora
                print "su sueldo es:",sueldo
                print"no posee horas extras"
            elif horas_trabajo>40:
                sueldo_extra=(extras*sueldo_hora)*.1
                sueldo=horas_trabajo*sueldo_hora
                sueldo_total=sueldo+sueldo_extra
                print "su sueldo es:",sueldo
                print "el sueldo de sus horas extras es:",sueldo_extra
                print "su sueldo total es",sueldo_total
            else:
                print "el numero que ingreso es incorrecto intente de nuevo POR FAVOR !"
            raw_input()

nombre = raw_input("Ingresar nombre de empleado: ")
eht = input("Ingresar horas trabajadas: ")

empleado1 = Empleado(nombre,eht,28, 0)

print empleado1.nombre

#print "El empleado", nombre1, "trabajo", eht1, "horas con un sueldo total de", empleado1.sueldo_total
