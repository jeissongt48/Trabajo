class Fecha():
 def __init__(self):
 self.__dia = 1
 def getDia(self):
 return self.__dia
 def setDia(self, dia):
 if dia > 0 and dia < 31:
 self.__dia = dia
 else:
 print “Error”
mi_fecha = Fecha()
mi_fecha.setDia(33)
# segundo ejemplo de encapsulamiento
class Fecha(object):
 def __init__(self):
 self.__dia = 1
 def getDia(self):
 return self.__dia
 def setDia(self, dia):
 if dia > 0 and dia < 31:
 self.__dia = dia
 else:
 print “Error”
 dia = property(getDia, setDia)
mi_fecha = Fecha()
mi_fecha.dia = 33