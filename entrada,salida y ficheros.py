#entrada
import sys
if(len(sys.argv) > 1):
 print ('Abriendo ') + sys.argv[1]
else:
 print ('Debes indicar el nombre del archivo')
#salida
print ('Hola %s' % 'mundo')
print ('%s %s' % ('Hola', 'mundo'))
#archivos
f = open(“archivo.txt”, “w”)
completo = f.read()
parte = f2.read(512)
while True:
 linea = f.readline()
 if not linea: break
 print (linea)
 