class Instrumento:
 def __init__(self, precio):
  self.precio = precio
 def tocar(self):
 	print “Estamos tocando musica”
 def romper(self):
    print “Eso lo pagas tu”
    print “Son”, self.precio, “$$$”
class Bateria(Instrumento):
    pass
class Guitarra(Instrumento):
    pass

   #herencia multiples
class Terrestre:
 def desplazar(self):
 print “El animal anda”
class Acuatico:
 def desplazar(self):
 print “El animal nada”
class Cocodrilo(Terrestre, Acuatico):
 pass
c = Cocodrilo()
c.desplazar()