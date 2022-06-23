def mi_decorador(funcion):
 def nueva(*args):
  print ('Llamada a la funcion'), (funcion.__name__)
  retorno = funcion(*args)
  return retorno
 return nueva
# mas de una versión decorada
@otro_decorador
@mi_decorador
def imp(s):
 print (s)