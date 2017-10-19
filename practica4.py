#1. tiempo de ejecucion de una funcion
'''import time

t0 = time.time()
for i in xrange(1000000):
    i += 5
    print time.time()-t0'''

#2. uso de rangos de tiempo de ejecucion
'''from time import time
t = time()
list = ['a','b','is','Python','json','Nombre','Omar','with','Telefono','tester','pdf','Computadora','lapto','ind','basico','none','nada','var','office']

print list
filter = []
for i in range (100):
    for find in ['is','hat','new','list','old','.']:
        if find not in list:
            filter.append(find)
print "Total de tiempo de ejecucion:"
print time()-t'''

#3. Formato a los resultados del perfil sin tener que escribir los datos del perfil a un archivo
'''import cProfile, pstats, StringIO
pr = cProfile.Profile()
pr.enable()
# do something
pr.disable()
s = StringIO.StringIO()
sortby = 'cumulative'
ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
ps.print_stats()
print s.getvalue()'''

#4. Obtencion de una mejor constante para una determinada plataforma
'''import profile
pr = profile.Profile()
for i in range(5):
    print pr.calibrate(1000000000)'''

#5. Funcion que toma un solo argumento
'''import cProfile
import re
cProfile.run('re.compile("foo|bar")')'''

#6. Estadisticas de clase del modulo de PStats tiene una variedad de metodos para manipular e imprimir los datos guardados
'''import pstats
p = pstats.Stats('restats')
p.strip_dirs().sort_stats(-1).print_stats()'''

#7. Test de stress con subcadena
'''import time
loop_count = 10000000
def method0():
    var = "This is a short sentence"
    for num in xrange(loop_count):
        if "is" in var:
            pass
def method1():
    var = "This is a short sentence"
    for num in xrange(loop_count):
        if var.find("is"):
            pass
t0 = time.time()
method0()
print 'method0(): ' + `time.time()-t0`
t0 = time.time()
method1()
print 'method1(): ' + `time.time()-t0`'''
