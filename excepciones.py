try:
 num = int('3a')
 print ('no_existe')
except NameError:
 print ('La variable no existe')
except ValueError:
 print ('El valor no es un numero')
#trata mas de una excepción
try:
 num = int('3a')
 print ('no_existe')
except (NameError, ValueError):
 print ('Ocurrio un error')
 #excepciones propias
 class MiError(Exception):
  def __init__(self, valor):
   self.valor = valor
  def __str__(self):
 return 'Error' + str(self.valor)
try:
 if resultado > 20:
 raise MiError(33)
except MiError, e:
 print e