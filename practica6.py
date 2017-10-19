import threading, time
#Se crea clase de hilos
class MiThread(threading.Thread):
    #Inicializas metodo y lo declaras
    def __init__(self,evento):
        threading.Thread.__init__(self)
        self.evento = evento

    #Generas metodo que ejecute los hilos del evento
    def run(self):
        print self.getName(), "En espera del evento"
        self.evento.wait()
        print self.getName(), "Fin del evento"

# llamas al evento a traves de variables
evento = threading.Event()
t1 = MiThread(evento)
t1.start()
t2 = MiThread(evento)
t2.start()

#Espera del evento
time.sleep(3) # Es posible cambiar el No.3 a cualquier valor
evento.set()
