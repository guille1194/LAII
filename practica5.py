class Instrumento:
    def __init__(self, precio):
        self.precio = precio
    def tocar(self):
        print "Estamos tocando musica"
    def romper(self):
        print "Eso lo pagas tu"
        print "Son", self.precio, "$$$"

class Flauta(Instrumento):
    def __init__(self, precio, tipo_material):
        Instrumento.__init__(self, precio)
        self.material = tipo_material
        print "El material de mi flauta es"
        print self.material
    def tocar(self):
        print "Estamos tocando la flauta"

class Bateria(Instrumento):
    def __init__(self, precio, tipo_set):
        Instrumento.__init__(self, precio)
        self.set = tipo_set
        print "El set de mi bateria es"
        print self.set
    def tocar(self):
        print "Estamos tocando bateria"

class Guitarra(Instrumento):
    def __init__(self, precio, tipo_cuerda):
        Instrumento.__init__(self,precio)
        self.cuerda = tipo_cuerda
        print "Las cuerdas de mi guitarra son de"
        print self.cuerda
    def tocar(self):
        print "Estamos tocando guitarra"

class Saxofon(Instrumento):
    def __init__(self, precio, tipo_material):
        Instrumento.__init__(self,precio)
        self.material = tipo_material
        print "El material de mi saxofon es de"
        print self.material
    def tocar(self):
        print "Estamos tocando saxofon"

class Bajo(Instrumento):
    def __init__(self, precio, tipo_cuerda):
        Instrumento.__init__(self,precio)
        self.cuerda = tipo_cuerda
        print "Las cuerdas de mi bajo son de"
        print self.cuerda
    def tocar(self):
        print "Estamos tocando bajo"

guitarra = Guitarra(2000,"metal")
bateria = Bateria(7000, "basico")
